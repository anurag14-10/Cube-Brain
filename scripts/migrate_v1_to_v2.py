#!/usr/bin/env python3
"""Migrate a Cube-Brain from schema v1 (34 types, 6 layers) to v2 (8 types).

v2 drops the app's code level and turns closed sets into variables:

  folded into concepts/   dimensions/ sub-categories/ stages/ cells/
                          (one concept page per dimension carrying its
                          sub-categories and cells; one per stage) and rules/
                          (concept_kind: rule)
  folded into units/      patterns/ (unit_type: Problem-Solution Pattern)
  became variables        corpora/ teams/ (MASTERS 13, 15) — the values that
                          referenced them are unchanged slugs
  removed                 roles/ features/ workflows/ pages/ endpoints/
                          chat-modes/ prompts/ contracts/ tables/ migrations/
                          modules/ integrations/ config/ environments/
                          requirements/ releases/ tech-debt/ incidents/

Field mapping on what remains:

  every entry   code_refs → appended to doc_refs; verified_at_commit dropped;
                schema_version 1 → 2
  concept       code_identifier dropped
  pathway       corpus_files → appended to doc_refs
  decision      affects_features / affects_tables / affects_modules dropped
  risk          integration, affects_features dropped (name the vendor in
                `organisation` by hand); owner_team kept as a variable
  milestone     owner_team kept as a variable
  body links    to a folded folder → its new page; to a removed folder → the
                link text alone

Everything removed stays in git history; nothing here is unrecoverable.

Usage:
  python3 scripts/migrate_v1_to_v2.py .            # migrate in place
  python3 scripts/migrate_v1_to_v2.py . --dry-run  # say what would change
  python3 scripts/migrate_v1_to_v2.py . --check    # exit 1 if anything is still v1
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from seed_from_repo import STAGES, render_dimension, render_stage  # noqa: E402

FRAMEWORK = ["dimensions", "sub-categories", "stages", "cells"]
VARIABLES = ["corpora", "teams"]
REMOVED = ["roles", "features", "workflows", "pages", "endpoints", "chat-modes", "prompts",
           "contracts", "tables", "migrations", "modules", "integrations", "config",
           "environments", "requirements", "releases", "tech-debt", "incidents"]
FOLDED = FRAMEWORK + VARIABLES + REMOVED + ["patterns", "rules"]
KEPT = ["concepts", "pathways", "units", "organisations", "people", "decisions", "risks", "milestones"]

DROP = {
    "*": ["verified_at_commit"],
    "concepts": ["code_identifier"],
    "decisions": ["affects_features", "affects_tables", "affects_modules"],
    "risks": ["integration", "affects_features"],
}

LINK = re.compile(r"\[([^\]]+)\]\(\.\./([a-z-]+)/([a-z0-9-]+)\.md(#[^)]*)?\)")


def read(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        return yaml.safe_load(fm) or {}, body
    return {}, text


def dump(fm: dict, body: str) -> str:
    return ("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100)
            + "---" + body)


def entries(root: Path, folder: str) -> list[Path]:
    return sorted((root / folder).glob("*.md")) if (root / folder).is_dir() else []


def first(*values):
    return next((v for v in values if v not in (None, "", [])), None)


def relink(body: str) -> str:
    def swap(m: re.Match) -> str:
        text, folder, slug, anchor = m.group(1), m.group(2), m.group(3), m.group(4) or ""
        if folder in ("dimensions", "stages", "rules"):
            return f"[{text}](../concepts/{slug}.md{anchor})"
        if folder in ("sub-categories", "cells"):
            return f"[{text}](../concepts/{slug.split('-')[0]}.md)"
        if folder == "patterns":
            return f"[{text}](../units/{slug}.md{anchor})"
        if folder in FOLDED:
            return text
        return m.group(0)
    return LINK.sub(swap, body)


def migrate_fields(folder: str, fm: dict) -> dict:
    """v1 frontmatter → v2, keeping key order; doc_refs takes code_refs' place."""
    refs: list = []
    for key in ("doc_refs", "code_refs", "corpus_files"):
        refs += [r for r in fm.get(key) or [] if r not in refs]
    dropped = set(DROP["*"] + DROP.get(folder, []))
    out: dict = {}
    for k, v in fm.items():
        if k in ("doc_refs", "code_refs", "corpus_files"):
            if refs and "doc_refs" not in out:
                out["doc_refs"] = refs
        elif k not in dropped:
            out[k] = v
    out["schema_version"] = 2
    return out


