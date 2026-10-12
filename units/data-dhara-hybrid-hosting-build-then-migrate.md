---
name: Build on public cloud for speed, then migrate to the institution's own cloud
type: unit
schema_version: 1
summary: Build on AWS for speed, then migrate to Invest UP's own cloud with full data and code ownership,
  keeping a cloud-agnostic open-source foundation layer separable from the vendor's instance to avoid
  lock-in.
code_refs:
- content/library-wiki/pathways/data-dhara.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/data-dhara.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: dimension, sub_category, stage and unit_type assigned by best reading against content/framework.md
    — the library document is a conversational overview, not framework-structured
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: data-dhara
unit_type: Tactical Decision
dimension: solution
sub_category: solution-c
stage: define
applies_when: Not documented in the source
fails_when: Not documented in the source
decision: 'Use a hybrid approach: build on AWS during the build phase for speed, then migrate to Invest
  UP''s own cloud infrastructure with full data and code ownership at Invest UP; keep the foundation layer
  cloud-agnostic and open-source, separable from the vendor instance.'
alternative_considered: Not documented in the source
reason: AWS gave speed during the build; separating the open-source foundation layer from the vendor instance
  avoids lock-in.
context: The vendor (Kenpath Technologies) builds and maintains the tools, pipeline, chatbot and telemetry;
  EkStep/People+AI own the reusable DPG layer.
before: The system was built and run on AWS during the build phase.
after: Hosted on Invest UP's own cloud infrastructure, with full data and code ownership sitting with
  Invest UP.
related_units:
- data-dhara-public-data-revocable-vendor-access
---

## Unit

According to the Data DHARA pathway's account of Nivesh Suvidha (Invest UP), this is a tactical decision from the deployment.

**Decision.** Use a hybrid approach: build on AWS during the build phase for speed, then migrate to Invest UP's own cloud infrastructure with full data and code ownership at Invest UP; keep the foundation layer cloud-agnostic and open-source, separable from the vendor instance.

**Alternative considered.** Not documented in the source

**Why.** AWS gave speed during the build; separating the open-source foundation layer from the vendor instance avoids lock-in.

**Context.** The vendor (Kenpath Technologies) builds and maintains the tools, pipeline, chatbot and telemetry; EkStep/People+AI own the reusable DPG layer.

## Condition

- **Applies when:** Not documented in the source
- **Fails when:** Not documented in the source

## Before → after

- **Before:** The system was built and run on AWS during the build phase.
- **After:** Hosted on Invest UP's own cloud infrastructure, with full data and code ownership sitting with Invest UP.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
