---
name: Reuse the governance template across instances, not just the code
type: unit
schema_version: 1
summary: When federating to new states, cooperatives or countries, transfer the institutional ownership
  structure, data accountability model and content-authority assignment along with the open-source code
  — local adaptation then happens inside it.
code_refs:
- content/wiki/pathways/unififed-ai-driven-agri-ecosystem.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/unififed-ai-driven-agri-ecosystem.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: unififed-ai-driven-agri-ecosystem
unit_type: Strategic Decision
dimension: institution
sub_category: institution-a
stage: scale
source_unit_id: Unit 6
applies_when: Federating across geographically or institutionally distinct deployments.
fails_when: A single institution controls the full deployment — the template overhead is then unnecessary.
decision: When federating the system across states, cooperatives, and countries, transfer the governance
  template — institutional ownership structure, data accountability model, content authority assignment
  — not just the open-source codebase.
alternative_considered: Providing the codebase and architecture documentation, and letting each new instance
  design its own governance.
reason: A new instance that takes the code but not the governance template faces the same institutional
  questions (who owns what the system says? who corrects a wrong answer?) without the answers worked out.
  The template does not eliminate local adaptation; it provides the structure within which local adaptation
  happens safely.
context: 'The OAN material states: ''What travels each time is the same governance, the same institutional
  ownership, the same template — made local at every stop.'''
before: Not documented in the source
after: MahaVISTAAR, Amul AI, Bihar Krishi, Ethiopia, Kenya and Sri Lanka all run on the same OAN governance
  template; each required localised knowledge bases and language models, none required redesigning the
  accountability structure.
adopter_intents:
- We want to expand to other states — how do we federate without losing governance?
- What travels when this model is adopted in another country?
- How quickly can a new country instance be stood up?
related_units:
- unififed-ai-driven-agri-ecosystem-federal-by-design-peer-instances
- unififed-ai-driven-agri-ecosystem-government-mandate-as-precondition
---

## Unit

According to the Bharat Vistaar pathway contributed by COSS (Centre for Open Societal Systems), this is a strategic decision from the deployment.

**Decision.** When federating the system across states, cooperatives, and countries, transfer the governance template — institutional ownership structure, data accountability model, content authority assignment — not just the open-source codebase.

**Alternative considered.** Providing the codebase and architecture documentation, and letting each new instance design its own governance.

**Why.** A new instance that takes the code but not the governance template faces the same institutional questions (who owns what the system says? who corrects a wrong answer?) without the answers worked out. The template does not eliminate local adaptation; it provides the structure within which local adaptation happens safely.

**Context.** The OAN material states: 'What travels each time is the same governance, the same institutional ownership, the same template — made local at every stop.'

## Condition

- **Applies when:** Federating across geographically or institutionally distinct deployments.
- **Fails when:** A single institution controls the full deployment — the template overhead is then unnecessary.

## Before → after

- **Before:** Not documented in the source
- **After:** MahaVISTAAR, Amul AI, Bihar Krishi, Ethiopia, Kenya and Sri Lanka all run on the same OAN governance template; each required localised knowledge bases and language models, none required redesigning the accountability structure.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
