---
name: Name the farmer's current workaround before designing the replacement
type: unit
schema_version: 2
summary: Document what farmers do today when formal advisory fails — who they call, whose advice they follow
  — and design the replacement to beat that workaround on what made it work; in Morocco the workaround's failure
  was bias, not latency.
doc_refs:
- content/wiki/pathways/ai-crop-diagnosis-advisory.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-crop-diagnosis-advisory.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against concepts/<dimension>.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ai-crop-diagnosis-advisory
unit_type: Strategic Decision
dimension: persona
sub_category: persona-b
stage: explore
source_unit_id: Unit 2
applies_when: The target population has been managing without the formal service for some time and has developed
  adaptive workarounds that reveal what actually matters to them.
fails_when: Not documented in the source
decision: Before designing any AI-assisted advisory service, document what the farmer currently does when the
  formal extension or advisory system fails — who they call, what they search, whose advice they follow.
alternative_considered: Assume the workaround is "nothing" or that farmers are simply underserved, and design
  the service from first principles.
reason: The workaround is the real baseline. If a farmer currently photographs a diseased leaf and sends it
  to a WhatsApp group of peers, the replacement must be meaningfully better on the dimensions that made that
  workaround work — speed, trust, language, format — not just technically more accurate.
context: Field observation in Morocco established that farmers' primary workaround was asking input dealers,
  who had an incentive to recommend high-margin products. The service design prioritised disinterested, grounded
  advice over speed, because the workaround's failure mode was bias, not latency.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do I define who this is actually for?
related_units:
- ai-crop-diagnosis-advisory-persona-by-advice-gap
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a strategic decision from the deployment.

**Decision.** Before designing any AI-assisted advisory service, document what the farmer currently does when the formal extension or advisory system fails — who they call, what they search, whose advice they follow.

**Alternative considered.** Assume the workaround is "nothing" or that farmers are simply underserved, and design the service from first principles.

**Why.** The workaround is the real baseline. If a farmer currently photographs a diseased leaf and sends it to a WhatsApp group of peers, the replacement must be meaningfully better on the dimensions that made that workaround work — speed, trust, language, format — not just technically more accurate.

**What this looked like here.** Field observation in Morocco established that farmers' primary workaround was asking input dealers, who had an incentive to recommend high-margin products. The service design prioritised disinterested, grounded advice over speed, because the workaround's failure mode was bias, not latency.

## Condition

- **Applies when:** The target population has been managing without the formal service for some time and has developed adaptive workarounds that reveal what actually matters to them.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the reasoning show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
