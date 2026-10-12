# Conventions — Cube-Brain

The rules for writing to this brain. Written so any teammate or any agent
(with or without the `cube-brain` skill) can add an entry that validates and
fits the graph.

- **`SCHEMA.yml`** is the machine-readable model: entity types, fields,
  references, rules. When this file and `SCHEMA.yml` disagree, `SCHEMA.yml`
  wins and this file is wrong.
- **`MASTERS.md`** holds every controlled vocabulary — including the
  framework's closed sets (dimensions, stages, sub-categories, grid keys),
  the corpora and the teams. Do not invent values.
- **`SOURCES.md`** says which systems may corroborate an entry;
  **`SOURCE-SEMANTICS.md`** says what each of them means here.

## Scope

This brain holds **the knowledge of the Diffusion Cube project** (product
name "Diffusion Cube | 100 Pathways", repository `diffusion-cube`, the
conversational companion to 100pathways.com):

1. **The framework and the corpus** — the AI Diffusion Pathway Framework
   (dimensions with their sub-categories and grid cells, stages, unit types,
   every framework concept and product rule), the pathways and their
   micro-innovation units, patterns included.
2. **The actors** — organisations and people (professional role only), with
   team membership as a variable.
3. **Delivery** — the decisions behind the framework, corpus and programme,
   the dated risks, and the charter milestones.

It does **not** hold:

- **The app's code level** — pages, API endpoints, chat modes, prompts,
  tables, migrations, modules, integrations, env vars, environments,
  releases, tech debt, incidents. The code and its git history are their own
  record. Schema v1 modelled all of it; the last commit that has it is
  `0296ca8` — restore from there if it is ever wanted again.
- **Secrets or config values** of any kind.
- **Personal data** — no emails, phones, or personal details; no user data
  from the production database (adoptions, chats, registrations). Count or
  describe; never copy rows.
- **Commercial terms** — contract values, rates, invoices. Those belong in a
  commercial brain, not here.
- **Other Tekdi projects.** A pathway or organisation unrelated to the Cube
  goes to the company brain (`anurag14-10/Anurag-Brain` or the company
  wiki), not here. A pathway that *is* in the Cube's corpus belongs here even
  if another brain also has it — note the other brain in `external_refs`.
- **Full document copies.** A pathway entry summarises and links
  (`doc_refs`); the canonical text stays in the diffusion-cube repo or
  `published_pathways`.
- **Sprint-level task tracking.** Only a charter-level requirement is
  recorded, as a milestone's `deliverables`.

## Schema version

Current schema version: **2**

Every entity file carries `schema_version: 2`. A file below the current
version is stale; it is migrated when touched, and in bulk when somebody
explicitly asks. **A bump ships with its migrator** (`scripts/migrate_vN_to_vM.py`)
or it is not finished.

### Version history

**Whoever bumps the version records the field-level mapping from the
previous one.** Never bump without it.

- **v1** (2026-10-08): Initial schema. 34 entity types in six layers
  (framework, corpus, actors, product, knowledge, delivery), 32 masters.
