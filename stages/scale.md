---
name: Scale
type: stage
schema_version: 1
summary: Can the institution own, sustain, and continuously improve it?
order: 4
central_question: Can the institution own, sustain, and continuously improve it?
done_when:
- Budget line.
- Named operational owner.
- Monitoring mechanism.
- Operating model written down.
previous_stage: pilot
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

Can the institution own, sustain, and continuously improve it?

## Done when

- Budget line.
- Named operational owner.
- Monitoring mechanism.
- Operating model written down.

## What changes for each dimension

See the four cells: [Persona](../cells/persona-scale.md), [Solution](../cells/solution-scale.md), [Institution](../cells/institution-scale.md), [Ecosystem](../cells/ecosystem-scale.md).

A deployment's stage is only ever taken from the user's own statement —
never assigned by the model (`designs.meta.stage`).
