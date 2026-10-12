---
name: AI layer retrieves through APIs; each data source stays with its accountable owner
type: unit
schema_version: 2
summary: Build the AI layer as a consumer, not a custodian — live data retrieved at runtime through APIs
  from each owner (NDDB, state government, 21 unions, cooperative banks), so owners fix errors without
  the AI team rebuilding anything.
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
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ai-advisory-for-dairy-farmers
unit_type: Strategic Decision
dimension: solution
sub_category: solution-d
stage: define
also_relevant_at:
- scale
source_unit_id: Unit 5
applies_when: Multiple external institutions own data that the AI layer must surface; data accuracy is
  safety-relevant (veterinary advice, financial transactions); the institution wants to add and remove
  data sources without rebuilding the AI layer.
fails_when: Not documented in the source
decision: Build the AI layer so that it retrieves data at runtime through APIs rather than owning or copying
  the data. Each data source remains with its accountable owner; the AI system is a consumer, not a custodian.
alternative_considered: Ingesting data into a single AI-owned store (the initial instinct, and what was
  done for the static knowledge corpus).
reason: At scale with multiple data sources and multiple institutional owners (NDDB, state government,
  21 unions, cooperative banks), data errors must be fixable by the data owner without requiring the AI
  team to rebuild anything. The AI layer presenting institutional knowledge must not become the de facto
  new source of truth — it must remain a surface over accountable, maintainable sources.
context: The architecture distinguishes between the static knowledge corpus (ingested documents from NDDB,
  vet colleges, state government, Amul's own 50-year archive) and live data retrieved at runtime (milk
  collection records, vaccination history, mandi prices via Bharat Vistaar). Union scheme information
  is pulled nightly from union websites, with named union IT coordinators responsible for keeping their
  page current. The pathway's Gap 2 notes that per-cow yield data, the input personalised advice would
  need, does not yet exist at scale.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do we handle multiple data owners without rebuilding the AI layer every time one changes their data?
- What does the data architecture look like when you have NDDB, state government, unions, and cooperative
  banks all as separate sources?
- What does it take to move from general knowledge retrieval to personalised per-cow advice?
related_units:
- ai-advisory-for-dairy-farmers-staged-open-source-migration
- ai-advisory-for-dairy-farmers-cooperative-tiers-as-distribution
- mahavistaar-federated-data-ownership
---

## Unit

According to GCMMF (Amul) and EkStep Foundation's Amul AI / Sarla Ben pathway, this is a strategic decision from the deployment.

**Decision.** Build the AI layer so that it retrieves data at runtime through APIs rather than owning or copying the data. Each data source remains with its accountable owner; the AI system is a consumer, not a custodian.

**Alternative considered.** Ingesting data into a single AI-owned store (the initial instinct, and what was done for the static knowledge corpus).

**Why.** At scale with multiple data sources and multiple institutional owners (NDDB, state government, 21 unions, cooperative banks), data errors must be fixable by the data owner without requiring the AI team to rebuild anything. The AI layer presenting institutional knowledge must not become the de facto new source of truth — it must remain a surface over accountable, maintainable sources.

**In this deployment.** The architecture distinguishes between the static knowledge corpus (ingested documents from NDDB, vet colleges, state government, Amul's own 50-year archive) and live data retrieved at runtime (milk collection records, vaccination history, mandi prices via Bharat Vistaar). Union scheme information is pulled nightly from union websites, with named union IT coordinators responsible for keeping their page current. The pathway's Gap 2 notes that per-cow yield data, the input personalised advice would need, does not yet exist at scale.

## Condition

- **Applies when:** Multiple external institutions own data that the AI layer must surface; data accuracy is safety-relevant (veterinary advice, financial transactions); the institution wants to add and remove data sources without rebuilding the AI layer.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
