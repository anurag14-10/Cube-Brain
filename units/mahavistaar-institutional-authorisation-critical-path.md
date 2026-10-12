---
name: MahaVISTAAR — institutional authorisation is the critical path
type: unit
schema_version: 2
summary: Treat institutional authorisation and named ownership (sponsor + nodal officers) as the critical
  path before any code — no vendor can grant cross-departmental data-sharing.
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
sub_category: institution-a
stage: explore
source_unit_id: Unit 26
applies_when: The deployment needs cross-departmental data-sharing authorisation no vendor can grant alone.
fails_when: Not documented in the source
decision: Treat institutional authorisation and named ownership as the critical path preceding technical
  work, not a parallel task — starting with a named sponsor and nodal officers.
reason: A vendor or technology team can't grant cross-departmental data-sharing authorisation on its own;
  without it, the technical build has nothing legitimate to connect to.
context: An Agri Secretary-level sponsor and named nodal officers across agriculture, IT, and field operations
  were the first concrete decisions.
before: Not documented in the source
after: Data-sharing sign-off across the Department of Agriculture, four universities, IMD, 307 APMCs,
  and MahaDBT was secured before a single line of production code was written.
adopter_intents:
- Who needs to sign off before we go live?
related_units:
- mahavistaar-governance-deferred-after-launch
- mahavistaar-speaks-as-the-institution
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Treat institutional authorisation and named ownership as the critical path preceding technical work, not a parallel task — starting with a named sponsor and nodal officers.

**Why:** A vendor or technology team can't grant cross-departmental data-sharing authorisation on its own; without it, the technical build has nothing legitimate to connect to.

**In this deployment:** An Agri Secretary-level sponsor and named nodal officers across agriculture, IT, and field operations were the first concrete decisions.

## Condition

- **Applies when:** The deployment needs cross-departmental data-sharing authorisation no vendor can grant alone.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Data-sharing sign-off across the Department of Agriculture, four universities, IMD, 307 APMCs, and MahaDBT was secured before a single line of production code was written.

## Why it is reusable

It re-orders the plan for any multi-institution deployment: authorisation first, code second.
