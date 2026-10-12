---
name: Bharat Vistaar
type: pathway
schema_version: 2
aliases:
- Bharat Vistaar
- Bharat VISTAAR
- unified-ai-driven-agri-ecosystem
summary: A Ministry of Agriculture-backed pan-India AI advisory platform that federates the OAN governance
  template across states and institutions to deliver voice-first agricultural advisory to 140M+ smallholder
  farmers.
tags:
- Voice AI
- Smallholder Farmers
- Digital Public Infrastructure
- Multilingual Advisory
title: Bharat Vistaar
pathway_kind: single-deployment
sector: Agriculture
use_case_category: Agricultural advisory — national voice-first AI advisory for smallholder farmers
geography: Pan-India; Phase 1 across Maharashtra, Bihar, Gujarat and Hindi/English-speaking states
population_served: 140M+ smallholder farmers — rural, low-income, digitally underserved, feature-phone
  users and low-literacy populations
stage_reached: scale
partner_organisations:
- ekstep-foundation
- icar
- india-meteorological-department
- ai4bharat
- bhashini
- voicera
- karya
- iiit-bangalore
- strathmore-university
key_dates: February 2026 — Phase 1 launch; mid-2026 — ~10M queries answered
scale_impact: ~10M queries answered and 378K+ farmers reached (as of mid-2026). State-level predecessor
  MahaVISTAAR ~3M queries and 646K+ farmers in 14 months; Amul AI ~1.4M queries and 230K+ farmers in 6
  months
cost_anchor: ₹2,800+ crore allocated for India's Digital Agriculture Mission (2024–26) — the budget envelope
  the deployment sits within; per-interaction cost not documented in the source
build_effort: Not documented for Bharat Vistaar itself; predecessor instances compressed from 9 months
  (MahaVISTAAR, built from scratch) to 3 months (Ethiopia) to 3 weeks (Amul AI) as the governance template
  matured
downstream_adoptions:
- Ethiopia — national agri and livestock AI advisory on the same OAN governance template
- Kenya — agri and livestock network with Strathmore University on the same template
- Sri Lanka — enterprise solutions provider using the same governance template
related_pathways:
- mahavistaar
- ai-advisory-for-dairy-farmers
coverage:
  persona:Explore: 2
  persona:Define: 1
  persona:Pilot: 0
  persona:Scale: 1
  solution:Explore: 2
  solution:Define: 2
  solution:Pilot: 0
  solution:Scale: 2
  institution:Explore: 2
  institution:Define: 2
  institution:Pilot: 0
  institution:Scale: 0
  ecosystem:Explore: 0
  ecosystem:Define: 2
  ecosystem:Pilot: 0
  ecosystem:Scale: 2
gaps:
- Pilot × all dimensions — what broke with real users before national rollout? The sources move directly
  from architecture design to Scale-stage metrics; no failure taxonomy, data quality incident or institutional
  response to a first public error is documented.
- Institution × Scale — who owns this operationally without the founding team? No named operational owner,
  standing review cadence or permanent budget line separate from the Digital Agriculture Mission envelope
  is documented.
- Persona × Pilot — which user interactions failed, and why? Scope failures are not distinguished from
  quality failures.
- Ecosystem × Explore — who else tried to solve this for this population, and what happened? Prior attempts
  by others at national-scale agricultural advisory AI in India are not assessed.
- Solution × Scale — which data sources are breaking under national load, and do formal SLAs exist? SLAs
  for ICAR, IMD, AgriStack and mandi price feeds, accountability for stale sources, and the most problematic
  source are not documented.
contributing_organisations:
- coss
deploying_organisations:
- ministry-of-agriculture-india
corpora:
- grounding-corpus
doc_refs:
- content/wiki/pathways/unififed-ai-driven-agri-ecosystem.md
lifecycle: unindexed
contested:
- field: coverage
  readings:
  - 'Section 2 grid: Institution × Scale is ○ (0)'
  - 'Section 3: Unit 6 (governance template across instances) is tagged Institution × Scale'
  note: The document disagrees with itself. `coverage` keeps the grid as written; the unit keeps its Section 3 tag. Found by `cube_report.py --section grid`, 2026-10-12.
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/unififed-ai-driven-agri-ecosystem.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/unififed-ai-driven-agri-ecosystem.md — Sections 1–2 (identity, effort, coverage
    grid, gaps)
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

According to the Bharat Vistaar pathway contributed by COSS (Centre for Open Societal Systems), Bharat VISTAAR (Virtually Integrated System to Access Agricultural Resources) is a Ministry of Agriculture-backed, pan-India AI advisory platform. Farmers reach it through a toll-free helpline (155261), a mobile app and a web portal, in Hindi and English, with 11 languages planned. It is built on the OAN 7-layer architecture, with ICAR, IMD, AgriStack and mandi price systems as named federated data sources, and it is the national instance of the governance template proven at state level in [MahaVISTAAR](mahavistaar.md) and [Amul AI](ai-advisory-for-dairy-farmers.md).

- **Sector:** Agriculture
- **Geography:** Pan-India; Phase 1 across Maharashtra, Bihar, Gujarat and Hindi/English-speaking states
- **Population served:** 140M+ smallholder farmers — rural, low-income, digitally underserved, feature-phone users and low-literacy populations
- **Stage reached:** [Scale](../concepts/scale.md)
- **Key dates:** February 2026 — Phase 1 launch; mid-2026 — about 10M queries answered

Contributed by: COSS (Centre for Open Societal Systems), a joint initiative of EkStep Foundation and IIIT Bangalore. The Ministry of Agriculture holds the mandate and the public-facing service.

