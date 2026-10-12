---
name: Treat the learner-data architecture as harder to recover from than any model
type: unit
schema_version: 1
summary: Invest in the competency structure, skill graph, prerequisite mapping and telemetry schema before
  optimising any model — models can be swapped later; a bad learner-data architecture corrupts all subsequent
  learner modelling.
code_refs:
- content/wiki/pathways/assisted-language-math-learning.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/assisted-language-math-learning.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: assisted-language-math-learning
unit_type: Strategic Decision
dimension: solution
sub_category: solution-d
stage: define
also_relevant_at:
- scale
source_unit_id: Unit 8
applies_when: The AI system maintains persistent learner models across sessions; multiple models or components
  will be updated over time; the deployment is intended to run for years across millions of learners.
fails_when: Not documented in the source
decision: Invest in the competency structure, skill graph, prerequisite mapping, and telemetry schema
  before optimising any AI model — on the principle that a poorly designed learner-data architecture is
  much harder to recover from than a suboptimal model.
alternative_considered: Focusing early investment on model accuracy (ASR recognition rate, recommendation
  algorithm quality) and treating the competency structure as something that can be corrected later.
reason: ASR engines and recommendation algorithms can be replaced as better options emerge. A competency
  structure that misrepresents prerequisites or cannot distinguish mastery from task completion corrupts
  all subsequent learner modelling; correcting it retrospectively means discarding historical learner
  data or reprocessing it against a new schema — costly and disruptive at scale.
context: AML's misconception taxonomy and skill graph were built from 2–3 million pen-and-paper responses
  and academic research before any product was deployed.
before: Not documented in the source
after: The architecture explicitly distinguishes level (which grade-equivalent concept) from step (which
  operation within a multi-step problem) — the distinction that makes PARS (Practice at the Right Step)
  possible.
adopter_intents:
- We're trying to decide what to build versus reuse versus integrate — where do we start?
- What data do I need before I build anything?
- What makes foundational math specifically tractable for AI?
- Should we build ASR ourselves or integrate it?
related_units:
- assisted-language-math-learning-misconception-taxonomy-before-product
- assisted-language-math-learning-named-partner-per-capability
---

## Unit

According to EkStep Foundation's AxL pathway, this is a strategic decision from the deployment.

**Decision.** Invest in the competency structure, skill graph, prerequisite mapping, and telemetry schema before optimising any AI model — on the principle that a poorly designed learner-data architecture is much harder to recover from than a suboptimal model.

**Alternative considered.** Focusing early investment on model accuracy (ASR recognition rate, recommendation algorithm quality) and treating the competency structure as something that can be corrected later.

**Why.** ASR engines and recommendation algorithms can be replaced as better options emerge. A competency structure that misrepresents prerequisites or cannot distinguish mastery from task completion corrupts all subsequent learner modelling; correcting it retrospectively means discarding historical learner data or reprocessing it against a new schema — costly and disruptive at scale.

**Context.** AML's misconception taxonomy and skill graph were built from 2–3 million pen-and-paper responses and academic research before any product was deployed.

## Condition

- **Applies when:** The AI system maintains persistent learner models across sessions; multiple models or components will be updated over time; the deployment is intended to run for years across millions of learners.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** The architecture explicitly distinguishes level (which grade-equivalent concept) from step (which operation within a multi-step problem) — the distinction that makes PARS (Practice at the Right Step) possible.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
