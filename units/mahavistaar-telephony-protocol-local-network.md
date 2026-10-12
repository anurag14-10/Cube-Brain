---
name: MahaVISTAAR — match telephony protocol to local network realities
type: unit
schema_version: 1
summary: Choose the telephony interface protocol from local network conditions (8kHz audio, PSTN, accents)
  — WebSocket APIs rather than the WebRTC some global guidance recommends.
code_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Tactical Decision
dimension: solution
sub_category: solution-b
stage: define
source_unit_id: Unit 14
applies_when: Local telephony/network conditions diverge materially from where 'best practice' recommendations
  were formed.
fails_when: Not documented in the source
decision: Choose the telephony interface protocol based on actual local network conditions, not global
  best-practice defaults.
alternative_considered: WebRTC, recommended in some global contexts.
reason: Global recommendations don't account for local conditions like 8kHz audio, PSTN requirements,
  and regional accent variation.
context: WebSocket APIs were used instead of WebRTC for Indian telephony conditions.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- What telephony protocol should we use?
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Choose the telephony interface protocol based on actual local network conditions, not global best-practice defaults.

**Alternative considered:** WebRTC, recommended in some global contexts.

**Why:** Global recommendations don't account for local conditions like 8kHz audio, PSTN requirements, and regional accent variation.

**In this deployment:** WebSocket APIs were used instead of WebRTC for Indian telephony conditions.

## Condition

- **Applies when:** Local telephony/network conditions diverge materially from where 'best practice' recommendations were formed.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

It warns adopters in PSTN-heavy, low-bandwidth settings not to inherit protocol defaults formed elsewhere.
