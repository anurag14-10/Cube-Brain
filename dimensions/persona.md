---
name: Persona
type: dimension
schema_version: 1
aliases:
- persona
summary: Are we solving the right problem for the right person?
code: persona
central_question: Are we solving the right problem for the right person?
shift: From starting with AI to starting with a specific human outcome
thesis_group: build-the-right-thing
ui_color: '#ff6543'
data_concern: evidence for problem/population/outcome
trust_concern: does the excluded user trust this channel enough to use it
order: 1
code_refs:
- lib/dimensions.ts
- content/framework.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/dimensions.ts
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/framework.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it asks

Are we solving the right problem for the right person?

*From starting with AI to starting with a specific human outcome*



## Sub-categories

- [A. Problem and Persona](../sub-categories/persona-a.md)
- [B. Current Journey and Friction](../sub-categories/persona-b.md)
- [C. Outcome and Success](../sub-categories/persona-c.md)
- [D. Scope, Inclusion, and Trust](../sub-categories/persona-d.md)

## Data and trust here

- **Data:** evidence for problem/population/outcome
- **Trust:** does the excluded user trust this channel enough to use it

## How the companion uses it

Grid cells for this dimension are keyed `persona:<Stage>` in `designs.grid_state`.
Which sub-categories the companion probes at a given stage is set by each
sub-category's stage weight. The dimension name is public vocabulary; the
sub-category letters are internal-only.
