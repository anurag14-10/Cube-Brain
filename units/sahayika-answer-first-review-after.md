---
name: Sahayika — send confident answers straight to the worker; doctors review a weekly sample afterwards
type: unit
schema_version: 2
summary: Answers above a retrieval-confidence threshold went directly to health workers, with doctors reviewing
  a weekly sample after the fact and updating the knowledge base; knowledge-base answers were well received, and
  no review findings are documented.
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
stage: define
also_relevant_at:
- pilot
applies_when: Not documented in the source
fails_when: Not documented in the source
decision: If retrieval confidence is sufficient, the LLM-drafted answer from the doctor-curated knowledge base
  is sent directly to the health worker. Humans review after the fact — two doctors review a weekly sample of sent
  answers and update the knowledge base. Below the threshold, the question is escalated to nurse-midwives.
context: Health workers' supervising nurse-midwives were often unreachable for days, so workers delayed or guessed
  on danger signs, drug doses and scheme questions (grant proposal).
before: Workers delayed or guessed when unsure, because supervisors were unreachable for days.
after: Knowledge-base answers were well received (steering group, month 14). The source documents no findings
  from the weekly sample review, so whether any unsafe answer reached a worker is not established.
related_units:
- mahavistaar-staged-gated-institutional-testing
- bhili-language-enablement-scope-to-what-institution-stands-behind
- sahayika-escalation-duty-needs-supervisor-assignment
---

## Unit

According to the research partner's Sahayika evaluation, the design team described its oversight model as human review after the fact. Confident answers drafted from a knowledge base curated by two doctors go straight to the health worker; doctors review a weekly sample and update the knowledge base. Less confident questions go to nurse-midwives.

## Condition

- **Applies when:** Not documented in the source.
- **Fails when:** Not documented in the source. The design depends on the escalation route for everything below the threshold — see the [escalation unit](sahayika-escalation-duty-needs-supervisor-assignment.md).

## Before → after

- **Before:** workers delayed or guessed when unsure.
- **After:** knowledge-base answers were well received. No sample-review findings are documented, so the safety of answer-first delivery is unverified.

## Why it is reusable

It is a concrete governance choice to set against gated, review-before-release designs elsewhere in the corpus. It is a suggestion from another adoption's lived experience, not a recommendation — and this record comes from a synthetic test document.
