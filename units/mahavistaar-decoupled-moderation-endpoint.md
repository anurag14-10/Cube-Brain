---
name: MahaVISTAAR — two-endpoint moderation, decoupled from the advisory engine
type: unit
schema_version: 1
summary: Run the moderation model on infrastructure entirely separate from the advisory model so the safety
  layer cannot fail together with the model it moderates.
tags:
- relevant-to-technologist
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
unit_type: Strategic Decision
dimension: solution
sub_category: solution-c
stage: define
source_unit_id: Unit 11
applies_when: A safety layer must not go down together with the primary model.
fails_when: Not documented in the source
decision: Run the moderation model (GPT-OSS Safeguard 20B) on entirely separate infrastructure from the
  advisory engine (Qwen3.5-27B).
alternative_considered: A single integrated model handling both safety and advisory.
reason: A safety layer that depends on the model it moderates is a single point of failure in the worst
  possible place; decoupling lets each fail independently.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do we keep our safety layer from going down with the main model?
related_units:
- mahavistaar-isolate-moderation-gpu-tp8
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Run the moderation model (GPT-OSS Safeguard 20B) on entirely separate infrastructure from the advisory engine (Qwen3.5-27B).

**Alternative considered:** A single integrated model handling both safety and advisory.

**Why:** A safety layer that depends on the model it moderates is a single point of failure in the worst possible place; decoupling lets each fail independently.

## Condition

- **Applies when:** A safety layer must not go down together with the primary model.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

It is an architecture rule any deployment with a safety layer can apply regardless of model choice.
