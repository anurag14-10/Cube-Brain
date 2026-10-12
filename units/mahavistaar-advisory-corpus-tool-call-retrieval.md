---
name: MahaVISTAAR — advisory corpus chunked and metadata-tagged for tool-call retrieval
type: unit
schema_version: 2
summary: ICAR and state-university crop/pest/scheme knowledge structured so the advisory engine calls
  it as a tool, not via free-text search.
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
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-d
stage: define
source_unit_id: Unit 15
applies_when: Not documented in the source
fails_when: Not documented in the source
purpose: Lets the advisory engine call structured knowledge as a tool at query time instead of relying
  on unstructured retrieval.
reuse_condition: Via OpenAgriNet; explicitly requires adaptation for different states' scheme structures.
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the asset is: ICAR and state-university crop/pest/scheme knowledge, structured for tool-call retrieval rather than free-text search.

**Purpose:** Lets the advisory engine call structured knowledge as a tool at query time instead of relying on unstructured retrieval.

**Reuse condition:** Via OpenAgriNet; explicitly requires adaptation for different states' scheme structures.

## Condition

- **Applies when:** Not documented in the source
- **Fails when:** Not documented in the source

## Why it is reusable

The structuring approach (chunked, metadata-tagged, exposed as a tool) transfers even where the content must be re-adapted per state.
