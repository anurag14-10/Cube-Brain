---
name: Voice AI for Inclusion — the sign of institutionalisation is who does the daily quality checks
type: unit
schema_version: 2
summary: Track whether one person inside the deploying organisation — not at the vendor — listens to real
  calls daily and fixes the script; every deployment in the synthesis that worked had this role, and pilots
  without it usually stalled.
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
pathway: voice-ai-for-inclusion
unit_type: Strategic Decision
dimension: institution
sub_category: institution-g
stage: pilot
also_relevant_at:
- scale
source_unit_id: Unit 5
applies_when: Assessing whether a deployment has genuinely absorbed a voice-AI system versus still depending
  on its original vendor or founding team.
fails_when: Not documented in the source
decision: Track whether one person inside the deploying organisation — not at the vendor — listens to real
  calls daily and fixes the script, as the clearest marker of whether a deployment is becoming institutionalised
  versus staying vendor-dependent.
reason: Every deployment in this synthesis that worked had this internal role; where it was missing, the
  pilot usually stalled. Dependency sets in when an organisation picks a vendor from a demo and dashboard,
  then discovers only after launch that the system can't handle its own users' dialects — because nobody
  inside was positioned to judge what they'd bought.
context: MahaVISTAAR is wired into the state's own systems (AgriStack, MahaDBT, PoCRA), so switching it
  off would break a working government process. Its Additional Chief Secretary and PoCRA Programme Director
  tested the live bot themselves at odd hours; the Bhili effort had the same marker in the Nandurbar District
  Collector, who convened and stayed personally invested from the start.
before: MahaVISTAAR's LLM was commercial GPT-4.1.
after: The department moved to a fine-tuned open model, cutting inference cost roughly 180×, with no vendor
  sign-off and no rebuild — because the department itself controlled the stack.
adopter_intents:
- How do we know if this deployment has become genuinely institutionalised?
related_units:
- voice-ai-for-inclusion-design-for-refusal
---

## Unit

According to EkStep Foundation's Voice AI for Inclusion pathway, this is a strategic decision about how to judge institutionalisation, recurring across the synthesised deployments.

**Decision.** Track whether one person inside the deploying organisation — not at the vendor — listens to real calls daily and fixes the script, as the clearest marker of whether a deployment is becoming institutionalised or staying vendor-dependent.

**Why.** Every deployment in the synthesis that worked had this internal role; where it was missing, the pilot usually stalled. Dependency sets in when an organisation picks a vendor from a demo and a dashboard, then finds after launch that the system cannot handle its own users' dialects, because nobody inside was positioned to judge what they had bought.

**What this looked like.** [MahaVISTAAR](../pathways/mahavistaar.md) is the clearest positive case: it is wired into the state's own systems (AgriStack, MahaDBT, PoCRA), so switching it off would break a working government process, not just close a helpline. The marker holds at the individual level too — MahaVISTAAR's Additional Chief Secretary and PoCRA Programme Director tested the live bot themselves at odd hours, past midnight more than once, and the [Bhili](../pathways/bhili-language-enablement.md) low-resource-language effort had it in the Nandurbar District Collector, who convened the effort and stayed personally invested from the start.

## Condition

- **Applies when:** Assessing whether a deployment has genuinely absorbed a voice-AI system versus still depending on its original vendor or founding team.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** MahaVISTAAR's LLM was commercial GPT-4.1.
- **After:** The department moved to a fine-tuned open model, cutting inference cost roughly 180×, with no vendor sign-off and no rebuild — because it controlled the stack.

## Why it is reusable

It gives an observable marker for institutionalisation. The pathway names the marker but no scoring method for confirming, rather than inferring, the outcome (one of its own gaps). A suggestion, not a recommendation.
