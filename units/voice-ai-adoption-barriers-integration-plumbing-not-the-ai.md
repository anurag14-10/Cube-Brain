---
name: Integration failures get blamed on the AI when they are really the plumbing
type: unit
schema_version: 2
summary: Sustainable Living Lab lost 40 days to an undelivered vendor web SDK and Rite Water could not reach
  go/no-go without a promised WhatsApp integration — treat integration deliverables as named, dated vendor
  commitments tracked separately from conversation-quality QA.
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
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: voice-ai-adoption-barriers
unit_type: Failure and Fix
dimension: institution
sub_category: institution-f
stage: pilot
source_unit_id: Unit 7
applies_when: The use case depends on the voice system connecting to another system (CRM, WhatsApp, a backend
  database) beyond the call itself.
fails_when: The use case is self-contained within the call — no external system dependency to fail.
failure: Sustainable Living Lab never received a promised web SDK from their vendor and lost 40 days building
  a manual workaround — a failure that had nothing to do with the AI's conversation quality but stalled the
  pilot as completely as a bad model would have. Rite Water could not reach a go/no-go decision at all because
  a promised WhatsApp follow-up integration was never completed, leaving the full user journey untested.
fix: Treat integration deliverables (SDKs, webhook handoffs, CRM or WhatsApp connections) as a named, dated
  commitment in the vendor relationship from day one, not an assumed byproduct of "the vendor being good" —
  and track it separately from conversation-quality QA, since the two fail independently and get confused with
  each other by default.
insight: When a pilot stalls, the instinct is to diagnose the model. In a meaningful share of the organisations
  synthesised, the actual blocker was integration plumbing the vendor had not delivered — a different failure
  with a different owner and a different fix.
adopter_intents:
- Our pilot is stalled and we're not sure if it's the AI
related_units:
- voice-ai-adoption-barriers-two-pass-call-qa
- voice-ai-adoption-barriers-connect-rate-is-operations
---

## Unit

According to EkStep Foundation / People+AI's Voice AI Adoption Barriers pathway, this is a failure and fix drawn from the organisations it synthesises.

**Failure.** Sustainable Living Lab never received a promised web SDK from their vendor and lost 40 days building a manual workaround — a failure that had nothing to do with the AI's conversation quality but stalled the pilot as completely as a bad model would have. Rite Water could not reach a go/no-go decision at all because a promised WhatsApp follow-up integration was never completed, leaving the full user journey untested.

**Fix.** Treat integration deliverables (SDKs, webhook handoffs, CRM or WhatsApp connections) as a named, dated commitment in the vendor relationship from day one, not an assumed byproduct of "the vendor being good" — and track it separately from conversation-quality QA, since the two fail independently and get confused with each other by default.

**Insight.** When a pilot stalls, the instinct is to diagnose the model. In a meaningful share of the organisations synthesised, the actual blocker was integration plumbing the vendor had not delivered — a different failure with a different owner and a different fix.

## Condition

- **Applies when:** The use case depends on the voice system connecting to another system (CRM, WhatsApp, a backend database) beyond the call itself.
- **Fails when:** The use case is self-contained within the call — no external system dependency to fail.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

The reusable part is the insight the fix revealed, read together with the condition tag above. It is a suggestion from other adoptions' lived experience, not a recommendation.
