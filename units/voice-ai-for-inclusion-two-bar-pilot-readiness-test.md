---
name: Voice AI for Inclusion — two-bar prototype-to-pilot readiness test
type: unit
schema_version: 2
summary: Before moving a voice prototype to a real-user pilot, clear a technical bar (real call, real dialects,
  under ~2s) and a human bar (a real reason to stay on the line, shown by connect rate and unprompted conversations)
  — the second is the one teams most often skip.
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
- field: dimension
  readings:
  - 'grounding corpus (content/wiki/pathways/voice-ai-for-inclusion.md): Persona × Pilot, with the lab-metrics-vs-users
    test inside this playbook'
  - 'library corpus (content/library-wiki/pathways/voice-ai-for-inclusion.md): "Use metrics to reject a
    model, use users to select it" placed under Technology × Pilot'
  note: The grounding copy is framework-structured and is the primary source; the unit keeps persona. Library
    placement recorded, not arbitrated.
pathway: voice-ai-for-inclusion
unit_type: Playbook
dimension: persona
sub_category: persona-c
stage: pilot
source_unit_id: Unit 7
applies_when: Moving any voice deployment from a working demo to a real-user pilot.
fails_when: The use case is a simple broadcast or yes/no poll — SMS or IVR is cheaper and this two-bar test
  is unnecessary overhead.
steps:
- '1. Technical bar: it runs on a real phone call, understands the actual dialects of the target users
  (tested with native speakers, not a generic benchmark), and replies in under roughly two seconds. Lab
  metrics (word error rate, latency, noise cancellation) are a rejection filter only; the pass/fail signal
  is whether the population served says, unprompted, that it understood them and did not sound robotic.'
- '2. Human bar: the person being called has a genuine reason to stay on the line — evidenced by a real
  connect rate and a few unprompted, genuine conversations, not clean demo calls.'
- '3. Operational check: someone inside the organisation owns it, the knowledge base is real content rather
  than placeholder data, and success metrics (connect rate, talk time, conversion) are fixed before the
  first live call goes out.'
- '4. Gate: commit from prototype to pilot only when both bars are cleared.'
common_failure_mode: Skipping the second (human) bar — a technically working prototype can still fail at
  pilot if nobody has a reason to answer it; cold outbound calling fails where opted-in advisory or reminders
  succeed.
adopter_intents:
- Is my prototype actually ready to move to a real pilot?
related_units:
- voice-ai-for-inclusion-name-the-excluded-person
- voice-ai-for-inclusion-who-does-daily-quality-checks
---

## Unit

According to EkStep Foundation's Voice AI for Inclusion pathway, this is a playbook (Section 4 lists it as the "two-bar prototype-to-pilot readiness test").

**Steps (in order):**

1. **Technical bar** — it runs on a real phone call, understands the actual dialects of the target users (tested with native speakers, not a generic benchmark), and replies in under roughly two seconds. Lab metrics (word error rate, latency, noise cancellation) are useful as a rejection filter but not as the pass/fail signal: the synthesised deployments converged on asking whether the population served says, unprompted, that it understood them and did not sound robotic. A model that clears every benchmark but fails that test is not ready; one that clears it is usually good enough even with mediocre lab numbers.
2. **Human bar** — the person being called has a genuine reason to stay on the line, shown by a real connect rate and a few unprompted, genuine conversations, not clean demo calls.
3. **Operational check** — someone inside the organisation owns it, the knowledge base is real content rather than placeholder data, and success metrics (connect rate, talk time, conversion) were fixed before the first live call.
4. **Gate** — commit from prototype to pilot only when both bars are cleared.

**Common failure mode.** The second bar is the one teams most often skip. Cold outbound calling fails where opted-in advisory or reminders succeed.

## Condition

- **Applies when:** Moving any voice deployment from a working demo to a real-user pilot.
- **Fails when:** The use case is a simple broadcast or yes/no poll — SMS or IVR is cheaper and this two-bar test is unnecessary overhead.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

It is a gated go/no-go test any voice team can run before a pilot, and it names the bar most often skipped. A suggestion, not a recommendation.
