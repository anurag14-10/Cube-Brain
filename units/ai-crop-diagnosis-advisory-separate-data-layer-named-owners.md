---
name: Separate the data layer from the AI layer, with a named owner for each source
type: unit
schema_version: 2
summary: Run satellite, weather and soil feeds through a distinct Data Hub layer, each source with a named
  accountable owner and update cadence — a delayed weather feed in the Morocco pilot was fixed without touching
  prompts or model architecture.
doc_refs:
- content/wiki/pathways/ai-crop-diagnosis-advisory.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-crop-diagnosis-advisory.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against concepts/<dimension>.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ai-crop-diagnosis-advisory
unit_type: Strategic Decision
dimension: solution
sub_category: solution-d
stage: define
source_unit_id: Unit 6
applies_when: Multiple data sources with different owners and update cadences; government or institutional
  deployment where data accountability must remain with named departments or providers.
fails_when: Not documented in the source
decision: Architect the Data Hub as a distinct layer from the AI reasoning layer, with each external data source
  (satellite imagery, hyperlocal weather, soil data) governed by a named accountable owner and a defined update
  cadence, rather than embedding data retrieval directly in the AI pipeline.
alternative_considered: Integrate data sources directly into the model pipeline; treat data freshness as an
  operational concern to be managed informally.
reason: When data errors are mixed into the AI layer, debugging requires touching model architecture. When
  the layers are separated, a stale weather feed is fixed by the data owner without touching the AI layer.
  Named accountability also makes it possible to negotiate formal SLAs with data providers at scale, because
  there is a defined interface to enforce.
context: The DeepLeaf Data Hub ingests satellite, weather, and soil feeds through a standardised API layer.
  Each source has a named internal owner responsible for monitoring freshness and raising failures. When a
  weather provider's feed was delayed during the Morocco pilot, the fix was a data-layer intervention that
  did not require any change to model prompts or architecture.
before: Data errors required rebuilding prompt architecture to compensate.
after: Data errors are fixed at the source layer without touching the AI layer.
adopter_intents:
- How do I keep data errors from breaking the AI layer?
related_units:
- ai-crop-diagnosis-advisory-data-ownership-table-template
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a strategic decision from the deployment.

**Decision.** Architect the Data Hub as a distinct layer from the AI reasoning layer, with each external data source (satellite imagery, hyperlocal weather, soil data) governed by a named accountable owner and a defined update cadence, rather than embedding data retrieval directly in the AI pipeline.

**Alternative considered.** Integrate data sources directly into the model pipeline; treat data freshness as an operational concern to be managed informally.

**Why.** When data errors are mixed into the AI layer, debugging requires touching model architecture. When the layers are separated, a stale weather feed is fixed by the data owner without touching the AI layer. Named accountability also makes it possible to negotiate formal SLAs with data providers at scale, because there is a defined interface to enforce.

**What this looked like here.** The DeepLeaf Data Hub ingests satellite, weather, and soil feeds through a standardised API layer. Each source has a named internal owner responsible for monitoring freshness and raising failures. When a weather provider's feed was delayed during the Morocco pilot, the fix was a data-layer intervention that did not require any change to model prompts or architecture.

## Condition

- **Applies when:** Multiple data sources with different owners and update cadences; government or institutional deployment where data accountability must remain with named departments or providers.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Data errors required rebuilding prompt architecture to compensate.
- **After:** Data errors are fixed at the source layer without touching the AI layer.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the reasoning show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
