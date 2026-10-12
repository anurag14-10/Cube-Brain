---
name: MahaVISTAAR — isolate moderation onto its own GPU to unlock TP=8
type: unit
schema_version: 1
summary: Moving the small moderation model off the shared 8-GPU node onto one dedicated H100 freed the
  node for TP=8 and roughly doubled concurrent users per node.
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
sub_category: solution-e
stage: scale
source_unit_id: Unit 21
applies_when: A small auxiliary model shares a node with a much larger primary model and blocks a step
  up in tensor-parallel width.
fails_when: Not documented in the source
decision: Move the moderation model off the shared 8-GPU node onto a dedicated single H100, freeing all
  8 main-node GPUs for the advisory LLM at TP=8.
alternative_considered: Leaving the naive 4/2/2 GPU split in place.
reason: Tensor parallelism only accepts power-of-two widths; a small auxiliary model sharing the node
  was blocking the step from TP=4 to TP=8.
before: ~80 concurrent users per node, 2 of 8 GPUs stranded.
after: ~160+ concurrent users per node, for one additional H100.
related_units:
- mahavistaar-decoupled-moderation-endpoint
- mahavistaar-cost-modelling-framework
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Move the moderation model off the shared 8-GPU node onto a dedicated single H100, freeing all 8 main-node GPUs for the advisory LLM at TP=8.

**Alternative considered:** Leaving the naive 4/2/2 GPU split in place.

**Why:** Tensor parallelism only accepts power-of-two widths; a small auxiliary model sharing the node was blocking the step from TP=4 to TP=8.

## Condition

- **Applies when:** A small auxiliary model shares a node with a much larger primary model and blocks a step up in tensor-parallel width.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** ~80 concurrent users per node, 2 of 8 GPUs stranded.
- **After:** ~160+ concurrent users per node, for one additional H100.

## Why it is reusable

A specific, checkable serving-stack fix for any self-hosted deployment co-locating a small auxiliary model with a large one.
