# Conventions — Cube-Brain

The rules for writing to this brain. Written so any teammate or any agent
(with or without the `cube-brain` skill) can add an entry that validates and
fits the graph.

- **`SCHEMA.yml`** is the machine-readable model: entity types, fields,
  references, rules. When this file and `SCHEMA.yml` disagree, `SCHEMA.yml`
  wins and this file is wrong.
- **`MASTERS.md`** holds every controlled vocabulary. Do not invent values.
- **`SOURCES.md`** says which systems may corroborate an entry;
  **`SOURCE-SEMANTICS.md`** says what each of them means here.

## Scope

This brain holds **everything about the Diffusion Cube project** (product
name "Diffusion Cube | 100 Pathways", repository `diffusion-cube`, the
conversational companion to 100pathways.com):

1. **The framework** it operationalises — the AI Diffusion Pathway Framework:
   dimensions, sub-categories, stages, the 16 grid cells, unit types and every
   framework concept.
2. **The corpus** it is grounded in — pathways, their micro-innovation units,
   problem→solution patterns, and the corpora that hold them.
3. **The actors** — organisations, people (professional role only), teams and
   the app's access roles.
4. **The product** — features, workflows, pages, API endpoints, chat modes,
   prompts, data contracts, tables, migrations, code modules, integrations,
   config variables and environments.
5. **The knowledge behind the product** — the rules it keeps and the
   decisions that shaped it.
6. **Delivery** — requirements, milestones, releases, tech debt, risks and
   incidents.

It does **not** hold:

- **Secrets or config values** of any kind — names of variables only.
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
  (`corpus_files`); the canonical text stays in the diffusion-cube repo or
  `published_pathways`.
- **Sprint-level task tracking.** A task becomes a `requirement` only when it
  is a charter/spec-level requirement.

## Schema version

Current schema version: **1**

Every entity file carries `schema_version: 1`. A file below the current
version is stale; it is migrated when touched, and in bulk when somebody
explicitly asks. **A bump ships with its migrator** (`scripts/migrate_vN_to_vM.py`)
or it is not finished.

### Version history

**Whoever bumps the version records the field-level mapping from the
previous one.** Never bump without it.

- **v1** (2026-10-08): Initial schema. 34 entity types in six layers
  (framework, corpus, actors, product, knowledge, delivery), 32 masters.

Retire a field over two versions — keep it populated as an alias, remove it
once nothing reads it.

---

## Entity types

| Layer | Folder | Type | Holds |
|---|---|---|---|
| Framework | `dimensions/` | `dimension` | Persona · Solution · Institution · Ecosystem (closed set of 4) |
| Framework | `sub-categories/` | `sub_category` | The 22 lettered sub-categories with per-stage weights |
| Framework | `stages/` | `stage` | Explore · Define · Pilot · Scale (closed set of 4) |
| Framework | `cells/` | `cell` | The 16 dimension×stage question-bank cells |
| Framework | `concepts/` | `concept` | Every other named idea + the glossary |
| Corpus | `pathways/` | `pathway` | One documented deployment journey |
| Corpus | `units/` | `unit` | One tagged micro-innovation from a pathway |
| Corpus | `patterns/` | `pattern` | Problem→solution patterns across units |
| Corpus | `corpora/` | `corpus` | Grounding corpus, library corpus, published_pathways |
| Actors | `organisations/` | `organisation` | Any organisation involved, any capacity |
| Actors | `people/` | `person` | Individuals — professional involvement only |
| Actors | `teams/` | `team` | Solution Team, Program Team … |
| Actors | `roles/` | `role` | adopter, pathway_contributor, admin, general_user, anonymous |
| Product | `features/` | `feature` | User-facing capabilities |
| Product | `workflows/` | `workflow` | End-to-end flows with ordered steps (W1…) |
| Product | `pages/` | `page` | UI routes |
| Product | `endpoints/` | `endpoint` | API route handlers and hooks |
| Product | `chat-modes/` | `chat_mode` | The 8 `/api/chat` modes |
| Product | `prompts/` | `prompt` | System-prompt builders and fixed prompts |
| Product | `contracts/` | `contract` | Non-table data shapes (grid_update, meta …) |
| Product | `tables/` | `table` | Postgres tables and storage buckets |
| Product | `migrations/` | `migration` | Numbered SQL migrations |
| Product | `modules/` | `module` | Source files / code units |
| Product | `integrations/` | `integration` | External services |
| Product | `config/` | `config_var` | Environment variable names (never values) |
| Product | `environments/` | `environment` | Where the app runs |
| Knowledge | `rules/` | `rule` | Product/business rules and where enforced |
| Knowledge | `decisions/` | `decision` | Decision records (ADRs) |
| Delivery | `requirements/` | `requirement` | Charter/spec requirements |
| Delivery | `milestones/` | `milestone` | Dated charter milestones |
| Delivery | `releases/` | `release` | Shipped change sets (PRs/deploys) |
| Delivery | `tech-debt/` | `tech_debt` | The TD register |
| Delivery | `risks/` | `risk` | Forward-looking threats, dated |
| Delivery | `incidents/` | `incident` | Things that actually broke |