The pathway's own reading guide says its main value for the next adopter is not the product (helpline, app, chatbot) but the governance architecture that makes federated AI advisory sustainable across institutions with different data owners, mandates and languages.

**Scope / does not transfer when.** The OAN architecture and governance template transfer; localised agricultural knowledge bases, language models and integration with country-specific agronomy and extension systems must be rebuilt at each deployment. The template fails when no research institution equivalent to ICAR exists to ground advisory in verified agronomic knowledge, or when no national farmer identity registry equivalent to AgriStack is available to give AI agents farmer context.

## Effort

- **Scale / impact achieved:** About 10M queries answered and 378K+ farmers reached (as of mid-2026). The state-level predecessor MahaVISTAAR reached about 3M queries and 646K+ farmers in 14 months; Amul AI about 1.4M queries and 230K+ farmers in 6 months.
- **Cost anchor:** ₹2,800+ crore allocated for India's Digital Agriculture Mission (2024–26), the budget envelope the deployment sits within. Per-interaction cost is not documented in the source.
- **Build effort:** Not documented for Bharat Vistaar itself. Predecessor instances compressed from 9 months (MahaVISTAAR, built from scratch) to 3 months (Ethiopia) to 3 weeks (Amul AI) as the governance template matured.
- **Downstream adoptions:** Ethiopia (national agri and livestock AI advisory), Kenya (agri and livestock network with Strathmore University) and Sri Lanka (an enterprise solutions provider), all on the same OAN governance template, localised at each stop.

## Coverage

From the document's own coverage grid (Section 2):

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●● | ● | ○ | ● |
| Solution | ●● | ●● | ○ | ●● |
| Institution | ●● | ●● | ○ | ○ |
| Ecosystem | ○ | ●● | ○ | ●● |

The densest knowledge sits at [Define](../concepts/define.md) and [Scale](../concepts/scale.md) (architecture decisions and the federation model). [Pilot](../concepts/pilot.md) is empty in every dimension; the document tells adopters building toward Scale to treat that as an active risk, not a resolved one.

## Gaps

The document names five gaps:

1. **What broke with real users before national rollout (Pilot × all dimensions).** The sources move straight from architecture design to Scale-stage metrics: no failure taxonomy, no data quality incident, no account of the institution's response to the first public error.
2. **Who owns this operationally without the founding team (Institution × Scale).** No named operational owner, standing review cadence, or permanent budget line separate from the Digital Agriculture Mission envelope is documented.
3. **Which user interactions failed, and why (Persona × Pilot).** Scope failures (questions outside the mandate) are not distinguished from quality failures (mandate questions answered badly).
4. **Who else tried to solve this, and what happened (Ecosystem × Explore).** Prior attempts by others at national-scale agricultural advisory AI in India are not assessed.
5. **Which data sources break under national load, and do SLAs exist (Solution × Scale).** Whether formal SLAs govern ICAR, IMD, AgriStack and mandi price feeds, who is accountable when a source goes stale, and which source causes the most quality problems are not documented.

## Where the reusable value is

Eight units for the eight micro-innovations in Section 3, plus four Toolkit Asset units for the Section 4 rows (the OAN 7-layer reference architecture, the federated ingestion pipeline, the partner role map and the multi-instance governance template). The document has no Section 5, so there are no patterns, and no unit sits at Pilot.

- **Who it is for and how they reach it.** [Voice-first, feature-phone-first design](../units/unififed-ai-driven-agri-ecosystem-voice-first-feature-phone-first.md) (Persona × Explore) and [Scope by the farmer's decision cycle, not departmental boundaries](../units/unififed-ai-driven-agri-ecosystem-scope-by-farmer-decision-cycle.md) (Persona × Define).
- **The architecture that is hard to reverse.** [OAN 7-layer open architecture as the foundation choice](../units/unififed-ai-driven-agri-ecosystem-oan-open-federated-architecture.md) and its [reference stack](../units/unififed-ai-driven-agri-ecosystem-oan-seven-layer-reference-architecture.md) (Solution × Define); [the AI layer retrieves but does not own institutional data](../units/unififed-ai-driven-agri-ecosystem-ai-layer-retrieves-not-owns-data.md) and the [federated ingestion pipeline](../units/unififed-ai-driven-agri-ecosystem-federated-ingestion-pipeline.md) (Solution × Define).
- **Mandate and governance.** [Government mandate as the irreplaceable precondition](../units/unififed-ai-driven-agri-ecosystem-government-mandate-as-precondition.md) (Institution × Explore); [reuse the governance template, not just the code](../units/unififed-ai-driven-agri-ecosystem-reuse-governance-template-not-just-code.md) and the [governance template itself](../units/unififed-ai-driven-agri-ecosystem-multi-instance-governance-template.md) (Institution × Scale).
- **The partner network and federation.** [30+ named partner roles resolved before model work begins](../units/unififed-ai-driven-agri-ecosystem-partner-roles-named-before-model-work.md) and the [partner role map](../units/unififed-ai-driven-agri-ecosystem-partner-role-map.md) (Ecosystem × Define); [federal-by-design peer instances](../units/unififed-ai-driven-agri-ecosystem-federal-by-design-peer-instances.md) (Ecosystem × Scale).

## Corpus copies

- `content/wiki/pathways/unififed-ai-driven-agri-ecosystem.md`

On disk in the grounding corpus but **not linked from `content/wiki/pathways/index.md`**, so excluded from grounding and the /wiki listing. It may still be live via `published_pathways` — check the DB before calling it unpublished. The slug's spelling ("unififed") is the corpus file's real stem.
