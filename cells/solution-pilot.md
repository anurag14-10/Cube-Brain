---
name: Solution × Pilot
type: cell
schema_version: 1
aliases:
- solution:Pilot
summary: Which component is causing the most pain, is it replaceable, and which data source is going stale
  or wrong?
dimension: solution
stage: pilot
grid_key: solution:Pilot
core_question: Which component is causing the most pain, is it replaceable, and which data source is going
  stale or wrong?
listening_for: Bundled-vs-unbundled plays out here. Data quality failures at Pilot look like AI failures
  to users.
insight_form: Component failure + replaceability + data quality issue + owner response time
corpus_example: 'MahaVISTAAR: mandi price 48hr lag caused wrong harvest-timing advice. Fix: governance
  call with APMC to 6-hr cadence — not a technical fix.'
example_pathway: mahavistaar
primary_sub_categories:
- solution-b
- solution-c
- solution-d
- solution-e
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

Which component is causing the most pain, is it replaceable, and which data source is going stale or wrong?

## Listening for

Bundled-vs-unbundled plays out here. Data quality failures at Pilot look like AI failures to users.

## Insight form

Component failure + replaceability + data quality issue + owner response time

## Corpus example

MahaVISTAAR: mandi price 48hr lag caused wrong harvest-timing advice. Fix: governance call with APMC to 6-hr cadence — not a technical fix.