Not entities: `activities/` (the capture ledger), `scripts/`, `site/`,
`skills/`, `reports/`, and `staging/` on per-person branches.

### Choosing the right type — the questions people get wrong

| If it is… | It is a… | Not a… |
|---|---|---|
| A reusable lesson from a *deployment in the corpus* | `unit` | `decision` (that is the Cube's own product) |
| A choice the *Cube team* made about the Cube | `decision` | `unit` |
| Something that *broke in the Cube app* | `incident` | `unit` (Failure and Fix is for corpus deployments) |
| A capability users see | `feature` | `module` |
| A sequence of steps across pages/endpoints | `workflow` | `feature` |
| A charter/spec line saying something should exist | `requirement` | `feature` with status live |
| A known shortcut or gap still in the code | `tech_debt` | `risk` |
| A dated external threat (account expiry, dependency) | `risk` | `tech_debt` |
| The app's `organisations` DB table | `table` (`tables/organisations-table`) | `organisation` |
| A word that needs defining | `concept` | a new folder |

---

## Slugs

Lowercase, hyphenated, ASCII. Slugs are the join key — every reference field
holds slugs. **Framework slugs are fixed** and must be used exactly:

| Type | Slug form | Examples |
|---|---|---|
| dimension | `<code>` | `persona`, `solution`, `institution`, `ecosystem` |
| stage | `<name>` | `explore`, `define`, `pilot`, `scale` |
| sub_category | `<dimension>-<letter>` | `persona-a`, `solution-e`, `institution-g`, `ecosystem-f` |
| cell | `<dimension>-<stage>` | `persona-explore`, `ecosystem-scale` |
| concept (unit type) | name | `strategic-decision`, `failure-and-fix`, `toolkit-asset` |
| pathway | the corpus file slug | `blue-dots`, `mahavistaar`, `unififed-ai-driven-agri-ecosystem` (typo is the real slug — keep it, add an alias) |
| unit | `<pathway>-<short-name>` | `mahavistaar-api-gateway-separation` |
| role | the DB role key, hyphenated | `adopter`, `pathway-contributor`, `admin`, `general-user`, `anonymous-visitor` |
| chat_mode | the mode key | `companion`, `analysis-doc`, `pathway-draft` |
| endpoint | path without `/api/`, slashes → `-`, params dropped, + method if one path has several handlers | `chat`, `pathways-assemble`, `admin-pathways-publish`, `pathways-join` |
| page | route, `/` → `-`, root → `home` | `explore`, `analyse`, `wiki-slug`, `home` |
| table | table name, `_` → `-`, `-table` suffix only where it clashes with another slug | `designs`, `published-pathways`, `organisations-table`, `toolkit-assets-bucket` |
| migration | `m<number>-<name>` | `m0027-design-documents-draft-type` |
| module | path without extension, `/` → `-` | `lib-system-prompts`, `components-chat-panel`, `proxy`, `content-framework` |
| prompt | function name kebab-cased | `explorer-system-prompt`, `library-kickoff-prompt` |
| contract | name | `grid-update`, `designs-meta`, `grid-state`, `pathway-frontmatter` |
| config_var | var name lower-kebab | `anthropic-api-key`, `next-public-supabase-url` |
| workflow | `w<n>-<name>` where numbered, else name | `w1-companion-chat-turn`, `w2-contributor-publish` |
| tech_debt | `td-<nn>-<name>` | `td-01-dead-code-dropped-table` |
| requirement / decision / risk / incident / release | descriptive | `auto-grant-adopter-on-signup`, `anthropic-account-expiry`, `pr-3-terms-and-conditions` |

Before creating anything, check `INDEX.md` (slugs + aliases) and run
`scripts/find_duplicates.py .`. A near-duplicate is worse than a merge.

---

## Edge directions

References are stored on **one side only**. The reverse is derived. Never add
a field to "the other side" to make a link visible — run
`scripts/build_backlinks.py` instead.

| Stored on | Field | Points at |
|---|---|---|
| sub_category | `dimension` | dimension |
| cell | `dimension`, `stage`, `example_pathway`, `primary_sub_categories` | dimension, stage, pathway, sub_category |
| stage | `previous_stage`, `next_stage` | stage |
| concept | `broader`, `see_also` | concept |
| unit | `pathway`, `dimension`, `sub_category`, `stage`, `also_relevant_at`, `related_units` | pathway, dimension, sub_category, stage, unit |
| pattern | `evidence_units`, `pathways`, `dimensions`, `stages` | unit, pathway, dimension, stage |
| pathway | `stage_reached`, `*_organisations`, `contributors`, `corpora`, `synthesises`, `related_pathways` | stage, organisation, person, corpus, pathway |
| corpus | `loader_modules`, `merges_with` | module, corpus |
| person | `affiliations`, `teams` | organisation, team |
| team | `organisations`, `members` | organisation, person |
| feature | `roles`, `pages`, `endpoints`, `workflows`, `tables`, `modules`, `owner_team`, `parent_feature` | … |
| workflow | `actors`, `pages`, `endpoints`, `chat_modes`, `tables`, `contracts`, `next_workflows` | … |
| page | `roles`, `components`, `calls_endpoints` | role, module, endpoint |
| endpoint | `roles`, `tables_read`, `tables_written`, `integrations` | role, table, integration |
| chat_mode | `endpoint`, `prompt`, `roles`, `corpora`, `contract` | … |
| prompt | `module`, `contract`, `carries_rules` | module, contract, rule |
| contract | `defined_in`, `producers`, `consumers`, `stored_in` | module, table |
| table | `references_tables`, `created_in`, `dropped_in` | table, migration |
| migration | `tables_touched`, `decision` | table, decision |
| module | `depends_on`, `integrations`, `tables` | module, integration, table |
| integration | `config_vars` | config_var |
| config_var | `read_by`, `integration`, `environments` | module, integration, environment |
| environment | `integrations` | integration |
| rule | `enforced_in`, `applies_to_modes` | module, chat_mode |
| decision | `decided_by`, `supersedes`, `affects_*` | person, decision, feature, table, module |
| requirement | `milestone`, `features` | milestone, feature |
| milestone | `owner_team` | team |
| release | `authors`, `features`, `migrations`, `decisions` | person, feature, migration, decision |
| tech_debt | `affected_*`, `requirement` | module, table, endpoint, requirement |
| risk | `integration`, `owner_team`, `affects_features` | integration, team, feature |
| incident | `fixed_by_migration`, `fixed_in_release`, `affected_features` | migration, release, feature |

The rule of thumb: **the more specific or more volatile entity points at the
more stable one.** A unit names its pathway; a pathway never lists its units.
A table names the migration that created it; a migration names the tables it
touched — those are two different facts, not one fact stored twice.

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
| `verified_at_commit` | The diffusion-cube commit the entry was checked against. |
| `decided_on`, `released_on`, `occurred_on`, `target_date`, `due_date`, `published_on`, `resolved_on` | When the real-world thing happened / is due. Blank if unknown — never default it to today. |

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

**Trust order for anything about how the app behaves:** code > migrations >
`ARCHITECTURE.md` > the generated `docs/wiki` > `CLAUDE.md` / older root docs
> conversation. If two disagree, record both in `contested` and say which the
> code supports — do not silently pick.

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
schema_version: 1                    # required
aliases: []                          # code ids, old names, spellings
summary: One or two sentences.
tags: []
code_refs: []                        # repo-relative paths in diffusion-cube
doc_refs: []                         # docs/specs/wiki/raw docs paths
verified_at_commit:                  # SHA, when checked against code
sources: []
first_logged: 2026-10-08
last_updated: 2026-10-08
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
| dimension | `## What it asks` · `## Sub-categories` (generated list is fine to omit) · `## Data and trust here` · `## How the companion uses it` |
| sub_category | `## What it covers` · `## Questions` · `## Stage weighting` (table) · `## Signals in a conversation` |
| stage | `## Central question` · `## Done when` · `## What changes for each dimension` |
| cell | `## Core question` · `## Listening for` · `## Insight form` · `## Corpus example` |
| concept | `## Definition` · `## How it is used` · `## Not to be confused with` |
| pathway | `## Identity` · `## Effort` · `## Coverage` (the 4×4 grid table) · `## Gaps` · `## Where the reusable value is` · `## Corpus copies` |
| unit | `## Unit` (the decision/failure/playbook/asset, in the framework's own form) · `## Condition` (applies when / fails when) · `## Before → after` · `## Why it is reusable` |
| pattern | `## Problem` · `## Root cause` · `## Solution` · `## Result` · `## Condition` · `## Evidence` |
| corpus | `## What it is` · `## How it is loaded` · `## Who reads it` · `## Divergence from other corpora` |
| organisation | `## Relationship to the Cube` · `## Notes` |
| person | `## Involvement` |
| team | `## Responsibilities` · `## Cadence` |
| role | `## Who has it` · `## How it is granted` · `## What it unlocks` · `## Gaps vs product intent` |
| feature | `## What the user can do` · `## How it works` · `## Status and gaps` |
| workflow | `## Trigger` · `## Steps` (numbered, each naming page/endpoint/table) · `## Failure modes` · `## Diagram` |
| page | `## What it renders` · `## Access behaviour` (anonymous / wrong role / approved) |
| endpoint | `## Contract` (request/response) · `## Enforcement` · `## Side effects` · `## Errors` |
| chat_mode | `## Purpose` · `## Grounding` · `## Output` · `## Triggered when` |
| prompt | `## Purpose` · `## What it injects` · `## Rules it carries` · `## Output contract` |
| contract | `## Shape` (fenced example) · `## Producers and consumers` · `## Invariants` |
| table | `## Columns` · `## RLS` · `## Lifecycle` · `## Gotchas` |
| migration | `## What it does` · `## Why` · `## Risk` |
| module | `## Responsibility` · `## Key exports` · `## Gotchas` |
| integration | `## Used for` · `## Configuration` (var names only) · `## Failure behaviour` · `## Account` |
| config_var | `## What it controls` · `## Where it is read` |
| environment | `## How it deploys` · `## What runs there` |
| rule | `## Rule` · `## Why` · `## Where enforced` · `## Known violations / gaps` |
| decision | `## Context` · `## Decision` · `## Alternatives considered` · `## Consequences` |
| requirement | `## Requirement` · `## Acceptance criteria` · `## Current state` |
| milestone | `## Outcome` · `## Status` |
| release | `## What shipped` · `## Migrations` · `## Notes` |
| tech_debt | `## Problem` · `## Impact` · `## Remediation` |
| risk | `## Risk` · `## Impact if it happens` · `## Mitigation` |
| incident | `## Symptom` · `## Root cause` · `## Fix` · `## What it revealed` |

Body links use relative paths (`[Blue Dots](../pathways/blue-dots.md)`) so
they work when browsing the repo.

---

## Corpus extraction rules (from the framework)

These are the framework's own extraction discipline, applied to `units/`.

1. **Tag every unit**: dimension + sub_category + stage + unit_type +
   condition (applies_when / fails_when). No untagged units. The
   `sub_category` must belong to the unit's `dimension` (`persona-c` only
   with `persona`) — the validator cannot check this cross-field rule, so you
   must.
2. **`stage` is the stage of origin** (where the evidence was found) and is
   what counts in a pathway's coverage grid. `also_relevant_at` is retrieval
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

## Product capture rules

1. **Trust the code.** Product-layer entries (features, endpoints, tables,
   modules …) are written from the code, carry `code_refs`, and record
   `verified_at_commit`. Where the docs say otherwise, record a `contested`
   entry and the code's reading.
2. **Status is evidence-graded.** `live` means it is reachable on the
   deployed path. Present-but-broken is `dead-code`; schema-but-unused is
   `inert`; charter-only is `planned`.
3. **A planned thing is never cited as delivered** — not a requirement, not a
   milestone, not a planned workflow.
4. **Code changed → brain changed.** A PR that adds a route, table,
   migration, chat mode or env var should land with (or be followed by) the
   matching brain entries and a `release` entry. `verified_at_commit` on
   touched entries moves to the new SHA.
5. **No values, no secrets, no user data.** Variable names only; no
   production rows; no keys even in examples.

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
