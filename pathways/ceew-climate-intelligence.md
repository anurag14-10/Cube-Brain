---
name: AI for Public Health Early-Warning — National
type: pathway
schema_version: 2
aliases:
- AI for Public Health Early-Warning — National
- CEEW Climate Intelligence
- Climate Intelligence for Public Decision-Making
summary: Two AI systems built with the Council on Energy, Environment and Water (CEEW) — a conversational
  climate-data agent and a dengue early-warning system — and the shared implementation lessons between
  them.
tags:
- Climate
- Public Health
- Policy
title: AI for Public Health Early-Warning — National
pathway_kind: single-deployment
sector: Public Health
use_case_category: Climate intelligence for public decision-making — conversational climate-data access
  and dengue outbreak early warning
population_served: Researchers and policymakers navigating fragmented climate datasets (CRAVIS.AI); public
  health officials deciding where to deploy limited resources before disease outbreaks (early-warning system)
stage_reached: pilot
related_pathways:
- data-dhara
gaps:
- Datasets on mosquito and viral serotype changes, which drive unusually severe dengue outbreaks, are rarely
  publicly available — diffusion here depends on strengthening the wider data ecosystem, not only on sharing
  AI models.
contributing_organisations:
- ceew
corpora:
- library-corpus
doc_refs:
- content/library-wiki/pathways/ceew-climate-intelligence.md
lifecycle: published
published_on: '2026-09-01'
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/library-wiki/pathways/ceew-climate-intelligence.md
- system: github_repo
  method: derived
  date: '2026-10-08'
  ref: published_on = date content/library-wiki/pathways/ceew-climate-intelligence.md was first committed
- system: diffusion_cube_code
  method: derived
  date: '2026-10-08'
  ref: sector inferred from title/tags; document states none
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/ceew-climate-intelligence.md — Overview (identity, population) and
    Ecosystem × Scale (named gap)
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

According to CEEW's Climate Intelligence pathway, based on practitioner insights led by the Council on Energy, Environment and Water (CEEW), the pathway draws on two complementary AI systems:

- **CRAVIS.AI** (Climate Resilience Analytics and Visualization System), a conversational agentic AI that helps researchers and policymakers search, analyse and interact with fragmented climate datasets in natural language. It addresses an information-access problem: climate data existed across repositories but was hard to discover, combine and interpret.
- **An AI-enabled Early Warning System (EWS)** that combines climate, health surveillance and geospatial data to forecast dengue outbreaks several weeks ahead. It addresses a decision-making problem: officials had surveillance data but no advance warning of where and when outbreaks would occur.

- **Sector:** Public Health (inferred; tags are Climate, Public Health, Policy)
- **Geography:** Not documented in the source beyond the title's "National"
- **Population served:** Researchers and policymakers navigating fragmented climate datasets (CRAVIS.AI); public health officials deciding where to deploy limited resources before outbreaks (EWS)
- **Stage reached:** [Pilot](../concepts/pilot.md), as the document's frontmatter states

Contributed by: Council on Energy, Environment and Water (CEEW), whose practitioner insights the pathway is based on.

The document is organised as six cross-cutting learnings rather than a stage-by-stage account, and it says itself that it does not carry the "deployment at a glance" scale figures other pathways in the library do.

## Effort

- **Scale / impact achieved:** Not documented in the source.
- **Cost anchor:** Not documented in the source.
- **Build effort:** Not documented in the source.
- **Downstream adoptions:** Not documented in the source.

## Coverage

The library document has no density grid. Its dimension/stage layout is described as a best-effort mapping in which several cells are thin because the source does not distinguish that stage, so `coverage` is left blank.

## Gaps

The document names one gap explicitly: datasets on mosquito and viral serotype changes, which drive unusually severe dengue outbreaks, are rarely publicly available. Diffusion here is therefore not only about sharing AI models but about strengthening the wider data ecosystem that enables them.

## Where the reusable value is

Five units. The library document does not number its learnings, so the units carry no `source_unit_id` and their tags are a best-effort reading against the framework. There is no Section 5, so there are no patterns.

- **Data before models.** [Audit the data before selecting a model](../units/ceew-climate-intelligence-audit-data-before-model.md) (Solution × Define). For the EWS, health surveillance data, not climate or geospatial data, was the binding constraint.
- **Ship early and learn.** [Deploy before models and data are perfect, and let deployment improve the data](../units/ceew-climate-intelligence-deploy-before-data-is-perfect.md) (Institution × Define).
- **Earn institutional trust.** [Introduce AI as decision support before embedding it in routine workflows](../units/ceew-climate-intelligence-decision-support-before-workflow-embedding.md) (Institution × Define).
- **Partners and what travels.** [Run AI deployment as a partnership, not a procurement exercise](../units/ceew-climate-intelligence-partnership-not-procurement.md) (Ecosystem × Define) and [the implementation journey, not the trained model, is the reusable asset](../units/ceew-climate-intelligence-implementation-journey-as-asset.md) (Ecosystem × Scale).

[Data DHARA](data-dhara.md) shares the "data quality and governance over model sophistication" lesson, applied to government administrative data.

## Corpus copies

- `content/library-wiki/pathways/ceew-climate-intelligence.md`

Library corpus only, a conversational overview grounded one document at a time behind the public Diffusion Library.
