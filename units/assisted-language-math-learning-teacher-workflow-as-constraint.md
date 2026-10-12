---
name: Design teacher workflow as a constraint, not a feature
type: unit
schema_version: 2
summary: 'Treat any added teacher effort as a design failure: the teacher''s role is reduced to identifying
  eligible students, finding a timetable period and getting students to the lab — no teaching, no change
  to classroom practice.'
doc_refs:
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
unit_type: Strategic Decision
dimension: persona
sub_category: persona-b
stage: define
also_relevant_at:
- pilot
- scale
source_unit_id: Unit 3
applies_when: Teachers are already managing large, multi-grade, multi-level classrooms with competing
  administrative responsibilities; the intervention is targeted at students whose learning gap is too
  large for in-class support to bridge.
fails_when: Not documented in the source
decision: 'Treat any requirement for additional teacher effort as a design failure to be removed, not
  a cost to be minimised — design the teacher''s role to be structurally minimal: identify eligible students
  (with the headmaster), find a timetable period, and get students to the lab.'
alternative_considered: An intervention that depends on teachers actively facilitating or scaffolding
  sessions in the lab, or changing how they teach in their regular classroom.
reason: Teachers' responsibilities extend well beyond math or reading (midday meals, supplementation tracking,
  well-being), so any new cognitive or time demand is likely to fail in adoption regardless of technical
  quality. And a student who cannot manage one-digit addition cannot be taught three-digit multiplication
  by explanation — teacher presence does not substitute for personalised, step-level practice.
context: The AML design requires only that any adult in the school system be present in the lab — not
  the teacher specifically.
before: Not documented in the source
after: No teaching is required in the lab; removing 10–20 struggling students leaves a more homogeneous
  remaining class that is easier for the teacher to manage and reduces a psychological burden they already
  carry.
adopter_intents:
- How do I make sure teachers don't reject this?
- What does the teacher actually do, and what are they explicitly not asked to do?
related_units:
- assisted-language-math-learning-state-deployment-sequence
---

## Unit

According to EkStep Foundation's AxL pathway, this is a strategic decision from the deployment.

**Decision.** Treat any requirement for additional teacher effort as a design failure to be removed, not a cost to be minimised — design the teacher's role to be structurally minimal: identify eligible students (with the headmaster), find a timetable period, and get students to the lab.

**Alternative considered.** An intervention that depends on teachers actively facilitating or scaffolding sessions in the lab, or changing how they teach in their regular classroom.

**Why.** Teachers' responsibilities extend well beyond math or reading (midday meals, supplementation tracking, well-being), so any new cognitive or time demand is likely to fail in adoption regardless of technical quality. And a student who cannot manage one-digit addition cannot be taught three-digit multiplication by explanation — teacher presence does not substitute for personalised, step-level practice.

**Context.** The AML design requires only that any adult in the school system be present in the lab — not the teacher specifically.

## Condition

- **Applies when:** Teachers are already managing large, multi-grade, multi-level classrooms with competing administrative responsibilities; the intervention is targeted at students whose learning gap is too large for in-class support to bridge.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** No teaching is required in the lab; removing 10–20 struggling students leaves a more homogeneous remaining class that is easier for the teacher to manage and reduces a psychological burden they already carry.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
