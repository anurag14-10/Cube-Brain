---
name: African Voice AI — a plugin architecture, not the use case, makes the SDK sector-agnostic
type: unit
schema_version: 2
summary: Build a standardised extension interface so any ASR, TTS or LLM component can be registered for
  any language or domain — agriculture is the first populated slot, and the interface specification is
  the actually reusable asset.
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
unit_type: Strategic Decision
dimension: solution
sub_category: solution-c
stage: define
source_unit_id: Unit 4
applies_when: Building infrastructure intended for reuse across sectors or languages.
fails_when: A single-purpose deployment with no reuse intent — the abstraction cost isn't repaid.
decision: Build a standardised extension interface allowing any ASR, TTS, or LLM component to be registered
  for any language or domain, rather than hard-coding agriculture into the platform.
reason: Agriculture is not hard-coded into this system — it is the first populated slot. The system is
  sector-agnostic only to the extent the interface itself guarantees it, which makes the interface specification,
  not the agricultural implementation, the actually reusable asset.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do we make one SDK work across sectors or languages?
related_units:
- african-voice-ai-sdk-plugin-interface
---

## Unit

According to Crane AI Labs and the UNDP AI Hub for Sustainable Development's African Voice AI pathway, this is a strategic decision from the Voicera Africa deployment in Kenya.

**Decision.** Build a standardised extension interface allowing any ASR, TTS, or LLM component to be registered for any language or domain, rather than hard-coding agriculture into the platform.

**Why.** Agriculture is not hard-coded into this system — it is the first populated slot. The system is sector-agnostic only to the extent the interface itself guarantees it, which makes the interface specification, not the agricultural implementation, the actually reusable asset.

## Condition

- **Applies when:** Building infrastructure intended for reuse across sectors or languages.
- **Fails when:** A single-purpose deployment with no reuse intent — the abstraction cost isn't repaid.

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

It tells an adopter where reuse value actually sits — in the extension interface, not the first domain built on it — and when the abstraction is not worth its cost. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
