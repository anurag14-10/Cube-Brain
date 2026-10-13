---
name: cube-brain
description: >
  Reads and writes the Cube-Brain, the knowledge graph of the Diffusion Cube /
  100 Pathways project (repo diffusion-cube). Use it to ANSWER questions about
  the AI Diffusion Pathway Framework (dimensions, sub-categories and stage
  weights, stages, grid cells, unit types, product rules), the pathway corpus
  (pathways, micro-innovation units, patterns, contributors), the people and
  organisations involved, and delivery (decisions, risks, milestones), e.g.
  "which units cover Institution at Pilot", "who contributed MahaVISTAAR",
  "what is due before the next milestone". Use it to CAPTURE such knowledge
  whenever it comes up (a framework or programme decision, a new pathway, a
  risk or deadline, a milestone) and when the user says "log this to the cube
  brain", "update the brain" or "ingest this pathway". Works from a local
  clone or, on Claude Desktop/web, through the GitHub connector. The app's
  code level (routes, tables, env vars) is not in this brain.
metadata:
  version: 2.2.2
  brain_schema: 2
---

# Cube-Brain

The Cube-Brain is a git repository of markdown entities with YAML frontmatter
that models the Diffusion Cube project's knowledge as one graph — 8 entity
types in three layers, with the framework's closed sets as variables. This
skill is how an agent reads it faithfully and writes to it without degrading
it.

## Configuration

```yaml
repo: anurag14-10/Cube-Brain     # GitHub owner/name of the brain
branch: main
commit_prefix: "cube-brain:"
admins: [anurag14-10]            # push straight to `branch`; everyone else opens a PR
pr_branch_prefix: capture/
local_brain: $CUBE_BRAIN, else the repo this skill sits in, else ~/brain/Cube-Brain
local_project: $CUBE_REPO, else diffusion-cube beside the brain
```

Resolve `local_brain` once: `$CUBE_BRAIN` if set; otherwise the git root of
this skill's own directory if it contains `SCHEMA.yml` (an install that is a
symlink or a clone of the brain); otherwise `~/brain/Cube-Brain`. The project
repo is `$CUBE_REPO`, else `../diffusion-cube` relative to the brain. Never
assume another person's absolute paths.

**Who writes where:** a login in `admins` commits to `branch` directly;
everyone else writes through a pull request an admin reviews and merges —
from a branch in `repo` if they have write access, from their own fork if not.
Follow **`references/write-route.md`** for every non-admin write, on any
surface.

## Pick the storage for this surface

