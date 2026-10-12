---
name: Ownership transfers fully to the state; plan for a narrow ongoing role
type: unit
schema_version: 2
summary: Design the post-deployment operating model so the state education department owns implementation
  entirely, with the founding foundation narrowed to training the trainers and troubleshooting support.
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
unit_type: Strategic Decision
dimension: institution
sub_category: institution-g
stage: scale
source_unit_id: Unit 10
applies_when: The deploying organisation is a non-government foundation working within a government school
  system; the government system has an existing field hierarchy capable of running programme implementation;
  the product is mature enough that ongoing product development is separable from day-to-day operational
  management.
fails_when: Not documented in the source
decision: 'Design the post-deployment operating model so that the state education department has complete
  ownership of programme implementation, with EkStep''s ongoing role narrowed to two functions: continuing
  to train the trainers, and continuing to provide troubleshooting support.'
alternative_considered: Retaining operational co-ownership or requiring ongoing EkStep involvement in
  programme management after deployment.
reason: State departments have the mandate, the field structure (BEO/DEO/HM/teacher chain) and the legitimacy
  to run this at scale; a model requiring continued external operational involvement does not institutionalise
  — it remains a project. EkStep's comparative advantage is product development and training, not operational
  management.
context: State leadership runs weekly or fortnightly review meetings, BEO/DEO go into the field, HMs ensure
  lab readiness, teachers get students to the lab.
before: Not documented in the source
after: Different states give the programme their own names; EkStep does not manage implementation and
  continues only training and troubleshooting. The stated long-term path is for PII-bearing services to
  move to state-hosted infrastructure, reducing even the hosting dependency.
adopter_intents:
- Who owns this after we deploy, and what does that look like?
- How do I convince a sceptical state secretary to commit?
- How do we keep costs low at a million learners?
- How do we design the system to survive a leadership change at the state level?
related_units:
- assisted-language-math-learning-state-deployment-sequence
- assisted-language-math-learning-separate-identity-from-learner-data
---

## Unit

According to EkStep Foundation's AxL pathway, this is a strategic decision from the deployment.

**Decision.** Design the post-deployment operating model so that the state education department has complete ownership of programme implementation, with EkStep's ongoing role narrowed to two functions: continuing to train the trainers, and continuing to provide troubleshooting support.

**Alternative considered.** Retaining operational co-ownership or requiring ongoing EkStep involvement in programme management after deployment.

**Why.** State departments have the mandate, the field structure (BEO/DEO/HM/teacher chain) and the legitimacy to run this at scale; a model requiring continued external operational involvement does not institutionalise — it remains a project. EkStep's comparative advantage is product development and training, not operational management.

**Context.** State leadership runs weekly or fortnightly review meetings, BEO/DEO go into the field, HMs ensure lab readiness, teachers get students to the lab.

## Condition

- **Applies when:** The deploying organisation is a non-government foundation working within a government school system; the government system has an existing field hierarchy capable of running programme implementation; the product is mature enough that ongoing product development is separable from day-to-day operational management.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Different states give the programme their own names; EkStep does not manage implementation and continues only training and troubleshooting. The stated long-term path is for PII-bearing services to move to state-hosted infrastructure, reducing even the hosting dependency.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
