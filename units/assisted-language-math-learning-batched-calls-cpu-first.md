---
name: Batch API calls to survive intermittent connectivity — and run on CPUs
type: unit
schema_version: 1
summary: Group 10–20 questions into one API call per set, run nearly all compute on CPUs, and deliver
  as a PWA — so sessions survive intermittent school-lab connectivity at under ₹10 per child per year.
code_refs:
- content/wiki/pathways/assisted-language-math-learning.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/assisted-language-math-learning.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: assisted-language-math-learning
unit_type: Tactical Decision
dimension: solution
sub_category: solution-c
stage: define
also_relevant_at:
- scale
source_unit_id: Unit 7
applies_when: Deployment environment has intermittent rather than continuous internet; devices are heterogeneous
  and often ageing; cost-per-interaction must remain viable at millions of learners.
fails_when: Not documented in the source
decision: Group 10–20 questions into a question set and make a single API call only when the set is complete,
  rather than after every question; run nearly all compute on CPUs, with GPU calls limited to a small
  subset of operations; deliver via PWA/web to handle heterogeneous school hardware without installation
  complexity.
alternative_considered: Cloud-first, always-connected architecture with per-question API calls and GPU-based
  inference.
reason: Public-school computer labs frequently have intermittent, not absent, connectivity — a connection
  exists at session start and at points through a session but cannot be assumed continuous. CPU-first
  keeps scaling costs low and avoids GPU availability constraints at state scale; PWA distribution removes
  installation and upgrade complexity on ageing hardware.
context: A student can complete an entire session if connectivity exists at session start and when moving
  between question sets — typically once or twice per session.
before: Per-question API calls would fail or stall every time connectivity dropped, interrupting sessions
  and raising server costs.
after: Sessions complete through realistic intermittent connectivity patterns; running cost remains under
  ₹10 per child per year at scale (AML, as of September 2026).
adopter_intents:
- How do we handle the fact that our schools have terrible internet?
- How do we keep costs low at a million learners?
---

## Unit

According to EkStep Foundation's AxL pathway, this is a tactical decision from the deployment.

**Decision.** Group 10–20 questions into a question set and make a single API call only when the set is complete, rather than after every question; run nearly all compute on CPUs, with GPU calls limited to a small subset of operations; deliver via PWA/web to handle heterogeneous school hardware without installation complexity.

**Alternative considered.** Cloud-first, always-connected architecture with per-question API calls and GPU-based inference.

**Why.** Public-school computer labs frequently have intermittent, not absent, connectivity — a connection exists at session start and at points through a session but cannot be assumed continuous. CPU-first keeps scaling costs low and avoids GPU availability constraints at state scale; PWA distribution removes installation and upgrade complexity on ageing hardware.

**Context.** A student can complete an entire session if connectivity exists at session start and when moving between question sets — typically once or twice per session.

## Condition

- **Applies when:** Deployment environment has intermittent rather than continuous internet; devices are heterogeneous and often ageing; cost-per-interaction must remain viable at millions of learners.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Per-question API calls would fail or stall every time connectivity dropped, interrupting sessions and raising server costs.
- **After:** Sessions complete through realistic intermittent connectivity patterns; running cost remains under ₹10 per child per year at scale (AML, as of September 2026).

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
