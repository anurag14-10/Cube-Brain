---
name: DeepLeaf AI Crop Diagnosis and Advisory
type: pathway
schema_version: 2
aliases:
- DeepLeaf AI Crop Diagnosis and Advisory
summary: An agentic agricultural Vision-Language Model that orchestrates narrow AI models and live satellite,
  weather, soil, and telemetry data to return grounded crop-health assessments — deployed through cooperatives,
  banks, and agritech platforms across Morocco, Senegal, Croatia, and beyond.
tags:
- Vision AI
- Agriculture
- Crop Diagnosis
title: DeepLeaf AI Crop Diagnosis and Advisory
pathway_kind: single-deployment
sector: Agriculture
use_case_category: crop diagnosis and agronomic advisory
geography: Origin Morocco; deployments in Senegal, Croatia, and multiple countries in Africa and Europe
population_served: Smallholder farmers and commercial agricultural operations; embedded through cooperatives,
  banks, input companies, agritech platforms, and government programmes
stage_reached: pilot
contributing_organisations:
- deepleaf
partner_organisations:
- undp-ai-hub
- cineca
- agrivi
- hassad-food
- soilpulse
key_dates: Pathway document as of August 2026; follow-up answers September 2026
scale_impact: 4.78 million weekly active users (internally validated, subject to final validation before
  publication; as of September 2026). Separately, 500,000 farmers with access through the Crédit Agricole
  du Maroc white-label deployment — an access figure, explicitly not the same metric as active use. No measured
  impact figure (yield, input use, income) published yet; independent measurement under way.
cost_anchor: 'As of September 2026: free tier for smallholders (limited credits and hectares, no data plan
  required); farmers tiered by farm size; programmes and enterprise quoted per engagement from published day
  rates; developers usage-based; hardware (where deployed) a yearly subscription with the first year included.
  A typical public-sector first module is a fixed lump sum against a defined deliverable list, then a capped
  monthly pilot support line, then metered steady-state usage. Per-unit rates in local currency, no external
  hard-currency API bill in the path. Hosting choice, local protocol and knowledge content build, and each
  additional voice language move the total materially.'
build_effort: Not documented in the source at a whole-deployment level. Development compute was accelerated
  through the AI Hub for Sustainable Development's Compute Accelerator Programme and CINECA's Leonardo supercomputer;
  production inference, monitoring, and maintenance require separately funded operating budgets.
downstream_adoptions:
- Agrivi (Croatia) — commercial agreement signed at GITEX
- Hassad Food — enterprise API integration
- Local companies in Africa and Europe building products on the model layer
- Senegal pilot — NGO consortium plus the national meteorological agency, 5,000 rice and millet farmers, French
  and Wolof
- SoilPulse — active field pilot
- 'Reuse accelerators named by the source: coverage-by-curation (no retraining for new crops or conditions),
  a published interface schema, a pre-registered evaluation protocol, and reusable institutional documents
  (terms of reference, data-ownership table, hosting-option framework)'
coverage:
  persona:Explore: 3
  persona:Define: 3
  persona:Pilot: 2
  persona:Scale: 2
  solution:Explore: 3
  solution:Define: 3
  solution:Pilot: 2
  solution:Scale: 2
  institution:Explore: 2
  institution:Define: 3
  institution:Pilot: 3
  institution:Scale: 2
  ecosystem:Explore: 2
  ecosystem:Define: 3
  ecosystem:Pilot: 3
  ecosystem:Scale: 2
gaps:
- 'Persona × Pilot — advice comprehension and action evidence (relates to Units 1, 2): the Senegal pilot serves
  5,000 rice and millet farmers in French and Wolof, but whether they understood the advice and acted on it
  is not documented; no consented case-log or action-taken data is surfaced.'
- 'Persona × Scale — user-segment variation across integrations (relates to Unit 3): the 4.78 million weekly-active-user
  figure aggregates integrations, languages, crops and geographies; how service quality, resolution rates
  or escalation patterns vary across those segments, and how that is tracked, is not documented.'
- 'Solution × Pilot — component failure taxonomy (relates to Units 5, 6): known risk categories are named
  (weak imagery, out-of-distribution cases, local treatment constraints, delayed human review), but no pilot-stage
  taxonomy separating model, data, integration and scope failures, and no before/after on a specific component
  fix in the Senegal or Morocco pilots.'
