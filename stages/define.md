---
name: Define
type: stage
schema_version: 1
summary: What must be true before building?
order: 2
central_question: What must be true before building?
done_when:
- Named data owners.
- Named mandate holder.
- Architecture posture chosen.
- Safety boundaries designed.
previous_stage: explore
next_stage: pilot
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

What must be true before building?

## Done when

- Named data owners.
- Named mandate holder.
- Architecture posture chosen.
- Safety boundaries designed.

## What changes for each dimension

See the four cells: [Persona](../cells/persona-define.md), [Solution](../cells/solution-define.md), [Institution](../cells/institution-define.md), [Ecosystem](../cells/ecosystem-define.md).

A deployment's stage is only ever taken from the user's own statement —
never assigned by the model (`designs.meta.stage`).
