---
name: MahaVISTAAR — don't over-commit to voice as the only channel
type: unit
schema_version: 1
summary: 'Cross-deployment failure: voice was assumed to carry the whole journey, but some users need
  images, text in noisy settings, or human escalation.'
code_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Failure and Fix
dimension: solution
sub_category: solution-b
stage: explore
source_unit_id: Unit 8
applies_when: A channel decision is made primarily from a literacy/device profile without testing the
  full task.
fails_when: Not documented in the source
failure: Multiple deployments (a cross-deployment observation) assumed voice alone would carry the full
  user journey.
fix: Recognise that voice opens the door, but some users need to send images, some prefer text in noisy
  environments, and some need human escalation the bot can't provide.
insight: Channel choice should be tested against the full task, not only against the population's literacy
  profile.
adopter_intents:
- Should we build for voice only?
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet:

- **Failure:** Multiple deployments (a cross-deployment observation) assumed voice alone would carry the full user journey.
- **Fix:** Recognise that voice opens the door, but some users need to send images, some prefer text in noisy environments, and some need human escalation the bot can't provide.
- **Insight:** Channel choice should be tested against the full task, not only against the population's literacy profile.

## Condition

- **Applies when:** A channel decision is made primarily from a literacy/device profile without testing the full task.
- **Fails when:** Not documented in the source

## Why it is reusable

It reframes the channel decision as a test against the full task, which any voice-first deployment can run before committing to a single channel.
