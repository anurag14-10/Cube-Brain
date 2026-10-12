---
name: MahaVISTAAR — fix dead silence with a hold message plus a latency investment
type: unit
schema_version: 2
summary: 3–4 seconds of silence during a multi-source fetch read as a dropped call; a hold message plus
  latency work (to ~1s) fixed it — in voice, perceived failure is silence.
doc_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: content/wiki/pathways/mahavistaar.md — sub_category inferred; the document tags each unit with dimension, stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Failure and Fix
dimension: solution
sub_category: solution-e
stage: pilot
source_unit_id: Unit 17
applies_when: The system must call multiple live sources before answering, on voice.
fails_when: Not documented in the source
failure: 3–4 seconds of silence during a multi-source backend fetch read to callers as a dropped call.
fix: A hold message plus a latency-reduction investment brought fetch time to roughly one second.
insight: In voice, perceived failure is about silence, not absolute latency — the first fix can be UX,
  not only engineering.
adopter_intents:
- Calls feel like they're dropping during a live lookup — what do we do?
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet:

- **Failure:** 3–4 seconds of silence during a multi-source backend fetch read to callers as a dropped call.
- **Fix:** A hold message plus a latency-reduction investment brought fetch time to roughly one second.
- **Insight:** In voice, perceived failure is about silence, not absolute latency — the first fix can be UX, not only engineering.

## Condition

- **Applies when:** The system must call multiple live sources before answering, on voice.
- **Fails when:** Not documented in the source

## Why it is reusable

It tells an adopter that the first response to latency complaints on voice can be a UX change, buying time for the engineering fix.
