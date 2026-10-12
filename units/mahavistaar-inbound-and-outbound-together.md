---
name: MahaVISTAAR — design inbound and outbound reach together
type: unit
schema_version: 2
summary: Build inbound question-answering and proactive outbound advisory into the initial design together;
  an inbound-only build needs major rearchitecting to add outbound later.
tags:
- relevant-to-technologist
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
unit_type: Strategic Decision
dimension: persona
sub_category: persona-d
stage: define
also_relevant_at:
- scale
source_unit_id: Unit 4
applies_when: The use case has structured trigger data (weather, crop calendar, scheme deadlines).
fails_when: Not documented in the source
decision: Build inbound query-answering and proactive outbound advisory (crop-calendar alerts, weather-triggered
  pest alerts, pre-harvest timing) into the initial design together, not outbound as a later addition.
alternative_considered: Launch inbound-only, add proactive push later.
reason: A system that only waits for questions is less valuable than one that anticipates them, and an
  inbound-only build needs significant rearchitecting to add outbound once it's live.
context: The pathway's effort section records that MahaVISTAAR was originally architected for inbound
  only; after roughly six months the department realised it needed outbound calling too, and outbound
  turned out to need different technology (one-way IVR delivery rather than a two-way conversational stack)
  that the original RFP and architecture had not anticipated.
before: Inbound-only — farmers call 155313 with questions.
after: 17 lakh farmers/day reached proactively without making a call.
adopter_intents:
- Should we launch inbound-only and add proactive alerts later?
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Build inbound query-answering and proactive outbound advisory (crop-calendar alerts, weather-triggered pest alerts, pre-harvest timing) into the initial design together, not outbound as a later addition.

**Alternative considered:** Launch inbound-only, add proactive push later.

**Why:** A system that only waits for questions is less valuable than one that anticipates them, and an inbound-only build needs significant rearchitecting to add outbound once it's live.

**In this deployment:** The pathway's effort section records that MahaVISTAAR was originally architected for inbound only; after roughly six months the department realised it needed outbound calling too, and outbound turned out to need different technology (one-way IVR delivery rather than a two-way conversational stack) that the original RFP and architecture had not anticipated.

## Condition

- **Applies when:** The use case has structured trigger data (weather, crop calendar, scheme deadlines).
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Inbound-only — farmers call 155313 with questions.
- **After:** 17 lakh farmers/day reached proactively without making a call.

## Why it is reusable

Direction of conversation is an architecture and procurement decision, not a feature toggle; an adopter writing an RFP can decide it up front instead of discovering it after launch.
