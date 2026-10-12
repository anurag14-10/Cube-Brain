---
name: Build the repository iteratively through live deployment, not before it
type: unit
schema_version: 2
summary: Deploy with the highest-value documents at whatever DHARA stage they can reach quickly and advance
  the rest while live, so real user queries — not internal assumptions — prioritise the data-structuring
  backlog.
doc_refs:
- content/wiki/pathways/nivesh-suvidha.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/nivesh-suvidha.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: nivesh-suvidha
unit_type: Strategic Decision
dimension: solution
sub_category: solution-d
stage: pilot
also_relevant_at:
- define
source_unit_id: Unit 5
applies_when: The dataset is large and heterogeneous; a meaningful subset of high-value documents can
  be made searchable and AI-ready ahead of the full corpus.
fails_when: Not documented in the source
decision: Begin deployment with the highest-value documents at whatever DHARA stage they can reach quickly,
  and advance remaining datasets through the pipeline iteratively as the system is live — rather than
  waiting for a fully harmonised repository before any deployment occurs.
alternative_considered: Waiting until all documents reached a uniform stage of readiness before deploying.
reason: A wait-for-completeness approach delays real user feedback indefinitely and removes the signal
  that live use provides about which data gaps actually matter to users. Iterative deployment lets user
  queries drive prioritisation of the data-structuring backlog.
context: Invest UP ingested existing documents first, at whatever stage of the DHARA lifecycle they could
  reach quickly, while continuing to harmonise additional policies and datasets as deployment progressed.
  Real user queries shaped which gaps were tackled next.
before: Teams assumed a fully harmonised repository was a prerequisite.
after: Live queries revealed which documents mattered most, allowing the structuring backlog to be prioritised
  by actual user need rather than internal assumptions.
adopter_intents:
- Do I need all my data ready before I deploy?
related_units:
- nivesh-suvidha-dhara-seven-stage-toolkit
- nivesh-suvidha-gap-flagging-loop
- data-dhara-iterate-instead-of-waiting-for-repository
---

## Unit

According to Invest UP's Nivesh Suvidha pathway, this is a strategic decision from the deployment.

**Decision.** Begin deployment with the highest-value documents at whatever DHARA stage they can reach quickly, and advance remaining datasets through the pipeline iteratively as the system is live — rather than waiting for a fully harmonised repository before any deployment occurs.

**Alternative considered.** Waiting until all documents reached a uniform stage of readiness before deploying.

**Why.** A wait-for-completeness approach delays real user feedback indefinitely and removes the signal that live use provides about which data gaps actually matter to users. Iterative deployment lets user queries drive prioritisation of the data-structuring backlog.

**What this looked like here.** Invest UP ingested existing documents first, at whatever stage of the DHARA lifecycle they could reach quickly, while continuing to harmonise additional policies and datasets as deployment progressed. Real user queries shaped which gaps were tackled next.

## Condition

- **Applies when:** The dataset is large and heterogeneous; a meaningful subset of high-value documents can be made searchable and AI-ready ahead of the full corpus.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Teams assumed a fully harmonised repository was a prerequisite.
- **After:** Live queries revealed which documents mattered most, allowing the structuring backlog to be prioritised by actual user need rather than internal assumptions.

## Why it is reusable

It answers "do we need all our data ready before we launch?" with a tested alternative, and it turns live use into the way the data backlog gets prioritised. The Data DHARA pathway records the same choice from its account of this deployment. It is a suggestion from another adoption's lived experience, not a recommendation.
