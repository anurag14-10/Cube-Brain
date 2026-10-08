#!/usr/bin/env python3
"""One-screen state of the Cube, read from the brain. Read-only.

Sections:
  counts      entities per type
  corpus      units per dimension × stage across the whole corpus (the corpus's
              own 4×4 coverage, counted from units by stage of ORIGIN — the
              same rule the framework uses), pathways with no units yet
  product     features by status; dead-code / inert things still in the repo
  delivery    open risks (with days to due), milestones, open tech debt by
              severity, requirements by status
  freshness   entries verified against an older commit than the repo HEAD

Usage:
  python3 scripts/cube_report.py [--brain PATH] [--repo PATH] [--section NAME]
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import os
import subprocess
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
    grid = collections.Counter((u.get("dimension"), u.get("stage")) for u in units)
    print("## Corpus coverage — units by dimension × stage of origin\n")
    print("  " + " " * 12 + "".join(f"{s.title():>9}" for s in STAGES))
    for d in DIMS:
        print(f"  {d.title():<12}" + "".join(f"{grid.get((d, s), 0):>9}" for s in STAGES))
    thin = [f"{d}-{s}" for d in DIMS for s in STAGES if grid.get((d, s), 0) <= 1]
    print(f"\n  thinnest cells (≤1 unit): {', '.join(thin) or 'none'}")
    by_type = collections.Counter(u.get("unit_type") for u in units)
    print("  by type: " + ", ".join(f"{k}: {v}" for k, v in by_type.most_common()))
    per_pw = collections.Counter(u.get("pathway") for u in units)
    print("\n  units per pathway:")
    for p in b.get("pathways", []):
        print(f"    {p['_slug']:<40}{per_pw.get(p['_slug'], 0):>4}   {p.get('lifecycle', ''):<10} {p.get('stage_reached', '')}")
    print(f"\n  patterns: {len(b.get('patterns', []))}\n")


def product(b):
    print("## Product\n")
    st = collections.Counter(f.get("status") for f in b.get("features", []))
    print("  features: " + ", ".join(f"{k}: {v}" for k, v in st.most_common()))
    for folder in ("endpoints", "modules", "tables", "prompts", "pages"):
        bad = [x["_slug"] for x in b.get(folder, []) if x.get("status") in ("dead-code", "inert", "dropped")]
        if bad:
            print(f"  {folder} not live: {', '.join(bad)}")
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
    debt = collections.defaultdict(list)
    for t in b.get("tech-debt", []):
        if t.get("status") not in ("resolved", "wont-fix"):
            debt[t.get("severity")].append(t.get("td_id") or t["_slug"])
    for sev in sorted(debt):
        print(f"  DEBT {sev}: {', '.join(sorted(debt[sev]))}")
    rq = collections.Counter(r.get("status") for r in b.get("requirements", []))
    print("  requirements: " + ", ".join(f"{k}: {v}" for k, v in rq.most_common()) + "\n")


def freshness(b, repo: Path):
    try:
        head = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("## Freshness\n\n  repo not reachable — skipped\n")
        return
    pinned = collections.Counter()
    for folder, items in b.items():
        for x in items:
            c = str(x.get("verified_at_commit") or "")
            if c:
                pinned["current" if head.startswith(c) or c.startswith(head[:7]) else c[:8]] += 1
    print(f"## Freshness (repo HEAD {head[:8]})\n")
    for k, v in pinned.most_common():
        print(f"  {k:<10}{v:>5} entries")
    if any(k != "current" for k in pinned):
        print("\n  → run scripts/cube_sync_plan.py to see what changed")
    print()


def main() -> int:
    here = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--brain", default=str(here))
    ap.add_argument("--repo", default=os.environ.get("CUBE_REPO", str(here.parent / "diffusion-cube")))
    ap.add_argument("--section", choices=["counts", "corpus", "product", "delivery", "freshness"])
    a = ap.parse_args()
    b = load(Path(a.brain))
    print(f"# Cube-Brain report — {dt.date.today()}\n")
    for name, fn in (("counts", counts), ("corpus", corpus), ("product", product), ("delivery", delivery)):
        if a.section in (None, name):
            fn(b)
    if a.section in (None, "freshness"):
        freshness(b, Path(a.repo))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
