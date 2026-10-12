---
name: MahaVISTAAR — define the excluded user precisely, not as a demographic
type: unit
schema_version: 2
summary: Target a precisely described excluded user (women farmers in Marathwada) rather than 'farmers'
  — the precise user fixes channel, model, data, language and testing.
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
sub_category: persona-a
stage: explore
source_unit_id: Unit 1
applies_when: Exclusion is driven by language, literacy, device access, or institutional reach.
fails_when: Not documented in the source
decision: Target women farmers in Marathwada specifically — small trust circles, don't visit agriculture
  offices, receive contradictory advice from fertiliser sellers — rather than 'farmers' or 'rural citizens'.
alternative_considered: Broader demographic targeting ('farmers', 'rural citizens', 'agricultural users').
reason: A precise user determines channel, model, data, language, and testing process; a vague demographic
  gives no fixed point to design against.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- Who exactly are we building this for?
related_units:
- mahavistaar-registered-farmer-not-decision-maker
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Target women farmers in Marathwada specifically — small trust circles, don't visit agriculture offices, receive contradictory advice from fertiliser sellers — rather than 'farmers' or 'rural citizens'.

**Alternative considered:** Broader demographic targeting ('farmers', 'rural citizens', 'agricultural users').

**Why:** A precise user determines channel, model, data, language, and testing process; a vague demographic gives no fixed point to design against.

## Condition

- **Applies when:** Exclusion is driven by language, literacy, device access, or institutional reach.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The excluded-user definition is the fixed point every later design choice is measured against; an adopter can apply the same test — can you name the person, their barrier and their current workaround? — before choosing a channel or model.
