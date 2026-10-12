---
name: Hosting-option framework (shared cloud / in-country / sovereign / on-premise)
type: unit
schema_version: 2
summary: A framework document spelling out the data-sovereignty, cost and operational implications of four
  hosting models, used by each partner to choose before technical integration; it surfaces regional GPU availability
  as a known constraint.
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
applies_when: Data-residency obligations or sovereignty requirements apply to the deploying institution.
fails_when: Not documented in the source
purpose: Lay out shared cloud, in-country cloud, sovereign and on-premise hosting with their data-sovereignty,
  cost and operational implications, so a partner institution can choose its hosting model as a governance
  decision before technical integration begins — including the constraint that not all cloud providers offer
  the required GPU families in all regions.
reuse_condition: Use when data-residency obligations or sovereignty requirements apply; surfaces GPU-availability
  constraints by region (Section 4, linked to Unit 12).
related_units:
- ai-crop-diagnosis-advisory-hosting-as-governance-decision
- ai-crop-diagnosis-advisory-operating-model-survives-founders
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, the asset is: hosting-option framework (shared cloud / in-country / sovereign / on-premise). It is listed in the pathway's toolkit; the document describes it but does not attach the file or a link.

**Purpose:** Lay out shared cloud, in-country cloud, sovereign and on-premise hosting with their data-sovereignty, cost and operational implications, so a partner institution can choose its hosting model as a governance decision before technical integration begins — including the constraint that not all cloud providers offer the required GPU families in all regions.

**Reuse condition:** Use when data-residency obligations or sovereignty requirements apply; surfaces GPU-availability constraints by region (Section 4, linked to Unit 12).

## Condition

- **Applies when:** Data-residency obligations or sovereignty requirements apply to the deploying institution.
- **Fails when:** Not documented in the source

## Why it is reusable

The pathway records it as part of a document set designed from the first deployment to be adapted locally rather than rebuilt, so the next adopter can start from its structure. It is a suggestion from another adoption's lived experience, not a recommendation.
