---
name: Open-source models as the day-one goal, migrated in validated stages
type: unit
schema_version: 2
summary: Commit from the start to open-source models, using proprietary models only as a transition scaffold;
  migrate 20/80 → 40/60 → 100% open-source, privately hosted, with no farmer data going to external model
  providers.
doc_refs:
- content/wiki/pathways/ai-advisory-for-dairy-farmers.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-advisory-for-dairy-farmers.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
contested:
- field: unit_type
  readings:
  - Strategic Decision (Section 3, Unit 4)
  - 'Tactical Decision (Section 4 table, row 4: ''Open-source model migration staging (20/40/100%)'')'
  note: Both readings are in the same grounding document; Section 3 is the unit's own tag and is used
    here.
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ai-advisory-for-dairy-farmers
unit_type: Strategic Decision
dimension: solution
sub_category: solution-c
stage: define
source_unit_id: Unit 4
applies_when: The institution is cost-sensitive and sovereignty-conscious; the deployment is in a regulated
  or trust-sensitive domain where data residency matters; the institution has (or can access) technical
  expertise to evaluate open-source model performance.
fails_when: Not documented in the source
decision: Commit from the start to running on open-source models, with proprietary models (OpenAI, Claude)
  used only as a transition scaffold while open-source performance was validated.
alternative_considered: Remaining on proprietary cloud models (OpenAI, Claude were both tested).
reason: The deployment is for a not-for-profit cooperative with cost-consciousness built into its operating
  philosophy. Sovereign data custody and long-term cost control both point toward open-source. The goal
  was stated at the Delhi demo that triggered the project.
context: Migration was staged — started at approximately 20% open-source / 80% cloud, moved to 40/60,
  eventually reached 100% open-source. The team continues to monitor whether newer models outperform the
  current one. The system is hosted privately; no farmer data travels to external model providers.
before: 100% proprietary cloud model.
after: 100% open-source, privately hosted, with an ongoing model-evaluation practice in place.
adopter_intents:
- Should we use open-source or proprietary models?
related_units:
- ai-advisory-for-dairy-farmers-api-retrieval-not-data-custody
---

## Unit

According to GCMMF (Amul) and EkStep Foundation's Amul AI / Sarla Ben pathway, this is a strategic decision from the deployment.

**Decision.** Commit from the start to running on open-source models, with proprietary models (OpenAI, Claude) used only as a transition scaffold while open-source performance was validated.

**Alternative considered.** Remaining on proprietary cloud models (OpenAI, Claude were both tested).

**Why.** The deployment is for a not-for-profit cooperative with cost-consciousness built into its operating philosophy. Sovereign data custody and long-term cost control both point toward open-source. The goal was stated at the Delhi demo that triggered the project.

**In this deployment.** Migration was staged — started at approximately 20% open-source / 80% cloud, moved to 40/60, eventually reached 100% open-source. The team continues to monitor whether newer models outperform the current one. The system is hosted privately; no farmer data travels to external model providers.

## Condition

- **Applies when:** The institution is cost-sensitive and sovereignty-conscious; the deployment is in a regulated or trust-sensitive domain where data residency matters; the institution has (or can access) technical expertise to evaluate open-source model performance.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** 100% proprietary cloud model.
- **After:** 100% open-source, privately hosted, with an ongoing model-evaluation practice in place.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
