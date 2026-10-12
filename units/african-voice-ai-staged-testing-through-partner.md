---
name: African Voice AI — staged, gated testing through the partner relationship
type: unit
schema_version: 2
summary: Internal development team → partner staff (Hello Tractor hub managers) → booking agents → farmers,
  advancing only when a named gate criterion is met — the gate criteria themselves are not documented.
doc_refs:
- content/wiki/pathways/african-voice-ai.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/african-voice-ai.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: african-voice-ai
unit_type: Playbook
dimension: ecosystem
sub_category: ecosystem-c
stage: define
source_unit_id: Unit 7
applies_when: An institutional or commercial partner sits between the technology and the end user — common
  wherever trust is borrowed rather than institutionally owned.
fails_when: Not documented in the source
steps:
- 1. Internal development team.
- 2. Partner staff (Hello Tractor hub managers).
- 3. Booking agents (field users).
- 4. Farmers (end users).
- 'Gates between stages: a named gate criterion is required before advancing to the next stage; the specific
  gate criteria are not documented in the source.'
common_failure_mode: Not documented in the source
adopter_intents:
- How should we sequence testing before real end users touch the system?
related_units:
- african-voice-ai-borrow-trust-from-partner
- mahavistaar-staged-gated-institutional-testing
contested:
- field: stage
  readings:
  - Section 3 tags Unit 7 as Ecosystem × Define (Playbook).
  - The document's own coverage grid cites Unit 7 as the evidence for Solution × Pilot (partial).
  note: The same document disagrees with itself. This entry follows the explicit Section 3 tag; the grid
    reading is kept here rather than arbitrated. The pathway's coverage map is carried from the grid as
    written.
---

## Unit

According to Crane AI Labs and the UNDP AI Hub for Sustainable Development's African Voice AI pathway, this is a playbook from the Voicera Africa deployment in Kenya.

**Steps (in order):**

1. Internal development team.
2. Partner staff (Hello Tractor hub managers).
3. Booking agents (field users).
4. Farmers (end users).

**Gates.** A named gate criterion is required before advancing to the next stage. The specific gate criteria are not documented in the source.

The contributing team notes that the sequence itself is intuitive; the actual discipline is not advancing until a criterion is genuinely met. They also note it independently mirrors the staged institutional-testing chain used in the Indian deployments (see [MahaVISTAAR](../pathways/mahavistaar.md) and [Voice AI for Inclusion](../pathways/voice-ai-for-inclusion.md)), arrived at separately rather than copied.

**Common failure mode.** Not documented in the source

## Condition

- **Applies when:** An institutional or commercial partner sits between the technology and the end user — common wherever trust is borrowed rather than institutionally owned.
- **Fails when:** Not documented in the source

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

It routes testing through the partner that holds the user relationship, in the same widening order a separate deployment arrived at on its own. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
