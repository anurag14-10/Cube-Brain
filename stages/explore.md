---
name: Explore
type: stage
schema_version: 1
summary: Is AI appropriate, and what would it take?
order: 1
central_question: Is AI appropriate, and what would it take?
done_when:
- Precise excluded-user definition.
- Honest comparison with alternatives.
- Order-of-magnitude cost sense.
next_stage: define
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

## Central question

Is AI appropriate, and what would it take?

## Done when

- Precise excluded-user definition.
- Honest comparison with alternatives.
- Order-of-magnitude cost sense.

## What changes for each dimension

See the four cells: [Persona](../cells/persona-explore.md), [Solution](../cells/solution-explore.md), [Institution](../cells/institution-explore.md), [Ecosystem](../cells/ecosystem-explore.md).

A deployment's stage is only ever taken from the user's own statement —
never assigned by the model (`designs.meta.stage`).
