---
name: Choose the hosting model as a governance decision, not a technical one
type: unit
schema_version: 2
summary: Shared cloud, in-country cloud, sovereign or on-premise is chosen jointly with the deploying institution's
  legal and policy leads before technical integration, because it fixes where farmer data lives and whose law
  governs it.
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
dimension: ecosystem
sub_category: ecosystem-b
stage: define
source_unit_id: Unit 12
applies_when: The deploying institution has data-residency obligations, operates in a jurisdiction with data-sovereignty
  requirements, or serves a population whose data is politically sensitive.
fails_when: Not documented in the source
decision: Treat the hosting choice — shared cloud, in-country cloud, sovereign deployment, on-premise — as
  a governance and data-sovereignty decision made jointly with the deploying institution's legal and policy
  leads, not as a technical optimisation made by the engineering team.
alternative_considered: Default to the lowest-cost or highest-performance hosting option and handle data-sovereignty
  concerns as compliance add-ons if they arise.
reason: Hosting choices determine where farmer data resides, which jurisdiction's law governs it, which regulators
  have authority over the service, and whether the institution can meet its own data-protection obligations.
  Those are legal and policy questions, not engineering questions. Making the hosting choice without legal
  and policy input creates compliance risk that is expensive to unwind after deployment.
context: Each partner institution selects a hosting model using DeepLeaf's hosting-option framework before
  technical integration begins; the framework surfaces regional GPU availability as a real deployment constraint
  rather than something discovered during implementation.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do I handle data-residency and sovereignty requirements?
- What institutional documents should I prepare before a new deployment?
related_units:
- ai-crop-diagnosis-advisory-hosting-option-framework
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a strategic decision from the deployment.

**Decision.** Treat the hosting choice — shared cloud, in-country cloud, sovereign deployment, on-premise — as a governance and data-sovereignty decision made jointly with the deploying institution's legal and policy leads, not as a technical optimisation made by the engineering team.

**Alternative considered.** Default to the lowest-cost or highest-performance hosting option and handle data-sovereignty concerns as compliance add-ons if they arise.

**Why.** Hosting choices determine where farmer data resides, which jurisdiction's law governs it, which regulators have authority over the service, and whether the institution can meet its own data-protection obligations. Those are legal and policy questions, not engineering questions. Making the hosting choice without legal and policy input creates compliance risk that is expensive to unwind after deployment.

**What this looked like here.** Each partner institution selects a hosting model using DeepLeaf's hosting-option framework before technical integration begins; the framework surfaces regional GPU availability as a real deployment constraint rather than something discovered during implementation.

## Condition

- **Applies when:** The deploying institution has data-residency obligations, operates in a jurisdiction with data-sovereignty requirements, or serves a population whose data is politically sensitive.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the reasoning show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
