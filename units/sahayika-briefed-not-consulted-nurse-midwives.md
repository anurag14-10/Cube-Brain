---
name: Sahayika — nurse-midwives were briefed on their escalation role, not asked to design it
type: unit
schema_version: 2
summary: Design input from nurse-midwives was considered but not scheduled; they learned their role at a one-hour
  briefing, and the constraints that broke the route — clinic hours, unassigned duty — only surfaced in interviews
  at month 8.
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
also_relevant_at:
- define
applies_when: A new duty for frontline staff is designed by the project team rather than with the staff who will
  carry it
fails_when: Not documented in the source
failure: Design input from nurse-midwives "was considered but not scheduled, due to time" (design note, month
  3). They received a one-hour briefing at the block meeting on how escalations reach them and how to reply.
  Several first heard of their role at that briefing and were not asked how it should work — "Nobody asked what
  time we have."
fix: 'Not yet applied: the nurses'' own suggestions, gathered in month-8 interviews, were a supervisor-assigned
  rota and a fixed time slot each day. The steering group''s rebuild has supervisors formally assign the duty.'
insight: The two constraints that broke the escalation route — messages arriving in clinic hours, and the duty
  not being part of the job — were known to the nurses and surfaced only once someone asked them, five months
  after the role went live.
related_units:
- sahayika-escalation-duty-needs-supervisor-assignment
---

## Unit

According to the research partner's Sahayika evaluation, this is a failure and fix from the pilot.

**Failure.** Nurse-midwife design input was considered but not scheduled, for lack of time. The nurses were briefed for an hour on their role and were not asked how it should work.

**Fix (not yet applied).** In interviews at month 8 the nurses proposed a supervisor-assigned rota and a fixed daily time slot. The steering group's rebuild has supervisors formally assign the duty.

**Insight.** The constraints that broke the route were known to the nurses and surfaced only once someone asked them.

## Condition

- **Applies when:** a new duty for frontline staff is designed by the project team rather than with the staff who will carry it.
- **Fails when:** Not documented in the source.

## Before → after

- **Before:** role designed without the nurses; one-hour briefing.
- **After:** the role was experienced as an unassigned favour, and escalation waits stretched to days. No co-designed version has been run yet.

## Why it is reusable

It names a cheap step skipped under time pressure and what skipping it cost. It is a suggestion from another adoption's lived experience, not a recommendation — and this record comes from a synthetic test document.
