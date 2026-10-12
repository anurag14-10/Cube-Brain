---
name: MahaVISTAAR — weather data gaps handled by fallback routing, not by fixing the data
type: unit
schema_version: 2
summary: Rural weather-coverage gaps were handled with wider search radii and graceful fallback in the
  routing layer — tolerance for gaps, not demands for better data.
doc_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Failure and Fix
dimension: ecosystem
sub_category: ecosystem-b
stage: scale
source_unit_id: Unit 40
applies_when: A live external data feed has known, uneven geographic or temporal coverage.
fails_when: Not documented in the source
failure: Some weather data sources have geographic coverage gaps in rural Maharashtra, risking incomplete
  responses.
fix: Expanded search radii and graceful fallback logic built into the routing layer.
insight: When an external dependency has a structural limitation the deployment can't fix, the fix belongs
  in the system's tolerance for gaps, not in a demand for better data.
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet:

- **Failure:** Some weather data sources have geographic coverage gaps in rural Maharashtra, risking incomplete responses.
- **Fix:** Expanded search radii and graceful fallback logic built into the routing layer.
- **Insight:** When an external dependency has a structural limitation the deployment can't fix, the fix belongs in the system's tolerance for gaps, not in a demand for better data.

## Condition

- **Applies when:** A live external data feed has known, uneven geographic or temporal coverage.
- **Fails when:** Not documented in the source

## Why it is reusable

It tells an adopter where to put the fix for external data they don't control.
