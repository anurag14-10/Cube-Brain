---
name: Treat data structuring as the primary build task, not a prerequisite
type: unit
schema_version: 2
summary: In a government AI deployment built on existing data, the substantive effort is data engineering
  — discovery, cataloguing, schema standardisation, quality verification — not model selection or prompt
  design; allocate time and team accordingly.
doc_refs:
- content/wiki/pathways/nivesh-suvidha.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/nivesh-suvidha.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: nivesh-suvidha
unit_type: Strategic Decision
dimension: solution
sub_category: solution-d
stage: explore
also_relevant_at:
- define
source_unit_id: Unit 3
applies_when: Source data is heterogeneous (PDFs, scanned documents, structured APIs, GIS layers) and
  held across multiple departments in inconsistent formats.
fails_when: Not documented in the source
decision: Recognise at the outset that the substantive implementation effort in a government AI deployment
  built on existing data is data engineering — discovery, cataloguing, schema standardisation, quality
  verification — not model selection or prompt design. Allocate time and team accordingly.
alternative_considered: Not documented in the source
reason: A language model can only answer questions the underlying data has already been structured to
  support. Underinvesting in the data layer and overinvesting in the AI layer produces a system that sounds
  capable but answers unreliably — which in a government context damages institutional trust faster than
  it builds it.
context: The implementation effort at Invest UP centred on turning policy documents, government orders,
  circulars, APIs and GIS data into a machine-readable schema before the conversational interface was
  built; the model was layered on top of that structured repository, not substituted for it.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- How do I know whether my problem is a data problem or an AI problem?
- What should I build first — the AI layer or the data layer?
- How do I structure a heterogeneous mix of PDFs, APIs, and GIS data?
related_units:
- nivesh-suvidha-discoverability-not-missing-data
- nivesh-suvidha-dhara-seven-stage-toolkit
- data-dhara-ai-readiness-document-schema
---

## Unit

According to Invest UP's Nivesh Suvidha pathway, this is a strategic decision from the deployment.

**Decision.** Recognise at the outset that the substantive implementation effort in a government AI deployment built on existing data is data engineering — discovery, cataloguing, schema standardisation, quality verification — not model selection or prompt design. Allocate time and team accordingly.

**Alternative considered.** Not documented in the source

**Why.** A language model can only answer questions the underlying data has already been structured to support. Underinvesting in the data layer and overinvesting in the AI layer produces a system that sounds capable but answers unreliably — which in a government context damages institutional trust faster than it builds it.

**What this looked like here.** The implementation effort at Invest UP centred on turning policy documents, government orders, circulars, APIs and GIS data into a machine-readable schema before the conversational interface was built. The model was layered on top of that structured repository, not substituted for it.

## Condition

- **Applies when:** Source data is heterogeneous (PDFs, scanned documents, structured APIs, GIS layers) and held across multiple departments in inconsistent formats.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

It changes how an adopter staffs and schedules the build: most of the time and team go to the data layer, not the model. It is a suggestion from another adoption's lived experience, not a recommendation.
