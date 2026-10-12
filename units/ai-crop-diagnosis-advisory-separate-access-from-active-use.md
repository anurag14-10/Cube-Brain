---
name: Track access and active use as separate metrics from the start
type: unit
schema_version: 2
summary: Keep programme enrolment (access) and farmer-initiated interactions (active use) as separately tracked
  metrics and never report one as evidence of the other — 500,000 farmers with access through a white-label
  bank programme is not the 4.78 million weekly-active-user figure.
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
sub_category: persona-c
stage: define
also_relevant_at:
- pilot
- scale
source_unit_id: Unit 3
applies_when: The service is embedded in a larger programme or platform where enrolment substantially exceeds
  active use, and where funders or partners may conflate the two.
fails_when: Not documented in the source
decision: Define access (farmer enrolled in a programme that includes the service) and active use (farmer who
  initiated an interaction in a given period) as separate metrics with separate tracking, and never report
  one as evidence of the other.
alternative_considered: Report programme enrolment or platform registration as the primary reach figure.
reason: Access figures are easier to produce and look larger, but they do not establish that a farmer received
  or acted on advice. Conflating them produces misleading impact claims and hides whether the service is actually
  being used. Separating them forces honest measurement from the start and avoids a later audit finding.
context: The 500,000-farmer Crédit Agricole du Maroc figure is explicitly labelled as an access figure (farmers
  enrolled in the white-label programme), and the 4.78 million weekly-active-user figure is maintained as a
  separate metric. The pathway document carries both without treating one as proof of the other.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do I avoid overstating reach in my impact reporting?
- How do I track whether farmers are actually using the service?
related_units:
- ai-crop-diagnosis-advisory-pre-register-evaluation-protocol
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a strategic decision from the deployment.

**Decision.** Define access (farmer enrolled in a programme that includes the service) and active use (farmer who initiated an interaction in a given period) as separate metrics with separate tracking, and never report one as evidence of the other.

**Alternative considered.** Report programme enrolment or platform registration as the primary reach figure.

**Why.** Access figures are easier to produce and look larger, but they do not establish that a farmer received or acted on advice. Conflating them produces misleading impact claims and hides whether the service is actually being used. Separating them forces honest measurement from the start and avoids a later audit finding.

**What this looked like here.** The 500,000-farmer Crédit Agricole du Maroc figure is explicitly labelled as an access figure (farmers enrolled in the white-label programme), and the 4.78 million weekly-active-user figure is maintained as a separate metric. The pathway document carries both without treating one as proof of the other.

## Condition

- **Applies when:** The service is embedded in a larger programme or platform where enrolment substantially exceeds active use, and where funders or partners may conflate the two.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the reasoning show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
