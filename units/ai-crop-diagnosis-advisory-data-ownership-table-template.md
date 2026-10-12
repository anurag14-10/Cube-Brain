---
name: Data-ownership table template
type: unit
schema_version: 2
summary: A Define-stage template that assigns a named accountable owner and an update cadence to each external
  data source before integration; part of the reusable institutional document set each new deployment inherits.
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
  ref: unit_type, dimension, sub_category and stage assigned by reading the Section 4 row against concepts/ecosystem.md
    — Section 4 gives no tags; Section 0 places data-ownership tables and hosting-choice governance at Ecosystem
    × Define
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ai-crop-diagnosis-advisory
unit_type: Toolkit Asset
dimension: ecosystem
sub_category: ecosystem-b
stage: define
applies_when: Use at Define stage, before integration, when the service depends on external data sources (in
  this deployment satellite imagery, hyperlocal weather and soil data).
fails_when: Not documented in the source
purpose: Assign a named accountable owner and update cadence to each external data source before integration,
  so data accountability is settled before anything is built on the source.
reuse_condition: Use at Define stage to assign a named accountable owner and update cadence to each external
  data source before integration (Section 4, linked to Units 6 and 7).
related_units:
- ai-crop-diagnosis-advisory-separate-data-layer-named-owners
- ai-crop-diagnosis-advisory-seven-institutional-changes-before-signing
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, the asset is: data-ownership table template. It is listed in the pathway's toolkit; the document describes it but does not attach the file or a link.

**Purpose:** Assign a named accountable owner and update cadence to each external data source before integration, so data accountability is settled before anything is built on the source.

**Reuse condition:** Use at Define stage to assign a named accountable owner and update cadence to each external data source before integration (Section 4, linked to Units 6 and 7).

## Condition

- **Applies when:** Use at Define stage, before integration, when the service depends on external data sources (in this deployment satellite imagery, hyperlocal weather and soil data).
- **Fails when:** Not documented in the source

## Why it is reusable

The pathway records it as part of a document set designed from the first deployment to be adapted locally rather than rebuilt, so the next adopter can start from its structure. It is a suggestion from another adoption's lived experience, not a recommendation.
