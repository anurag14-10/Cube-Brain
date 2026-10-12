---
name: Two-team execution model with weekly and milestone reviews
type: decision
schema_version: 2
summary: The Cube is delivered by a Solution Team (Kamesh + Tekdi) and a Program Team (David, Anupama + team), jointly accountable for adoption, with a weekly cross-team review and a formal milestone review with senior management at each boundary.
tags:
- programme
- governance
doc_refs:
- docs/raw_documents/AI DIffusion Cube - Product Charter.docx
status: accepted
context: The Product Charter sets out how the Cube is built, curated and adopted between EkStep and Tekdi.
decision: 'Two teams. The Solution Team (Kamesh + Tekdi Team) owns functionality, UI/UX, data and technical architecture, builds and maintains the web app and the Claude Skill integration, and handles product and technical user issues. The Program Team (David, Anupama + Team) owns stakeholder communication and the pathway content lifecycle, onboards adopters, relays user feedback and facilitates testing sessions. Both are jointly accountable for adoption. Cadence: a weekly cross-team review against the current milestone, and a milestone review with senior management at each milestone boundary.'
alternatives: []
consequences:
- Pathway review and publishing sits with the Program Team; the app's admin publish step is where it happens
- Feedback is logged in the charter's Feedback tab, triaged weekly, and accepted items move to the Requirements tab
- Each milestone boundary decides whether the milestone is met, extended or rescoped
decided_by: []
sources:
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: Product Charter § 4 Execution Approach (Team & Roles, Shared Responsibility, Working cadence, Tracking)
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Context

The [Product Charter](../milestones/web-app-with-20-pathways.md) sets out how the Cube is built, curated and adopted.

## Decision

- **Solution Team** ("Kamesh + Tekdi Team"): owns functionality, UI/UX, data and technical architecture; builds and maintains the web app and the Claude Skill integration; handles product and technical issues; joins pathway collection conversations to improve the process.
- **Program Team** ("David, Anupama + Team"): owns stakeholder communication and the pathway content lifecycle (reviewing and publishing contributor submissions); onboards adopters; passes user feedback to the Solution Team; runs testing sessions and walkthroughs.
- **Shared:** both teams are jointly accountable for adoption.
- **Cadence:** a weekly cross-team review of progress against the current milestone, open decisions and Program-surfaced feedback. At each milestone boundary, a formal milestone review with senior management decides whether the milestone is met, needs extension, or should be rescoped.

Team membership is the `teams` variable on people entries (MASTERS 15).

## Alternatives considered

None are recorded in the charter.

## Consequences

- Feedback is logged in the charter's Feedback tab, triaged at the weekly review, and accepted items move to the Requirements tab. There is no external ticket tracker.
- The charter gives no decision date or decider, so `decided_on` and `decided_by` are blank.
