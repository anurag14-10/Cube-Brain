#!/usr/bin/env python3
"""One-screen state of the Cube, read from the brain. Read-only.

Sections:
  counts      entities per type
  corpus      units per dimension × stage across the whole corpus (the corpus's
              own 4×4 coverage, counted from units by stage of ORIGIN — the
              same rule the framework uses), pathways with no units yet
  grid        each pathway's `coverage` map against its units: missing maps,
              dense cells with no unit, units in cells the grid calls empty
  delivery    open risks (with days to due), milestones, decisions by status

Usage:
  python3 scripts/cube_report.py [--brain PATH] [--section NAME]
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
from pathlib import Path

import yaml

DIMS = ["persona", "solution", "institution", "ecosystem"]
STAGES = ["explore", "define", "pilot", "scale"]


def load(brain: Path) -> dict[str, list[dict]]:
    schema = yaml.safe_load((brain / "SCHEMA.yml").read_text(encoding="utf-8"))
    out: dict[str, list[dict]] = {}
    for spec in schema["entities"].values():
        items = []
        for f in sorted((brain / spec["folder"]).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            if text.startswith("---"):
                try:
                    fm = yaml.safe_load(text.split("---", 2)[1]) or {}
                except yaml.YAMLError:
                    continue
                fm["_slug"] = f.stem
                items.append(fm)
        out[spec["folder"]] = items
    return out


def as_date(v) -> dt.date | None:
    try:
        return dt.date.fromisoformat(str(v)[:10])
    except (TypeError, ValueError):
        return None


def counts(b):
    print("## Entities\n")
    total = 0
    for folder, items in b.items():
        if items:
            print(f"  {folder:<16}{len(items):>5}")
            total += len(items)
    print(f"  {'total':<16}{total:>5}\n")


def corpus(b):
    units = b.get("units", [])
    patterns = [u for u in units if u.get("unit_type") == "Problem-Solution Pattern"]
    units = [u for u in units if u not in patterns]
    grid = collections.Counter((u.get("dimension"), u.get("stage")) for u in units)
    print("## Corpus coverage — units by dimension × stage of origin\n")
    print("  " + " " * 12 + "".join(f"{s.title():>9}" for s in STAGES))
    for d in DIMS:
        print(f"  {d.title():<12}" + "".join(f"{grid.get((d, s), 0):>9}" for s in STAGES))
    thin = [f"{d}-{s}" for d in DIMS for s in STAGES if grid.get((d, s), 0) <= 1]
    print(f"\n  patterns: {len(patterns)}")
    print(f"  thinnest cells (≤1 unit): {', '.join(thin) or 'none'}")
    by_type = collections.Counter(u.get("unit_type") for u in units)
    print("  by type: " + ", ".join(f"{k}: {v}" for k, v in by_type.most_common()))
    per_pw = collections.Counter(u.get("pathway") for u in units)
    print("\n  units per pathway:")
    for p in b.get("pathways", []):
        print(f"    {p['_slug']:<40}{per_pw.get(p['_slug'], 0):>4}   {p.get('lifecycle', ''):<10} {p.get('stage_reached', '')}")
    print()


def grid(b):
    """Each pathway's stated coverage against the units extracted from it.

    The two answer different questions -- `coverage` is the document's own
    grid, units are what the brain extracted -- so disagreement is not always
    a fault. But a dense cell with no unit usually means extraction is
    incomplete, and a unit in a cell the grid calls empty means a mis-tag or a
    stale grid. Nothing else puts the two side by side.
    """
    units = [u for u in b.get("units", []) if u.get("unit_type") != "Problem-Solution Pattern"]
    print("## Grid consistency — pathway coverage vs units by stage of origin\n")
    clean = True
    for p in b.get("pathways", []):
        slug, cov = p["_slug"], p.get("coverage") or {}
        have = collections.Counter(f"{u.get('dimension')}:{str(u.get('stage') or '').title()}"
                                   for u in units if u.get("pathway") == slug)
        notes = []
        if have and not cov:
            notes.append(f"{sum(have.values())} units but no `coverage` map")
        if cov and not have:
            notes.append("`coverage` map but no units")
        if cov and have:
            dense = [k for k, v in cov.items() if (v or 0) >= 2 and not have.get(k)]
            empty = [k for k in have if not cov.get(k)]
            if dense:
                notes.append("density ≥2, no unit: " + ", ".join(sorted(dense)))
            if empty:
                notes.append("unit in a cell the grid calls 0: " + ", ".join(sorted(empty)))
        for n in notes:
            clean = False
            print(f"  {slug:<40} {n}")
    print("  consistent" if clean else "")
    print()


def delivery(b):
    today = dt.date.today()
    print("## Delivery\n")
    for r in sorted(b.get("risks", []), key=lambda r: str(r.get("due_date") or "9999")):
        if r.get("status") in ("open", "materialised"):
            due = as_date(r.get("due_date"))
            days = f"{(due - today).days:+d}d" if due else "no date"
            print(f"  RISK  {r['_slug']:<40} {r.get('impact', ''):<9} due {due or '—'} ({days})")
    for m in sorted(b.get("milestones", []), key=lambda m: str(m.get("target_date"))):
        print(f"  MILESTONE {m['_slug']:<36} {str(m.get('target_date')):<11} {m.get('status')}")
    ds = collections.Counter(d.get("status") for d in b.get("decisions", []))
    print("  decisions: " + (", ".join(f"{k}: {v}" for k, v in ds.most_common()) or "none") + "\n")


def main() -> int:
    here = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--brain", default=str(here))
    ap.add_argument("--section", choices=["counts", "corpus", "grid", "delivery"])
    a = ap.parse_args()
    b = load(Path(a.brain))
    print(f"# Cube-Brain report — {dt.date.today()}\n")
    for name, fn in (("counts", counts), ("corpus", corpus), ("grid", grid), ("delivery", delivery)):
        if a.section in (None, name):
            fn(b)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
