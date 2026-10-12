---
name: African Voice AI — telephony integration does not port across regions
type: unit
schema_version: 2
summary: The orchestration pattern's telephony layer expected Plivo-compatible interfaces; Kenya's practical
  provider, Africa's Talking, is not Plivo-compatible, so a custom serialiser was needed — porting telephony
  is a development workstream, not a configuration step.
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
unit_type: Failure and Fix
dimension: ecosystem
sub_category: ecosystem-b
stage: define
source_unit_id: Unit 3
applies_when: Porting any telephony-dependent voice stack across regions.
fails_when: Not documented in the source
failure: The orchestration pattern's telephony layer expects Plivo-compatible interfaces; the practical
  Kenyan telephony provider, Africa's Talking, is not Plivo-compatible, so telephony could not be configured
  out of the box.
fix: A custom serialiser adapting the orchestration pattern to Africa's Talking's interface. Whether this
  fix is complete is not documented in the source.
insight: Orchestration patterns encode the infrastructure assumptions of their region of origin, and telephony
  is where those assumptions are most deeply buried — porting telephony is a development workstream, not
  a configuration step.
adopter_intents:
- Can we reuse an existing voice orchestration stack instead of building one?
- Why won't our telephony provider connect after porting a voice stack?
related_units:
- african-voice-ai-adapt-orchestration-not-fork
- mahavistaar-telephony-protocol-local-network
---

## Unit

According to Crane AI Labs and the UNDP AI Hub for Sustainable Development's African Voice AI pathway, this is a failure and its fix from the Voicera Africa deployment in Kenya.

**Failure.** The orchestration pattern's telephony layer expects Plivo-compatible interfaces; the practical Kenyan telephony provider, Africa's Talking, is not Plivo-compatible, so telephony could not be configured out of the box.

**Fix.** A custom serialiser adapting the orchestration pattern to Africa's Talking's interface. Whether this fix is complete is not documented in the source.

**Insight.** Orchestration patterns encode the infrastructure assumptions of their region of origin, and telephony is where those assumptions are most deeply buried — porting telephony is a development workstream, not a configuration step.

## Condition

- **Applies when:** Porting any telephony-dependent voice stack across regions.
- **Fails when:** Not documented in the source

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

An adopter porting a voice stack can check the local telephony provider's interface against the stack's assumptions before planning, and budget the adapter as engineering work. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
