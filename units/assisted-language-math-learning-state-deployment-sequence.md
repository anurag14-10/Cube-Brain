---
name: The state deployment sequence is fixed and largely non-compressible
type: unit
schema_version: 1
summary: A six-step gated sequence for each new state — leadership buy-in, infrastructure assessment,
  naming and MOU, train-the-trainer, student selection, sessions with troubleshooting — where compressing
  or reordering produces predictable failures.
code_refs:
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
unit_type: Playbook
dimension: institution
sub_category: institution-a
stage: define
also_relevant_at:
- pilot
source_unit_id: Unit 9
applies_when: Deploying in a new Indian state government context with an existing school system and computer
  lab infrastructure. Steps 1–3 may look different in non-government or international contexts.
fails_when: Not documented in the source
before: Based on Delhi observation, rigid weekly-period mandates were issued, which schools found difficult
  to execute consistently.
after: Flexible cumulative-hours targets (8 hours by Diwali, 8 more by session end) replaced the fixed
  mandate, and usage improved.
steps:
- '1. Secure named leadership buy-in — education minister, education secretary, or SCERT director, whichever
  role sits over school leadership in that state. Gate: prerequisite for everything; the programme is
  driven by state leadership, not the implementing organisation.'
- '2. Conduct infrastructure assessment — the school''s UDISE score plus surveys of computer lab availability,
  computer count and internet connectivity. Gate: determines which schools can be included.'
- 3. In parallel with step 2 — state leadership decides the programme's own name and where it sits in
  the state's broader configuration; an MOU is signed.
- '4. Train the trainers — state trainers are trained in batches of thousands, then train teachers on
  the ground; refreshed annually with in-between refreshers. Gate: nothing teacher-facing begins before
  this step.'
- 5. Teachers select participating students — via existing state-defined groupings, teacher judgement,
  or a diagnostic baseline — and a timetable period is allocated.
- 6. Sessions begin. The first one to two weeks involve substantial troubleshooting, mostly connectivity
  and ageing hardware rather than the product, with EkStep WhatsApp and phone support; usage stabilises
  after this period.
common_failure_mode: 'Compressing or reordering the sequence: without leadership buy-in, timetable allocation
  does not happen; without infrastructure assessment, the wrong schools are included; without train-the-trainer,
  teachers cannot run sessions; without student selection, struggling students are not reached.'
adopter_intents:
- What broke first when we went live in schools?
- How do I make sure teachers don't reject this?
- What is the sequence of steps to deploy in a new state?
- How do I convince a sceptical state secretary to commit?
- What does the teacher actually do, and what are they explicitly not asked to do?
related_units:
- assisted-language-math-learning-teacher-workflow-as-constraint
- assisted-language-math-learning-full-state-ownership-narrow-role
---

## Unit

According to EkStep Foundation's AxL pathway, this is a playbook from the deployment.

**Steps (in order):**

- 1. Secure named leadership buy-in — education minister, education secretary, or SCERT director, whichever role sits over school leadership in that state. Gate: prerequisite for everything; the programme is driven by state leadership, not the implementing organisation.
- 2. Conduct infrastructure assessment — the school's UDISE score plus surveys of computer lab availability, computer count and internet connectivity. Gate: determines which schools can be included.
- 3. In parallel with step 2 — state leadership decides the programme's own name and where it sits in the state's broader configuration; an MOU is signed.
- 4. Train the trainers — state trainers are trained in batches of thousands, then train teachers on the ground; refreshed annually with in-between refreshers. Gate: nothing teacher-facing begins before this step.
- 5. Teachers select participating students — via existing state-defined groupings, teacher judgement, or a diagnostic baseline — and a timetable period is allocated.
- 6. Sessions begin. The first one to two weeks involve substantial troubleshooting, mostly connectivity and ageing hardware rather than the product, with EkStep WhatsApp and phone support; usage stabilises after this period.

**Common failure mode.** Compressing or reordering the sequence: without leadership buy-in, timetable allocation does not happen; without infrastructure assessment, the wrong schools are included; without train-the-trainer, teachers cannot run sessions; without student selection, struggling students are not reached.

## Condition

- **Applies when:** Deploying in a new Indian state government context with an existing school system and computer lab infrastructure. Steps 1–3 may look different in non-government or international contexts.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Based on Delhi observation, rigid weekly-period mandates were issued, which schools found difficult to execute consistently.
- **After:** Flexible cumulative-hours targets (8 hours by Diwali, 8 more by session end) replaced the fixed mandate, and usage improved.

## Why it is reusable

The order of the steps is the reusable part. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