def framework_pages(root: Path) -> dict[str, tuple[dict, str]]:
    """The eight v2 concept pages, rebuilt from the v1 framework folders."""
    pages: dict[str, tuple[dict, str]] = {}
    subs_by_dim: dict[str, list] = {}
    for p in entries(root, "sub-categories"):
        fm, _ = read(p)
        subs_by_dim.setdefault(fm["dimension"], []).append({
            "code": fm["code"], "name": fm["name"], "questions": fm.get("questions") or [],
            "weights": {st: fm.get(f"weight_{st.lower()}", "") for st in STAGES}})
    cells: dict[tuple[str, str], dict] = {}
    for p in entries(root, "cells"):
        fm, _ = read(p)
        cells[(fm["dimension"], fm["stage"])] = fm

    def shared(fm: dict) -> dict:
        refs = list(fm.get("doc_refs") or [])
        refs += [r for r in fm.get("code_refs") or [] if r not in refs]
        return {"sources": fm.get("sources") or [], "doc_refs": refs,
                "first_logged": fm.get("first_logged"), "last_updated": fm.get("last_updated")}

    for p in entries(root, "dimensions"):
        fm, body = read(p)
        code = fm.get("code") or p.stem
        intro = re.search(r"^\*[^\n]+\*\n\n(.+?)\n\n## Sub-categories", body, re.S | re.M)
        fields, new_body = render_dimension({
            "code": code, "name": fm["name"], "central_question": fm["central_question"],
            "shift": fm.get("shift"), "intro": intro.group(1).strip() if intro else None,
            "thesis_group": fm.get("thesis_group"), "data": fm.get("data_concern"),
            "trust": fm.get("trust_concern"), "order": fm.get("order"),
            "subs": sorted(subs_by_dim.get(code, []), key=lambda s: s["code"]),
            "cells": {st: c for (d, s), c in cells.items() if d == code
                      for st in STAGES if st.lower() == s},
        })
        pages[code] = ({"name": fm["name"], "type": "concept", "schema_version": 2, **fields,
                        **shared(fm)}, new_body)

    for p in entries(root, "stages"):
        fm, _ = read(p)
        slug = p.stem
        fields, new_body = render_stage({
            "name": fm["name"], "order": fm["order"], "central_question": fm["central_question"],
            "done_when": fm.get("done_when"), "previous": fm.get("previous_stage"),
            "next": fm.get("next_stage"),
            "cells": {d: c["core_question"] for (d, s), c in sorted(
                cells.items(), key=lambda kv: ["persona", "solution", "institution", "ecosystem"].index(kv[0][0]))
                if s == slug},
        })
        pages[slug] = ({"name": fm["name"], "type": "concept", "schema_version": 2, **fields,
                        **shared(fm)}, new_body)
    for fm, _ in pages.values():
        for k in [k for k, v in fm.items() if v in (None, "", [])]:
            del fm[k]
    return pages


def rule_concept(fm: dict, body: str) -> tuple[dict, str]:
    fm = migrate_fields("rules", dict(fm))
    statement = fm.pop("statement", None)
    for key in ("enforcement", "enforced_in", "applies_to_modes"):
        fm.pop(key, None)
    fm["type"] = "concept"
    fm.setdefault("concept_kind", "rule")
    fm.setdefault("definition", statement)
    body = re.sub(r"\n## Where enforced\n.*?(?=\n## |\Z)", "\n", body, flags=re.S)
    return fm, relink(body)


def pattern_unit(fm: dict, body: str) -> tuple[dict, str]:
    fm = migrate_fields("patterns", dict(fm))
    fm["type"] = "unit"
    fm["unit_type"] = "Problem-Solution Pattern"
    return fm, relink(body)


def still_v1(root: Path) -> list[str]:
    out = [f"{f}/ still holds entries" for f in FOLDED if entries(root, f)]
    for folder in KEPT:
        for p in entries(root, folder):
            fm, _ = read(p)
            if fm.get("schema_version") != 2:
                out.append(f"{folder}/{p.name} is at schema v{fm.get('schema_version')}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    root = Path(a.root).resolve()

    if a.check:
        left = still_v1(root)
        for line in left:
            print(line)
        print("schema v2: " + ("NOT migrated" if left else "current"))
        return 1 if left else 0

    writes: dict[Path, str] = {}
    for slug, (fm, body) in framework_pages(root).items():
        target = root / "concepts" / f"{slug}.md"
        if not target.exists():
            writes[target] = dump(fm, "\n\n" + body.strip() + "\n")
    for p in entries(root, "rules"):
        writes[root / "concepts" / p.name] = dump(*rule_concept(*read(p)))
    for p in entries(root, "patterns"):
        writes[root / "units" / p.name] = dump(*pattern_unit(*read(p)))

    for folder in KEPT:
        for p in entries(root, folder):
            if p in writes:
                continue
            fm, body = read(p)
            new = dump(migrate_fields(folder, fm), relink(body))
            if new != p.read_text(encoding="utf-8"):
                writes[p] = new
    doomed = [root / f for f in FOLDED if (root / f).is_dir()]
    verb = "would" if a.dry_run else "did"
    print(f"{verb} write {len(writes)} files, remove {len(doomed)} folders")
    for p in sorted(writes):
        print("  ~", p.relative_to(root))
    for d in doomed:
        print("  -", d.relative_to(root), f"({len(entries(root, d.name))} entries)")
    if a.dry_run:
        return 0
    for p, text in writes.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    for d in doomed:
        shutil.rmtree(d)
    return 0


if __name__ == "__main__":
    sys.exit(main())
