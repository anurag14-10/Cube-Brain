---
name: MahaVISTAAR — inventory what already exists before specifying what to build
type: unit
schema_version: 2
summary: Map every institution, dataset and service already serving the population before writing a spec,
  so feasibility becomes 'what can be joined'.
tags:
- relevant-to-social-sector-enterprise
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
dimension: ecosystem
sub_category: ecosystem-a
stage: explore
source_unit_id: Unit 36
applies_when: Multiple institutions already hold relevant data or services independently.
fails_when: Not documented in the source
steps:
- Before writing a specification, map every institution, dataset, and service already operating for the
  target population.
- Only once that map exists, assess feasibility as 'what can be joined' rather than 'what should we build',
  and write the specification from it.
common_failure_mode: Skipping the inventory — which produces a system that duplicates institutional data
  instead of connecting to it.
related_units:
- mahavistaar-four-layer-enabler-map
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the sequence is:

1. Before writing a specification, map every institution, dataset, and service already operating for the target population.
2. Only once that map exists, assess feasibility as 'what can be joined' rather than 'what should we build', and write the specification from it.

**Common failure mode:** Skipping the inventory — which produces a system that duplicates institutional data instead of connecting to it.

## Condition

- **Applies when:** Multiple institutions already hold relevant data or services independently.
- **Fails when:** Not documented in the source

## Why it is reusable

It reorders specification work so adopters connect to existing assets instead of rebuilding them.
