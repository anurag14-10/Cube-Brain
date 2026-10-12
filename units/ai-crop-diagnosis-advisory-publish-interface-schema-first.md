---
name: Publish the interface schema before any integration partner starts building
type: unit
schema_version: 2
summary: A stable, versioned schema — inputs, outputs, confidence format, abstention codes, error responses
  — published before partners build, so API, SDK and white-label integration becomes configuration rather than
  bilateral negotiation.
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
sub_category: ecosystem-a
stage: define
source_unit_id: Unit 10
applies_when: More than one integration partner is planned; the deploying organisation cannot afford to be
  the bottleneck for each partner's technical onboarding.
fails_when: Not documented in the source
decision: Before any integration partner (API, SDK, white-label) begins building, publish a stable, versioned
  interface schema — input fields, output fields, confidence format, abstention codes, error responses — so
  integration becomes configuration rather than negotiation.
alternative_considered: Negotiate integration details bilaterally with each partner as they onboard, adapting
  the interface to each partner's system.
reason: 'Bilateral negotiation produces bespoke integrations that cannot be maintained at scale and that make
  the AI provider the bottleneck for every new partner. A published schema inverts this: partners self-serve
  against a documented interface, DeepLeaf''s team is not in the critical path for each integration, and the
  corpus of integrations becomes auditable because all of them implement the same contract.'
context: Agrivi's integration (Croatia) and Hassad Food's enterprise API integration both proceeded against
  the published schema without requiring custom interface negotiation. The Senegal pilot's NGO consortium used
  the same schema with local language and crop adaptations that did not require interface changes.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do I onboard multiple integration partners without becoming a bottleneck?
- What makes this approach transferable to a new geography?
related_units:
- ai-crop-diagnosis-advisory-abstention-and-confidence-as-outputs
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a strategic decision from the deployment.

**Decision.** Before any integration partner (API, SDK, white-label) begins building, publish a stable, versioned interface schema — input fields, output fields, confidence format, abstention codes, error responses — so integration becomes configuration rather than negotiation.

**Alternative considered.** Negotiate integration details bilaterally with each partner as they onboard, adapting the interface to each partner's system.

**Why.** Bilateral negotiation produces bespoke integrations that cannot be maintained at scale and that make the AI provider the bottleneck for every new partner. A published schema inverts this: partners self-serve against a documented interface, DeepLeaf's team is not in the critical path for each integration, and the corpus of integrations becomes auditable because all of them implement the same contract.

**What this looked like here.** Agrivi's integration (Croatia) and Hassad Food's enterprise API integration both proceeded against the published schema without requiring custom interface negotiation. The Senegal pilot's NGO consortium used the same schema with local language and crop adaptations that did not require interface changes.

## Condition

- **Applies when:** More than one integration partner is planned; the deploying organisation cannot afford to be the bottleneck for each partner's technical onboarding.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the reasoning show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
