---
name: African Voice AI — build offline on-device inference first, add telephony second
type: unit
schema_version: 2
summary: Invert the telephony-first sequence of the Indian reference deployments — build offline on-device
  inference as the first architectural phase and add telephony second, where connectivity is unreliable
  and users own smartphone-class devices.
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
sub_category: solution-b
stage: explore
source_unit_id: Unit 1
applies_when: Connectivity is unreliable or absent, and users own smartphone-class devices.
fails_when: Users hold feature phones without app capability — telephony is then the only channel, and
  the sequence reverses back to telephony-first.
decision: Build offline on-device inference as the first architectural phase; add telephony as a second
  phase, rather than the telephony-first sequence used in the reference Indian implementations.
alternative_considered: Telephony-first, matching the Indian deployments this stack was ported from.
reason: In this deployment geography, connectivity is unreliable enough that a network-dependent service
  fails at the exact moment a user needs it; per-minute telephony cost is a real barrier at scale; and
  entry-level Android devices can now run quantised models locally.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- Should we build offline-first or telephony-first?
related_units:
- african-voice-ai-adapt-orchestration-not-fork
---

## Unit

According to Crane AI Labs and the UNDP AI Hub for Sustainable Development's African Voice AI pathway, this is a strategic decision from the Voicera Africa deployment in Kenya.

**Decision.** Build offline on-device inference as the first architectural phase; add telephony as a second phase, rather than the telephony-first sequence used in the reference Indian implementations.

**Alternative considered.** Telephony-first, matching the Indian deployments this stack was ported from.

**Why.** In this deployment geography, connectivity is unreliable enough that a network-dependent service fails at the exact moment a user needs it; per-minute telephony cost is a real barrier at scale; and entry-level Android devices can now run quantised models locally.

## Condition

- **Applies when:** Connectivity is unreliable or absent, and users own smartphone-class devices.
- **Fails when:** Users hold feature phones without app capability — telephony is then the only channel, and the sequence reverses back to telephony-first.

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

It shows that the channel sequence of a reference deployment is a regional choice, not a property of the stack: an adopter porting a voice system can check connectivity and device ownership before inheriting the original order. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
