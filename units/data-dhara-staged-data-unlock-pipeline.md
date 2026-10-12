---
name: Staged data-unlock pipeline from departmental PDFs to agent access
type: unit
schema_version: 2
summary: The Delhi vital-statistics sibling pathway's staged sequence — dataset inventory → metadata tagging
  → schema transformation → dissemination-ready datasets → API access → discoverable catalogue → agent/MCP
  access — runnable inside a department's own infrastructure.
doc_refs:
- content/library-wiki/pathways/data-dhara.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/data-dhara.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: dimension, sub_category, stage and unit_type assigned by best reading against content/framework.md
    — the library document is a conversational overview, not framework-structured
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: data-dhara
unit_type: Playbook
dimension: solution
sub_category: solution-d
stage: pilot
applies_when: Vital-statistics or similar departmental data is locked inside PDFs and not linkable across
  health, nutrition and education systems, and the pipeline must run inside the department's own infrastructure.
fails_when: The underlying data genuinely doesn't exist yet, rather than existing but being fragmented,
  siloed or PDF-locked.
steps:
- 1. Dataset inventory.
- 2. Metadata tagging.
- 3. Schema transformation.
- 4. Dissemination-ready datasets.
- 5. API access.
- 6. Discoverable catalogue.
- 7. Agent/MCP access.
- 'Gates between stages: Not documented in the source.'
common_failure_mode: Not documented in the source
related_units:
- data-dhara-ai-readiness-document-schema
---

## Unit

According to the Data DHARA pathway's account of Nivesh Suvidha (Invest UP), this is a playbook from the deployment.

**Steps (in order):**

- 1. Dataset inventory.
- 2. Metadata tagging.
- 3. Schema transformation.
- 4. Dissemination-ready datasets.
- 5. API access.
- 6. Discoverable catalogue.
- 7. Agent/MCP access.
- Gates between stages: Not documented in the source.

**Common failure mode.** Not documented in the source

## Condition

- **Applies when:** Vital-statistics or similar departmental data is locked inside PDFs and not linkable across health, nutrition and education systems, and the pipeline must run inside the department's own infrastructure.
- **Fails when:** The underlying data genuinely doesn't exist yet, rather than existing but being fragmented, siloed or PDF-locked.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

The order of the steps is the reusable part. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
