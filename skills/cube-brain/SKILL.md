---
name: cube-brain
description: >
  Reads and writes the Cube-Brain — the structured knowledge graph of the
  Diffusion Cube / 100 Pathways project (repo `diffusion-cube`). Use it to
  ANSWER any question about the project: the AI Diffusion Pathway Framework
  (dimensions, sub-categories, stages, grid cells, unit types), the pathway
  corpus (pathways, micro-innovation units, patterns, who contributed what),
  the app (features, flows, pages, API routes, chat modes, prompts, the
  grid_update contract, tables, migrations, env vars, integrations,
  deployment), and delivery (decisions, requirements, milestones, releases,
  tech debt, risks, incidents) — "how does publish work", "which units cover
  Institution at Pilot", "what reads published_pathways", "why did we drop
  pathway_submissions", "what's due before the next milestone". Use it to
  CAPTURE whenever project knowledge appears — a decision made, a feature or
  PR shipped, a migration added, a new pathway contributed, an incident, a
  risk or deadline — and when the user says "log this to the cube brain",
  "update the brain", "sync the brain", "ingest this pathway". Also runs the
  brain's validation, reports and local site.
metadata:
  version: 1.0.0
  brain_schema: 1
---

# Cube-Brain

The Cube-Brain is a git repository of markdown entities with YAML frontmatter
that models the whole Diffusion Cube project as one graph — 34 entity types in
six layers. This skill is how an agent reads it faithfully and writes to it
without degrading it.

## Locations

| What | Path | Override |
|---|---|---|
| The brain | `/home/ttpl-rt-259/brain/Cube-Brain` | env `CUBE_BRAIN` |
| The project repo | `/home/ttpl-rt-259/brain/diffusion-cube` | env `CUBE_REPO` |
| Brain scripts | `$CUBE_BRAIN/scripts/` | — |

Every command below runs from the brain root. If the brain path does not
exist, say so and stop — never write brain entries anywhere else.

## Step 0 — Orient (once per session)

1. `cd $CUBE_BRAIN && git pull --rebase` if it has a remote (others write here).
2. Read `CONVENTIONS.md` (rules, slugs, edge directions, body skeletons) and
   skim `SCHEMA.yml` (the entity model — each type's `description:` says what
   that type MEANS and may be used for). Read `MASTERS.md` before writing any
   vocab field. Do not rely on memory of these files; they evolve.
3. `INDEX.md` lists every slug and alias — grep it before creating anything.

## The model in one table

| Layer | Types (folder) |
|---|---|
| Framework | dimension (`dimensions/`), sub_category (`sub-categories/`), stage (`stages/`), cell (`cells/`), concept (`concepts/`) |
| Corpus | pathway (`pathways/`), unit (`units/`), pattern (`patterns/`), corpus (`corpora/`) |
| Actors | organisation, person (`people/`), team, role |
| Product | feature, workflow, page, endpoint, chat_mode (`chat-modes/`), prompt, contract, table, migration, module, integration, config_var (`config/`), environment |
| Knowledge | rule, decision |
| Delivery | requirement, milestone, release, tech_debt (`tech-debt/`), risk, incident |

Fixed framework slugs: `persona|solution|institution|ecosystem`,
`explore|define|pilot|scale`, sub-categories `persona-a` … `ecosystem-f`,
cells `<dimension>-<stage>`.

---

## Mode A — Answer from the brain

Use whenever the user asks what the project has, does, decided, or knows.

