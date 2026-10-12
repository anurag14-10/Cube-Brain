---
name: Gap-flagging loop to sustain data quality after launch
type: unit
schema_version: 2
summary: Log every query the system cannot answer (or answers below a confidence threshold), route it
  to the data team as a data-readiness task rather than a model-tuning task, advance the dataset, re-test,
  and review the aggregate as a data-gap dashboard.
doc_refs:
- content/wiki/pathways/nivesh-suvidha.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/nivesh-suvidha.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only; fails_when taken from the unit's Note
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: nivesh-suvidha
unit_type: Playbook
dimension: institution
sub_category: institution-g
stage: pilot
also_relevant_at:
- scale
source_unit_id: Unit 7
applies_when: The repository is live but incomplete; user queries will outrun the data that has been structured
  so far. Use from first live deployment onward; requires a data team with capacity to act on flagged
  queries.
fails_when: Flagged queries are routed to the AI team as prompt-engineering problems rather than to the
  data team as data-readiness problems.
steps:
- 1. Instrument the conversational interface to log every query the system cannot answer or answers below
  a defined confidence threshold.
- 2. Route flagged queries to the data team as explicit data-collection or tagging tasks — not as model-tuning
  tasks.
- 3. The data team advances the relevant dataset through the next DHARA stage(s) required to answer the
  query.
- 4. Re-test the query against the updated repository before closing the loop.
- 5. Treat the aggregate of flagged queries over a reporting period as a data-gap dashboard for institutional
  review.
common_failure_mode: Treating an unanswered query as a model failure when it is a data-absence failure.
before: Unanswered queries were silent failures.
after: Each unanswered query became a prioritised data-collection task, advancing the repository's coverage
  systematically.
adopter_intents:
- How do I keep the system accurate after launch?
- What do I do when the system can't answer a user's question?
related_units:
- nivesh-suvidha-iterate-repository-through-live-use
- nivesh-suvidha-dhara-seven-stage-toolkit
---

## Unit

According to Invest UP's Nivesh Suvidha pathway, this is a playbook from the deployment.

**Steps (in order):**

1. Instrument the conversational interface to log every query the system cannot answer or answers below a defined confidence threshold.
2. Route flagged queries to the data team as explicit data-collection or tagging tasks — not as model-tuning tasks.
3. The data team advances the relevant dataset through the next DHARA stage(s) required to answer the query.
4. Re-test the query against the updated repository before closing the loop.
5. Treat the aggregate of flagged queries over a reporting period as a data-gap dashboard for institutional review.

**Common failure mode.** The loop breaks if flagged queries are routed to the AI team as prompt-engineering problems rather than to the data team as data-readiness problems. The most common failure is treating an unanswered query as a model failure when it is a data-absence failure.

## Condition

- **Applies when:** The repository is live but incomplete; user queries will outrun the data that has been structured so far. The pathway's toolkit table adds: use from first live deployment onward; it requires a data team with capacity to act on flagged queries.
- **Fails when:** Flagged queries are routed to the AI team as prompt-engineering problems rather than to the data team as data-readiness problems.

## Before → after

- **Before:** Unanswered queries were silent failures.
- **After:** Each unanswered query became a prioritised data-collection task, advancing the repository's coverage systematically.

## Why it is reusable

The routing rule is the decision that matters: an unanswered query goes to the data team, not the model team. The steps do not depend on the domain. The pathway does not categorise which failures were scope, quality or freshness problems (it names this as a gap). It is a suggestion from another adoption's lived experience, not a recommendation.
