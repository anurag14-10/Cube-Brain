---
name: Sahayika — an escalation route staffed on goodwill collapses; the duty must be assigned by whoever sets staff duties
type: unit
schema_version: 2
summary: Escalated questions went to nurse-midwives as unassigned extra work; the median wait rose from 4 hours
  to over 3 days, health workers stopped asking hard questions, and the steering group decided the route must
  be formally assigned by nurse supervisors.
tags:
- synthetic-test
sources:
- system: conversation
  method: stated
  date: '2026-10-16'
  ref: Sahayika project documents shared by vinod303 in a Claude session — 01-grant-proposal.md, 02-design-note.md,
    03-pilot-dashboard-notes.md, 04-nurse-interview-notes.md, 05-steering-group-minutes.md, 99-sahayika-evaluation.md.
    Not in the diffusion-cube repo; every file is marked "Synthetic test document"
- system: conversation
  method: derived
  date: '2026-10-16'
  ref: dimension, sub_category, stage and unit_type assigned by best reading against concepts/institution.md
    — the source is project documents, not a framework-structured pathway document
first_logged: '2026-10-16'
last_updated: '2026-10-16'
pathway: sahayika
unit_type: Failure and Fix
dimension: institution
sub_category: institution-b
stage: pilot
applies_when: Questions the AI cannot answer are escalated to government staff whose duties are set by their
  own supervisor, not by the project (the district health officer, steering group minutes)
fails_when: Not documented in the source
failure: Questions below the retrieval-confidence threshold went to five nurse-midwives in the block. Every
  interviewed nurse said answering was extra work outside their duties that nobody counted or assigned; messages
  arrived in clinic hours and were answered, if at all, at night. The median wait rose from 4 hours (pilot month
  1) to 72 hours (month 2) and 80 hours (month 3). Escalations fell from 212 to 61 a month — not because fewer
  questions needed a human, but because health workers stopped sending the kinds of question they expected the
  bot could not answer ("no point asking, nobody replies"). The most-escalated topics were drug interactions,
  scheme-eligibility edge cases and newborn danger signs.
fix: 'Decided, not yet applied: the steering group (project month 14) chose to rebuild the escalation route
  before any wider rollout, with nurse supervisors formally assigning escalation duty. The nurses'' own suggestions
  were a supervisor-assigned rota and a fixed daily time slot.'
insight: A human fallback that depends on goodwill is not a fallback. Only the person who sets the staff's duties
  — here the block supervisor — can make it part of the job. Falling escalation volume can mean users have given
  up on the hardest questions, not that fewer questions need a human.
related_units:
- sahayika-briefed-not-consulted-nurse-midwives
- sahayika-hold-expansion-until-escalation-holds
- data-dhara-name-nodal-officer-before-work
- nivesh-suvidha-gap-flagging-loop
---

## Unit

According to the research partner's Sahayika evaluation, this is a failure and fix from the pilot.

**Failure.** Escalated questions went to five nurse-midwives in the block. Every interviewed nurse described answering as extra work outside their duties that nobody counted or assigned, done at night after clinic. The median wait rose from 4 hours in pilot month 1 to 72 hours in month 2 and 80 hours in month 3. Escalations fell from 212 to 61 a month because health workers stopped sending the questions they expected the bot could not answer — drug interactions, scheme-eligibility edge cases, newborn danger signs.

**Fix (decided, not yet applied).** At month 14 the steering group decided to rebuild the escalation route before any wider rollout, with nurse supervisors formally assigning the duty. The district health officer said nurse duties are set by the block supervisor and nothing changes without that. The nurses proposed a supervisor-assigned rota and a fixed daily slot.

**Insight.** A human fallback that depends on goodwill is not a fallback; only the person who sets staff duties can make it part of the job. A falling escalation count can mean users gave up, not that fewer questions need a human.

## Condition

- **Applies when:** questions the AI cannot answer are escalated to government staff whose duties are set by their own supervisor, not by the project.
- **Fails when:** Not documented in the source.

## Before → after

- **Before:** escalation answered within about 4 hours in the first weeks, on the nurses' goodwill.
- **After:** a median wait of over 3 days by month 2, and health workers no longer asking the questions that most needed a human. The effect of the supervisor-assigned route is not yet documented.

## Why it is reusable

Any deployment with a human fallback can check, before launch, who formally owns answering it. It is a suggestion from another adoption's lived experience, not a recommendation — and this record comes from a synthetic test document.
