---
name: Build abstention and confidence reporting as core outputs, not post-hoc safeguards
type: unit
schema_version: 2
summary: The output schema carries a confidence field and a defined abstention response ("retake in natural
  light"); low-confidence and out-of-distribution cases go to the agronomist review queue first.
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
dimension: solution
sub_category: solution-b
stage: define
source_unit_id: Unit 5
applies_when: The advice has material consequences — treatment decisions, input purchases, harvest timing —
  where a wrong confident answer is worse than an honest non-answer.
fails_when: Not documented in the source
decision: Design the system to return an explicit confidence level and to abstain — returning "I cannot reliably
  assess this" — when image quality, out-of-distribution conditions, or knowledge-corpus gaps make a reliable
  assessment impossible, rather than always returning a best-guess answer.
alternative_considered: Return the highest-probability answer always, with a generic disclaimer, and allow
  the user to decide how much to trust it.
reason: 'A system that always answers trains users to trust outputs regardless of reliability, which is dangerous
  in a high-stakes advisory context. Abstention with an explanation maintains calibrated user trust and directs
  the farmer toward a better interaction rather than a wrong decision. Confidence reporting also creates a
  signal the agronomist review queue can prioritise: low-confidence cases go to human review first.'
context: DeepLeaf's output schema includes a confidence field and a defined abstention response. The agronomist
  review rota prioritises cases flagged as low-confidence or out-of-distribution. Field testing in Morocco
  established that farmers responded better to an honest "I need a clearer image" than to a confident wrong
  answer.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do I make the system honest about what it doesn't know?
- How do I structure agronomist review and escalation?
related_units:
- ai-crop-diagnosis-advisory-agronomist-owns-content-authority
- ai-crop-diagnosis-advisory-seven-institutional-changes-before-signing
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a strategic decision from the deployment.

**Decision.** Design the system to return an explicit confidence level and to abstain — returning "I cannot reliably assess this" — when image quality, out-of-distribution conditions, or knowledge-corpus gaps make a reliable assessment impossible, rather than always returning a best-guess answer.

**Alternative considered.** Return the highest-probability answer always, with a generic disclaimer, and allow the user to decide how much to trust it.

**Why.** A system that always answers trains users to trust outputs regardless of reliability, which is dangerous in a high-stakes advisory context. Abstention with an explanation maintains calibrated user trust and directs the farmer toward a better interaction rather than a wrong decision. Confidence reporting also creates a signal the agronomist review queue can prioritise: low-confidence cases go to human review first.

**What this looked like here.** DeepLeaf's output schema includes a confidence field and a defined abstention response. The agronomist review rota prioritises cases flagged as low-confidence or out-of-distribution. Field testing in Morocco established that farmers responded better to an honest "I need a clearer image" than to a confident wrong answer.

## Condition

- **Applies when:** The advice has material consequences — treatment decisions, input purchases, harvest timing — where a wrong confident answer is worse than an honest non-answer.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the reasoning show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
