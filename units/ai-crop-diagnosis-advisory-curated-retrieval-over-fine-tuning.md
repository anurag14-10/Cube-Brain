---
name: Use a curated, versioned retrieval corpus over fine-tuning for agronomic content
type: unit
schema_version: 2
summary: Ground advice in a curated, versioned corpus tagged by crop, condition, geography and source authority
  — agronomists update entries without retraining, and every recommendation returns citations a reviewer can
  check.
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
sub_category: solution-c
stage: define
source_unit_id: Unit 4
applies_when: The advice domain requires ongoing updates (new crop varieties, changing pest pressures, revised
  pesticide registrations), and the deploying institution must be able to audit what the system is saying and
  why.
fails_when: The knowledge domain is highly stable and the primary risk is model capability, not content currency.
decision: Ground the advisory system in a curated, versioned retrieval corpus rather than baking agronomic
  knowledge into model weights through fine-tuning or RAG over unstructured text.
alternative_considered: Fine-tune a base language model on agronomic text corpora, or use general-purpose RAG
  over unstructured extension documents.
reason: Fine-tuned knowledge becomes stale without retraining and cannot be audited at the claim level. Unstructured
  RAG retrieves plausible-sounding but unverifiable content. A curated retrieval corpus with named source documents
  and versioned entries makes every claim traceable, allows agronomists to update content without touching
  model weights, and makes the system auditable — which is a prerequisite for regulatory and institutional
  trust in an advice-giving system.
context: DeepLeaf maintains a structured knowledge corpus where each entry is tagged by crop, condition, geography,
  and source authority. Updates to protocols or treatment recommendations are made by agronomists editing corpus
  entries, not by retraining. The system returns citations alongside recommendations so reviewers can verify
  what was retrieved.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- Should I fine-tune a model or use retrieval for agronomic knowledge?
related_units:
- ai-crop-diagnosis-advisory-agronomist-owns-content-authority
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a strategic decision from the deployment.

**Decision.** Ground the advisory system in a curated, versioned retrieval corpus rather than baking agronomic knowledge into model weights through fine-tuning or RAG over unstructured text.

**Alternative considered.** Fine-tune a base language model on agronomic text corpora, or use general-purpose RAG over unstructured extension documents.

**Why.** Fine-tuned knowledge becomes stale without retraining and cannot be audited at the claim level. Unstructured RAG retrieves plausible-sounding but unverifiable content. A curated retrieval corpus with named source documents and versioned entries makes every claim traceable, allows agronomists to update content without touching model weights, and makes the system auditable — which is a prerequisite for regulatory and institutional trust in an advice-giving system.

**What this looked like here.** DeepLeaf maintains a structured knowledge corpus where each entry is tagged by crop, condition, geography, and source authority. Updates to protocols or treatment recommendations are made by agronomists editing corpus entries, not by retraining. The system returns citations alongside recommendations so reviewers can verify what was retrieved.

## Condition

- **Applies when:** The advice domain requires ongoing updates (new crop varieties, changing pest pressures, revised pesticide registrations), and the deploying institution must be able to audit what the system is saying and why.
- **Fails when:** The knowledge domain is highly stable and the primary risk is model capability, not content currency.

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the reasoning show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
