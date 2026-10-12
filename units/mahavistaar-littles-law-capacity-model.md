---
name: MahaVISTAAR — Little's Law capacity model for concurrency planning
type: unit
schema_version: 2
summary: Occupancy per active user = call rate x time per call, used to derive a node's safe concurrent-user
  ceiling from observed data.
doc_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/mahavistaar.md — applies_when re-read from the unit's 'Reusable as-is' line (audit 2026-10-12)
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: content/wiki/pathways/mahavistaar.md — sub_category inferred; the document tags each unit with dimension, stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-e
stage: scale
source_unit_id: Unit 23
applies_when: Domain-general — any deployment that has its own call-rate and call-duration numbers.
fails_when: Not documented in the source
purpose: Turns observed call-rate and call-duration data into a defensible concurrency ceiling, instead
  of guessing at a load test.
reuse_condition: Domain-general; a new deployment only needs its own call-rate and duration numbers.
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the asset is: a capacity formula — occupancy per active user = call rate × time per call — used to derive a node's safe concurrent-user ceiling.

**Purpose:** Turns observed call-rate and call-duration data into a defensible concurrency ceiling, instead of guessing at a load test.

**Reuse condition:** Domain-general; a new deployment only needs its own call-rate and duration numbers.

## Condition

- **Applies when:** Domain-general — any deployment that has its own call-rate and call-duration numbers.
- **Fails when:** Not documented in the source

## Why it is reusable

A formula any voice deployment can apply with its own two numbers.
