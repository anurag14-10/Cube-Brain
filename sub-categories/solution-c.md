---
name: Model, Architecture, and Infrastructure
type: sub_category
schema_version: 1
aliases:
- Solution C
- solution:C
summary: 'Solution sub-category C: Model, Architecture, and Infrastructure.'
dimension: solution
code: C
weight_explore: secondary
weight_define: primary
weight_pilot: primary
weight_scale: primary
questions:
- What level of model capability is adequate for the problem?
- 'What constraints determine the model choice: quality, language support, latency, cost, privacy, or
  sovereignty?'
- What are the choices of compute, hosting, and deployment environment?
- Which architecture decisions would be difficult or expensive to reverse?
- Which components must remain modular and replaceable?
- What is the vendor posture, and how will lock-in be avoided or managed?
- What must remain within the institution, and what may travel to an external model or service?
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

## What it covers

Solution › **C. Model, Architecture, and Infrastructure** — part of "Are we building the right system to solve it?"

## Questions

- What level of model capability is adequate for the problem?
- What constraints determine the model choice: quality, language support, latency, cost, privacy, or sovereignty?
- What are the choices of compute, hosting, and deployment environment?
- Which architecture decisions would be difficult or expensive to reverse?
- Which components must remain modular and replaceable?
- What is the vendor posture, and how will lock-in be avoided or managed?
- What must remain within the institution, and what may travel to an external model or service?

## Stage weighting

| Stage | Weight |
|---|---|
| Explore | secondary |
| Define | primary |
| Pilot | primary |
| Scale | primary |

Primary at: Define, Pilot, Scale. Primary = ask directly;
secondary = only if surfaced; dormant = never initiate.
