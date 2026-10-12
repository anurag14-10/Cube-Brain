---
name: AI-readiness document schema for government policy documents
type: unit
schema_version: 1
summary: A metadata schema that turns unstructured circulars, manuals and government orders into AI-usable
  records — title, summary, text, category, sub-category, document type, tags, policy year, issuing department,
  fee, timelines, approval phase.
code_refs:
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
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-d
stage: explore
applies_when: The authoritative information exists but is fragmented, siloed or locked in PDFs, circulars,
  manuals, government orders and hidden URLs.
fails_when: The underlying data genuinely doesn't exist yet, rather than existing but being fragmented,
  siloed or PDF-locked.
purpose: 'Makes government policy, scheme, incentive and process documents usable by an AI pipeline (''for
  an AI pipeline, a PDF is not data — it''s a picture of data'') with fields: title, summary, text, category,
  sub-category, document type, tags, policy year, issuing department, fee, timelines, approval phase.
  In Nivesh Suvidha it sits alongside a document taxonomy and backs a chatbot that answers policy/scheme/land
  questions with traceability to source documents.'
reuse_condition: Where policy intelligence is fragmented across many issuing departments (45 in Uttar
  Pradesh's case) and buried in unstructured documents, and the deploying institution owns or may publish
  those documents.
related_units:
- data-dhara-public-data-revocable-vendor-access
---

## Unit

According to the Data DHARA pathway's account of Nivesh Suvidha (Invest UP), this is a toolkit asset from the deployment.

**What it is for.** Makes government policy, scheme, incentive and process documents usable by an AI pipeline ('for an AI pipeline, a PDF is not data — it's a picture of data') with fields: title, summary, text, category, sub-category, document type, tags, policy year, issuing department, fee, timelines, approval phase. In Nivesh Suvidha it sits alongside a document taxonomy and backs a chatbot that answers policy/scheme/land questions with traceability to source documents.

**Reuse condition.** Where policy intelligence is fragmented across many issuing departments (45 in Uttar Pradesh's case) and buried in unstructured documents, and the deploying institution owns or may publish those documents.

No file or link is attached — the document names the asset but does not publish it.

## Condition

- **Applies when:** The authoritative information exists but is fragmented, siloed or locked in PDFs, circulars, manuals, government orders and hidden URLs.
- **Fails when:** The underlying data genuinely doesn't exist yet, rather than existing but being fragmented, siloed or PDF-locked.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

It is an artifact the next adopter can adapt rather than rebuild, within the reuse condition above. It is a suggestion from another adoption's lived experience.
