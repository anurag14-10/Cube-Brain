---
name: African Voice AI — adapt the orchestration pattern; there is no single repository to fork
type: unit
schema_version: 2
summary: Reuse the Pipecat-based orchestration pattern and service-factory structure instead of building
  orchestration from scratch — and do not expect a single forkable "VoicERA" codebase, because the stack
  is a name over open components.
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
unit_type: Tactical Decision
dimension: solution
sub_category: solution-c
stage: explore
source_unit_id: Unit 2
applies_when: Porting any voice stack across regions.
fails_when: Not documented in the source
decision: Adapt the Pipecat-based orchestration pattern and service-factory structure rather than build
  orchestration from scratch, or assume a single "VoicERA" codebase exists to clone.
alternative_considered: Building orchestration in-house; expecting a single forkable repository.
reason: There is no single repository — the stack is a name over open components (Pipecat, ULCA, AI4Bharat
  models). Adopters expecting a clonable repo lose real time discovering this isn't how it works.
before: An assumption of a forkable stack.
after: An adaptation workstream, with the pattern reused and the components rebuilt for the new context.
adopter_intents:
- Can we reuse an existing voice orchestration stack instead of building one?
related_units:
- african-voice-ai-telephony-does-not-port
- mahavistaar-voiceera-orchestration-platform
---

## Unit

According to Crane AI Labs and the UNDP AI Hub for Sustainable Development's African Voice AI pathway, this is a tactical decision from the Voicera Africa deployment in Kenya.

**Decision.** Adapt the Pipecat-based orchestration pattern and service-factory structure rather than build orchestration from scratch, or assume a single "VoicERA" codebase exists to clone.

**Alternative considered.** Building orchestration in-house; expecting a single forkable repository.

**Why.** There is no single repository — the stack is a name over open components (Pipecat, ULCA, AI4Bharat models). Adopters expecting a clonable repo lose real time discovering this isn't how it works.

## Condition

- **Applies when:** Porting any voice stack across regions.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** An assumption of a forkable stack.
- **After:** An adaptation workstream, with the pattern reused and the components rebuilt for the new context.

## Why it is reusable

It resets an adopter's plan for reusing the India-built orchestration stack (see the [MahaVISTAAR](../pathways/mahavistaar.md) orchestration platform): budget an adaptation workstream, not a clone-and-configure step. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
