#!/usr/bin/env python3
"""Plan a brain sync after the diffusion-cube code moved on.

Decides nothing and writes nothing. It answers one question deterministically
so an agent spends tokens on judgment rather than on bookkeeping:

    "Since the commit the brain was last verified against, which files
     changed in the repo, which brain entries describe those files, and which
     changed files have NO entry yet (and what type it should be)?"

How "last verified" is chosen: the most common `verified_at_commit` across the
brain, unless --since is given. Entries pinned to an older commit than that are
listed separately as individually stale.

Usage:
  python3 scripts/cube_sync_plan.py [--repo PATH] [--brain PATH] [--since SHA] [--json]
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

# changed path -> (entity type, folder, what to do). First match wins.
PATH_RULES = [
    (r"^content/framework\.md$", "framework", None,
     "framework content changed: run scripts/seed_from_repo.py --only framework --dry-run, diff, then --force selectively"),
    (r"^lib/dimensions\.ts$", "framework", None,
     "framework SHAPE changed (dimensions/sub-categories/weights/unit types): reseed framework AND check MASTERS 1/2"),
    (r"^content/wiki/pathways/index\.md$", "pathway", "pathways",
     "grounding index changed: pathway lifecycle (published/unindexed) may have changed"),
    (r"^content/(library-)?wiki/pathways/.+\.md$", "pathway", "pathways",
     "pathway document added/changed: seed or update the pathway, then run the ingest-pathway procedure for its units"),
    (r"^supabase/migrations/.+\.sql$", "migration", "migrations",
     "new/changed migration: create the migration entry, update every table it touches, add a decision if it embodies one"),
    (r"^app/api/.+/route\.ts$", "endpoint", "endpoints",
     "route handler changed: update endpoint (access, tables, status) and any feature/workflow using it"),
    (r"^app/.+/page\.tsx$", "page", "pages", "page changed: update page (access behaviour, components, endpoints)"),
    (r"^lib/system-prompts\.ts$", "prompt", "prompts",
     "prompts changed: update prompts, chat-modes, the grid-update contract and any rule they carry"),
    (r"^lib/grid-update\.ts$|^lib/adoption-conversation\.ts$", "contract", "contracts",
     "client/contract logic changed: check grid-update, designs-meta, grid-state contracts"),
    (r"^(lib|components|app)/.+\.(ts|tsx)$", "module", "modules", "module changed: update its module entry"),
    (r"^content/.+\.md$", "module", "modules", "content file changed: update its module entry"),
    (r"^(Dockerfile|\.github/workflows/.+|next\.config\.ts|proxy\.ts)$", "module", "modules",
     "infra/middleware changed: update module + environment entries"),
    (r"^specs/.+\.md$|^docs/tasks/.+\.md$", "requirement", "requirements",
     "spec/task doc changed: update or add requirements (and decisions it records)"),
    (r"^docs/raw_documents/.+", "requirement", "requirements",
     "raw document changed (charter/framework PDF): re-read for milestones, requirements, risks"),
    (r"^package\.json$", "integration", "integrations", "dependencies changed: check integration sdk ranges"),
]
IGNORE = re.compile(r"^(docs/wiki/|\.claude/|package-lock\.json|tsconfig|public/|\.next/|node_modules/)")


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


def load_entities(brain: Path) -> list[dict]:
    schema = yaml.safe_load((brain / "SCHEMA.yml").read_text(encoding="utf-8"))
    out = []
    for spec in schema["entities"].values():
        for f in sorted((brain / spec["folder"]).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            try:
                fm = yaml.safe_load(text.split("---", 2)[1]) or {}
            except yaml.YAMLError:
                continue
            refs = []
            for key in ("code_refs", "corpus_files"):
                refs += [str(r).split("#")[0].rstrip("/") for r in (fm.get(key) or [])]
            for key in ("path", "file"):
                if fm.get(key):
                    refs.append(str(fm[key]))
            out.append({"id": f"{spec['folder']}/{f.stem}", "refs": set(refs),
                        "commit": str(fm.get("verified_at_commit") or "")})
    return out


def env_vars_added(repo: Path, since: str) -> list[str]:
    diff = git(repo, "diff", f"{since}..HEAD", "--unified=0", "--", "app", "lib", "components", "proxy.ts", "scripts")
    added = set(re.findall(r"^\+.*process\.env\.([A-Z_][A-Z0-9_]*)", diff, re.M))
    return sorted(v for v in added if v != "NODE_ENV")


def main() -> int:
    here = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=os.environ.get("CUBE_REPO", str(here.parent / "diffusion-cube")))
    ap.add_argument("--brain", default=str(here))
    ap.add_argument("--since", help="commit to diff from (default: most common verified_at_commit)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    repo, brain = Path(args.repo).resolve(), Path(args.brain).resolve()

    entities = load_entities(brain)
    head = git(repo, "rev-parse", "HEAD").strip()
    commits = collections.Counter(e["commit"] for e in entities if e["commit"])
    since = args.since or (commits.most_common(1)[0][0] if commits else None)
    if not since:
        print("no entry carries verified_at_commit; pass --since", file=sys.stderr)
        return 2
    if git(repo, "rev-parse", since).strip() == head:
        print(f"brain is verified at repo HEAD ({head[:8]}) — nothing to sync")
        return 0

    changes = []
    for line in git(repo, "diff", "--name-status", f"{since}..HEAD").splitlines():
        parts = line.split("\t")
        status, path = parts[0][0], parts[-1]
        if not IGNORE.match(path):
            changes.append((status, path))

    plan = []
    for status, path in changes:
        hits = sorted(e["id"] for e in entities
                      if path in e["refs"] or any(path.startswith(r + "/") for r in e["refs"] if r))
        rule = next(((t, f, why) for pat, t, f, why in PATH_RULES if re.search(pat, path)), None)
        plan.append({"status": {"A": "added", "M": "modified", "D": "deleted", "R": "renamed"}.get(status, status),
                     "path": path, "entries": hits,
                     "suggested_type": rule[0] if rule else None,
                     "action": rule[2] if rule else "no rule — decide whether this matters to the brain"})

    stale = sorted(e["id"] for e in entities if e["commit"] and e["commit"] != since
                   and e["commit"] != head)
    new_env = env_vars_added(repo, since)
    log = git(repo, "log", "--format=%h %as %an %s", f"{since}..HEAD").strip().splitlines()

    result = {"since": since, "head": head, "commits": log, "changes": plan,
              "new_env_vars": new_env, "individually_stale_entries": stale}
    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"# Brain sync plan  {since[:8]} → {head[:8]}  ({len(log)} commits)\n")
    print("## Commits\n" + "\n".join(f"- {c}" for c in log) + "\n")
    print("## Changed files → brain entries\n")
    for p in plan:
        tgt = ", ".join(p["entries"]) if p["entries"] else f"**NO ENTRY** → create `{p['suggested_type']}`"
        print(f"- [{p['status']}] `{p['path']}` → {tgt}\n    - {p['action']}")
    if new_env:
        print("\n## New env vars read by code\n" + "\n".join(f"- {v} → config/{v.lower().replace('_', '-')}.md" for v in new_env))
    print("\n## Always\n- add a `releases/` entry for the merged PR(s)\n"
          f"- set `verified_at_commit: {head}` on every entry you re-checked\n"
          "- run scripts/validate_wiki.py . before committing")
    if stale:
        print(f"\n## Entries pinned to some other commit ({len(stale)})\n" + "\n".join(f"- {s}" for s in stale[:50]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
