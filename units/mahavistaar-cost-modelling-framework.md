---
name: MahaVISTAAR — cost modelling framework (bundled vs self-hosted)
type: unit
schema_version: 2
summary: Azure-vs-self-hosted cost comparison, prefix-caching strategy and GPU allocation guidance for
  TP=4→TP=8; stated to apply above 100K queries/month.
doc_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-c
stage: scale
source_unit_id: Unit 25
applies_when: Deployments at more than 100K queries/month.
fails_when: Not documented in the source
purpose: Gives a deployment approaching six-figure monthly volume a concrete basis for the bundled-vs-self-hosted
  decision, rather than a rough guess.
reuse_condition: Documented in the MahaVISTAAR Architecture Note (May 2026); stated to apply at >100K
  queries/month.
adopter_intents:
- What's actually driving our LLM costs, and can we bring them down?
related_units:
- mahavistaar-start-bundled-design-to-unbundle
- mahavistaar-prefix-caching
- mahavistaar-isolate-moderation-gpu-tp8
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the asset is: Azure-vs-self-hosted cost comparison, prefix-caching strategy, and GPU allocation guidance for a TP=4→TP=8 migration.

**Purpose:** Gives a deployment approaching six-figure monthly volume a concrete basis for the bundled-vs-self-hosted decision, rather than a rough guess.

**Reuse condition:** Documented in the MahaVISTAAR Architecture Note (May 2026); stated to apply at >100K queries/month.

**In this deployment:** The pathway's cost anchor: the self-hosted 16-GPU build-out pencils at roughly ₹2 crore annually against a projected ₹18 crore/year on Azure at the same scale (as of mid-2026).

## Condition

- **Applies when:** Deployments at more than 100K queries/month.
- **Fails when:** Not documented in the source

## Why it is reusable

It gives an adopter approaching scale a worked basis for the unbundling decision instead of a guess.
