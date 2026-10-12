---
name: Voice AI for Inclusion — design for refusal, not just for response
type: unit
schema_version: 2
summary: Build a safety and stress-test bank before public launch (out-of-scope, distress, abuse, complaints
  about officials, jailbreaks, escalation) and test through graded, widening institutional stages — an
  institution's voice agent is experienced as the institution.
doc_refs:
- content/wiki/pathways/voice-ai-for-inclusion.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/voice-ai-for-inclusion.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
contested:
- field: stage
  readings:
  - 'grounding corpus (content/wiki/pathways/voice-ai-for-inclusion.md): Institution × Define'
  - 'library corpus (content/library-wiki/pathways/voice-ai-for-inclusion.md): placed under Institution
    × Pilot ("Design for refusal, not just response")'
  note: The grounding copy is framework-structured and is the primary source; the unit keeps define. Library
    placement recorded, not arbitrated.
pathway: voice-ai-for-inclusion
unit_type: Strategic Decision
dimension: institution
sub_category: institution-c
stage: define
source_unit_id: Unit 6
applies_when: The deployment is institutionally branded and public-facing.
fails_when: Not documented in the source
decision: Build a safety and stress-test bank before public launch, covering in-scope questions, out-of-scope
  questions, sensitive and distress scenarios, abuse or harassment, complaints about officials or policy,
  jailbreak attempts, and questions needing human escalation.
reason: A voice agent backed by an institution is experienced as that institution — a wrong answer, silence,
  or a mishandled sensitive question is read as the institution failing the caller, not as a model error.
  Several deployments reported it as central, particularly where the system used a female voice and drew
  inappropriate conversation attempts.
context: Institutional testing moved through graded, widening stages — the builder team, then a small institutional
  group, then a wider institutional group across geographies and accents, then a limited public rollout
  — with the institution's own staff kept in the loop throughout rather than the testing fully outsourced
  to a vendor.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do we handle out-of-scope or sensitive questions?
related_units:
- voice-ai-for-inclusion-who-does-daily-quality-checks
---

## Unit

According to EkStep Foundation's Voice AI for Inclusion pathway, this is a strategic decision about governance and safety that recurred across the synthesised deployments.

**Decision.** Before public launch, build a safety and stress-test bank covering in-scope questions, out-of-scope questions, sensitive and distress scenarios, abuse or harassment, complaints about officials or policy, jailbreak attempts, and questions needing human escalation.

**Why.** A voice agent backed by an institution is experienced as that institution: a wrong answer, silence, or a mishandled sensitive question is read as the institution failing the caller, not as a model error. Several deployments reported this as central, not marginal — particularly where the system used a female voice and drew inappropriate conversation attempts.

**What this looked like.** Institutional testing moved through graded, widening stages — builder team → small institutional group → wider institutional group across geographies and accents → limited public rollout — with the institution's own staff kept in the loop throughout rather than the testing fully outsourced to a vendor.

## Condition

- **Applies when:** The deployment is institutionally branded and public-facing.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The stress-test categories and the widening test sequence are directly liftable by any institution putting its name on a voice agent. A suggestion, not a recommendation.
