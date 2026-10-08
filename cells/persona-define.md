---
name: Persona × Define
type: cell
schema_version: 1
aliases:
- persona:Define
summary: What is the one question a user will ask that this system must answer, or the pilot fails?
dimension: persona
stage: define
grid_key: persona:Define
core_question: What is the one question a user will ask that this system must answer, or the pilot fails?
listening_for: Forces scope to its minimum. Shapes data model, prompt design, safety boundaries.
insight_form: Single critical use case + binary success definition
corpus_example: 'Voice AI Adoption Barriers: Pradical Works fixed connect rate, talk-time distribution,
  and lead conversion as success metrics before a single call went out — the resulting pilot data was
  measurably cleaner than every other pilot in the same cohort.'
example_pathway: voice-ai-adoption-barriers
primary_sub_categories:
- persona-c
- persona-d
code_refs:
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

## Core question

What is the one question a user will ask that this system must answer, or the pilot fails?

## Listening for

Forces scope to its minimum. Shapes data model, prompt design, safety boundaries.

## Insight form

Single critical use case + binary success definition

## Corpus example

Voice AI Adoption Barriers: Pradical Works fixed connect rate, talk-time distribution, and lead conversion as success metrics before a single call went out — the resulting pilot data was measurably cleaner than every other pilot in the same cohort.
