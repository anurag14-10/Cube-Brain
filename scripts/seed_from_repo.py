#!/usr/bin/env python3
"""Seed the Cube-Brain's deterministic layers from the diffusion-cube repo.

What it generates (all derivable from files, no judgment needed):

  framework  dimensions/ sub-categories/ stages/ cells/ concepts/
             from content/framework.md + lib/dimensions.ts
  corpus     pathways/ (identity stubs: title, sector, stage, coverage grid,
             gaps, corpus copies) and corpora/
             from content/wiki/pathways + content/library-wiki/pathways
  actors     organisations/ named as pathway contributors

What it deliberately does NOT generate: units, patterns, decisions, or
anything whose content needs reading and judgment. Those are the cube-brain
skill's job ("ingest pathway", "capture").

Idempotent: an existing file is never overwritten unless --force is given,
because a seeded file may since have been enriched by hand.

Usage:
  python3 scripts/seed_from_repo.py [--repo PATH] [--brain PATH] [--force] [--dry-run]
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

TODAY = dt.date.today().isoformat()
SCHEMA_VERSION = 1


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = text.replace("+", " plus ").replace("&", " and ")
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return re.sub(r"-{2,}", "-", text)


def md_clean(text: str) -> str:
    """Strip markdown emphasis/links for use as a frontmatter string."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"(?<!\w)\*(?!\s)([^*]+)\*(?!\w)", r"\1", text)
    return " ".join(text.split())


def table_rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|") or re.match(r"^\|[\s|:-]+\|$", line):
            continue
        rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows


