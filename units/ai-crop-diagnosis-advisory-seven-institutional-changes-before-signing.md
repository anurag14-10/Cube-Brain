---
name: Name the seven institutional changes before any partner signs
type: unit
schema_version: 2
summary: Walk every partner's named decision-maker through seven institutional changes — operator, review rota,
  recurring budget line, curation owner, data-rights framework, escalation path, pause authority — and do not
  start technical integration until all seven are named, not promised.
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
unit_type: Playbook
dimension: institution
sub_category: institution-f
stage: define
source_unit_id: Unit 7
applies_when: Any institutional partner (cooperative, bank, government programme, agritech platform) is embedding
  the service under their own brand or within their own farmer-facing channel.
fails_when: Not documented in the source
steps:
- 1. A named operator accountable for day-to-day service.
- 2. A staffed agronomist review rota with defined coverage hours.
- 3. A recurring operating budget line separate from project or grant funding.
- 4. A named curation owner responsible for keeping local knowledge content current.
- 5. A data-rights and consent framework covering farmer data.
- 6. A defined escalation path for complaints and harmful-advice incidents.
- 7. A named person authorised to pause or withdraw the service.
- 'Gate: walk all seven with the named decision-maker before the partner signs an integration agreement; do
  not advance to technical integration until all seven are named — not promised, named.'
common_failure_mode: Treating items 2, 3 and 4 (review rota, budget line, curation owner) as implementation
  details to be resolved after sign-off. A deployment that launches without a staffed review rota or a budget
  line is not a pilot — it is a demo with a launch date.
adopter_intents:
- What does a partner institution actually need to have in place before we launch?
- What institutional documents should I prepare before a new deployment?
- How do I structure agronomist review and escalation?
related_units:
- ai-crop-diagnosis-advisory-agronomist-owns-content-authority
- ai-crop-diagnosis-advisory-operating-model-survives-founders
- ai-crop-diagnosis-advisory-data-ownership-table-template
---

## Unit

According to DeepLeaf's DeepLeaf AI Crop Diagnosis and Advisory pathway, this is a playbook from the deployment: before any partner organisation signs an integration agreement, walk through seven required institutional changes with the named decision-maker at that organisation.

**Steps (in order):**

- 1. A named operator accountable for day-to-day service.
- 2. A staffed agronomist review rota with defined coverage hours.
- 3. A recurring operating budget line separate from project or grant funding.
- 4. A named curation owner responsible for keeping local knowledge content current.
- 5. A data-rights and consent framework covering farmer data.
- 6. A defined escalation path for complaints and harmful-advice incidents.
- 7. A named person authorised to pause or withdraw the service.
- Gate: walk all seven with the named decision-maker before the partner signs an integration agreement; do not advance to technical integration until all seven are named — not promised, named.

**Common failure mode.** Treating items 2, 3 and 4 (review rota, budget line, curation owner) as implementation details to be resolved after sign-off. A deployment that launches without a staffed review rota or a budget line is not a pilot — it is a demo with a launch date.

## Condition

- **Applies when:** Any institutional partner (cooperative, bank, government programme, agritech platform) is embedding the service under their own brand or within their own farmer-facing channel.
- **Fails when:** Not documented in the source

## Before → after

Not documented in the source for a specific before/after case. The pathway is explicit that deployments stall at or shortly after launch when these seven conditions are not met before technical integration begins.

## Why it is reusable

The seven items and the single gate — named, not promised, before technical integration — can be run with any institutional partner embedding the service under its own brand. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
