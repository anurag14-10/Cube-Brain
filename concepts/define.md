---
name: Define
type: concept
schema_version: 2
aliases:
- Define
- Define stage
summary: What must be true before building?
concept_kind: stage
definition: Define — What must be true before building?
audience: public-vocabulary
broader: grid
central_question: What must be true before building?
done_when:
- Named data owners.
- Named mandate holder.
- Architecture posture chosen.
- Safety boundaries designed.
order: 2
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/dimensions.ts
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/framework.md
doc_refs:
- lib/dimensions.ts
- content/framework.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Definition

What must be true before building?

Stage 2 of 4, after [Explore](explore.md) and before [Pilot](pilot.md).

## Done when

- Named data owners.
- Named mandate holder.
- Architecture posture chosen.
- Safety boundaries designed.

## What changes for each dimension

- **[Persona](persona.md)** (`persona:Define`) — What is the one question a user will ask that this system must answer, or the pilot fails?
- **[Solution](solution.md)** (`solution:Define`) — Which architecture choices, if wrong, would take six months to undo — and is every data source named, with an accountable owner for each?
- **[Institution](institution.md)** (`institution:Define`) — Who approves what the system says, have they agreed to own that, and what testing/timeline has the institution committed to before real users?
- **[Ecosystem](ecosystem.md)** (`ecosystem:Define`) — Which parts can you not build yourselves — and do you have a named partner for each?

## How it is used

Units carry `stage: define` as their stage of ORIGIN (what counts in a
grid); `also_relevant_at` is retrieval only. A deployment's stage is only
ever taken from the user's own statement — never assigned by the model.
