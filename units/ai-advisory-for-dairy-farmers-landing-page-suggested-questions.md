---
name: Landing-page entry point with rotating suggested questions doubled usage
type: unit
schema_version: 2
summary: Put Sarla Ben on the app's landing screen with 150 suggested questions shown five at a time,
  so a farmer taps instead of composing a question; usage doubled, and top questions from daily analysis
  keep being promoted.
doc_refs:
- content/wiki/pathways/ai-advisory-for-dairy-farmers.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-advisory-for-dairy-farmers.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ai-advisory-for-dairy-farmers
unit_type: Tactical Decision
dimension: solution
sub_category: solution-b
stage: pilot
source_unit_id: Unit 3
applies_when: The app already has a meaningful user base (Amul had 10 lakh downloads before this change);
  the barrier is starting, not sustaining; users have enough familiarity with touchscreens to tap a suggested
  question.
fails_when: Not documented in the source
decision: Place a Sarla Ben entry point on the app's landing screen (not buried in a menu), with 150 suggested
  questions shown five at a time in random rotation, so a farmer only has to tap rather than compose a
  question from scratch.
alternative_considered: Keeping Sarla Ben as a separate section users navigate to, requiring them to know
  what to ask.
reason: Farmers were not failing to use the system because they lacked interest — they were failing to
  start because typing a question is hard and knowing what questions are answerable is not obvious. Reducing
  the cognitive and mechanical cost of a first interaction removes the barrier without changing the underlying
  capability.
context: 'The 150 questions in the backend are rotated in sets of five; the most-asked questions from
  the daily pivot-table analysis are promoted to the landing page. This is now a continuous loop: analyse
  top questions → fix most popular on the landing page → observe new top questions.'
before: Farmers had to navigate to a separate Sarla Ben section and compose a question.
after: Usage doubled; engagement begins from the moment the app opens.
adopter_intents:
- How do we get farmers to start using the system?
related_units:
- ai-advisory-for-dairy-farmers-chat-for-advice-voice-for-transactions
---

## Unit

According to GCMMF (Amul) and EkStep Foundation's Amul AI / Sarla Ben pathway, this is a tactical decision from the deployment.

**Decision.** Place a Sarla Ben entry point on the app's landing screen (not buried in a menu), with 150 suggested questions shown five at a time in random rotation, so a farmer only has to tap rather than compose a question from scratch.

**Alternative considered.** Keeping Sarla Ben as a separate section users navigate to, requiring them to know what to ask.

**Why.** Farmers were not failing to use the system because they lacked interest — they were failing to start because typing a question is hard and knowing what questions are answerable is not obvious. Reducing the cognitive and mechanical cost of a first interaction removes the barrier without changing the underlying capability.

**In this deployment.** The 150 questions in the backend are rotated in sets of five; the most-asked questions from the daily pivot-table analysis are promoted to the landing page. This is now a continuous loop: analyse top questions → fix most popular on the landing page → observe new top questions.

## Condition

- **Applies when:** The app already has a meaningful user base (Amul had 10 lakh downloads before this change); the barrier is starting, not sustaining; users have enough familiarity with touchscreens to tap a suggested question.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Farmers had to navigate to a separate Sarla Ben section and compose a question.
- **After:** Usage doubled; engagement begins from the moment the app opens.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
