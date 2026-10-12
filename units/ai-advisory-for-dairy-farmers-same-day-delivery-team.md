---
name: No-holiday internal team with a same-day delivery mandate
type: unit
schema_version: 2
summary: For a fixed external deadline, form a dedicated internal team with a no-holiday, same-day-completion
  mandate matched to the technical partner's pace; the first version shipped in three weeks and the daily
  iteration pace carried into Scale.
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
dimension: institution
sub_category: institution-b
stage: define
source_unit_id: Unit 7
applies_when: An external deadline is fixed and non-negotiable; the institution's leadership has visibly
  committed; the technical partner matches the same delivery pace.
fails_when: Not documented in the source
decision: Form a dedicated internal team with an explicit no-holiday, same-day-completion mandate for
  the build period, matched to the EkStep team's own response speed.
alternative_considered: Normal project management with sprint cycles and approval gates.
reason: 'The one-month timeline was set externally (the Global AI Summit in February). Meeting it required
  eliminating the internal delays — waiting for approvals, scheduling reviews, batching tasks — that would
  have consumed the month. The Amul official''s framing was: "whatever guidance and instructions they
  give, we''ll do it the same day."'
context: 'The team delivered the first version in three weeks (the Prime Minister described it as a miracle).
  The same-day delivery culture has continued beyond the build: the EkStep technical team delivers suggested
  changes same-day, and the Amul team''s morning routine starts with a 10-minute review of previous-day
  usage data.'
before: Standard project cadence.
after: Three-week delivery to a live, demo-ready system; daily iteration pace sustained into Scale.
adopter_intents:
- How did Amul build this in one month?
related_units:
- ai-advisory-for-dairy-farmers-md-personal-ownership
---

## Unit

According to GCMMF (Amul) and EkStep Foundation's Amul AI / Sarla Ben pathway, this is a tactical decision from the deployment.

**Decision.** Form a dedicated internal team with an explicit no-holiday, same-day-completion mandate for the build period, matched to the EkStep team's own response speed.

**Alternative considered.** Normal project management with sprint cycles and approval gates.

**Why.** The one-month timeline was set externally (the Global AI Summit in February). Meeting it required eliminating the internal delays — waiting for approvals, scheduling reviews, batching tasks — that would have consumed the month. The Amul official's framing was: "whatever guidance and instructions they give, we'll do it the same day."

**In this deployment.** The team delivered the first version in three weeks (the Prime Minister described it as a miracle). The same-day delivery culture has continued beyond the build: the EkStep technical team delivers suggested changes same-day, and the Amul team's morning routine starts with a 10-minute review of previous-day usage data.

## Condition

- **Applies when:** An external deadline is fixed and non-negotiable; the institution's leadership has visibly committed; the technical partner matches the same delivery pace.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Standard project cadence.
- **After:** Three-week delivery to a live, demo-ready system; daily iteration pace sustained into Scale.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
