---
name: Design around user workflows, not available technology
type: unit
schema_version: 2
summary: Map the workflow the target user follows to get an answer today, friction points included, and
  design the AI layer to remove those specific frictions — the workflow decides what the data layer must
  do before any AI is built on top.
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
dimension: persona
sub_category: persona-b
stage: define
also_relevant_at:
- explore
source_unit_id: Unit 2
applies_when: The target user's workflow is well-defined and the friction is traceable to specific information-access
  failures, not to a diffuse lack of capability.
fails_when: Not documented in the source
decision: Before selecting a model or architecture, map the actual workflow the target user follows to
  get an answer today — including the friction points — and design the AI layer to remove those friction
  points specifically, rather than showcasing available AI capability.
alternative_considered: Not documented in the source
reason: Investors and Udyami Mitras had a clearly defined task — finding accurate, current policy and
  approval information — and a clearly defined failure mode — hunting across siloed, inconsistent sources.
  Designing around that workflow determined what the data layer needed to do before the AI layer was built
  on top of it.
context: The conversational interface was built on top of a harmonised, catalogued repository structured
  to answer the specific questions investors and Udyami Mitras actually asked — not as a general-purpose
  language model deployment.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do I figure out what the user actually needs before I start building?
related_units:
- nivesh-suvidha-discoverability-not-missing-data
- nivesh-suvidha-data-structuring-is-the-build
---

## Unit

According to Invest UP's Nivesh Suvidha pathway, this is a strategic decision from the deployment.

**Decision.** Before selecting a model or architecture, map the actual workflow the target user follows to get an answer today — including the friction points — and design the AI layer to remove those friction points specifically, rather than showcasing available AI capability.

**Alternative considered.** Not documented in the source

**Why.** The population Nivesh Suvidha serves (investors and Udyami Mitras) had a clearly defined task — finding accurate, current policy and approval information — and a clearly defined failure mode — hunting across siloed, inconsistent sources. Designing around that specific workflow determined what the data layer needed to do before the AI layer was built on top of it.

**What this looked like here.** The conversational interface was built on top of a harmonised, catalogued repository structured to answer the specific questions investors and Udyami Mitras actually asked — not as a general-purpose language model deployment.

## Condition

- **Applies when:** The target user's workflow is well-defined and the friction is traceable to specific information-access failures, not to a diffuse lack of capability.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

It moves the first design input from "what can the model do" to "which questions do users fail to get answered today", which in turn sets the shape of the data layer. It is a suggestion from another adoption's lived experience, not a recommendation.
