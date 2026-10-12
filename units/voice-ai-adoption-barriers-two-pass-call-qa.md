---
name: Run call QA in two passes — a fast scan for every call, a deep audit for the flagged few
type: unit
schema_version: 2
summary: Phase 1 scans 50–100 calls at one to two minutes each for red flags (pass/fail, mostly automatable);
  Phase 2 deep-audits only the ~10–20% flagged plus a few good calls, tracing the ASR→LLM→TTS failure and rolling
  up to a comparable 1–5 call score.
doc_refs:
- content/wiki/pathways/voice-ai-adoption-barriers.md
- content/library-wiki/pathways/voice-ai-adoption-barriers.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/voice-ai-adoption-barriers.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/voice-ai-adoption-barriers.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against concepts/<dimension>.md — the document tags dimension,
    stage and type only
contested:
- field: dimension
  readings:
  - 'Grounding copy: Solution × Pilot (Unit 6).'
  - 'Library copy: "QA discipline determines whether pilots improve or stagnate" sits under Institution × Pilot,
    and QA audit is one of six organisational-readiness workstreams.'
  note: Tags follow the grounding copy.
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: voice-ai-adoption-barriers
unit_type: Playbook
dimension: solution
sub_category: solution-e
stage: pilot
also_relevant_at:
- scale
source_unit_id: Unit 6
applies_when: Any voice AI system is live and generating a call volume too large to review call-by-call in
  full depth.
fails_when: Call volume is small enough that full manual review of every call is still practical — the two-phase
  split adds process without saving effort at that scale.
steps:
- 1. Phase 1, quick scan — one to two minutes per call across a large batch (50–100 calls at once), looking
  only for obvious red flags (missing consent, policy or bias issues, silence or dropouts, complete conversational
  breakdown); simple pass/fail, mostly automatable.
- 'Gate: only the roughly 10–20% of calls flagged as risky, plus a handful of good calls for comparison, go
  forward.'
- 2. Phase 2, deep audit — as long as it takes per call, tracing exactly what broke across the ASR, LLM and
  TTS pipeline; each issue rated critical, major or minor.
- 3. Roll issues up to a 1–5 call score that stays comparable across model updates, languages and configurations.
common_failure_mode: Without this discipline errors compound silently — skipping it let bad data through undetected
  on more than one pilot in the dataset, with mistagged fields and incorrect entries flowing into production
  databases before anyone was systematically checking.
adopter_intents:
- How do we catch quality problems before they scale?
related_units:
- voice-ai-adoption-barriers-integration-plumbing-not-the-ai
- voice-ai-adoption-barriers-one-accountable-owner
---

## Unit

According to EkStep Foundation / People+AI's Voice AI Adoption Barriers pathway, this is a playbook drawn from the organisations it synthesises.

**Steps (in order):**

- 1. Phase 1, quick scan — one to two minutes per call across a large batch (50–100 calls at once), looking only for obvious red flags (missing consent, policy or bias issues, silence or dropouts, complete conversational breakdown); simple pass/fail, mostly automatable.
- Gate: only the roughly 10–20% of calls flagged as risky, plus a handful of good calls for comparison, go forward.
- 2. Phase 2, deep audit — as long as it takes per call, tracing exactly what broke across the ASR, LLM and TTS pipeline; each issue rated critical, major or minor.
- 3. Roll issues up to a 1–5 call score that stays comparable across model updates, languages and configurations.

**Common failure mode.** Without this discipline errors compound silently — skipping it let bad data through undetected on more than one pilot in the dataset, with mistagged fields and incorrect entries flowing into production databases before anyone was systematically checking.

**Practice seen.** Randstad India's own best practice was one to two hours a day of a small team manually auditing call transcripts, specifically to catch flow failures and skipped steps before they scaled into a much larger problem.

## Condition

- **Applies when:** Any voice AI system is live and generating a call volume too large to review call-by-call in full depth.
- **Fails when:** Call volume is small enough that full manual review of every call is still practical — the two-phase split adds process without saving effort at that scale.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

The order of the passes and the gate between them are the reusable part. It is a suggestion from other adoptions' lived experience, to be checked against the condition tag above.