- **v2** (2026-10-12): 8 entity types in three layers, 19 masters. Migrator:
  `scripts/migrate_v1_to_v2.py`.
  - `dimensions/`, `sub-categories/`, `stages/`, `cells/` → variables
    (MASTERS 2, 4, 3, 5) plus one concept page per dimension (carrying its
    sub-categories' weights and questions and its four cells) and per stage
    (`concept_kind: dimension | stage`).
  - `rules/` → `concepts/` (`concept_kind: rule`; `statement` → `definition`,
    `rationale` kept; `enforcement`, `enforced_in`, `applies_to_modes` dropped).
  - `patterns/` → `units/` (`unit_type: Problem-Solution Pattern`).
  - `corpora/`, `teams/` → variables (MASTERS 13, 15); slugs unchanged.
  - Removed: `roles/` and the whole product layer, plus `requirements/`,
    `releases/`, `tech-debt/`, `incidents/`. TD-16 (vendor account expiry)
    became the risks `anthropic-account-expiry` and `aws-account-expiry`.
  - Every entry: `code_refs` → `doc_refs`; `verified_at_commit` dropped.
    Pathway `corpus_files` → `doc_refs`. Concept `code_identifier` dropped.
    Decision `affects_*` dropped. Risk `integration` → `organisation`,
    `affects_features` dropped. Unit `pathway` / `dimension` / `sub_category`
    / `stage` are now required by rule for the five framework unit types.

Retire a field over two versions — keep it populated as an alias, remove it
once nothing reads it.

---

## Entity types

| Layer | Folder | Type | Holds |
|---|---|---|---|
| Framework + corpus | `concepts/` | `concept` | Dimensions (with sub-categories and cells), stages, unit types, sections, methods, product rules — every defined term |
| Framework + corpus | `pathways/` | `pathway` | One documented deployment journey |
| Framework + corpus | `units/` | `unit` | One tagged micro-innovation from a pathway, or a problem→solution pattern across units |
| Actors | `organisations/` | `organisation` | Any organisation involved, any capacity (vendors included) |
| Actors | `people/` | `person` | Individuals — professional involvement only |
| Delivery | `decisions/` | `decision` | Decision records about framework, corpus, programme |
| Delivery | `risks/` | `risk` | Forward-looking threats, dated |
| Delivery | `milestones/` | `milestone` | Dated charter milestones and their deliverables |

**Variables, not folders** (MASTERS.md): dimension (2), stage (3),
sub-category (4), grid key (5), corpus (13), team (15).

Not entities: `activities/` (the capture ledger), `scripts/`, `site/`,
`skills/`, `reports/`, and `staging/` on per-person branches.

### Choosing the right type — the questions people get wrong

| If it is… | It is a… | Not a… |
|---|---|---|
| A reusable lesson from a *deployment in the corpus* | `unit` | `decision` (that is the Cube's own choice) |
| A pattern seen across several units/pathways | `unit` with `unit_type: Problem-Solution Pattern` | a new folder |
| A choice the *Cube team* made about the framework, corpus or programme | `decision` | `unit` |
| A rule the Cube must always keep | `concept` with `concept_kind: rule` | `decision` |
| A dated external threat (account expiry, dependency) | `risk` | — |
| A charter line saying something should exist by a date | a milestone's `deliverables` | evidence that it exists |
| A dimension, stage, sub-category, cell, corpus or team | a MASTERS.md value (definition on its concept page) | a new entity |
| A route, table, migration, env var or code file | out of scope — the code is its record | anything here |
| A word that needs defining | `concept` | a new folder |

---

## Slugs

Lowercase, hyphenated, ASCII. Slugs are the join key — every reference field
holds slugs. **Framework values are fixed** and must be used exactly:

| What | Form | Examples |
|---|---|---|
| dimension (variable + concept slug) | `<code>` | `persona`, `solution`, `institution`, `ecosystem` |
| stage (variable + concept slug) | `<name>` | `explore`, `define`, `pilot`, `scale` |
| sub_category (variable) | `<dimension>-<letter>` | `persona-a`, `solution-e`, `institution-g`, `ecosystem-f` |
| grid key (variable, `coverage` map key) | `<dimension>:<Stage>` | `persona:Explore`, `ecosystem:Scale` |
| concept (unit type) | name | `strategic-decision`, `failure-and-fix`, `toolkit-asset` |
| pathway | the corpus file slug | `blue-dots`, `mahavistaar`, `unififed-ai-driven-agri-ecosystem` (typo is the real slug — keep it, add an alias) |
| unit | `<pathway>-<short-name>`; a cross-pathway pattern `pattern-<short-name>` | `mahavistaar-api-gateway-separation` |
| organisation / person | name | `ekstep-foundation`, `amazon-web-services`, `anurag-goutam` |
| decision / risk / milestone | descriptive | `anthropic-account-expiry`, `web-app-with-20-pathways` |

Before creating anything, check `INDEX.md` (slugs + aliases) and run
`scripts/find_duplicates.py .`. A near-duplicate is worse than a merge.

---

## Edge directions

References are stored on **one side only**. The reverse is derived. Never add
a field to "the other side" to make a link visible — run
`scripts/build_backlinks.py` instead.

| Stored on | Field | Points at |
|---|---|---|
| concept | `broader`, `see_also` | concept |
| unit | `pathway`, `related_units`, `evidence_units`, `pathways` | pathway, unit |
| pathway | `*_organisations`, `contributors`, `synthesises`, `related_pathways` | organisation, person, pathway |
| organisation | `parent_organisation` | organisation |
| person | `affiliations` | organisation |
| decision | `decided_by`, `supersedes` | person, decision |
| risk | `organisation` | organisation |

Variables (`dimension`, `stage`, `sub_category`, `also_relevant_at`,
`corpora`, `teams`, `owner_team` …) are not edges; the site and the backlink
builder do not draw them. Find "everything at Ecosystem × Scale" by grepping
the fields (`grep -l "^stage: scale" units/*.md | xargs grep -l "^dimension: ecosystem"`).

The rule of thumb: **the more specific or more volatile entity points at the
more stable one.** A unit names its pathway; a pathway never lists its units.

**Every slug in a reference field must exist after the commit.** Create the
target in the same commit, or leave the name in the body prose. A dangling
reference turns the build red.

---

## Dates

| Field | Means |
|---|---|
| `first_logged` | When this entry was added to the brain. Bookkeeping only. |
| `last_updated` | When this entry was last edited. Bookkeeping only. |
| `last_reviewed` | When a person confirmed it is still TRUE. |
| `decided_on`, `target_date`, `due_date`, `published_on` | When the real-world thing happened / is due. Blank if unknown — never default it to today. |

All dates `YYYY-MM-DD`. Conflating "when we wrote it down" with "when it
happened" is the most common way a brain goes wrong.

---

## Provenance

Every entry records what it rests on in `sources`:

```yaml
sources:
  - { system: diffusion_cube_code, method: queried, date: 2026-10-08, ref: lib/dimensions.ts }
  - { system: conversation, method: stated, date: 2026-10-08 }
```

| `method` | Means |
|---|---|
| `queried` | Read directly from a system of record (the code, the DB schema, GitHub) |
| `document` | Read from a document (framework.md, a pathway doc, the charter, a spec) |
| `stated` | Somebody said it; not checked |
| `derived` | Inferred (e.g. a feature's status inferred from routes existing) — must not read like verified |
| `public` | From a public source |

`system` must be a source id from `SOURCES.md`.

When two sources disagree, record both in `contested` and say which one the
stronger source supports — do not silently pick.

For anything about the **framework**: `content/framework.md` +
`lib/dimensions.ts` are authoritative (they transcribe the Pathway Framework
PDF). For a **pathway's content**: the pathway document is authoritative; the
brain summarises it and never adds facts the document does not contain.

---

## Frontmatter — every entry

```yaml
---
name: Human-readable name            # required
type: <entity type from SCHEMA.yml>  # required, must match the folder
schema_version: 2                    # required
aliases: []                          # old names, spellings
summary: One or two sentences.
tags: []
doc_refs: []                         # repo-relative paths: framework, pathway docs, specs, raw docs
sources: []
first_logged: 2026-10-12
last_updated: 2026-10-12
---
```

Then the type-specific fields from `SCHEMA.yml`. Leave unknowns **blank** (or
omit the key). Never fill a field to make an entry look complete.

## Body — what goes under the frontmatter

Bodies are markdown. Each type has a fixed skeleton so entries read alike and
an agent knows where to find things. Omit a heading only if there is genuinely
nothing; do not invent content to fill one. Never hand-write a `## Related`
section — it is generated.

| Type | Body skeleton |
|---|---|
| concept (dimension) | `## Definition` · `## Sub-categories` (weight table, then `### <letter>. <name>` with its questions) · `## Grid cells` (one `### <Dimension> × <Stage>` per stage: core question, listening for, insight form, corpus example) · `## Data and trust here` · `## How it is used` |
| concept (stage) | `## Definition` · `## Done when` · `## What changes for each dimension` · `## How it is used` |
| concept (rule) | `## Rule` · `## Why` · `## Known violations / gaps` |
| concept (other) | `## Definition` · `## How it is used` · `## Not to be confused with` |
| pathway | `## Identity` · `## Effort` · `## Coverage` (the 4×4 grid table) · `## Gaps` · `## Where the reusable value is` · `## Corpus copies` |
| unit | `## Unit` (the decision/failure/playbook/asset, in the framework's own form) · `## Condition` (applies when / fails when) · `## Before → after` · `## Why it is reusable` |
| unit (pattern) | `## Problem` · `## Root cause` · `## Solution` · `## Result` · `## Condition` · `## Evidence` |
| organisation | `## Relationship to the Cube` · `## Notes` |
| person | `## Involvement` |
| decision | `## Context` · `## Decision` · `## Alternatives considered` · `## Consequences` |
| milestone | `## Outcome` · `## Deliverables` · `## Status` |
| risk | `## Risk` · `## Impact if it happens` · `## Mitigation` |

Body links use relative paths (`[Blue Dots](../pathways/blue-dots.md)`) so
they work when browsing the repo. Link a dimension or stage to its concept
page (`[Persona](../concepts/persona.md)`).

---

## Corpus extraction rules (from the framework)

These are the framework's own extraction discipline, applied to `units/`.

1. **Tag every unit**: dimension + sub_category + stage + unit_type +
   condition (applies_when / fails_when). No untagged units. All three tags
   are variables (MASTERS 2, 4, 3). The `sub_category` must belong to the
   unit's `dimension` (`persona-c` only with `persona`) — the validator's
   `sub-category-outside-dimension` rule fails the build otherwise; the
   dimension's concept page lists its sub-categories and their stage weights.
2. **`stage` is the stage of origin** (where the evidence was found) and is
   what counts in a pathway's coverage grid (`python3 scripts/cube_report.py
   --section grid` puts each pathway's `coverage` map beside its units). `also_relevant_at` is retrieval
   only and never counts. Never merge the two, and never list the origin
   stage in `also_relevant_at`.
3. **Write the before→after** for every Strategic/Tactical Decision.
4. **Name the failure specifically** for Failure and Fix: failure, fix, and
   the insight the fix revealed.
5. **A Playbook is a gated sequence.** A single procedural-sounding decision
   is a Decision. A **Toolkit Asset is an artifact**; a decision about how to
   structure something is a Decision.
6. **Don't fabricate.** Where the pathway does not say, write
   `Not documented in the source` — that is a valid value for the condition
   tag and for before/after.
7. **The synthesis test**: could someone who never saw the raw material make
   a different decision because of this unit? If not, it is not a unit.
8. **Attribute.** A unit is the contributor's account. Body prose says
   "According to <contributor>'s <pathway> pathway…", never states it as fact.
9. **Source Trace is contributor-only.** Do not copy a pathway's Source Trace
   appendix into a unit or pathway body. Record which raw files fed a pathway
   only in `sources` / `doc_refs`.
10. **A pattern is a unit too.** A pathway's Section 5 problem→solution
    pattern is a unit with `unit_type: Problem-Solution Pattern`, `problem`,
    `root_cause`, `solution`, `result`, `condition`, its `evidence_units`, and
    the `pathways` / `dimensions` / `stages` it spans. Before writing one,
    grep units for the same problem and extend its evidence instead.

## Delivery capture rules

1. **Intent is never evidence.** A milestone and its deliverables are what
   the charter wants by a date — never cite them as built.
2. **Risks carry a date** where the source gives one, and name the vendor or
   partner in `organisation`. An open risk past its `due_date` turns the
   validator's warning on; act or re-date it.
3. **A decision keeps its reasoning.** Superseded decisions stay, pointing at
   their successor.
4. **No values, no secrets, no user data.**

## General rules

1. **Leave unknowns blank.** A blank is honest; a plausible guess becomes
   fact within weeks.
2. **Read before writing.** Never overwrite a file you have not read; merge.
3. **One commit per logging event**, with message prefix `cube-brain:`.
4. **Never commit credentials**, tokens, keys or env values.
5. **No personal information** — professional role and involvement only.
6. **Prefer merging to duplicating.** Check `INDEX.md` first.
7. **Don't invent vocabulary.** Propose an addition to `MASTERS.md`.
8. **Absence is not permission.** Nothing here is cleared for publication.
9. **Validate before you commit**: `python3 scripts/validate_wiki.py .` must
   exit 0.

## Activity log format

Each capture writes one entry file
`activities/entries/{YYYY-MM}/{YYYY-MM-DDTHHMMSSZ}-{writer}-a1.md`
containing one line:

```
- {YYYY-MM-DD}: [{type}] {name} — {one-line summary}
```

`activities/{YYYY-MM}.md` is generated from the entry files
(`scripts/build_activity_log.py`) — never edit it by hand. The log records
what was decided and on whose authority; git records what changed.
