---
name: Build the misconception taxonomy before building the product
type: unit
schema_version: 1
summary: Map learners' specific error patterns through pen-and-paper data collection at scale before any
  digital product exists, and make that taxonomy the data architecture all AI personalisation is built
  on.
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
stage: explore
also_relevant_at:
- define
source_unit_id: Unit 5
applies_when: The domain is structured enough that a finite, mappable set of misconceptions exists; the
  target learner population is accessible for pre-product data collection; the deploying organisation
  can invest in data infrastructure before the product generates its own.
fails_when: Not documented in the source
decision: Before building any digital product, map the specific error patterns and misconceptions learners
  make through pen-and-paper data collection at scale, and use that taxonomy as the foundational data
  architecture for all subsequent AI personalisation.
alternative_considered: Beginning with a digital product and collecting error data through product telemetry
  once deployed.
reason: Telemetry from a deployed product tells you what answer a student gave, not the intermediate steps
  or reasoning. Pen-and-paper responses revealed actual thinking (stick counting, digits in the wrong
  column) at a granularity that confirmed the taxonomy was real, not a model artefact.
context: 'For 27+14, common wrong answers include 311 (carry treated as a digit in the middle) and 31
  (carry dropped entirely) — each maps to a misconception with two parts: which skill is involved and
  which incorrect execution produced the answer.'
before: Not documented in the source
after: Roughly 2–3 million pen-and-paper responses were scanned and analysed before any state deployment,
  so the AI system was built around a validated understanding of misconceptions; AML now holds 20 million+
  question-answer pairs.
adopter_intents:
- What data do I need before I build anything?
- What makes foundational math specifically tractable for AI?
related_units:
- assisted-language-math-learning-learner-data-architecture-first
---

## Unit

According to EkStep Foundation's AxL pathway, this is a strategic decision from the deployment.

**Decision.** Before building any digital product, map the specific error patterns and misconceptions learners make through pen-and-paper data collection at scale, and use that taxonomy as the foundational data architecture for all subsequent AI personalisation.

**Alternative considered.** Beginning with a digital product and collecting error data through product telemetry once deployed.

**Why.** Telemetry from a deployed product tells you what answer a student gave, not the intermediate steps or reasoning. Pen-and-paper responses revealed actual thinking (stick counting, digits in the wrong column) at a granularity that confirmed the taxonomy was real, not a model artefact.

**Context.** For 27+14, common wrong answers include 311 (carry treated as a digit in the middle) and 31 (carry dropped entirely) — each maps to a misconception with two parts: which skill is involved and which incorrect execution produced the answer.

## Condition

- **Applies when:** The domain is structured enough that a finite, mappable set of misconceptions exists; the target learner population is accessible for pre-product data collection; the deploying organisation can invest in data infrastructure before the product generates its own.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Roughly 2–3 million pen-and-paper responses were scanned and analysed before any state deployment, so the AI system was built around a validated understanding of misconceptions; AML now holds 20 million+ question-answer pairs.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
