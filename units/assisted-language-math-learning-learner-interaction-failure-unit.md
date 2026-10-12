---
name: The smallest unit of failure is the learner interaction, not the model call
type: unit
schema_version: 2
summary: Technically correct model outputs did not guarantee a useful intervention for the learner; monitoring
  moved from model-level accuracy to whether each learner, in each session, received a useful intervention.
doc_refs:
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
unit_type: Failure and Fix
dimension: solution
sub_category: solution-e
stage: pilot
also_relevant_at:
- scale
source_unit_id: Unit 6
applies_when: The AI system involves multiple interacting components (ASR, recommendation, content, scaffolding);
  model-level metrics are already being tracked; the question is whether the combination is creating learning
  value for specific learners.
fails_when: Not documented in the source
failure: Early deployments showed that technically correct model outputs — ASR correctly transcribing
  a reading response, a recommendation engine returning an appropriate next task — did not guarantee the
  learner received a useful intervention, while incorrect or incomplete outputs inside a strong instructional
  feedback loop sometimes still produced learning value. Evaluating at the model level missed the actual
  failure unit.
fix: Shifted the governance and monitoring frame from model-level metrics (ASR recognition rate, recommendation
  similarity score, task completion rate) to learner-interaction-level outcomes — did this learner, in
  this session, receive a useful intervention? — and built telemetry and analytics to track learner state
  change, not just model performance.
insight: AI quality in educational systems cannot exceed the quality of the learning measurement architecture
  surrounding it. A weak model inside a strong instructional feedback loop can create substantial learning
  value; a well-performing model inside a poorly designed loop produces activity, not learning.
adopter_intents:
- What broke first when we went live in schools?
- How do we measure whether the AI is actually working?
- What counts as success — usage, or something else?
related_units:
- assisted-language-math-learning-reintegration-as-measured-outcome
- assisted-language-math-learning-learner-data-architecture-first
---

## Unit

According to EkStep Foundation's AxL pathway, this is a failure and fix from the deployment.

**Failure.** Early deployments showed that technically correct model outputs — ASR correctly transcribing a reading response, a recommendation engine returning an appropriate next task — did not guarantee the learner received a useful intervention, while incorrect or incomplete outputs inside a strong instructional feedback loop sometimes still produced learning value. Evaluating at the model level missed the actual failure unit.

**Fix.** Shifted the governance and monitoring frame from model-level metrics (ASR recognition rate, recommendation similarity score, task completion rate) to learner-interaction-level outcomes — did this learner, in this session, receive a useful intervention? — and built telemetry and analytics to track learner state change, not just model performance.

**Insight.** AI quality in educational systems cannot exceed the quality of the learning measurement architecture surrounding it. A weak model inside a strong instructional feedback loop can create substantial learning value; a well-performing model inside a poorly designed loop produces activity, not learning.

## Condition

- **Applies when:** The AI system involves multiple interacting components (ASR, recommendation, content, scaffolding); model-level metrics are already being tracked; the question is whether the combination is creating learning value for specific learners.
- **Fails when:** Not documented in the source

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

The reusable part is the insight the fix revealed, read together with the condition tag above. It is a suggestion from another adoption's lived experience, not a recommendation.
