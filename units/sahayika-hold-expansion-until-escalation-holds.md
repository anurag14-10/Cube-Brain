---
name: Sahayika — hold expansion and run a second pilot until the escalation route is rebuilt
type: unit
schema_version: 2
summary: Faced with a broken escalation route, the steering group chose to rework the system and run a second
  pilot at the same 120 workers, rebuilding escalation with supervisor-assigned duty before any wider rollout.
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
unit_type: Strategic Decision
dimension: institution
sub_category: institution-c
stage: pilot
applies_when: The pilot's AI answers are well received but its human escalation route has broken down
fails_when: Not documented in the source
decision: Rework the system and run a second pilot; rebuild the escalation route before any wider rollout, with
  nurse supervisors formally assigning it; do not expand beyond the current 120 health workers.
reason: Escalation will not hold unless nurse supervisors formally assign it (steering group, month 14).
context: Knowledge-base answers were well received, but the escalation route had broken down and weekly use had
  halved over three months, cause not investigated. The district health officer attended as an observer.
before: A 120-worker pilot with well-received knowledge-base answers and a failed escalation route.
after: Decided at month 14 — rework and a second pilot at the same scale. The outcome is not yet documented.
related_units:
- sahayika-escalation-duty-needs-supervisor-assignment
- voice-ai-adoption-barriers-three-month-pilot-timeline
---

## Unit

According to the research partner's Sahayika evaluation, the steering group decided at month 14 to rework the system and run a second pilot, rebuilding the escalation route before any wider rollout, on the reasoning that escalation will not hold unless nurse supervisors formally assign it. It also decided not to expand beyond the current 120 workers.

This is the project owning its first visible failure rather than scaling past it — the signal the Institution × Pilot cell asks about.

## Condition

- **Applies when:** the AI answers are well received but the human escalation route has broken down.
- **Fails when:** Not documented in the source.

## Before → after

- **Before:** a 120-worker pilot with a failed escalation route.
- **After:** a second pilot at the same scale, with a supervisor-assigned route. Outcome not yet documented.

## Why it is reusable

It shows a funder, NGO and research lab choosing to gate scale on the human part of the system, not the model. It is a suggestion from another adoption's lived experience, not a recommendation — and this record comes from a synthetic test document.
