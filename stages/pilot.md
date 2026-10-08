---
name: Pilot
type: stage
schema_version: 1
summary: What breaks with real users and real institutional conditions?
order: 3
central_question: What breaks with real users and real institutional conditions?
done_when:
- Failure taxonomy.
- Named institutional response to first public failure.
- Real cost-per-interaction data.
previous_stage: define
next_stage: scale
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

What breaks with real users and real institutional conditions?

## Done when

- Failure taxonomy.
- Named institutional response to first public failure.
- Real cost-per-interaction data.

## What changes for each dimension

See the four cells: [Persona](../cells/persona-pilot.md), [Solution](../cells/solution-pilot.md), [Institution](../cells/institution-pilot.md), [Ecosystem](../cells/ecosystem-pilot.md).

A deployment's stage is only ever taken from the user's own statement —
never assigned by the model (`designs.meta.stage`).
