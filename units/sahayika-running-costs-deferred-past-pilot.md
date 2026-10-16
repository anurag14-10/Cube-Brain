---
name: Sahayika — running costs left to "discuss during the pilot" were still unfunded at month 14
type: unit
schema_version: 2
summary: The grant covered build and pilot only; the plan to discuss running costs with the state health mission
  during the pilot was not acted on, and funding beyond the grant was unresolved at the month-14 review.
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
sub_category: institution-f
stage: pilot
also_relevant_at:
- explore
applies_when: A grant funds design, build and pilot, and running costs (model usage, knowledge-base maintenance)
  are left to a later conversation with a government body
fails_when: Not documented in the source
failure: The grant proposal (month 0) said running costs would be discussed with the state health mission during
  the pilot, with no commitment yet sought. At the month-14 steering group the foundation asked about running costs
  after the grant; there was no answer and the state health mission had not been approached.
fix: Not documented in the source — funding beyond the grant remained open at month 14.
insight: Deferring the sustainability conversation to "during the pilot" meant it did not happen while the pilot
  ran; at review time the project could not say who would pay to keep it running.
related_units:
- data-dhara-plan-steady-state-operations
---

## Unit

According to the research partner's Sahayika evaluation, the grant covers building and piloting Sahayika and no source of funding for running it afterwards has been identified.

**Failure.** The proposal deferred running costs to a discussion with the state health mission during the pilot. By month 14 that body had not been approached, and the funder's question went unanswered.

**Fix.** Not documented in the source.

**Insight.** A sustainability conversation scheduled for "during the pilot" did not happen during the pilot.

## Condition

- **Applies when:** a grant funds build and pilot, and running costs are left to a later conversation with a government body.
- **Fails when:** Not documented in the source.

## Before → after

Not documented in the source — the gap is still open.

## Why it is reusable

It is a dated warning about a common grant structure. It is a suggestion from another adoption's lived experience, not a recommendation — and this record comes from a synthetic test document.
