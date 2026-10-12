---
name: Assign content authority to a named agronomist, not the technology team
type: unit
schema_version: 2
summary: A named qualified agronomist in or contracted to the deploying institution decides which crops, treatments
  and abstention triggers the system covers, and signs off before new crops or conditions are added.
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
dimension: institution
sub_category: institution-a
stage: define
source_unit_id: Unit 8
applies_when: The system gives advice with material consequences; the deploying institution has or can contract
  a qualified agronomist; regulatory or reputational risk from wrong advice is non-trivial.
fails_when: Not documented in the source
decision: Assign authority over what the system is permitted to say — which crops are covered, which treatments
  are recommended, which conditions trigger abstention — to a named qualified agronomist within or contracted
  to the deploying institution, not to the technology or product team.
alternative_considered: Allow the technology team to manage knowledge corpus content as a product decision,
  with agronomists consulted when issues arise.
reason: 'When the technology team controls content, agronomic errors are discovered by users rather than prevented
  by domain experts. Naming a content authority creates a single accountable person whose professional reputation
  is tied to what the system says — the strongest governance mechanism available. It also creates a clear escalation
  path: any advice dispute goes to that person, not to a support queue.'
context: Each DeepLeaf deployment has a named agronomist who owns the local knowledge corpus and whose sign-off
  is required before new crops or conditions are added to the system's coverage. The agronomist, not the product
  team, defines what the system does and does not cover.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- Who should own what the system is allowed to say?
- How do I structure agronomist review and escalation?
related_units:
- ai-crop-diagnosis-advisory-curated-retrieval-over-fine-tuning
- ai-crop-diagnosis-advisory-seven-institutional-changes-before-signing
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a strategic decision from the deployment.

**Decision.** Assign authority over what the system is permitted to say — which crops are covered, which treatments are recommended, which conditions trigger abstention — to a named qualified agronomist within or contracted to the deploying institution, not to the technology or product team.

**Alternative considered.** Allow the technology team to manage knowledge corpus content as a product decision, with agronomists consulted when issues arise.

**Why.** When the technology team controls content, agronomic errors are discovered by users rather than prevented by domain experts. Naming a content authority creates a single accountable person whose professional reputation is tied to what the system says — the strongest governance mechanism available. It also creates a clear escalation path: any advice dispute goes to that person, not to a support queue.

**What this looked like here.** Each DeepLeaf deployment has a named agronomist who owns the local knowledge corpus and whose sign-off is required before new crops or conditions are added to the system's coverage. The agronomist, not the product team, defines what the system does and does not cover.

## Condition

- **Applies when:** The system gives advice with material consequences; the deploying institution has or can contract a qualified agronomist; regulatory or reputational risk from wrong advice is non-trivial.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the reasoning show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
