---
name: MahaVISTAAR — name the data owner before naming the data source
type: unit
schema_version: 2
summary: Every data source formalised before launch gets a named institutional owner accountable for accuracy,
  update frequency and correction (ICAR, IMD, APMC, NIPHM).
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
dimension: institution
sub_category: institution-e
stage: define
source_unit_id: Unit 29
applies_when: Multiple institutions or departments each hold a piece of the data the system depends on.
fails_when: Not documented in the source
decision: Give each data source formalised before launch a named institutional owner accountable for accuracy,
  update frequency, and correction.
reason: Discovering an unowned data source at Pilot stage risks costing months; naming the owner upfront
  makes correction someone's job rather than nobody's.
context: ICAR, IMD, APMC, and NIPHM each had a named institutional owner before launch.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- What data questions should we ask before writing any code?
related_units:
- mahavistaar-five-data-questions-checklist
- mahavistaar-federated-data-ownership
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Give each data source formalised before launch a named institutional owner accountable for accuracy, update frequency, and correction.

**Why:** Discovering an unowned data source at Pilot stage risks costing months; naming the owner upfront makes correction someone's job rather than nobody's.

**In this deployment:** ICAR, IMD, APMC, and NIPHM each had a named institutional owner before launch.

## Condition

- **Applies when:** Multiple institutions or departments each hold a piece of the data the system depends on.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

It converts a data-source list into an accountability list before build, which is where an adopter can still fix gaps cheaply.
