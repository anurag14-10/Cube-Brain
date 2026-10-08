---
name: Persona × Pilot
type: cell
schema_version: 1
aliases:
- persona:Pilot
summary: Which user interactions are failing — is that a scope problem or a quality problem?
dimension: persona
stage: pilot
grid_key: persona:Pilot
core_question: Which user interactions are failing — is that a scope problem or a quality problem?
listening_for: Scope = outside mandate. Quality = mandate questions answered badly. Different fixes.
insight_form: 'Failure taxonomy: scope vs quality vs experience'
corpus_example: 'AI-Assisted Job Matching: pilot support issues are logged into eight categories from
  day one — software, data, vacancy input, recommendation quality, workflow, access, training, unknown
  — so a bad recommendation''s real cause is never guessed at after the fact.'
example_pathway: ai-assisted-job-matching
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

Which user interactions are failing — is that a scope problem or a quality problem?

## Listening for

Scope = outside mandate. Quality = mandate questions answered badly. Different fixes.

## Insight form

Failure taxonomy: scope vs quality vs experience

## Corpus example

AI-Assisted Job Matching: pilot support issues are logged into eight categories from day one — software, data, vacancy input, recommendation quality, workflow, access, training, unknown — so a bad recommendation's real cause is never guessed at after the fact.
