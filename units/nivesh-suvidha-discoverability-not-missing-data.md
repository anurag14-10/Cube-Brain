---
name: Frame the problem as data discoverability, not missing data
type: unit
schema_version: 2
summary: Before scoping any AI capability, establish whether users face an absence of data or an inability
  to find, connect and trust data departments already hold — if it is discoverability, the first investment
  belongs in harmonisation, not model selection or new data collection.
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
stage: explore
also_relevant_at:
- define
source_unit_id: Unit 1
applies_when: The intended users already have workarounds; the data exists in departmental systems but
  is fragmented and inconsistent across them.
fails_when: Not documented in the source
decision: Before scoping any AI capability, establish whether the barrier users face is an absence of
  data or an inability to find, connect, and trust data that already exists across departments. If the
  barrier is discoverability, the first investment belongs in harmonisation — not in model selection or
  new data collection.
alternative_considered: Not documented in the source
reason: Misdiagnosing a discoverability problem as a data-gap problem leads to building new data collection
  infrastructure when the real work is structural — locating, cataloguing and connecting what departments
  already hold. Investors and Udyami Mitras were already generating workarounds (searching across government
  websites, PDFs, circulars and hidden URLs) that confirmed the data existed.
context: Invest UP found that policy, incentive and approval information already existed but was scattered
  across government orders, circulars, GIS layers and APIs; the implementation team focused first on harmonising
  access to that data rather than on AI capability.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do I know whether my problem is a data problem or an AI problem?
related_units:
- nivesh-suvidha-data-structuring-is-the-build
- nivesh-suvidha-design-around-user-workflows
---

## Unit

According to Invest UP's Nivesh Suvidha pathway, this is a strategic decision from the deployment.

**Decision.** Before scoping any AI capability, establish whether the barrier users face is an absence of data or an inability to find, connect, and trust data that already exists across departments. If the barrier is discoverability, the first investment belongs in harmonisation — not in model selection or new data collection.

**Alternative considered.** Not documented in the source

**Why.** Misdiagnosing a discoverability problem as a data-gap problem leads to building new data collection infrastructure when the real work is structural: locating, cataloguing, and connecting what departments already hold. In the investment-facilitation context, investors and Udyami Mitras (investment facilitation officers) were already generating workarounds — searching across government websites, PDFs, circulars and hidden URLs — which confirmed the data existed.

**What this looked like here.** Invest UP found that policy, incentive and approval information already existed but was scattered across government orders, circulars, GIS layers and APIs. The implementation team focused first on harmonising access to that data rather than on AI capability.

## Condition

- **Applies when:** The intended users already have workarounds; the data exists in departmental systems but is fragmented and inconsistent across them.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The users' existing workarounds are the test: if people are already hunting across sources, the data exists and the first build is harmonisation. That changes where an adopter spends first. It is a suggestion from another adoption's lived experience, not a recommendation.
