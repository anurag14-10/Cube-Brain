---
name: MahaVISTAAR — published transferable-asset bundle for the next adopter
type: unit
schema_version: 2
summary: The architecture note, cost model, adversarial test set, bilingual glossary and data-connector
  governance templates, published together as one bundle for a next adopter in a similar domain.
doc_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/mahavistaar.md — Section 4 (Toolkits and Playbooks), row 8
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: content/wiki/pathways/mahavistaar.md — unit_type recorded as Toolkit Asset although Section 4 labels
    the row Playbook (no steps are given); dimension, sub_category and stage inferred, the row carries none
contested:
- field: unit_type
  readings:
  - 'grounding Section 4, row 8: Playbook'
  - 'brain: Toolkit Asset — the row names a bundle of artifacts and gives no gated sequence of steps'
  note: CONVENTIONS rule 5 says a Playbook is a gated sequence and a Toolkit Asset is an artifact. No steps
    are recorded because the document gives none. Not arbitrated beyond that.
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Toolkit Asset
dimension: ecosystem
sub_category: ecosystem-f
stage: scale
source_unit_id: Section 4, row 8
applies_when: Any deployment expecting to inform a next adopter in a similar domain.
fails_when: Not documented in the source
purpose: Publishes the deployment's transferable assets together — architecture note, cost model, adversarial
  test set, bilingual glossary and data-connector governance templates — for a next adopter in a similar
  domain.
reuse_condition: Applies to any deployment expecting to inform a next adopter in a similar domain. Per
  the pathway, the cost model sits in the MahaVISTAAR Architecture Note (May 2026), the adversarial test
  set and glossary are reached via the OpenAgriNet ecosystem, and the governance templates via EkStep Foundation.
related_units:
- mahavistaar-dual-provider-inference-stack
- mahavistaar-cost-modelling-framework
- mahavistaar-adversarial-test-set
- mahavistaar-bilingual-agri-glossary
- mahavistaar-data-connector-governance-templates
- mahavistaar-architecture-transfers-trust-doesnt
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the deployment published a transferable-asset bundle made up of five pieces:

- the architecture note ([dual-provider inference stack](mahavistaar-dual-provider-inference-stack.md));
- the cost model ([cost modelling framework](mahavistaar-cost-modelling-framework.md));
- the [adversarial test set](mahavistaar-adversarial-test-set.md);
- the [bilingual Marathi↔English glossary](mahavistaar-bilingual-agri-glossary.md);
- the [data-connector governance templates](mahavistaar-data-connector-governance-templates.md).

The document's toolkit table lists this bundle as a Playbook but gives no steps. The brain records it as an artifact bundle (see `contested`).

## Condition

- **Applies when:** Any deployment expecting to inform a next adopter in a similar domain.
- **Fails when:** Not documented in the source

## Why it is reusable

It tells a next adopter which of this deployment's artifacts were packaged for transfer, so they can ask for the set instead of piecing it together. The pathway also records what reuse led to: Ethiopia's ATI built on MahaVISTAAR's architecture in three months, and Amul/Sarlaben, drawing on two cycles of shared learning, launched in three weeks ([what transfers and what doesn't](mahavistaar-architecture-transfers-trust-doesnt.md)). The document does not say the bundle itself caused those speed-ups.
