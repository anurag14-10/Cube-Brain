# Ingest a pathway into the Cube-Brain

Turns one pathway document into a `pathways/` entry, its `units/` (Section 5
patterns included), and the organisations/people it names. The framework's own
extraction discipline (content/framework.md § Extraction discipline) governs
every step — this file applies it to the brain.

## 0. Locate the source

| Where the pathway lives | Source to read |
|---|---|
| Grounding corpus | `$CUBE_REPO/content/wiki/pathways/<slug>.md` (framework-structured — primary) |
| Library corpus only | `$CUBE_REPO/content/library-wiki/pathways/<slug>.md` (overview tone — extract only substantive units; mark inferred tags `method: derived`) |
| DB only (`published_pathways`) | the document the user supplies, or, with the user's go-ahead, `python3 scripts/probe_published_pathways.py --content <slug>` (anon key from env; the published document only — never user rows). Record `sources: {system: supabase_db, method: queried}` and add `published-pathways-corpus` to `corpora` |

The slug is the corpus file's stem, typos included (`unififed-ai-driven-agri-ecosystem`).

## 1. Pathway entity

1. `python3 scripts/seed_from_repo.py --only corpus --dry-run` shows whether a
   stub would be created. For a NEW pathway, run it without `--dry-run` (it
   never overwrites existing files).
2. Read `pathways/<slug>.md`, then fill from Sections 1–2 of the document:
   geography, population_served, key_dates, scale_impact (with as-of date),
   cost_anchor (with as-of date), build_effort, downstream_adoptions,
   contributing/deploying/partner organisations, contributors, related or
   synthesised pathways. Replace the "Where the reusable value is" placeholder.
3. `lifecycle`: `published` only if linked from `index.md` (grounding), present
   in the library corpus, or confirmed in `published_pathways`; `unindexed` if
   on disk but not in `index.md`; `assembled` if only committed via assemble.

## 2. Units — one per micro-innovation

For every unit in Section 3 (keep its number in `source_unit_id`):

| Field | How |
|---|---|
| `unit_type` | Exact MASTERS 1 term. A single procedural-sounding decision is a Decision, not a Playbook. A decision about how to structure something is a Decision, not a Toolkit Asset. |
| `dimension`, `sub_category` | The sub-category MUST belong to the dimension (`institution-c` only with `institution`). The dimension's concept page (`concepts/<dimension>.md`) lists its sub-categories, their names and stage weights. All three tags are MASTERS variables (2, 4, 3). |
| `stage` | Stage of ORIGIN — where the evidence came from. This is what counts in the grid. |
| `also_relevant_at` | Retrieval only. Never includes the origin stage. |
| `applies_when` / `fails_when` | The condition tag. Required. `Not documented in the source` if absent — never invent. |
| Decision units | `decision`, `before`, `after` required; `alternative_considered`, `reason`, `context` when stated. |
| Failure and Fix | `failure`, `fix`, `insight` (the structural lesson the fix revealed). |
| Playbook | `steps` in order, with the gate between them; `common_failure_mode`. |
| Toolkit Asset | `purpose`, `reuse_condition`; `asset_kind`/`asset_link`/`share_consent: true` only if an actual file/https link exists and was consented. |
| `adopter_intents` | From the Section 6 retrieval guide entries that point at this unit. |

Slug: `<pathway>-<short-name>` (kebab, ≤ 6 words). Body: `## Unit` ·
`## Condition` · `## Before → after` · `## Why it is reusable`, attributing
the account to the contributor.

Apply **the synthesis test** to each: could someone who never saw the raw
material make a different decision because of it? If not, do not create it.

Section 4 (toolkits & playbooks): create a unit only for rows that are a real
artifact or gated sequence not already captured; otherwise link the existing
unit via `related_units`.

## 3. Patterns

From Section 5 (problem → root cause → solution → result → condition). A
pattern is a unit with `unit_type: Problem-Solution Pattern`, carrying
`problem`, `root_cause`, `solution`, `result`, `condition`, `evidence_units`
and the `pathways` / `dimensions` / `stages` it spans. Grep
`grep -l "^unit_type: Problem-Solution Pattern" units/*.md` first — if the same
problem exists, extend its `evidence_units` and `pathways` instead of creating
a duplicate. Slug `<pathway>-<short-name>`, or `pattern-<short-name>` once it
spans pathways. A pattern with one piece of evidence is fine to record but say
so in the body.

## 4. Actors

Organisations and people the document names: reuse existing slugs (check
`INDEX.md`); create new ones only with professional role/involvement. Never
copy contact details.

## 5. Never

- Never copy the **Source Trace / Provenance appendix** into any entry — it is
  contributor-only. Record source files only in `sources` / `doc_refs`.
- Never add facts the document does not contain. The brain summarises; it does
  not improve the contributor's account.
- Never use sub-category codes or density symbols in prose meant for adopters.

## 6. Finish

`python3 scripts/validate_wiki.py .` (fix all errors and the unit-rule warnings
you introduced) → `python3 scripts/cube_report.py --section corpus` to show the
new coverage and `--section grid` to check the pathway's `coverage` map against
its units → `python3 scripts/check_corpus_drift.py` shows it no longer
`not-ingested` → activity entry → one commit:
`cube-brain: ingest pathway <slug> (<n> units, <m> patterns)`, written by the
route in `write-route.md` — straight to `main` for an admin, otherwise a
capture branch and a PR holding only the pathway, unit, actor and activity
entry files (§3).
