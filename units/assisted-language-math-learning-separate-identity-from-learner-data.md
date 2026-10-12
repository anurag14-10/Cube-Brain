---
name: Separate the learner's identity from the learner's data
type: unit
schema_version: 1
summary: Key all telemetry and progression to pseudonymous learner identifiers, restrict identifiable
  data by role, and plan from day one for states — not the foundation — to host PII-bearing services.
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
dimension: ecosystem
sub_category: ecosystem-e
stage: define
also_relevant_at:
- scale
source_unit_id: Unit 12
applies_when: The deployment involves children's data in a government school context; long-term sustainability
  requires reducing dependency on the founding organisation's infrastructure; multiple state government
  partners each require data sovereignty over their own learners.
fails_when: Not documented in the source
decision: 'Design the system so personalisation never depends on a child''s name or other direct identifiers:
  represent learners through virtual or pseudonymous identifiers, attach all telemetry, assessment and
  progression data to those identifiers, restrict access to sensitive data through role-based controls,
  and plan from the outset for PII-bearing services to be hosted by state governments rather than retained
  by EkStep.'
alternative_considered: Using student identity (name, enrollment ID, or other direct identifiers) as the
  key for the learner model, with EkStep retaining hosting of all services.
reason: Personalisation needs a persistent learner model, not a name. Separating identity from learning
  data allows rich longitudinal profiles without making PII a dependency of the AI system — reducing privacy
  risk and enabling handover of PII hosting to states, so sustainability depends less on EkStep's own
  infrastructure budget.
context: States are expected to host services containing personally identifiable information themselves.
before: Not documented in the source
after: EkStep assists states with configuration and provides engineering bandwidth to set up PII hosting,
  but does not retain custody of PII long-term.
adopter_intents:
- How do we protect children's data while still building a useful learner model?
related_units:
- assisted-language-math-learning-full-state-ownership-narrow-role
---

## Unit

According to EkStep Foundation's AxL pathway, this is a strategic decision from the deployment.

**Decision.** Design the system so personalisation never depends on a child's name or other direct identifiers: represent learners through virtual or pseudonymous identifiers, attach all telemetry, assessment and progression data to those identifiers, restrict access to sensitive data through role-based controls, and plan from the outset for PII-bearing services to be hosted by state governments rather than retained by EkStep.

**Alternative considered.** Using student identity (name, enrollment ID, or other direct identifiers) as the key for the learner model, with EkStep retaining hosting of all services.

**Why.** Personalisation needs a persistent learner model, not a name. Separating identity from learning data allows rich longitudinal profiles without making PII a dependency of the AI system — reducing privacy risk and enabling handover of PII hosting to states, so sustainability depends less on EkStep's own infrastructure budget.

**Context.** States are expected to host services containing personally identifiable information themselves.

## Condition

- **Applies when:** The deployment involves children's data in a government school context; long-term sustainability requires reducing dependency on the founding organisation's infrastructure; multiple state government partners each require data sovereignty over their own learners.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** EkStep assists states with configuration and provides engineering bandwidth to set up PII hosting, but does not retain custody of PII long-term.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
