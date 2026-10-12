---
name: Use-case complexity ladder (Level 0–4) — size the build to what the use case needs
type: unit
schema_version: 2
summary: 'A five-level ladder from static broadcast to integrated workflow automation, each level with its
  matched tech stack and build time — and a filter first: Level 0–1 use cases may not need voice AI at all.'
doc_refs:
- content/wiki/pathways/voice-ai-adoption-barriers.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/voice-ai-adoption-barriers.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against concepts/<dimension>.md — the document tags dimension,
    stage and type only
contested:
- field: unit_type
  readings:
  - 'Grounding copy, Section 3 Unit 4: Playbook.'
  - 'Grounding copy, Section 4 row 4: Toolkit Asset (use-case complexity ladder).'
  note: Recorded as Toolkit Asset — the content is a classification ladder with matched stacks (an artifact),
    not a gated sequence; one unit covers both.
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: voice-ai-adoption-barriers
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-a
stage: define
also_relevant_at:
- explore
source_unit_id: Unit 4
applies_when: Scoping any new use case before choosing a stack or a vendor tier.
fails_when: The use case is already clearly Level 3 or 4 and well understood — the ladder adds little at that
  point.
purpose: Place the use case on a five-level complexity ladder before committing to a stack. Level 0, static
  information dissemination (one-way pre-recorded broadcast; telephony + IVR + pre-recorded audio; a few days).
  Level 1, basic feedback collection (simple outbound, yes/no or numeric, no verification; telephony + IVR
  + basic ASR + a response database; about a week). Level 2, enhanced feedback with verification (inbound and
  outbound, data cross-checked against records; streaming STT/TTS + database + analytics; a few weeks). Level
  3, conversational intelligence with analytics (context-aware, sentiment and trend analysis, multichannel;
  streaming STT + LLM + TTS, turn-taking, multichannel CRM; one to three months). Level 4, integrated workflow
  automation (calls trigger real backend actions and escalations; Level 3 plus tool-calling, API integration
  and human handoff; three to six-plus months).
reuse_condition: Applies at the scoping stage, before vendor selection; explicitly flags that Level 0–1 use
  cases may not need voice AI at all.
adopter_intents:
- Do we even need voice AI for this, or is it overkill?
related_units:
- voice-ai-adoption-barriers-weighted-vendor-scorecard
- voice-ai-adoption-barriers-use-case-before-vendor
---

## Unit

According to EkStep Foundation / People+AI's Voice AI Adoption Barriers pathway, the asset is: place the use case on a five-level complexity ladder before committing to a stack. Level 0, static information dissemination (one-way pre-recorded broadcast; telephony + IVR + pre-recorded audio; a few days). Level 1, basic feedback collection (simple outbound, yes/no or numeric, no verification; telephony + IVR + basic ASR + a response database; about a week). Level 2, enhanced feedback with verification (inbound and outbound, data cross-checked against records; streaming STT/TTS + database + analytics; a few weeks). Level 3, conversational intelligence with analytics (context-aware, sentiment and trend analysis, multichannel; streaming STT + LLM + TTS, turn-taking, multichannel CRM; one to three months). Level 4, integrated workflow automation (calls trigger real backend actions and escalations; Level 3 plus tool-calling, API integration and human handoff; three to six-plus months).

**Reuse condition:** Applies at the scoping stage, before vendor selection; explicitly flags that Level 0–1 use cases may not need voice AI at all.

**Examples per level (from the document).** Level 0: voter-awareness calls, vaccination alerts. Level 1: "press 1 if ration received".

**Note.** The ladder's first job is as a filter, not just a sizing guide, before any vendor conversation starts.

## Condition

- **Applies when:** Scoping any new use case before choosing a stack or a vendor tier.
- **Fails when:** The use case is already clearly Level 3 or 4 and well understood — the ladder adds little at that point.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

It is an artifact a next adopter can lift and adapt directly, within the reuse condition above. It is a suggestion from other adoptions' lived experience, not a recommendation.
