---
name: Scale
type: concept
schema_version: 2
aliases:
- Scale
- Scale stage
summary: Can the institution own, sustain, and continuously improve it?
concept_kind: stage
definition: Scale — Can the institution own, sustain, and continuously improve it?
audience: public-vocabulary
broader: grid
central_question: Can the institution own, sustain, and continuously improve it?
done_when:
- Budget line.
- Named operational owner.
- Monitoring mechanism.
- Operating model written down.
order: 4
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

Can the institution own, sustain, and continuously improve it?

Stage 4 of 4, after [Pilot](pilot.md).

## Done when

- Budget line.
- Named operational owner.
- Monitoring mechanism.
- Operating model written down.

## What changes for each dimension

- **[Persona](persona.md)** (`persona:Scale`) — Are new user segments arriving that the pilot wasn't designed for?
- **[Solution](solution.md)** (`solution:Scale`) — Which components are you now unbundling, what triggered it — and which data sources are breaking under scale, do formal SLAs exist?
- **[Institution](institution.md)** (`institution:Scale`) — Has the institution absorbed this — budget line, named owner, review cadence — and does the system leave people more capable or more dependent?
- **[Ecosystem](ecosystem.md)** (`ecosystem:Scale`) — What from your deployment could the next adopter reuse — with what conditions?

## How it is used

Units carry `stage: scale` as their stage of ORIGIN (what counts in a
grid); `also_relevant_at` is retrieval only. A deployment's stage is only
ever taken from the user's own statement — never assigned by the model.
