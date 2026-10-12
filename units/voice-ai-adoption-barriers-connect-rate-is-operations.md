---
name: Low outbound connect rates are usually an operations problem, not a model problem
type: unit
schema_version: 2
summary: Randstad India saw 60–70% of outbound calls go unanswered because of spam-flagging and no number whitelisting;
  the fix is operational — rotate number series, call when the population answers, retry two to three times,
  pre-announce by SMS.
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
- field: fix
  readings:
  - 'Grounding copy: the 30–35% → 60–70% pickup jump came "simply by shifting all outbound calls to a 7–8am
    window"; retries and a pre-call SMS are listed as separate tactics.'
  - 'Library copy (Karnataka government agriculture use case): calling between 7–8am, a prior WhatsApp/text
    alert, and two or three spaced attempts "together" moved pickup from 30–35% to 60–70%, with no change to
    the model.'
  note: The copies disagree on whether the jump is attributable to call timing alone or to the three tactics
    combined, and on the alert channel (SMS vs WhatsApp/text). Not arbitrated.
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: voice-ai-adoption-barriers
unit_type: Failure and Fix
dimension: solution
sub_category: solution-e
stage: pilot
source_unit_id: Unit 5
applies_when: Outbound connect rate is low and the conversation itself, once answered, performs reasonably
  well.
fails_when: Calls are being answered at a normal rate and still failing — that points to conversation design
  or model quality instead.
failure: Randstad India found 60–70% of outbound calls went unanswered — not because the conversation itself
  failed, but because of TrueCaller spam-flagging and the absence of telecom number whitelisting, an operational
  ceiling no amount of model improvement could fix.
fix: Rotate the outbound number series as soon as it gets spam-flagged rather than waiting it out; call at
  the time of day the target population actually answers — a government agriculture survey found pickup rates
  jumped from roughly 30–35% to 60–70% simply by shifting all outbound calls to a 7–8am window, once farmer
  call-answering patterns were actually observed rather than assumed; trigger two to three attempts per contact
  at spaced intervals rather than a single try; and where feasible, precede the call with an SMS naming the
  expected caller.
insight: A call that never gets answered produces the same failure signal as a call that goes badly — but the
  diagnosis and the fix are completely different, and conflating the two sends teams chasing a model or script
  problem that doesn't exist.
adopter_intents:
- Our outbound calls aren't getting picked up
related_units:
- voice-ai-adoption-barriers-weighted-vendor-scorecard
- voice-ai-adoption-barriers-integration-plumbing-not-the-ai
---

## Unit

According to EkStep Foundation / People+AI's Voice AI Adoption Barriers pathway, this is a failure and fix drawn from the organisations it synthesises.

**Failure.** Randstad India found 60–70% of outbound calls went unanswered — not because the conversation itself failed, but because of TrueCaller spam-flagging and the absence of telecom number whitelisting, an operational ceiling no amount of model improvement could fix.

**Fix.** Rotate the outbound number series as soon as it gets spam-flagged rather than waiting it out; call at the time of day the target population actually answers — a government agriculture survey found pickup rates jumped from roughly 30–35% to 60–70% simply by shifting all outbound calls to a 7–8am window, once farmer call-answering patterns were actually observed rather than assumed; trigger two to three attempts per contact at spaced intervals rather than a single try; and where feasible, precede the call with an SMS naming the expected caller.

**Insight.** A call that never gets answered produces the same failure signal as a call that goes badly — but the diagnosis and the fix are completely different, and conflating the two sends teams chasing a model or script problem that doesn't exist.

## Condition

- **Applies when:** Outbound connect rate is low and the conversation itself, once answered, performs reasonably well.
- **Fails when:** Calls are being answered at a normal rate and still failing — that points to conversation design or model quality instead.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

The reusable part is the insight the fix revealed, read together with the condition tag above. It is a suggestion from other adoptions' lived experience, not a recommendation.
