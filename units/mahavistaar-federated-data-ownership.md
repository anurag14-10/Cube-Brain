---
name: MahaVISTAAR — federated data ownership with four named external relationships
type: unit
schema_version: 2
summary: Federate with each legitimate external data owner (ICAR, IMD, APMC, NIPHM) at query time rather
  than centralising data in an AI-owned repository.
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
unit_type: Strategic Decision
dimension: ecosystem
sub_category: ecosystem-b
stage: define
source_unit_id: Unit 38
applies_when: Sovereignty, DPDP Act compliance, and backend resilience all matter.
fails_when: Not documented in the source
decision: Federate with each legitimate external data owner rather than centralising their data into an
  AI-owned repository.
alternative_considered: Centralising data into an AI-owned repository.
reason: Sovereignty, DPDP Act compliance, and backend resilience all depend on data staying with organisationally
  distinct owners, connected at query time rather than copied.
context: Four relationships were formalised before launch — ICAR (crop advisories), IMD (weather), APMC
  (mandi prices), NIPHM (pest alerts).
before: Not documented in the source
after: Not documented in the source
related_units:
- mahavistaar-name-data-owner-first
- mahavistaar-data-connector-governance-templates
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Federate with each legitimate external data owner rather than centralising their data into an AI-owned repository.

**Alternative considered:** Centralising data into an AI-owned repository.

**Why:** Sovereignty, DPDP Act compliance, and backend resilience all depend on data staying with organisationally distinct owners, connected at query time rather than copied.

**In this deployment:** Four relationships were formalised before launch — ICAR (crop advisories), IMD (weather), APMC (mandi prices), NIPHM (pest alerts).

## Condition

- **Applies when:** Sovereignty, DPDP Act compliance, and backend resilience all matter.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

It is the hard-to-reverse data posture decision an adopter federating government data must take before build.