- 'Solution × Scale — data SLAs with external suppliers (relates to Unit 6): whether formal service-level agreements
  govern the satellite, hyperlocal weather and soil suppliers at scale, and what happens when those sources
  go stale or unavailable, is not documented.'
- 'Institution × Scale — absorption indicators (relates to Units 8, 9): steady state is specified (named operator,
  staffed review rota, operating budget line, curation owner) and escalation standardisation across deployments
  is unfinished; whether any deployment has formally crossed into steady state is not documented.'
- 'Ecosystem × Explore — precedent deployments and what transferred (relates to Unit 11): what prior adopters
  in adjacent geographies learned, and how the Senegal NGO consortium and meteorological agency arrangement
  was formed and precedent-checked, is not documented.'
- 'Ecosystem × Scale — compute resilience and regional GPU availability (relates to Unit 12): commercial serving
  depends on one cloud provider''s GPU families, not available in every region; whether a second provider
  or fallback compute arrangement exists is not documented.'
deploying_organisations:
- credit-agricole-du-maroc
corpora:
- grounding-corpus
doc_refs:
- content/wiki/pathways/ai-crop-diagnosis-advisory.md
lifecycle: unindexed
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/ai-crop-diagnosis-advisory.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-crop-diagnosis-advisory.md Sections 1–2 (identity, effort, coverage grid,
    gaps)
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: use_case_category paraphrased from the document title and summary; partner_organisations undp-ai-hub
    matched from "AI Hub for Sustainable Development's Compute Accelerator Programme" (Section 1, build effort)
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

An agentic agricultural Vision-Language Model that orchestrates narrow AI models and live satellite, weather, soil, and telemetry data to return grounded crop-health assessments — deployed through cooperatives, banks, and agritech platforms across Morocco, Senegal, Croatia, and beyond.

Contributed by: [DeepLeaf](../organisations/deepleaf.md).

According to DeepLeaf's account, the system returns assessments with confidence and abstention, agronomist review, and national pesticide-registry checks. It is delivered through direct channels and through embedded API, SDK and white-label integrations, so the deploying institution keeps its brand and farmer relationship while DeepLeaf supplies the technology layer. It originated in Morocco and has expanded through institutional and commercial integrations; the stage reached is [Pilot](../concepts/pilot.md).

- **Geography:** origin Morocco; deployments in Senegal, Croatia, and multiple countries in Africa and Europe.
- **Population served:** smallholder farmers and commercial agricultural operations, reached through cooperatives, banks, input companies, agritech platforms and government programmes.
- **Scale (as of September 2026):** 4.78 million weekly active users (internally validated, subject to final validation before publication). Separately, 500,000 farmers have *access* through the Crédit Agricole du Maroc white-label deployment — the document is explicit that this is not active use. No measured impact figure (yield, input use, income) is published yet; independent measurement is under way.
- **Applies when:** a trusted farmer-facing or enterprise channel exists with local crop, language and agronomic content; the gap is diffusion of already-validated agronomic knowledge, not a shortage of it; the institution can staff qualified agronomists in-jurisdiction to review before advice reaches a farmer; data rights, consent, review responsibility, export provisions and a recurring operating budget are in place or committable.
- **Does not transfer when:** the gap is genuinely a knowledge gap (retrieval-based grounding needs something real to retrieve), or the institution cannot staff or contract qualified agronomists accountable for review in-jurisdiction.
- **Key dates:** document as of August 2026; follow-up answers September 2026.

## Effort

- **Build effort:** not documented in the source at a whole-deployment level. Development compute was accelerated through the AI Hub for Sustainable Development's Compute Accelerator Programme and CINECA's Leonardo supercomputer; production inference, monitoring and maintenance need separately funded operating budgets.
- **Cost anchor (as of September 2026):** a free tier for smallholders; farmers tiered by farm size; programmes and enterprise quoted per engagement from published day rates; developers usage-based; hardware, where deployed, a yearly subscription with the first year included. A typical public-sector first module is a fixed lump sum against a defined deliverable list, then a capped monthly pilot support line, then metered steady-state usage. Rates are in local currency with no external hard-currency API bill. Hosting choice, local protocol and knowledge content build, and each additional voice language move the total materially.
- **Downstream adoptions:** Agrivi (Croatia, commercial agreement signed at GITEX); Hassad Food (enterprise API integration); local companies in Africa and Europe building on the model layer; the Senegal pilot (NGO consortium plus the national meteorological agency, 5,000 rice and millet farmers, French and Wolof); an active SoilPulse field pilot. The document credits reuse to coverage-by-curation, the published interface schema, the pre-registered evaluation protocol, and the reusable institutional documents.

