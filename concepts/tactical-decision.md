---
name: Tactical Decision
type: concept
schema_version: 2
aliases:
- Tactical Decision
summary: A stack, sequence, cost, or implementation decision specific enough to reuse.
concept_kind: unit-type
definition: A stack, sequence, cost, or implementation decision specific enough to reuse.
audience: internal-only
what_makes_it_reusable: 'A before→after: what changed because of this decision.'
broader: unit
doc_refs:
- content/framework.md
- lib/dimensions.ts
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/framework.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Definition

A stack, sequence, cost, or implementation decision specific enough to reuse.

## How it is used

One of the five types every corpus unit is tagged with (`unit_type` on `units/`).

**What makes it reusable:** A before→after: what changed because of this decision.
