---
name: MahaVISTAAR — staged, gated institutional testing before public launch
type: unit
schema_version: 2
summary: Builder team → small institutional group → wider institutional group across geographies/accents
  → limited district rollout; don't outsource testing to the vendor.
doc_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: content/wiki/pathways/mahavistaar.md — sub_category inferred; the document tags each unit with dimension, stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Playbook
dimension: institution
sub_category: institution-c
stage: pilot
also_relevant_at:
- define
source_unit_id: Unit 33
applies_when: The system will speak in the name of a public institution.
fails_when: Not documented in the source
steps:
- The builder/project team tests first.
- A small institutional group tests next.
- A wider institutional group tests across geographies, accents, and scenarios.
- Only then does a limited district-level rollout begin, ahead of wider expansion.
common_failure_mode: Fully outsourcing testing to a vendor — explicitly flagged as risky, because the
  vendor's public credibility isn't the one on the line.
adopter_intents:
- How do we test this without breaking public trust on day one?
related_units:
- mahavistaar-adversarial-test-set
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the sequence is:

1. The builder/project team tests first.
2. A small institutional group tests next.
3. A wider institutional group tests across geographies, accents, and scenarios.
4. Only then does a limited district-level rollout begin, ahead of wider expansion.

**Common failure mode:** Fully outsourcing testing to a vendor — explicitly flagged as risky, because the vendor's public credibility isn't the one on the line.

## Condition

- **Applies when:** The system will speak in the name of a public institution.
- **Fails when:** Not documented in the source

## Why it is reusable

The widening, gated sequence keeps the institution's own staff in the loop and lets an adopter plan test stages with named gates.
