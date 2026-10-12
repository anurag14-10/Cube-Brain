---
name: MahaVISTAAR — the registered farmer isn't always the decision-maker
type: unit
schema_version: 2
summary: Design around who actually makes crop decisions, not who is listed in land records — registry
  data can point at the wrong user.
tags:
- relevant-to-government
doc_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Strategic Decision
dimension: persona
sub_category: persona-a
stage: explore
source_unit_id: Unit 2
applies_when: Government registry data is being used as a proxy for 'the user'.
fails_when: Not documented in the source
decision: Design around who actually makes crop decisions, not who is listed in land records.
reason: Many women farm the land while it stays registered in a husband's name — designing to the registry
  would target the wrong person.
context: Land-title records in Maharashtra frequently name the husband while the wife makes the sowing,
  spraying, and selling decisions.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- Who exactly are we building this for?
related_units:
- mahavistaar-precise-excluded-user
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Design around who actually makes crop decisions, not who is listed in land records.

**Why:** Many women farm the land while it stays registered in a husband's name — designing to the registry would target the wrong person.

**In this deployment:** Land-title records in Maharashtra frequently name the husband while the wife makes the sowing, spraying, and selling decisions.

## Condition

- **Applies when:** Government registry data is being used as a proxy for 'the user'.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

Any deployment that sources its user list from an administrative registry inherits the registry's blind spots; this unit is a check to run before the registry becomes the target population.