1. **Locate**: grep `INDEX.md` for names/aliases; then `grep -rl` across
   folders for terms. For graph questions ("what touches table X", "which
   units are Ecosystem/Scale"), grep frontmatter fields:
   `grep -l "^stage: scale" units/*.md | xargs grep -l "^dimension: ecosystem"`.
   For whole-brain state run `python3 scripts/cube_report.py`.
2. **Read** the entries you will rely on — frontmatter AND body.
3. **Answer with citations** — name the entry (`units/blue-dots-open-rails.md`)
   each claim rests on, so it can be checked.
4. **Never upgrade a record's standing.** Carry each type's meaning into the
   answer:
   - a `requirement`, a `milestone`, a `planned` feature/workflow is INTENT —
     never describe it as built;
   - a `unit` / `pathway` is the CONTRIBUTOR's account — attribute it
     ("According to EkStep Foundation's Blue Dots pathway…"), never state it
     as the Cube's own fact, and always carry its condition tag;
   - status `dead-code` / `inert` / `dropped` means present-but-not-working —
     say so;
   - a `contested` field holds a live disagreement — show both readings.
5. **Check freshness when it matters.** Product facts carry
   `verified_at_commit`; if the repo HEAD has moved (`cube_report.py
   --section freshness`), verify the specific claim against the code before
   asserting it, and offer to sync.
6. **Say what the brain does not hold.** If nothing matches, say so plainly;
   then (optionally) answer from the repo directly and offer to capture it.
7. **Respect the product's own rules** when the answer is user-facing copy:
   sub-category codes, densities and unit-type labels are internal-only
   (`concept.audience`); Source Trace content is contributor-only.

## Mode B — Capture new knowledge

Triggered by "log/add/update this", or when the user agrees to an offer. When
you merely *notice* something worth capturing mid-task, finish the task, then
offer once in one line ("Worth logging to the Cube-Brain: decision X, release
PR #4 — log them?"). Do not interrupt; do not re-offer after a no.

1. **Classify** — pick the type with the "Choosing the right type" table in
   `CONVENTIONS.md` (a Cube-team choice is a `decision`, not a `unit`; a
   corpus lesson is a `unit`, not a `decision`; something that broke in the
   app is an `incident`).
2. **Resolve** — grep `INDEX.md` and the folder; an existing entry under
   another name is common. Update rather than duplicate.
3. **Corroborate** — product facts against the code in `$CUBE_REPO` (trust
   the code over any doc); framework facts against `content/framework.md` /
   `lib/dimensions.ts`; pathway facts against the pathway document. Record
   each in `sources` with the right `method` (`queried`, `document`,
   `stated`, `derived`). A thing only said in conversation is `stated`.
4. **Propose** — short and scannable, naming the brain, new vs update, and
   what each item rests on:
   > Worth logging to the **Cube-Brain**:
   > - **New decision:** move corpus loading to … — *code-confirmed at a1b2c3d*
   > - **Update:** `features/toolkit-asset-files` → live — *route + migration 0034 present*
   > - **New risk:** … *(asserted — no source)*
   >
   > Log these? (yes / edit / skip)
   Skip the proposal when the user explicitly asked for the exact capture.
5. **Write** — read any file before editing it and merge (never blind
   overwrite). New files follow the frontmatter + body skeleton for the type
   in `CONVENTIONS.md`. Fill only what is known; blank beats plausible.
   **Every slug in a ref field must exist after this commit** — create it in
   the same commit or keep the name in prose. Respect edge directions (store
   the reference on the side `CONVENTIONS.md` § Edge directions says).
   Set `last_updated` to today; set `verified_at_commit` to the repo HEAD on
   any product entry you checked against code.
6. **Log** — one activity entry per capture:
   `python3 scripts/log_activity.py . --scope "$(git config user.name)" --text "- $(date +%F): [decision] <name> — <one line>"`
7. **Regenerate + validate**:
   ```bash
   python3 scripts/build_index.py . && python3 scripts/build_backlinks.py . \
     && python3 scripts/build_activity_log.py . && python3 scripts/validate_wiki.py .
   ```
   Validation must exit 0. Fix errors you introduced; never commit a red brain.
8. **Commit** — one commit per logging event, message prefixed `cube-brain:`;
   push if a remote exists and the user has not said otherwise. Confirm in one
   line what was written and what it rests on. Only claim success if the
   commit (and push) succeeded.

## Mode C — Ingest a pathway into units

When a new or revised pathway document lands (new file in
`content/wiki/pathways/`, a `publish pathway:` commit, or the user pastes a
pathway), follow **`references/ingest-pathway.md`**: seed/refresh the
pathway entity, then extract one `unit` per micro-innovation with full tags
and condition, toolkit assets and playbooks, Section 5 patterns, and the
organisations/people it names.

## Mode D — Sync the brain after code changes

When the user says "sync the brain", after merging a PR, or when Mode A finds
the brain stale, follow **`references/sync-from-code.md`**. It starts with
`python3 scripts/cube_sync_plan.py`, which lists every changed file since the
brain's last verified commit, the entries describing it, and files with no
entry yet.

## Mode E — Maintain and report

| Need | Command |
|---|---|
| Is the brain valid? | `python3 scripts/validate_wiki.py .` (`--stats` for model + coverage) |
| Whole-project status | `python3 scripts/cube_report.py` |
| Duplicates | grep `INDEX.md`; `python3 scripts/find_duplicates.py .` |
| Re-derive framework from code | `python3 scripts/seed_from_repo.py --only framework --dry-run` (then `--force` deliberately) |
| Local website (graph, tabs, search) | `python3 scripts/add_site.py .` once, then `python3 scripts/build_site.py . && python3 -m http.server -d site 8000` |
| Schema change | see `references/schema-change.md` |

Publishing the site anywhere is a separate decision for the brain's owner —
never set it up as a side effect.

---

## Rules that are never relaxed

- **No secrets, no values.** Config entries hold variable NAMES only. Never
  read `.env.local` into the brain. No tokens or keys in any file or commit.
- **No personal data.** People entries: professional role and involvement
  only — no emails, phones, personal details. No production user data
  (adoptions, chats, registrations): count, never copy.
- **No commercial terms** (contract values, rates) — out of scope here.
- **Don't fabricate.** Missing condition tags or outcomes are written as
  `Not documented in the source`; other unknowns stay blank.
- **Don't invent vocabulary.** A value missing from `MASTERS.md` is proposed
  there (same commit, with a reason), never used uncontrolled.
- **Trust the code** for product facts; record doc-vs-code disagreements in
  `contested` instead of silently choosing.
- **Never write to the project repo, its database, or GitHub from this skill.**
  The brain is updated from them, never the reverse.
- **Scope.** Knowledge about other Tekdi projects belongs in the company brain
  (`company-brain-capture` skill), not here; a pathway in the Cube's corpus
  belongs here even if the company brain also has it (link via
  `external_refs: [{store: company_brain, id: <slug>, verified: <date>}]`).

## Reference files

| File | When |
|---|---|
| `references/ingest-pathway.md` | Mode C — turning a pathway document into units/patterns |
| `references/sync-from-code.md` | Mode D — bringing the brain level with the repo |
| `references/schema-change.md` | Adding a type/field/vocab term or bumping the schema version |
