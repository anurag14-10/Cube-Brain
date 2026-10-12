#!/usr/bin/env python3
"""Where the brain has fallen behind the diffusion-cube corpus. Read-only.

The brain is only updated when somebody runs the skill, so nothing tells anyone
that a pathway document landed, changed or vanished in the project repo. This
compares the two at a git ref -- read with `git show` / `git ls-tree`, so the
project's working tree, branch and uncommitted edits are never touched.

Reports, per corpus document:
  missing      a document with no pathways/<slug>.md entry
  not-ingested an entry with zero units
  changed      the document's last commit is newer than the entry's newest
               `sources` date for it -- re-read and refresh (Mode C)
  corpus       the entry's `corpora` does not list the corpus the file is in
  lifecycle    grounding file linked from index.md but not `published`, or
               unlinked but not `unindexed`
  removed      an entry's doc_ref no longer exists at the ref

Usage:
  python3 scripts/check_corpus_drift.py [--repo PATH] [--ref REF] [--check]

  --ref     default HEAD; `git -C "$CUBE_REPO" fetch` first and pass e.g.
            origin/main to compare against what is actually merged
  --check   exit 1 when anything drifted (for CI / scripted use)
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

CORPORA = {
    "content/wiki/pathways": "grounding-corpus",
    "content/library-wiki/pathways": "library-corpus",
}
INDEX = "content/wiki/pathways/index.md"


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, text=True).stdout


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    try:
        return yaml.safe_load(text.split("---", 2)[1]) or {}
    except yaml.YAMLError:
        return {}


def newest_source_date(fm: dict, doc: str) -> str:
    dates = [str(s.get("date", ""))[:10] for s in fm.get("sources") or []
             if isinstance(s, dict) and doc in str(s.get("ref", ""))]
    return max(dates, default=str(fm.get("last_updated") or "")[:10])


def main() -> int:
    brain = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=os.environ.get("CUBE_REPO",
                                                     str(brain.parent / "diffusion-cube")))
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    repo = Path(a.repo)
    if not (repo / ".git").exists():
        sys.exit(f"no diffusion-cube clone at {repo} (set CUBE_REPO or --repo)")

    sha = git(repo, "rev-parse", "--short", a.ref).strip()
    files = set(git(repo, "ls-tree", "-r", "--name-only", a.ref, "--",
                    *CORPORA).split())
    try:
        index = git(repo, "show", f"{a.ref}:{INDEX}")
    except subprocess.CalledProcessError:
        index = ""
    indexed = set(re.findall(r"\(([a-z0-9-]+)\.md\)", index))

    entries = {p.stem: frontmatter(p) for p in sorted((brain / "pathways").glob("*.md"))}
    units = {}
    for p in (brain / "units").glob("*.md"):
        pw = frontmatter(p).get("pathway")
        if pw:
            units[pw] = units.get(pw, 0) + 1

    findings: list[tuple[str, str, str]] = []
    for path in sorted(files):
        if not path.endswith(".md") or path == INDEX:
            continue
        folder, slug = path.rsplit("/", 1)[0], Path(path).stem
        corpus = CORPORA[folder]
        fm = entries.get(slug)
        if fm is None:
            findings.append(("missing", slug, f"{path} has no pathways/{slug}.md"))
            continue
        if corpus not in (fm.get("corpora") or []):
            findings.append(("corpus", slug, f"in {corpus} but `corpora` does not say so"))
        changed = git(repo, "log", "-1", "--format=%cs", a.ref, "--", path).strip()
        seen = newest_source_date(fm, path)
        if changed and seen and changed > seen:
            findings.append(("changed", slug, f"{path} changed {changed}, entry last read {seen}"))
        if corpus == "grounding-corpus":
            life = fm.get("lifecycle")
            if slug in indexed and life not in ("published", "retired"):
                findings.append(("lifecycle", slug, f"linked from index.md but lifecycle is {life!r}"))
            if slug not in indexed and life == "published" and "library-corpus" not in (fm.get("corpora") or []) \
                    and "published-pathways-corpus" not in (fm.get("corpora") or []):
                findings.append(("lifecycle", slug, "not linked from index.md but lifecycle is 'published'"))

    for slug, fm in entries.items():
        if not units.get(slug):
            findings.append(("not-ingested", slug, "0 units point at this pathway"))
        for ref in fm.get("doc_refs") or []:
            if any(str(ref).startswith(f) for f in CORPORA) and str(ref) not in files:
                findings.append(("removed", slug, f"doc_ref {ref} is not in {a.ref}"))

    print(f"# Corpus drift — brain vs diffusion-cube {a.ref} ({sha})\n")
    if not findings:
        print("  no drift")
    for kind in ("missing", "changed", "removed", "not-ingested", "corpus", "lifecycle"):
        rows = [f for f in findings if f[0] == kind]
        if rows:
            print(f"## {kind} ({len(rows)})")
            for _, slug, note in rows:
                print(f"  {slug}: {note}")
            print()
    return 1 if (a.check and findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
