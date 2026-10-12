---
name: MahaVISTAAR — narrow scope to a single answerable question
type: unit
schema_version: 2
summary: Scope the system to one concrete question type needing synthesis across live sources (e.g. 'should
  I harvest my paddy now?'), not a whole domain.
doc_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: content/wiki/pathways/mahavistaar.md — sub_category inferred; the document tags each unit with dimension, stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Strategic Decision
dimension: persona
sub_category: persona-d
stage: define
source_unit_id: Unit 5
applies_when: The answer genuinely requires synthesis across multiple live sources within one response.
fails_when: Not documented in the source
decision: Scope the system to answer a single, concrete question type in one response — e.g. 'should I
  harvest my paddy now?', requiring weather, market price, and crop-stage advisory assembled together
  — rather than 'agricultural advisory' broadly.
reason: A precise use case defines exactly which data sources, languages, and safety boundaries the build
  actually needs; a broad domain doesn't.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- What's the minimum viable scope for a first pilot?
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Scope the system to answer a single, concrete question type in one response — e.g. 'should I harvest my paddy now?', requiring weather, market price, and crop-stage advisory assembled together — rather than 'agricultural advisory' broadly.

**Why:** A precise use case defines exactly which data sources, languages, and safety boundaries the build actually needs; a broad domain doesn't.

## Condition

- **Applies when:** The answer genuinely requires synthesis across multiple live sources within one response.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

A single answerable question becomes the specification for data sources, languages and safety boundaries; an adopter can use it to cut a first pilot down to what must be true.
