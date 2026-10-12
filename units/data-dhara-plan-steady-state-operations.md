---
name: Plan the post-pilot steady state around LLM cost and knowledge-repo upkeep
type: unit
schema_version: 2
summary: Cloud and LLM usage drive cost, and LLM usage is where pilot costs rose unexpectedly; steady state
  needs usage tracking, a self-updating knowledge repository, a self-hosted-vs-subscription LLM decision and
  continuous feedback.
doc_refs:
- content/library-wiki/pathways/data-dhara.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/data-dhara.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: dimension, sub_category, stage and unit_type assigned by best reading against content/framework.md —
    the library document is a conversational overview, not framework-structured
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: data-dhara
unit_type: Tactical Decision
dimension: institution
sub_category: institution-f
stage: pilot
also_relevant_at:
- scale
applies_when: Not documented in the source
fails_when: Not documented in the source
decision: 'Plan the post-pilot steady state around five requirements: infrastructure and LLM usage tracking;
  a process to self-update the knowledge repository; a self-hosted versus subscription LLM decision; continuous
  feedback collection; continuous enhancement of the knowledge repository.'
reason: The cost drivers are cloud cost and LLM (Claude credit) usage, and LLM usage is where costs unexpectedly
  increased.
before: LLM (Claude credit) usage was where pilot costs unexpectedly increased.
after: Not documented in the source
related_units:
- data-dhara-hybrid-hosting-build-then-migrate
- data-dhara-iterate-instead-of-waiting-for-repository
---

## Unit

According to the Data DHARA pathway's account of Nivesh Suvidha (Invest UP), this is a tactical decision from the deployment.

**Decision.** Plan the post-pilot steady state around five requirements: infrastructure and LLM usage tracking; a process to self-update the knowledge repository; a self-hosted versus subscription LLM decision; continuous feedback collection; continuous enhancement of the knowledge repository.

**Why.** The cost drivers are cloud cost and LLM (Claude credit) usage, and LLM usage is where costs unexpectedly increased.

## Condition

- **Applies when:** Not documented in the source
- **Fails when:** Not documented in the source

## Before → after

- **Before:** LLM (Claude credit) usage was where pilot costs unexpectedly increased.
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
