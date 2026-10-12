---
name: Voice AI for Inclusion — price against the managed platform you will start on
type: unit
schema_version: 2
summary: Estimate voice-AI cost as calls/month × minutes/call × the managed-platform rate (~₹2.5–4.5/min)
  a first deployment actually starts on, not the self-hosted floor (~₹0.5–1.5/min) earned only after scale.
doc_refs:
- content/wiki/pathways/voice-ai-for-inclusion.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/voice-ai-for-inclusion.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
contested:
- field: stage
  readings:
  - 'grounding corpus (content/wiki/pathways/voice-ai-for-inclusion.md): the Jal Jeevan Mission Assam
    "phone numbers and five yes/no questions" example sits inside this Solution × Explore unit'
  - 'library corpus (content/library-wiki/pathways/voice-ai-for-inclusion.md): the same example is placed
    under Ecosystem × Scale ("the minimum viable data requirement comes from the use case")'
  note: The grounding copy is framework-structured and is the primary source; the unit keeps its tags. Library
    placement recorded, not arbitrated.
pathway: voice-ai-for-inclusion
unit_type: Strategic Decision
dimension: solution
sub_category: solution-e
stage: explore
source_unit_id: Unit 2
applies_when: Estimating cost before any pilot has run.
fails_when: Not documented in the source
decision: Estimate voice-AI cost at the exploration stage by multiplying calls per month × minutes per
  call × the per-minute rate of the managed platform a first deployment will actually start on (roughly
  ₹2.5–4.5/minute) — not the open-source, self-hosted rate (₹0.5–1.5/minute) that a deployment earns only
  after real scale and its own migration work.
alternative_considered: Budgeting against the open-source floor from the outset, assuming it's achievable
  immediately.
reason: Cost is no longer the primary obstacle to voice AI adoption — but budgeting against a rate a deployment
  hasn't earned yet produces a plan that looks cheaper than it will actually be in the phase that matters,
  the first one.
context: The number of languages barely moves the bill; call duration and concurrency move it far more.
  First-time adopters reliably under-provision for the parts that aren't AI at all — content, data and
  system integration. A water-supply feedback line in Assam needed only a phone-number list and five yes/no
  questions; cost and build effort should scale with the use case's real complexity.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How much should I budget before running a pilot?
---

## Unit

According to EkStep Foundation's Voice AI for Inclusion pathway, this is a strategic decision about costing that recurred across the synthesised deployments.

**Decision.** Estimate cost at exploration as calls per month × minutes per call × the per-minute rate of the managed platform a first deployment will actually start on (roughly ₹2.5–4.5/minute) — not the open-source, self-hosted rate (₹0.5–1.5/minute) that a deployment earns only after real scale and its own migration work. For comparison the pathway gives above ₹6/minute for a human-only call centre.

**Alternative considered.** Budgeting against the open-source floor from the outset, assuming it is achievable immediately.

**Why.** Cost is no longer the primary obstacle to voice AI adoption, but budgeting against a rate not yet earned produces a plan that looks cheaper than it will be in the first phase — the one that matters.

**What this looked like.** The number of languages supported barely moves the bill; call duration and concurrency move it far more. First-time adopters reliably under-provision for the non-AI parts: content, data and system integration. Not every use case needs rich data: a water-supply feedback line in Assam (Jal Jeevan Mission) needed only a phone-number list and five yes/no questions (did water arrive, on schedule, in sufficient quantity, adequate quality, are you satisfied) to show where a 55-litres-per-person mandate was actually being met.

## Condition

- **Applies when:** Estimating cost before any pilot has run.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

It gives a next adopter a costing formula, the rate band to plug into it, and the two variables (duration, concurrency) that actually move the bill. The per-minute figures are a synthesised range across deployments, not a confirmed number for any one of them. A suggestion, not a recommendation.
