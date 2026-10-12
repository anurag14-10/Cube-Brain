---
name: DHARA 7-Stage Toolkit as a sequenced data-readiness work programme
type: unit
schema_version: 2
summary: A seven-stage pipeline (Found → Labeled → Standardized → Checked → Connectable → Searchable →
  AI-ready) that gives teams a shared vocabulary and gate structure for each dataset, with Stage 6 (searchable)
  as the minimum bar for inclusion in a governed use case.
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
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-d
stage: define
also_relevant_at:
- pilot
- scale
source_unit_id: Unit 4
applies_when: The deployment draws on multiple heterogeneous datasets from different departmental owners;
  a shared standard is needed to coordinate data-readiness work across teams.
fails_when: Not documented in the source
purpose: Provides a common vocabulary and gate structure so teams know exactly what state each dataset
  is in, what work remains, and what threshold (Stage 6 — searchable) must be reached before a dataset
  is eligible for inclusion in a governed use case. The seven stages are (1) Data is Found, (2) Data is
  Labeled, (3) Data is Standardized, (4) Data is Checked, (5) Data is Connectable, (6) Data is Searchable,
  (7) Data is AI-ready.
reuse_condition: Each stage is defined independently of the investment-facilitation domain, so any department
  can track its own datasets against the seven stages and treat the sequence as a work programme rather
  than inventing its own data-readiness criteria. Use when coordinating data across multiple departments
  with heterogeneous formats; treat Stage 6 as the minimum bar for any governed use case.
adopter_intents:
- What should I build first — the AI layer or the data layer?
- Is there a standard sequence for getting government data AI-ready?
- What should I be building that the next state or department can reuse?
- How do I structure a heterogeneous mix of PDFs, APIs, and GIS data?
- What is the minimum data-readiness threshold before I connect data to an AI system?
related_units:
- nivesh-suvidha-data-structuring-is-the-build
- nivesh-suvidha-iterate-repository-through-live-use
- nivesh-suvidha-gap-flagging-loop
- data-dhara-staged-data-unlock-pipeline
---

## Unit

According to Invest UP's Nivesh Suvidha pathway, the asset is the DHARA 7-Stage Toolkit — a sequenced pipeline for advancing raw government data from inventory to AI-readiness:

1. Data is Found
2. Data is Labeled
3. Data is Standardized
4. Data is Checked
5. Data is Connectable
6. Data is Searchable
7. Data is AI-ready

**Purpose:** Provides a common vocabulary and gate structure so teams know exactly what state each dataset is in, what work remains, and what threshold — Stage 6, searchable — must be reached before a dataset is eligible for inclusion in a governed use case.

**Reuse condition:** Each stage is defined independently of the investment-facilitation domain. Any department can track its own datasets against the seven stages and treat the sequence as a work programme rather than inventing its own data-readiness criteria. The pathway's toolkit table adds: treat Stage 6 as the minimum bar for any governed use case.

No file or link to the toolkit is attached in the source.

## Condition

- **Applies when:** The deployment draws on multiple heterogeneous datasets from different departmental owners; a shared standard is needed to coordinate data-readiness work across teams.
- **Fails when:** Not documented in the source

## Before → after

Not documented in the source.

## Why it is reusable

It is domain-independent, and it gives an adopter a ready-made definition of "ready enough to connect to the AI" (Stage 6), so they do not have to set their own threshold. The Data DHARA pathway describes a related staged sequence from a sibling deployment. It is a suggestion from another adoption's lived experience, not a recommendation.