## Coverage

From the document's own Section 2 coverage map.

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●●● | ●●● | ●● | ●● |
| Solution | ●●● | ●●● | ●● | ●● |
| Institution | ●● | ●●● | ●●● | ●● |
| Ecosystem | ●● | ●●● | ●●● | ●● |

## Gaps

The document names seven open questions:

- **Persona × Pilot — advice comprehension and action.** Whether the Senegal farmers understood the advice and acted on it is not documented; no consented case-log or action-taken data is surfaced.
- **Persona × Scale — variation across integrations.** How service quality, resolution and escalation vary across the integrations, languages, crops and geographies behind the weekly-active-user figure is not documented.
- **Solution × Pilot — component failure taxonomy.** Risk categories are named, but there is no taxonomy separating model, data, integration and scope failures, and no before/after on a specific component fix.
- **Solution × Scale — data SLAs.** Whether formal SLAs govern the satellite, weather and soil suppliers, and what happens when they go stale or unavailable, is not documented.
- **Institution × Scale — absorption indicators.** Steady-state criteria are specified and escalation standardisation is unfinished; whether any deployment has crossed into steady state is not documented.
- **Ecosystem × Explore — precedent.** What prior adopters in adjacent geographies learned, and how the Senegal consortium arrangement was formed, is not documented.
- **Ecosystem × Scale — compute resilience.** Serving depends on one cloud provider's GPU families, not available in every region; whether a fallback exists is not documented.

## Where the reusable value is

According to DeepLeaf, value concentrates at [Solution](../concepts/solution.md) × Define, [Institution](../concepts/institution.md) × Define and [Ecosystem](../concepts/ecosystem.md) × Define, and the operating-model and continuity units transfer unusually well because they were designed to outlive the original deployer. The document's 30/70 note: seven institutional changes were needed inside every partner, and a deployment stalls without all seven however capable the model is.

- **Persona:** [define the persona by the advice gap](../units/ai-crop-diagnosis-advisory-persona-by-advice-gap.md), [name the workaround first](../units/ai-crop-diagnosis-advisory-name-the-workaround-first.md), [separate access from active use](../units/ai-crop-diagnosis-advisory-separate-access-from-active-use.md).
- **Solution:** [curated retrieval over fine-tuning](../units/ai-crop-diagnosis-advisory-curated-retrieval-over-fine-tuning.md), [abstention and confidence as outputs](../units/ai-crop-diagnosis-advisory-abstention-and-confidence-as-outputs.md), [separate data layer with named owners](../units/ai-crop-diagnosis-advisory-separate-data-layer-named-owners.md).
- **Institution:** [seven institutional changes before signing](../units/ai-crop-diagnosis-advisory-seven-institutional-changes-before-signing.md) (playbook), [agronomist owns content authority](../units/ai-crop-diagnosis-advisory-agronomist-owns-content-authority.md), [operating model that survives the founders](../units/ai-crop-diagnosis-advisory-operating-model-survives-founders.md).
- **Ecosystem:** [publish the interface schema first](../units/ai-crop-diagnosis-advisory-publish-interface-schema-first.md), [pre-register the evaluation protocol](../units/ai-crop-diagnosis-advisory-pre-register-evaluation-protocol.md), [hosting as a governance decision](../units/ai-crop-diagnosis-advisory-hosting-as-governance-decision.md).
- **Toolkit:** [data-ownership table template](../units/ai-crop-diagnosis-advisory-data-ownership-table-template.md), [hosting-option framework](../units/ai-crop-diagnosis-advisory-hosting-option-framework.md). The document's other toolkit rows — the seven-change checklist, the evaluation protocol template, the institutional document set and the interface schema — are covered by the units above.

The document has no Section 5, so no problem→solution pattern is recorded.

## Corpus copies

- `content/wiki/pathways/ai-crop-diagnosis-advisory.md`

On disk in the grounding corpus but **not linked from `content/wiki/pathways/index.md`**, so excluded from grounding and the /wiki listing. It may still be live via `published_pathways` — check the DB before calling it unpublished.
