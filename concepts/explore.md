---
name: Explore
type: concept
schema_version: 2
aliases:
- Explore
- Explore stage
summary: Is AI appropriate, and what would it take?
concept_kind: stage
definition: Explore — Is AI appropriate, and what would it take?
audience: public-vocabulary
broader: grid
central_question: Is AI appropriate, and what would it take?
done_when:
- Precise excluded-user definition.
- Honest comparison with alternatives.
- Order-of-magnitude cost sense.
order: 1
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

Is AI appropriate, and what would it take?

Stage 1 of 4, before [Define](define.md).

## Done when

- Precise excluded-user definition.
- Honest comparison with alternatives.
- Order-of-magnitude cost sense.

## What changes for each dimension

- **[Persona](persona.md)** (`persona:Explore`) — Who specifically is excluded from this service today — and what do they do instead?
- **[Solution](solution.md)** (`solution:Explore`) — What channel or system are you replacing, what does it fail at, and is AI actually the right tool for that failure?
- **[Institution](institution.md)** (`institution:Explore`) — Who inside the institution has to personally want this to work — and do they know yet?
- **[Ecosystem](ecosystem.md)** (`ecosystem:Explore`) — Who else has tried to solve this for this population, and what happened?

## How it is used

Units carry `stage: explore` as their stage of ORIGIN (what counts in a
grid); `also_relevant_at` is retrieval only. A deployment's stage is only
ever taken from the user's own statement — never assigned by the model.
