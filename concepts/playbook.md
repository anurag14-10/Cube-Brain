---
name: Playbook
type: concept
schema_version: 1
aliases:
- Playbook
summary: A genuine multi-step, gated sequence — "do X, then don't proceed to Y until X clears, then Z."
  A single decision that merely sounds procedural is a Decision, not a Playbook.
concept_kind: unit-type
definition: A genuine multi-step, gated sequence — "do X, then don't proceed to Y until X clears, then
  Z." A single decision that merely sounds procedural is a Decision, not a Playbook.
audience: internal-only
what_makes_it_reusable: The steps themselves, in order, with the gate between them — plus the common failure
  mode of skipping one.
broader: unit
code_identifier: Playbook
code_refs:
- content/framework.md
- lib/dimensions.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/framework.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Definition

A genuine multi-step, gated sequence — "do X, then don't proceed to Y until X clears, then Z." A single decision that merely sounds procedural is a Decision, not a Playbook.

## How it is used

One of the five types every corpus unit is tagged with (`unit_type` on `units/`).

**What makes it reusable:** The steps themselves, in order, with the gate between them — plus the common failure mode of skipping one.
