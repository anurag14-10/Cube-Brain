---
name: Define the excluded persona by the advice gap, not the technology gap
type: unit
schema_version: 2
summary: Define the target farmer by the agronomic advice gap they face (biased input-dealer advice, no trusted
  local expert, no service in their language) rather than by device or connectivity profile.
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
dimension: persona
sub_category: persona-a
stage: explore
source_unit_id: Unit 1
applies_when: The advice gap and the technology access gap do not perfectly overlap; some farmers with devices
  still lack trusted advice, and some farmers without devices are the most underserved.
fails_when: Not documented in the source
decision: Define the target persona by the specific agronomic advice gap they face — unreliable input-dealer
  recommendations, no trusted local expert, no service in their language — rather than by their technology
  access profile.
alternative_considered: Segment by device type or connectivity level as a proxy for who to serve.
reason: Technology access predicts reach but not need. Farmers with smartphones still receive wrong or commercially
  biased advice; farmers without smartphones may have the most acute advice gap. Starting from the advice gap
  identifies who actually needs the service and shapes what the system must do, rather than who is easiest
  to reach technically.
context: DeepLeaf's entry point in Morocco was the observation that fertiliser-dealer advice was the dominant
  agronomic information channel for smallholders, and that advice was commercially biased. The persona was
  defined as a farmer making input and treatment decisions without access to a disinterested, validated source
  — not as a smartphone user or a connected farmer.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do I define who this is actually for?
related_units:
- ai-crop-diagnosis-advisory-name-the-workaround-first
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a strategic decision from the deployment.

**Decision.** Define the target persona by the specific agronomic advice gap they face — unreliable input-dealer recommendations, no trusted local expert, no service in their language — rather than by their technology access profile.

**Alternative considered.** Segment by device type or connectivity level as a proxy for who to serve.

**Why.** Technology access predicts reach but not need. Farmers with smartphones still receive wrong or commercially biased advice; farmers without smartphones may have the most acute advice gap. Starting from the advice gap identifies who actually needs the service and shapes what the system must do, rather than who is easiest to reach technically.

**What this looked like here.** DeepLeaf's entry point in Morocco was the observation that fertiliser-dealer advice was the dominant agronomic information channel for smallholders, and that advice was commercially biased. The persona was defined as a farmer making input and treatment decisions without access to a disinterested, validated source — not as a smartphone user or a connected farmer.

## Condition

- **Applies when:** The advice gap and the technology access gap do not perfectly overlap; some farmers with devices still lack trusted advice, and some farmers without devices are the most underserved.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the reasoning show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