def section(text: str, start_pat: str, stop_pat: str = r"^#{1,3} ") -> str:
    m = re.search(start_pat, text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    stop = re.search(stop_pat, rest, re.M)
    return rest[: stop.start()] if stop else rest


def split_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            try:
                return yaml.safe_load(parts[1]) or {}, parts[2]
            except yaml.YAMLError:
                return {}, parts[2]
    return {}, text


class Writer:
    def __init__(self, brain: Path, commit: str, force: bool, dry: bool):
        self.brain, self.commit, self.force, self.dry = brain, commit, force, dry
        self.written: list[str] = []
        self.skipped: list[str] = []

    def write(self, folder: str, slug: str, etype: str, name: str,
              fields: dict, body: str, sources: list[dict],
              code_refs: list[str] | None = None, doc_refs: list[str] | None = None) -> None:
        path = self.brain / folder / f"{slug}.md"
        rel = f"{folder}/{slug}.md"
        if path.exists() and not self.force:
            self.skipped.append(rel)
            return
        fm: dict = {"name": name, "type": etype, "schema_version": SCHEMA_VERSION}
        for k, v in fields.items():
            if v not in (None, "", [], {}):
                fm[k] = v
        if code_refs:
            fm["code_refs"] = code_refs
            fm["verified_at_commit"] = self.commit
        if doc_refs:
            fm["doc_refs"] = doc_refs
        fm["sources"] = sources
        fm["first_logged"] = TODAY
        fm["last_updated"] = TODAY
        text = ("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100)
                + "---\n\n" + body.strip() + "\n")
        self.written.append(rel)
        if not self.dry:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")


def src(system: str, method: str, ref: str) -> dict:
    return {"system": system, "method": method, "date": TODAY, "ref": ref}


# ---------------------------------------------------------------------------
# framework
# ---------------------------------------------------------------------------

DIMENSION_ORDER = ["persona", "solution", "institution", "ecosystem"]
STAGES = ["Explore", "Define", "Pilot", "Scale"]
THESIS = {"persona": "build-the-right-thing", "solution": "build-the-right-thing",
          "institution": "enable-adoption", "ecosystem": "enable-adoption"}

# Corpus examples in the question bank name pathways by title; map to slugs.
PATHWAY_NAME_TO_SLUG = {
    "MahaVISTAAR": "mahavistaar",
    "Blue Dots": "blue-dots",
    "Bhili Language Enablement": "bhili-language-enablement",
    "Voice AI for Inclusion": "voice-ai-for-inclusion",
    "Voice AI Adoption Barriers": "voice-ai-adoption-barriers",
    "African Voice AI": "african-voice-ai",
    "AI-Assisted Job Matching": "ai-assisted-job-matching",
    "Nivesh Suvidha": "nivesh-suvidha",
}


def parse_dimensions_ts(ts: str) -> dict[str, dict]:
    dims: dict[str, dict] = {}
    for block in re.finditer(r"code: '(\w+)',\s*name: '([^']+)',\s*centralQuestion: '([^']+)',"
                             r"\s*subCategories: \[(.*?)\n    \],", ts, re.S):
        code, name, cq, subs_raw = block.groups()
        subs = []
        for s in re.finditer(r"code: '([A-Z])',\s*name: '([^']+)',\s*weights: \{ Explore: '(\w+)', "
                             r"Define: '(\w+)', Pilot: '(\w+)', Scale: '(\w+)' \}", subs_raw):
            subs.append({"code": s.group(1), "name": s.group(2),
                         "weights": dict(zip(STAGES, s.groups()[2:]))})
        dims[code] = {"name": name, "central_question": cq, "subs": subs}
    colors = dict(re.findall(r"^\s+(\w+): '(#[0-9a-f]{6})'", ts, re.M))
    for code in dims:
        dims[code]["color"] = colors.get(code)
    return dims


def parse_framework(md: str) -> dict:
    out: dict = {}
    # cross-cutting concerns
    concerns: dict[str, dict[str, str]] = {"data": {}, "trust": {}}
    for key, label in (("data", "Data"), ("trust", "Trust")):
        block = section(md, rf"^\*\*{label}:\*\*", r"^\*\*|^## ")
        for dim, txt in re.findall(r"^- (Persona|Solution|Institution|Ecosystem) — (.+)$", block, re.M):
            concerns[key][dim.lower()] = txt.strip()
    out["concerns"] = concerns
    # 30/70
    m = re.search(r"\*\*30/70 thesis:\*\*\s*(.+)", md)
    out["thesis"] = m.group(1).strip() if m else ""
    # stages
    out["stages"] = {}
    for row in table_rows(section(md, r"^## The four adopter stages", r"^## ")):
        if row[0] in STAGES:
            out["stages"][row[0]] = {"central_question": row[1],
                                     "done_when": [s.strip() + "." for s in row[2].split(".") if s.strip()]}
    # question bank
    out["cells"] = {}
    for stage in STAGES:
        block = section(md, rf"^### {stage.upper()} — ", r"^### |^## ")
        for row in table_rows(block):
            if row[0] in ("Persona", "Solution", "Institution", "Ecosystem"):
                out["cells"][(row[0].lower(), stage)] = {
                    "core_question": row[1], "listening_for": row[2],
                    "insight_form": row[3], "corpus_example": row[4]}
    # exhaustive questions, per dimension number (2 is titled "Technology" = Solution)
    out["questions"] = {}
    out["shift"] = {}
    for num, dim in enumerate(DIMENSION_ORDER, 1):
        dblock = section(md, rf"^### {num}\. ", r"^### |^## ")
        sm = re.search(r"^\*(.+)\*$", dblock, re.M)
        out["shift"][dim] = sm.group(1).strip() if sm else ""
        for letter, sub in re.findall(r"^#### ([A-G])\. (.+)$", dblock, re.M):
            sblock = section(dblock, rf"^#### {letter}\. ", r"^#### ")
            out["questions"][(dim, letter)] = [q.strip() for q in re.findall(r"^- (.+)$", sblock, re.M)]
        intro = re.search(r"^(No population-scale.+)$", dblock, re.M)
        if intro:
            out.setdefault("dim_intro", {})[dim] = intro.group(1).strip()
    # unit types
    out["unit_types"] = []
    for row in table_rows(section(md, r"^## The five unit types", r"^\*\*Tag every")):
        if row[0] != "Type":
            out["unit_types"].append({"name": row[0], "definition": row[1], "reusable": row[2]})
    # pathway sections
    out["sections"] = []
    for row in table_rows(section(md, r"^## The pathway document — output structure", r"^## ")):
        if row[0] == "#":
            continue
        out["sections"].append({"num": row[0], "name": row[1], "purpose": row[2], "contents": row[3]})
    out["extraction"] = section(md, r"^## Extraction discipline", r"^## ").strip()
    out["source_trace"] = section(md, r"^## Source Trace appendix — specification", r"^## ").strip()
    out["pathway_def"] = section(md, r"^## The pathway document — output structure", r"^\| #").strip()
    return out


def seed_framework(w: Writer, repo: Path) -> None:
    fw_ref, dim_ref = "content/framework.md", "lib/dimensions.ts"
    dims = parse_dimensions_ts((repo / dim_ref).read_text(encoding="utf-8"))
    fw = parse_framework((repo / fw_ref).read_text(encoding="utf-8"))
    s_code = [src("diffusion_cube_code", "queried", dim_ref), src("diffusion_cube_code", "document", fw_ref)]

    # -- dimensions --------------------------------------------------------
    for order, code in enumerate(DIMENSION_ORDER, 1):
        d = dims[code]
        subs_md = "\n".join(f"- [{s['code']}. {s['name']}](../sub-categories/{code}-{s['code'].lower()}.md)"
                            for s in d["subs"])
        body = f"""## What it asks

{d['central_question']}

*{fw['shift'].get(code, '')}*

{fw.get('dim_intro', {}).get(code, '')}

## Sub-categories

{subs_md}

## Data and trust here

- **Data:** {fw['concerns']['data'].get(code, 'Not documented in the source')}
- **Trust:** {fw['concerns']['trust'].get(code, 'Not documented in the source')}

## How the companion uses it

Grid cells for this dimension are keyed `{code}:<Stage>` in `designs.grid_state`.
Which sub-categories the companion probes at a given stage is set by each
sub-category's stage weight. The dimension name is public vocabulary; the
sub-category letters are internal-only.
"""
        w.write("dimensions", code, "dimension", d["name"], {
            "aliases": [code], "summary": d["central_question"], "code": code,
            "central_question": d["central_question"], "shift": fw["shift"].get(code),
            "thesis_group": THESIS[code], "ui_color": d["color"],
            "data_concern": fw["concerns"]["data"].get(code),
            "trust_concern": fw["concerns"]["trust"].get(code), "order": order,
        }, body, s_code, code_refs=[dim_ref, fw_ref])

        # -- sub-categories ------------------------------------------------
        for s in d["subs"]:
            slug = f"{code}-{s['code'].lower()}"
            qs = fw["questions"].get((code, s["code"]), [])
            weights_tbl = "\n".join(f"| {st} | {s['weights'][st]} |" for st in STAGES)
            primary_at = [st for st in STAGES if s["weights"][st] == "primary"]
            body = f"""## What it covers

{d['name']} › **{s['code']}. {s['name']}** — part of "{d['central_question']}"

## Questions

{chr(10).join('- ' + q for q in qs) or 'Not documented in the source.'}

## Stage weighting

| Stage | Weight |
|---|---|
{weights_tbl}

Primary at: {', '.join(primary_at) or 'no stage'}. Primary = ask directly;
secondary = only if surfaced; dormant = never initiate.
"""
            w.write("sub-categories", slug, "sub_category", s["name"], {
                "aliases": [f"{d['name']} {s['code']}", f"{code}:{s['code']}"],
                "summary": f"{d['name']} sub-category {s['code']}: {s['name']}.",
                "dimension": code, "code": s["code"],
                "weight_explore": s["weights"]["Explore"], "weight_define": s["weights"]["Define"],
                "weight_pilot": s["weights"]["Pilot"], "weight_scale": s["weights"]["Scale"],
                "questions": qs,
            }, body, s_code, code_refs=[dim_ref, fw_ref])

    # -- stages ------------------------------------------------------------
    for i, st in enumerate(STAGES):
        info = fw["stages"].get(st, {})
        slug = st.lower()
        body = f"""## Central question

{info.get('central_question', '')}

## Done when

{chr(10).join('- ' + x for x in info.get('done_when', []))}

## What changes for each dimension

See the four cells: {', '.join(f'[{d.title()}](../cells/{d}-{slug}.md)' for d in DIMENSION_ORDER)}.

A deployment's stage is only ever taken from the user's own statement —
never assigned by the model (`designs.meta.stage`).
"""
        w.write("stages", slug, "stage", st, {
            "summary": info.get("central_question"), "order": i + 1,
            "central_question": info.get("central_question"),
            "done_when": info.get("done_when"),
            "previous_stage": STAGES[i - 1].lower() if i else None,
            "next_stage": STAGES[i + 1].lower() if i < 3 else None,
        }, body, s_code, code_refs=[dim_ref, fw_ref])

    # -- cells -------------------------------------------------------------
    for code in DIMENSION_ORDER:
        for st in STAGES:
            c = fw["cells"].get((code, st))
            if not c:
                continue
            ex_name = c["corpus_example"].split(":", 1)[0].strip()
            ex_slug = PATHWAY_NAME_TO_SLUG.get(ex_name)
            primary = [f"{code}-{s['code'].lower()}" for s in dims[code]["subs"]
                       if s["weights"][st] == "primary"]
            body = f"""## Core question

{c['core_question']}

## Listening for

{c['listening_for']}

## Insight form

{c['insight_form']}

## Corpus example

{c['corpus_example']}
"""
            w.write("cells", f"{code}-{st.lower()}", "cell", f"{dims[code]['name']} × {st}", {
                "aliases": [f"{code}:{st}"], "summary": c["core_question"],
                "dimension": code, "stage": st.lower(), "grid_key": f"{code}:{st}",
                "core_question": c["core_question"], "listening_for": c["listening_for"],
                "insight_form": c["insight_form"], "corpus_example": c["corpus_example"],
                "example_pathway": ex_slug, "primary_sub_categories": primary,
            }, body, s_code, code_refs=[fw_ref])

    # -- concepts ----------------------------------------------------------
    s_fw = [src("diffusion_cube_code", "document", fw_ref)]
    for ut in fw["unit_types"]:
        w.write("concepts", slugify(ut["name"]), "concept", ut["name"], {
            "aliases": [ut["name"]], "summary": ut["definition"], "concept_kind": "unit-type",
            "definition": ut["definition"], "audience": "internal-only",
            "what_makes_it_reusable": ut["reusable"], "broader": "unit",
            "code_identifier": ut["name"],
        }, f"## Definition\n\n{ut['definition']}\n\n## How it is used\n\nOne of the five types every corpus unit is tagged with (`unit_type` on `units/`).\n\n**What makes it reusable:** {ut['reusable']}\n",
            s_fw, code_refs=[fw_ref, dim_ref])

    for key, label in (("data", "Data"), ("trust", "Trust")):
        lines = "\n".join(f"- **{d.title()}** — {fw['concerns'][key].get(d, '')}" for d in DIMENSION_ORDER)
        w.write("concepts", f"{key}-cross-cutting-concern", "concept", f"{label} (cross-cutting concern)", {
            "aliases": [label], "concept_kind": "cross-cutting-concern",
            "summary": f"{label} is examined in every dimension, differently in each.",
            "definition": f"{label} is a concern that cuts across all four dimensions; each dimension asks a different {label.lower()} question.",
            "audience": "public-vocabulary",
        }, f"## Definition\n\n{label} cuts across all four dimensions.\n\n## How it is used\n\n{lines}\n", s_fw,
            code_refs=[fw_ref])

    for sec in fw["sections"]:
        name = sec["name"]
        slug = slugify(name) + "-section"
        num = sec["num"]
        audience = "contributor-only" if "Source Trace" in name else "public-vocabulary"
        w.write("concepts", slug, "concept", f"Pathway section: {md_clean(name)}", {
            "aliases": [md_clean(name)] + ([f"Section {num}"] if num else []),
            "concept_kind": "pathway-section", "summary": md_clean(sec["purpose"]),
            "definition": md_clean(f"{sec['purpose']}. Contents: {sec['contents']}"),
            "audience": audience, "broader": "pathway-document",
        }, f"## Definition\n\n**Section {num or '—'} — {name}.** {sec['purpose']}\n\n## How it is used\n\n{sec['contents']}\n",
            s_fw, code_refs=[fw_ref])

    extra = [
        ("unit", "Unit (micro-innovation)", "method",
         "An individually tagged piece of corpus knowledge — one of five unit types — carrying dimension, sub-category, stage, type and a condition tag.",
         "internal-only", ["Micro-innovation", "micro-innovation unit"], None),
        ("pathway-document", "Pathway document", "method",
         "A document written for the next adopter — what they would need to decide, the alternatives, and the conditions under which different choices are correct. Not a case study: a marked trail, not the pioneer's route. Sections 0–6 plus a contributor-only Source Trace appendix.",
         "public-vocabulary", ["pathway write-up"], None),
        ("condition-tag", "Condition tag", "method",
         "The applies-when / fails-when annotation every unit carries. It is what makes a decision reusable.",
         "internal-only", ["applies when / fails when"], "unit"),
        ("also-relevant-at", "Also relevant at", "grid-construct",
         "Optional cross-stage tag on a unit naming stages where it is useful beyond its stage of origin. Feeds retrieval only; never counts toward grid density.",
         "internal-only", [], "unit"),
        ("density", "Density", "grid-construct",
         "How well established a grid cell is, 0–3, rendered ○ / ● / ●● / ●●●. 0 means not yet established, never failed.",
         "internal-only", ["cell density", "○●"], "grid"),
        ("grid", "The 4×4 grid", "grid-construct",
         "Dimensions × stages, 16 cells. In a pathway it is the Section 2 coverage map; in an adoption it is designs.grid_state tracking what is known.",
         "internal-only", ["coverage grid", "grid_state", "cube"], None),
        ("stage-weighting", "Stage weighting (primary / secondary / dormant)", "weight-level",
         "Each sub-category is weighted per stage: primary = ask directly, secondary = only if surfaced, dormant = never initiate.",
         "internal-only", ["primary", "secondary", "dormant"], None),
        ("thirty-seventy-thesis", "30/70 thesis", "thesis", fw["thesis"], "internal-only", ["30/70"], None),
        ("synthesis-test", "The synthesis test", "method",
         "Could someone who never saw the raw material make a different decision because of this unit? If yes it is a real unit; if it just describes what happened, it is not.",
         "internal-only", [], "unit"),
        ("extraction-discipline", "Extraction discipline", "method",
         "The rules for turning raw material into units: tag every unit, write the before→after, name the failure specifically, flag gaps against primary sub-categories, never fabricate.",
         "internal-only", [], "unit"),
        ("matching-test", "Matching test (same sector AND use-case category)", "method",
         "'Relevant' means same sector and same use-case category — one test applied everywhere a pathway is surfaced. Adjacent matches are presented with the mismatch stated.",
         "internal-only", ["relevance test"], None),
    ]
    for slug, name, kind, definition, audience, aliases, broader in extra:
        w.write("concepts", slug, "concept", name, {
            "aliases": aliases, "summary": definition, "concept_kind": kind, "definition": definition,
            "audience": audience, "broader": broader,
        }, f"## Definition\n\n{definition}\n", s_fw, code_refs=[fw_ref])


# ---------------------------------------------------------------------------
# corpus
# ---------------------------------------------------------------------------

SECTOR_NORMALISE = {
    "Agriculture": "Agriculture", "Agriculture / Dairy": "Agriculture / Dairy",
    "Livelihoods": "Livelihoods", "Education": "Education", "Cross-Sector": "Cross-Sector",
    "Government / Investment Facilitation": "Industry and Investment",
}


def identity_field(body: str, label: str) -> str:
    """A value from the document's Pathway Identity table (| **Sector** | … |)."""
    m = re.search(rf"^\|\s*\**{label}\**\s*\|\s*(.+?)\s*\|\s*$", body, re.M | re.I)
    return md_clean(m.group(1)) if m else ""


def first_added(repo: Path, rel: str) -> str | None:
    out = subprocess.run(["git", "-C", str(repo), "log", "--diff-filter=A", "--format=%as", "--", rel],
                         capture_output=True, text=True).stdout.split()
    return out[-1] if out else None
# Pathways whose document states no sector: (sector, how derived)
DERIVED_SECTOR = {
    "nivesh-suvidha": "Industry and Investment",
    "ceew-climate-intelligence": "Public Health",
    "data-dhara": "Data Infrastructure",
}
PATHWAY_KIND = {
    "voice-ai-for-inclusion": "cross-deployment-synthesis",
    "voice-ai-adoption-barriers": "cross-deployment-synthesis",
    "data-dhara": "horizontal-enabler",
}
# contributor strings -> (slug, display name, aliases)
ORG_CANON = {
    "EkStep Foundation": ("ekstep-foundation", "EkStep Foundation", ["EkStep"]),
    "People+AI": ("people-plus-ai", "People+AI", []),
    "GCMMF (Amul)": ("gcmmf-amul", "GCMMF (Amul)", ["Amul", "Gujarat Cooperative Milk Marketing Federation"]),
    "Crane AI Labs": ("crane-ai-labs", "Crane AI Labs", []),
    "UNDP AI Hub for Sustainable Development": ("undp-ai-hub", "UNDP AI Hub for Sustainable Development", ["UNDP AI Hub"]),
    "DeepLeaf": ("deepleaf", "DeepLeaf", []),
    "Department of Agriculture, Government of Maharashtra": (
        "maharashtra-department-of-agriculture", "Department of Agriculture, Government of Maharashtra",
        ["GoM Agriculture Department"]),
    "OpenAgriNet (OAN)": ("openagrinet", "OpenAgriNet", ["OAN"]),
}
GOV = {"maharashtra-department-of-agriculture"}


def split_orgs(raw: str) -> list[str]:
    parts = re.split(r"\s*;\s*|\s+/\s+", raw or "")
    return [p.strip() for p in parts if p.strip()]


def parse_grid(body: str) -> dict:
    block = section(body, r"^#{1,3} .*4×4 Coverage Grid", r"^#{1,3} ")
    grid: dict = {}
    for row in table_rows(block):
        dim = row[0].replace("*", "").strip().lower()
        if dim not in DIMENSION_ORDER or len(row) < 5:
            continue
        for st, cell in zip(STAGES, row[1:5]):
            grid[f"{dim}:{st}"] = cell.count("●")
    return grid


def parse_gaps(body: str) -> list[str]:
    block = section(body, r"^#{1,3} Gaps", r"^#{1,3} ")
    return [md_clean(g) for g in re.findall(r"^\d+\.\s+(.+)$", block, re.M)]


def seed_corpus(w: Writer, repo: Path) -> None:
    grounding = repo / "content/wiki/pathways"
    library = repo / "content/library-wiki/pathways"
    index_text = (grounding / "index.md").read_text(encoding="utf-8")
    indexed = set(re.findall(r"\]\(([a-z0-9-]+)\.md\)", index_text))

    docs: dict[str, dict] = {}
    for corpus_slug, folder in (("grounding-corpus", grounding), ("library-corpus", library)):
        for f in sorted(folder.glob("*.md")):
            if f.name == "index.md":
                continue
            fm, body = split_frontmatter(f.read_text(encoding="utf-8"))
            d = docs.setdefault(f.stem, {"copies": [], "fm": {}, "body": "", "corpora": []})
            d["copies"].append(str(f.relative_to(repo)))
            d["corpora"].append(corpus_slug)
            if corpus_slug == "grounding-corpus" or not d["fm"]:
                # grounding copy wins for identity; library fills gaps
                merged = dict(fm)
                merged.update({k: v for k, v in d["fm"].items() if k not in fm})
                d["fm"] = merged
                d["body"] = body if corpus_slug == "grounding-corpus" or not d["body"] else d["body"]

    orgs: dict[str, tuple[str, list[str]]] = {}
    for slug, d in docs.items():
        fm, body = d["fm"], d["body"]
        title = fm.get("title")
        if not title:
            h1 = re.search(r"^# (.+)$", body, re.M)
            title = h1.group(1).strip() if h1 else slug
        raw_sector = str(fm.get("sector") or identity_field(body, "Sector") or "")
        sector, use_case, sector_src = None, None, "document"
        if raw_sector:
            head = re.split(r"\s+—\s+", raw_sector, maxsplit=1)
            sector = SECTOR_NORMALISE.get(head[0].strip()) or SECTOR_NORMALISE.get(raw_sector.strip())
            if raw_sector.strip() in SECTOR_NORMALISE and raw_sector.strip() != sector:
                use_case = raw_sector.strip()
            if len(head) > 1:
                use_case = head[1].strip()
        if not sector and slug in DERIVED_SECTOR:
            sector, sector_src = DERIVED_SECTOR[slug], "derived"
        org_slugs = []
        for raw in split_orgs(str(fm.get("contributor") or "")):
            oslug, oname, oalias = ORG_CANON.get(raw, (slugify(raw), raw, []))
            org_slugs.append(oslug)
            orgs.setdefault(oslug, (oname, oalias))
        in_grounding = "grounding-corpus" in d["corpora"]
        if in_grounding and slug in indexed:
            lifecycle = "published"
        elif in_grounding:
            lifecycle = "unindexed"
        else:
            lifecycle = "published"   # library corpus has no index; every file is listed
        stage = (str(fm.get("stage") or "").strip() or identity_field(body, "Stage reached")).split(" ")[0].lower() or None
        if stage not in ("explore", "define", "pilot", "scale"):
            stage = None
        published_on = first_added(repo, d["copies"][0]) if lifecycle == "published" else None
        grid = parse_grid(body)
        gaps = parse_gaps(body)
        sources = [src("diffusion_cube_code", "document", c) for c in d["copies"]]
        if published_on:
            sources.append(src("github_repo", "derived", f"published_on = date {d['copies'][0]} was first committed"))
        if sector_src == "derived":
            sources.append(src("diffusion_cube_code", "derived", "sector inferred from title/tags; document states none"))
        grid_md = ""
        if grid:
            grid_md = "| | " + " | ".join(STAGES) + " |\n|---|---|---|---|---|\n" + "\n".join(
                f"| {dm.title()} | " + " | ".join(["○", "●", "●●", "●●●"][grid.get(f'{dm}:{st}', 0)] for st in STAGES) + " |"
                for dm in DIMENSION_ORDER)
        notes = []
        if lifecycle == "unindexed":
            notes.append("On disk in the grounding corpus but **not linked from `content/wiki/pathways/index.md`**, "
                         "so excluded from grounding and the /wiki listing (TD-07). It may still be live via "
                         "`published_pathways` — check the DB before calling it unpublished.")
        if len(d["copies"]) > 1:
            notes.append("Exists in **both** in-repo corpora as independently maintained documents (TD-02) — "
                         "same slug, different text.")
        body_md = f"""## Identity

{md_clean(str(fm.get('description') or ''))}

Contributed by: {fm.get('contributor') or 'Not documented in the source'}.

## Coverage

{grid_md or 'The document carries no parseable 4×4 coverage grid.'}

## Gaps

{chr(10).join('- ' + g for g in gaps) or 'None named in the document.'}

## Where the reusable value is

Not yet extracted — run the cube-brain skill's *ingest pathway* operation to
create its `units/`.

## Corpus copies

{chr(10).join('- `' + c + '`' for c in d['copies'])}

{chr(10).join(notes)}
"""
        w.write("pathways", slug, "pathway", md_clean(str(title)), {
            "aliases": [md_clean(str(title))] if md_clean(str(title)) != slug else [],
            "summary": md_clean(str(fm.get("description") or "")) or None,
            "tags": fm.get("tags") or [], "title": md_clean(str(title)),
            "pathway_kind": PATHWAY_KIND.get(slug, "single-deployment"),
            "sector": sector, "use_case_category": use_case, "stage_reached": stage,
            "contributing_organisations": org_slugs, "coverage": grid or None, "gaps": gaps,
            "corpora": sorted(set(d["corpora"])), "corpus_files": d["copies"],
            "lifecycle": lifecycle, "published_on": published_on, "document_version": fm.get("version"),
        }, body_md, sources, code_refs=d["copies"])

    for oslug, (oname, oalias) in orgs.items():
        kinds = ["contributing-organisation"]
        if oslug == "ekstep-foundation":
            kinds = ["product-owner", "contributing-organisation"]
        if oslug in GOV:
            kinds.append("government-body")
        w.write("organisations", oslug, "organisation", oname, {
            "aliases": oalias, "org_kinds": kinds,
        }, "## Relationship to the Cube\n\nNamed as a contributor on one or more corpus pathways "
           "(see the generated Related section).\n",
            [src("diffusion_cube_code", "document", "content/wiki/pathways/*.md frontmatter `contributor`")])

    # -- corpora -----------------------------------------------------------
    w.write("corpora", "grounding-corpus", "corpus", "Grounding corpus", {
        "aliases": ["content/wiki/pathways", "wiki corpus"],
        "summary": "In-repo pathway documents the Explorer and Contributor flows are grounded in, whole-corpus.",
        "corpus_kind": "static-repo", "location": "content/wiki/pathways",
        "index_file": "content/wiki/pathways/index.md", "grounding_scope": "whole corpus (~22K tokens with framework)",
        "voice": "advisory, framework-tagged, drives <grid_update>", "merges_with": ["published-pathways-corpus"],
    }, """## What it is

The framework-structured pathway documents (Sections 0–6 + Source Trace) committed in the repo.

## How it is loaded

`lib/wiki-loader.ts` reads files linked from `index.md` (the sole discovery path), merges
`published_pathways` rows by slug (DB wins). `lib/wiki-content.ts` is a second read path for
`/wiki` browsing, stripping frontmatter and the Source Trace appendix.

## Divergence from other corpora

Shares several slugs with the library corpus but the documents are maintained independently (TD-02).
""", [src("diffusion_cube_code", "queried", "lib/wiki-loader.ts"), src("diffusion_cube_docs", "document", "docs/wiki/diffusion-cube/integrations/ai-llm.md")],
        code_refs=["content/wiki/pathways", "lib/wiki-loader.ts", "lib/wiki-content.ts"])
    w.write("corpora", "library-corpus", "corpus", "Library corpus", {
        "aliases": ["content/library-wiki/pathways", "Diffusion Library"],
        "summary": "In-repo, conversational-tone pathway documents behind the public /explore library, grounded one document at a time.",
        "corpus_kind": "static-repo", "location": "content/library-wiki/pathways",
        "grounding_scope": "one document at a time", "voice": "conversational, no grid",
        "merges_with": ["published-pathways-corpus"],
    }, """## What it is

Overview-style pathway documents for the public, no-login Diffusion Library (`/explore`).

## How it is loaded

`lib/library-wiki-loader.ts`; no index file. Merged with `published_pathways` by slug (DB wins).

## Divergence from other corpora

Not the same documents as the grounding corpus even where slugs match (TD-02).
""", [src("diffusion_cube_code", "queried", "lib/library-wiki-loader.ts")],
        code_refs=["content/library-wiki/pathways", "lib/library-wiki-loader.ts"])
    w.write("corpora", "published-pathways-corpus", "corpus", "Published pathways (database corpus)", {
        "aliases": ["published_pathways"],
        "summary": "Community-contributed pathways made live by admin publish; merged into both in-repo corpora at read time.",
        "corpus_kind": "database", "location": "published_pathways",
        "grounding_scope": "merged into both corpora by slug",
    }, """## What it is

Rows in the `published_pathways` table, public-read. The only place community content goes live —
written by `POST /api/admin/pathways/publish`, no redeploy needed.

## Who reads it

All three corpus loaders. A DB row overrides an in-repo file with the same slug.
""", [src("diffusion_cube_code", "queried", "supabase/migrations/0012_published_pathways.sql")],
        code_refs=["supabase/migrations/0012_published_pathways.sql", "app/api/admin/pathways/publish/route.ts"])


# ---------------------------------------------------------------------------

def main() -> int:
    here = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=os.environ.get("CUBE_REPO", str(here.parent / "diffusion-cube")))
    ap.add_argument("--brain", default=str(here))
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", choices=["framework", "corpus"], help="seed one layer")
    args = ap.parse_args()

    repo, brain = Path(args.repo).resolve(), Path(args.brain).resolve()
    if not (repo / "lib/dimensions.ts").is_file():
        print(f"not a diffusion-cube checkout: {repo}", file=sys.stderr)
        return 2
    commit = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                            capture_output=True, text=True).stdout.strip()
    w = Writer(brain, commit, args.force, args.dry_run)
    if args.only in (None, "framework"):
        seed_framework(w, repo)
    if args.only in (None, "corpus"):
        seed_corpus(w, repo)
    print(f"{'would write' if args.dry_run else 'wrote'} {len(w.written)} files; "
          f"kept {len(w.skipped)} existing (use --force to overwrite)")
    for p in w.written:
        print("  +", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
