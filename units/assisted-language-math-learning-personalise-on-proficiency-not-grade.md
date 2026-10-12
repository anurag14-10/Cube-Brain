---
name: Personalise on demonstrated proficiency, not grade
type: unit
schema_version: 1
summary: Drive each learner's pathway from what they can demonstrably do rather than grade, age or a fixed
  curriculum sequence — three simpler alternatives were explicitly evaluated and rejected.
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
dimension: persona
sub_category: persona-d
stage: define
also_relevant_at:
- explore
- scale
source_unit_id: Unit 2
applies_when: Learners within the same classroom are meaningfully different in actual proficiency; the
  delivery system can maintain a persistent learner model across sessions; teachers cannot provide continuous
  one-to-one diagnosis.
fails_when: Not documented in the source
decision: Personalise the learning pathway based on each learner's demonstrated proficiency — what they
  can actually do — rather than their administrative grade, age, or a fixed curriculum sequence.
alternative_considered: 'Three alternatives were explicitly evaluated: (a) digitising the curriculum so
  every learner follows the same sequence; (b) allowing learners or teachers to freely select content;
  (c) using simple completion rules — finish a set and move forward.'
reason: 'Each alternative reproduces the core limitation of grade-based instruction: it assumes learners
  are at a similar level, treats completion as learning, and cannot identify or respond to specific gaps.
  Only proficiency-based personalisation asks ''what should this specific learner practise next?'' fresh
  for every learner in every session.'
context: AxL builds learner discovery and assessment, proficiency and milestone models, recommendation
  logic, adaptive practice, continuous telemetry, reassessment, and longitudinal analytics — all in service
  of that one question.
before: Not documented in the source
after: A student still struggling with one-digit addition is not served three-digit multiplication questions,
  regardless of their grade.
adopter_intents:
- How do I explain to a state government why they need this before any AI exists?
- What is the right way to frame what this product actually does?
- Why is personalising on grade a mistake?
related_units:
- assisted-language-math-learning-heterogeneity-not-content-scarcity
- assisted-language-math-learning-learner-data-architecture-first
---

## Unit

According to EkStep Foundation's AxL pathway, this is a strategic decision from the deployment.

**Decision.** Personalise the learning pathway based on each learner's demonstrated proficiency — what they can actually do — rather than their administrative grade, age, or a fixed curriculum sequence.

**Alternative considered.** Three alternatives were explicitly evaluated: (a) digitising the curriculum so every learner follows the same sequence; (b) allowing learners or teachers to freely select content; (c) using simple completion rules — finish a set and move forward.

**Why.** Each alternative reproduces the core limitation of grade-based instruction: it assumes learners are at a similar level, treats completion as learning, and cannot identify or respond to specific gaps. Only proficiency-based personalisation asks 'what should this specific learner practise next?' fresh for every learner in every session.

**Context.** AxL builds learner discovery and assessment, proficiency and milestone models, recommendation logic, adaptive practice, continuous telemetry, reassessment, and longitudinal analytics — all in service of that one question.

## Condition

- **Applies when:** Learners within the same classroom are meaningfully different in actual proficiency; the delivery system can maintain a persistent learner model across sessions; teachers cannot provide continuous one-to-one diagnosis.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** A student still struggling with one-digit addition is not served three-digit multiplication questions, regardless of their grade.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
