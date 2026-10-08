---
name: Solution
type: dimension
schema_version: 1
aliases:
- solution
summary: Are we building the right system to solve it?
code: solution
central_question: Are we building the right system to solve it?
shift: From choosing a model to designing a reliable and adaptable system
thesis_group: build-the-right-thing
ui_color: '#0099ff'
data_concern: is data usable/reliable/current
trust_concern: is trust conveyed through channel/UX choices — tone, disclosure, voice vs. text
order: 2
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

Are we building the right system to solve it?

*From choosing a model to designing a reliable and adaptable system*



## Sub-categories

- [A. AI Fit and Comparative Advantage](../sub-categories/solution-a.md)
- [B. UX, Channel, and Integration](../sub-categories/solution-b.md)
- [C. Model, Architecture, and Infrastructure](../sub-categories/solution-c.md)
- [D. Data and Knowledge Readiness](../sub-categories/solution-d.md)
- [E. Performance, Reliability, and Scale](../sub-categories/solution-e.md)

## Data and trust here

- **Data:** is data usable/reliable/current
- **Trust:** is trust conveyed through channel/UX choices — tone, disclosure, voice vs. text

## How the companion uses it

Grid cells for this dimension are keyed `solution:<Stage>` in `designs.grid_state`.
Which sub-categories the companion probes at a given stage is set by each
sub-category's stage weight. The dimension name is public vocabulary; the
sub-category letters are internal-only.
