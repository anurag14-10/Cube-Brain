---
name: Pilot
type: concept
schema_version: 2
aliases:
- Pilot
- Pilot stage
summary: What breaks with real users and real institutional conditions?
concept_kind: stage
definition: Pilot — What breaks with real users and real institutional conditions?
audience: public-vocabulary
broader: grid
central_question: What breaks with real users and real institutional conditions?
done_when:
- Failure taxonomy.
- Named institutional response to first public failure.
- Real cost-per-interaction data.
order: 3
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

What breaks with real users and real institutional conditions?

Stage 3 of 4, after [Define](define.md) and before [Scale](scale.md).

## Done when

- Failure taxonomy.
- Named institutional response to first public failure.
- Real cost-per-interaction data.

## What changes for each dimension

- **[Persona](persona.md)** (`persona:Pilot`) — Which user interactions are failing — is that a scope problem or a quality problem?
- **[Solution](solution.md)** (`solution:Pilot`) — Which component is causing the most pain, is it replaceable, and which data source is going stale or wrong?
- **[Institution](institution.md)** (`institution:Pilot`) — What has the institution seen fail publicly — and did they own it or disown it?
- **[Ecosystem](ecosystem.md)** (`ecosystem:Pilot`) — Which partner is underperforming — and do you have an alternative?

## How it is used

Units carry `stage: pilot` as their stage of ORIGIN (what counts in a
grid); `also_relevant_at` is retrieval only. A deployment's stage is only
ever taken from the user's own statement — never assigned by the model.
