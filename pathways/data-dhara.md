---
name: AI for Government Data Interoperability — National
type: pathway
schema_version: 2
aliases:
- AI for Government Data Interoperability — National
- Data DHARA
summary: A horizontal data-unlock pathway (Data DHARA) turning fragmented, siloed government records into
  coordinated, machine-readable systems — illustrated through Nivesh Suvidha (Invest UP) and three sibling
  deployments.
tags:
- Data Infrastructure
- Governance
title: AI for Government Data Interoperability — National
pathway_kind: horizontal-enabler
sector: Data Infrastructure
use_case_category: Government data interoperability — unlocking fragmented departmental records for AI
  in citizen and investor services
geography: India — Uttar Pradesh (Invest UP's Nivesh Suvidha and UPSIDA) and Delhi (vital statistics),
  plus a data-for-exports pathway for first-time MSME exporters
population_served: In the focus deployment (Nivesh Suvidha), investors setting up business in Uttar Pradesh
  and Udyami Mitras (investment facilitation officers) across 75 districts
stage_reached: define
deploying_organisations:
- invest-up
partner_organisations:
- ekstep-foundation
- people-plus-ai
- anthropic
- amazon-web-services
- kenpath-technologies
key_dates: August 2025 — workshop at EkStep's Bangalore office brings Invest UP leadership, the Udyami
  Mitra team and ecosystem players together; November 2025 — MoU; January 2026 — SOW; ~March 2026 — live
  pilot with 20 Udyami Mitras
scale_impact: Live pilot with 20 Udyami Mitras (as of ~March 2026); four sibling pathways have emerged
  from pilots. No usage or outcome figures documented
build_effort: Nivesh Suvidha took roughly 3–4 months from MoU (November 2025) to SOW (January 2026) to
  a live pilot (~March 2026)
synthesises:
- nivesh-suvidha
related_pathways:
- blue-dots
- ceew-climate-intelligence
corpora:
- library-corpus
doc_refs:
- content/library-wiki/pathways/data-dhara.md
lifecycle: published
published_on: '2026-09-01'
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/library-wiki/pathways/data-dhara.md
- system: github_repo
  method: derived
  date: '2026-10-08'
  ref: published_on = date content/library-wiki/pathways/data-dhara.md was first committed
- system: diffusion_cube_code
  method: derived
  date: '2026-10-08'
  ref: sector inferred from title/tags; document states none
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/data-dhara.md — Overview, Institution, Ecosystem and Operating Model
    sections (identity, partners, dates, effort)
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

According to the Data DHARA pathway, Data DHARA is a horizontal enabler pathway, not a single deployment: each implementation solves a local use case while producing reusable technical assets and non-technical know-how that lower cost and uncertainty for every later adopter. Its thesis is that AI adoption in citizen delivery systems is blocked less by absence of data than by absent institutional pathways (governance, inter-departmental coordination and operational trust) that turn fragmented information into coordinated, machine-readable systems.

Four sibling pathways have emerged from pilots:

| Pathway | Issue | Reusable asset |
|---|---|---|
| Delhi vital statistics → health outcomes | Vital-statistics data locked in departmental PDFs, not linkable across health, nutrition and education systems | Cross-department linkage playbook, harmonisation/linkage toolkit, AI-readiness dataset score |
| Invest UP — Nivesh Suvidha | Investment policy intelligence fragmented across 45 UP departments; ~15,000 investor queries backlogged | Document taxonomy, metadata schema, a chatbot answering policy, scheme and land questions with traceability to source documents |
| Invest UP — UPSIDA | Manual, hard-to-audit land-allotment scoring across 43 investor-facing services | Seven reusable use-case categories |
| Data for exports (first-time MSME exporters) | Trade, registry and compliance data fragmented, English-only and priced for large exporters | Schema-normalised, multilingual trade and registry datasets |

The document focuses on [Nivesh Suvidha](nivesh-suvidha.md), the sub-pathway with the most detailed interview material.

- **Sector:** Data Infrastructure (inferred; the document states none)
- **Geography:** India — Uttar Pradesh (Nivesh Suvidha, UPSIDA) and Delhi (vital statistics)
- **Population served:** In Nivesh Suvidha, investors setting up business in Uttar Pradesh and Udyami Mitras (investment facilitation officers) across 75 districts
- **Stage reached:** [Define](../concepts/define.md), as the document's frontmatter states
- **Key dates:** August 2025 workshop at EkStep's Bangalore office; November 2025 MoU; January 2026 SOW; live pilot with 20 Udyami Mitras around March 2026

Contributed by: not stated in the document. Named roles in Nivesh Suvidha: Invest UP (nodal institution, under UP's Infrastructure & Industrial Development Department; supplies and validates data), Kenpath Technologies (vendor; builds and maintains the tools, pipeline, chatbot and telemetry), EkStep / People+AI (AI expertise; own the reusable DPG layer), Anthropic (model supplier), the 26 Nivesh Mitra issuing departments (indirect contributors through their process-flow documents) and Udyami Mitras across 75 districts (frontline users). AWS was used during the build phase.

**Where this pathway doesn't apply.** Where an institution is unwilling to name a nodal owner for data, or where the underlying data genuinely does not exist yet (rather than existing but fragmented, siloed or PDF-locked).

## Effort

- **Scale / impact achieved:** A live pilot with 20 Udyami Mitras (around March 2026); four sibling pathways have emerged from pilots. No usage or outcome figures are documented.
- **Cost anchor:** Not documented in the source. The named cost drivers are cloud cost and LLM (Claude credit) usage, the latter being where costs unexpectedly increased.
- **Build effort:** Roughly 3–4 months for Nivesh Suvidha from MoU (November 2025) to SOW (January 2026) to live pilot (around March 2026).
- **Downstream adoptions:** Not documented in the source.

## Coverage

The library document is a conversational overview organised by theme and stage; it carries no density grid, so `coverage` is left blank. Several cells are stated as not distinctly documented (Workforce at Explore and Define, Operating Model at Explore).

## Gaps

The document names no gaps. Its own list of drawbacks of AI adoption at state scale is the closest thing to open questions: no internal digital-transformation leadership; a capacity-building gap for 0-to-1 deployment; dependency on SIs, consultants and vendors with no capability transfer; vendor procurement that ties institutions to poor performers with no easy exit; vendors going "out of sight, out of mind" after the engagement with no SLAs; and poor access to appropriate data, with no central repositories or ownership structures.

## Where the reusable value is

Twelve units. The library document does not number its micro-innovations, so the units carry no `source_unit_id` and their tags are a best-effort reading against the framework. The document has no Section 5, so there are no patterns.

- **Make the data AI-ready.** The [AI-readiness document schema](../units/data-dhara-ai-readiness-document-schema.md) (Solution × Explore), the [staged data-unlock pipeline from departmental PDFs to agent access](../units/data-dhara-staged-data-unlock-pipeline.md) (Solution × Pilot) and UPSIDA's [seven reusable AI use-case categories](../units/data-dhara-upsida-ai-use-case-categories.md) (Solution × Explore).
- **Hosting and data posture.** [Build on public cloud for speed, then migrate to the institution's own cloud](../units/data-dhara-hybrid-hosting-build-then-migrate.md) (Solution × Define) and [use only public, institution-owned data with revocable vendor access](../units/data-dhara-public-data-revocable-vendor-access.md) (Institution × Pilot).
- **Ownership and momentum.** [Name a nodal officer for data sourcing before work begins](../units/data-dhara-name-nodal-officer-before-work.md) (Institution × Pilot) and [build iteratively instead of waiting for a complete policy repository](../units/data-dhara-iterate-instead-of-waiting-for-repository.md) (Institution × Define).
- **People and judgment.** [Let use be the training for the first frontline cohort](../units/data-dhara-use-as-training-pilot-cohort.md) and [design the AI as an advisory layer, with judgment staying with officers](../units/data-dhara-advisory-layer-judgment-stays-human.md) (Institution × Pilot).
- **Sustaining it.** [Plan the post-pilot steady state around LLM cost and knowledge-repo upkeep](../units/data-dhara-plan-steady-state-operations.md) (Institution × Pilot) and [budget explicitly for the capacity-building gap](../units/data-dhara-budget-for-capacity-building.md) (Institution × Scale).
- **How the value travels.** [Package every engagement as a technical toolkit plus the non-technical mechanisms](../units/data-dhara-two-component-engagement-packaging.md) (Ecosystem × Scale). The document puts the non-technical part at roughly 70% of the value.

The [Nivesh Suvidha](nivesh-suvidha.md) pathway gives a separate, framework-structured account of the same deployment, and several of its units overlap with these.

## Corpus copies

- `content/library-wiki/pathways/data-dhara.md`

Library corpus only, a conversational overview grounded one document at a time behind the public Diffusion Library.