- **A shell AND a local clone exist** (Claude Code in a terminal, VS Code, or
  the Desktop app's Code tab): work in `$CUBE_BRAIN` (else `local_brain`)
  with git. Every command below runs from the brain root. The clone must be
  the user's own, with push credentials. A repo you cloned yourself into a
  chat sandbox does not count: it vanishes between tasks and cannot push — on
  such a surface use the connector, or the "Neither" route below.
- **No shell, or no local clone** (Claude Desktop chat, web, mobile): read and
  write `repo` on `branch` through the GitHub connector. Follow
  **`references/adapter-github-connector.md`** — it replaces the shell steps
  (git pull, scripts, commit) with connector calls.
- **Neither** (no GitHub write tools, and no clone of the user's own): say so
  before drafting anything, name the fix — the GitHub connector added in
  Settings → Connectors *and* switched on for this chat in the tools menu —
  and offer drafted markdown inline.
  **Never write brain entries to local or sandbox files as a fallback** — on a
  chat surface they vanish and the user believes the knowledge was saved.

If both are available, prefer the local clone.

## Step 0 — Orient (once per session)

1. Local clone: `cd $CUBE_BRAIN`, `git switch main` (a capture branch may be
   left checked out), then `git pull --rebase` from the remote whose URL is
   `repo` (others write here). Connector: nothing to pull — fetch each file
   fresh right before you rely on it.
   **Then, local clone only, check the brain against the project** — nothing
   else tells anyone a pathway landed or changed. If `$CUBE_REPO` (else
   `../diffusion-cube`) does not exist, skip this check and say so once in
   passing; it is not an error. `git -C "$CUBE_REPO" fetch --quiet` (a fetch
   only: never pull, checkout or touch its working tree), then
   `python3 scripts/check_corpus_drift.py --ref <ref>` with the branch the
   corpus is merged into (`HEAD` by default; `origin/cube-dev` also shows
   pathways only assembled, which are `lifecycle: assembled`, not published).
   Mention any `missing`, `changed` or `not-ingested` rows to the user once,
   in one line, and offer Mode C. If `SUPABASE_URL` and `SUPABASE_ANON_KEY` are
   in the environment, also run `python3 scripts/probe_published_pathways.py`
   for DB-only pathways.
2. Read `CONVENTIONS.md` (rules, slugs, edge directions, body skeletons) and
   skim `SCHEMA.yml` (the entity model — each type's `description:` says what
   that type MEANS and may be used for). Read `MASTERS.md` before writing any
   vocab field. Do not rely on memory of these files; they evolve.
3. `INDEX.md` lists every slug and alias — search it before creating
   anything (on the connector, fetch it and search the text).
4. **Before the first write** of the session, settle who is writing and where
   (`references/write-route.md` §1–2; on the connector, the adapter's tool
   check too). If the write cannot happen, say so before drafting.

## The model in one table

| Layer | Types (folder) | Variables (MASTERS.md) |
|---|---|---|
| Framework + corpus | concept (`concepts/`), pathway (`pathways/`), unit (`units/`) | dimension (2), stage (3), sub-category (4), grid key (5), corpus (13) |
| Actors | organisation (`organisations/`), person (`people/`) | team (15) |
| Delivery | decision (`decisions/`), risk (`risks/`), milestone (`milestones/`) | — |

Fixed framework values: `persona|solution|institution|ecosystem`,
`explore|define|pilot|scale`, sub-categories `persona-a` … `ecosystem-f`,
grid keys `<dimension>:<Stage>`. Each dimension's concept page
(`concepts/persona.md` …) holds its sub-categories (weights + questions) and
its four cells; each stage has `concepts/<stage>.md`. A problem→solution
pattern is a unit with `unit_type: Problem-Solution Pattern`; a product rule
is a concept with `concept_kind: rule`.

Out of scope: the app's code level. Its last brain model is commit `0296ca8`
of this repo — read it there (`git show 0296ca8:endpoints/chat.md`) if a
question needs the old record, but trust the current code over it.

---

## Mode A — Answer from the brain

Use whenever the user asks what the project has, does, decided, or knows.

1. **Locate**: grep `INDEX.md` for names/aliases; then `grep -rl` across
   folders for terms. For graph questions ("which units are Ecosystem/Scale",
   "which pathways sit in the library corpus"), grep frontmatter fields:
   `grep -l "^stage: scale" units/*.md | xargs grep -l "^dimension: ecosystem"`.
   For whole-brain state run `python3 scripts/cube_report.py`.
2. **Read** the entries you will rely on — frontmatter AND body.
3. **Answer with citations** — name the entry (`units/blue-dots-open-rails.md`)
   each claim rests on, so it can be checked.
4. **Never upgrade a record's standing.** Carry each type's meaning into the
   answer:
   - a `milestone` and its `deliverables` are INTENT — never describe them as
     built;
   - a `unit` / `pathway` is the CONTRIBUTOR's account — attribute it
     ("According to EkStep Foundation's Blue Dots pathway…"), never state it
     as the Cube's own fact, and always carry its condition tag;
   - a `contested` field holds a live disagreement — show both readings.
5. **Say what the brain does not hold.** If nothing matches, say so plainly;
   then (optionally) answer from the repo directly and offer to capture it.
6. **Respect the product's own rules** when the answer is user-facing copy:
   sub-category codes, densities and unit-type labels are internal-only
   (`concept.audience`); Source Trace content is contributor-only.

## Mode B — Capture new knowledge

Triggered by "log/add/update this", or when the user agrees to an offer. When
you merely *notice* something worth capturing mid-task, finish the task, then
offer once in one line ("Worth logging to the Cube-Brain: decision X, risk
Y — log them?"). Do not interrupt; do not re-offer after a no.

1. **Classify** — pick the type with the "Choosing the right type" table in
   `CONVENTIONS.md` (a Cube-team choice is a `decision`, not a `unit`; a
   corpus lesson is a `unit`, not a `decision`; a rule the Cube always keeps
   is a `concept`; a dimension, stage, corpus or team is a variable, never a
   new entity; code-level facts are out of scope).
2. **Resolve** — grep `INDEX.md` and the folder; an existing entry under
   another name is common. Update rather than duplicate.
3. **Corroborate** — framework facts against `content/framework.md` /
   `lib/dimensions.ts`; pathway facts against the pathway document; delivery
   facts against the Product Charter or the document that states them. Record
   each in `sources` with the right `method` (`queried`, `document`,
   `stated`, `derived`). A thing only said in conversation is `stated`.
4. **Propose** — short and scannable, naming the brain, new vs update, and
   what each item rests on:
   > Worth logging to the **Cube-Brain**:
   > - **New decision:** weight Institution C primary at Pilot — *framework.md updated*
   > - **Update:** `pathways/blue-dots` → 6 new units — *pathway document v2*
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
   Set `last_updated` to today.
   On the connector, steps 6–8 are different — follow the adapter file
   (one multi-file push; CI regenerates and validates). Not an admin? Start
   from a capture branch first — `references/write-route.md`.
6. **Log** — one activity entry per capture, scoped by GitHub login:
   `python3 scripts/log_activity.py . --scope <github-login> --text "- $(date +%F): [decision] <name> — <one line>"`
7. **Regenerate + validate**:
   ```bash
   python3 scripts/build_index.py . && python3 scripts/build_backlinks.py . \
     && python3 scripts/build_activity_log.py . && python3 scripts/validate_wiki.py .
   ```
   Validation must exit 0. Fix errors you introduced; never commit a red brain.
   `ModuleNotFoundError: yaml` → `pip install pyyaml` (or `pip install --user
   pyyaml`) and run it again.
8. **Commit** — one commit per logging event, message prefixed `cube-brain:`.
   Admin: `git pull --rebase` then push to `branch` (CI's own commits make a
   plain push fail as non-fast-forward) unless the user said otherwise.
   Anyone else: commit only your own files on the capture branch, push, and
   open the PR. Both: `references/write-route.md` §4. Confirm in one line
   what was written and what it rests on. Only claim success if the commit
   and push succeeded — and a PR is "opened, pending review", never "saved".

## Mode C — Ingest a pathway into units

When a new or revised pathway document lands — the drift check (Step 0)
lists it as `missing` / `changed` / `not-ingested`, the Supabase probe lists
it as `MISSING`, or the user pastes a pathway — follow
**`references/ingest-pathway.md`**: seed/refresh the
pathway entity, then extract one `unit` per micro-innovation with full tags
and condition, toolkit assets and playbooks, Section 5 patterns, and the
organisations/people it names.

## Mode D — Re-derive after the framework changes

When `content/framework.md` or `lib/dimensions.ts` changes in the repo, run
`python3 scripts/seed_from_repo.py --only framework --dry-run`, compare, then
re-seed deliberately (`--force` overwrites — read the existing concept pages
first and keep any hand-written enrichment). Update MASTERS 1–5 in the same
commit if a dimension, stage, sub-category or unit type changed.

## Mode E — Maintain and report

| Need | Command |
|---|---|
| Is the brain valid? | `python3 scripts/validate_wiki.py .` (`--stats` for model + coverage) |
| Whole-project status | `python3 scripts/cube_report.py` (`--section grid`: coverage maps vs units) |
| Brain behind the project corpus? | `python3 scripts/check_corpus_drift.py [--ref REF]` |
| Pathways live only in Supabase | `python3 scripts/probe_published_pathways.py` (anon key from env; metadata only, GET only) |
| Duplicates | grep `INDEX.md`; `python3 scripts/find_duplicates.py .` |
| Re-derive framework from the repo | `python3 scripts/seed_from_repo.py --only framework --dry-run` (then `--force` deliberately) |
| Every entry on the current schema? | `python3 scripts/migrate_v1_to_v2.py . --check` |
| Package the skill for Claude Desktop / web | `python3 scripts/build_skill.py [--repo owner/name]` → `dist/cube-brain.skill`, upload via Customize → Skills |
| Local website (graph, tabs, search) | `python3 scripts/add_site.py .` once, then `python3 scripts/build_site.py . && python3 -m http.server -d site 8000` |
| Schema change | see `references/schema-change.md` |

Publishing the site anywhere is a separate decision for the brain's owner —
never set it up as a side effect.

---

## Rules that are never relaxed

- **No secrets, no values.** Never read `.env.local` into the brain. No
  tokens or keys in any file or commit.
- **No personal data.** People entries: professional role and involvement
  only — no emails, phones, personal details. No production user data
  (adoptions, chats, registrations): count, never copy.
- **No commercial terms** (contract values, rates) — out of scope here.
- **Don't fabricate.** Missing condition tags or outcomes are written as
  `Not documented in the source`; other unknowns stay blank.
- **Don't invent vocabulary.** A value missing from `MASTERS.md` is proposed
  there (same commit, with a reason), never used uncontrolled.
- **Trust the source.** Framework facts come from `content/framework.md` /
  `lib/dimensions.ts`, pathway facts from the pathway document; record
  disagreements in `contested` instead of silently choosing.
- **Never write to the project repo, its database, or anything on GitHub
  except the brain `repo` and the writer's fork of it.** The brain is updated
  from the project, never the reverse.
- **Scope.** Knowledge about other Tekdi projects belongs in the company brain
  (`company-brain-capture` skill), not here; a pathway in the Cube's corpus
  belongs here even if the company brain also has it (link via
  `external_refs: [{store: company_brain, id: <slug>, verified: <date>}]`).

## Reference files

| File | When |
|---|---|
| `references/ingest-pathway.md` | Mode C — turning a pathway document into units/patterns |
| `references/schema-change.md` | Adding a type/field/vocab term or bumping the schema version |
| `references/adapter-github-connector.md` | No shell or no local clone — reading and writing through the GitHub connector |
| `references/write-route.md` | Any write by someone not in `admins` — capture branch, fork, pull request |
