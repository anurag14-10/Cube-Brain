---
name: Voice AI for Inclusion
type: pathway
schema_version: 2
aliases:
- Voice AI for Inclusion
- Voice AI — Cross-Deployment Synthesis — Multi-Geography
summary: A cross-deployment synthesis of what MahaVISTAAR, Bharat Vistaar, Amul/Sarlaben, Jal Jeevan Mission
  Assam, the Bhili effort, Lend A Hand, and the India–Africa exchange learned in common about reaching
  people digital services routinely miss.
tags:
- Voice AI
- Cross-Sector
- Synthesis
title: Voice AI for Inclusion
pathway_kind: cross-deployment-synthesis
sector: Cross-Sector
stage_reached: scale
use_case_category: Voice AI service channels for populations excluded by literacy, language, device access
  or connectivity (agriculture advisory, water-service feedback, dairy, skilling/livelihoods)
geography: India (Maharashtra, Assam, Gujarat) plus the India–Africa exchange
population_served: Female farmers, feature-phone users, Indic-language speakers, migrant labourers, rural
  households — populations excluded by literacy, language, device access, or connectivity from existing
  digital service channels
contributing_organisations:
- ekstep-foundation
deploying_organisations:
- maharashtra-department-of-agriculture
- gcmmf-amul
- crane-ai-labs
- jal-jeevan-mission-assam
- lend-a-hand
key_dates: As of July 2026
scale_impact: 'As of mid-2026: MahaVISTAAR 342K+ unique users, 1.67M+ questions answered, 17 lakh farmers/day
  via proactive alerts; Amul/Sarlaben 3.6M farmers, launched in 3 weeks. Compression across the pattern:
  9 months (MahaVISTAAR, from scratch) → 3 months (Ethiopia ATI) → 3 weeks (Amul/Sarlaben).'
cost_anchor: 'As of Jul 2026: ~$250K setup, ~$250K/year at MahaVISTAAR''s scale — an order-of-magnitude
  anchor across the pattern, not a single deployment''s precise figure. Per-minute telephony: ~₹0.5–1.5/min
  open self-hosted once earned at scale, ₹2.5–4.5/min fully managed commercial platform (the realistic
  start), above ₹6/min for a human-only call centre. Call duration and concurrency move the bill more
  than the per-minute rate; the number of languages barely moves it.'
build_effort: 'Varies by deployment; the compression pattern is the finding — 9 months (MahaVISTAAR, built
  from scratch) → 3 months (Ethiopia''s ATI, drawing on MahaVISTAAR''s architecture) → 3 weeks (Amul/Sarlaben,
  drawing on two full cycles of shared learning).'
synthesises:
- mahavistaar
- unififed-ai-driven-agri-ecosystem
- ai-advisory-for-dairy-farmers
- bhili-language-enablement
- african-voice-ai
related_pathways:
- voice-ai-adoption-barriers
coverage:
  persona:Explore: 3
  persona:Define: 1
  persona:Pilot: 2
  persona:Scale: 1
  solution:Explore: 2
  solution:Define: 3
  solution:Pilot: 1
  solution:Scale: 1
  institution:Explore: 1
  institution:Define: 2
  institution:Pilot: 2
  institution:Scale: 1
  ecosystem:Explore: 0
  ecosystem:Define: 1
  ecosystem:Pilot: 1
  ecosystem:Scale: 2
gaps:
- No single, precise per-deployment cost breakdown is given for most of the seven source deployments —
  the per-minute figures are a synthesised range across them, not a confirmed number for any one. (Solution/Explore)
- No documented method for confirming, rather than inferring, that a given deployment has genuinely reached
  the workforce-capability outcome described in Unit 5, versus dependency — the interview names the marker
  (who does daily QA) but not a scoring method. (Institution/Pilot)
- The India–Africa reverse-technology-transfer claim referenced in this pathway's own source material
  is explicitly unverified at the time of writing — carried through here as a direction worth testing,
  not a settled fact (see the African Voice AI pathway in this corpus for the fuller, appropriately-hedged
  treatment). (Ecosystem/Scale)
- No consolidated, single list of which of the seven source deployments have published their own reusable
  toolkits versus which remain internal-only. (Ecosystem/Scale)
contested:
- field: cost_anchor
  readings:
  - 'grounding corpus (content/wiki/pathways/voice-ai-for-inclusion.md): "an order-of-magnitude anchor
    across the pattern, not a single deployment''s precise figure" (as of Jul 2026)'
  - 'library corpus (content/library-wiki/pathways/voice-ai-for-inclusion.md): "an order-of-magnitude anchor,
    not a voice-specific benchmark" (mid-2026)'
  note: Same figures, different qualifier on what the anchor means; the entry carries the grounding wording.
- field: key_dates
  readings:
  - 'grounding corpus: frontmatter timestamp 2026-08-31; Section 1 "As of July 2026"'
  - 'library corpus: frontmatter timestamp 2026-07-26'
  note: Document dates differ between the two copies; neither is a deployment date.
partner_organisations:
- bhashini
- ethiopia-ati
corpora:
- grounding-corpus
- library-corpus
doc_refs:
- content/wiki/pathways/voice-ai-for-inclusion.md
- content/library-wiki/pathways/voice-ai-for-inclusion.md
lifecycle: published
published_on: '2026-07-31'
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/voice-ai-for-inclusion.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/library-wiki/pathways/voice-ai-for-inclusion.md
- system: github_repo
  method: derived
  date: '2026-10-08'
  ref: published_on = date content/wiki/pathways/voice-ai-for-inclusion.md was first committed
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/voice-ai-for-inclusion.md — Sections 1–2 (identity, effort) and Section 3 units
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/voice-ai-for-inclusion.md — related_pathways (its "Related pathways"
    line) and the contested readings
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: synthesises = the source deployments named in Sections 0–1 that exist as pathways here (Bharat Vistaar
    is the slug unififed-ai-driven-agri-ecosystem; Amul/Sarlaben is ai-advisory-for-dairy-farmers; the
    India–Africa exchange is african-voice-ai); deploying_organisations = the source-deployment organisations
    Section 1 names that exist here; use_case_category paraphrased from Sections 0–1
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

A cross-deployment synthesis of what MahaVISTAAR, Bharat Vistaar, Amul/Sarlaben, Jal Jeevan Mission Assam, the Bhili effort, Lend A Hand, and the India–Africa exchange learned in common about reaching people digital services routinely miss.

Contributed by: EkStep Foundation (synthesis), drawn from a structured interview with EkStep Foundation's Lead for Voice and Language AI. According to the pathway, its source deployments are [MahaVISTAAR](mahavistaar.md) (Department of Agriculture, Government of Maharashtra), [Bharat Vistaar](unififed-ai-driven-agri-ecosystem.md), [Amul/Sarlaben](ai-advisory-for-dairy-farmers.md), Jal Jeevan Mission Assam, the [Bhili language effort](bhili-language-enablement.md), Lend A Hand, and the India–Africa exchange with Crane AI Labs ([African Voice AI](african-voice-ai.md)).

- **Sector:** Cross-Sector (agriculture, water services, dairy, skilling/livelihoods)
- **Geography:** India (Maharashtra, Assam, Gujarat) plus the India–Africa exchange
- **Population served:** female farmers, feature-phone users, Indic-language speakers, migrant labourers, rural households — people excluded by literacy, language, device access or connectivity from existing digital service channels
- **Stage reached:** Scale — synthesised from deployments spanning Explore through Scale
- **Scale (as of mid-2026):** MahaVISTAAR 342K+ unique users, 1.67M+ questions answered, 17 lakh farmers/day via proactive alerts; Amul/Sarlaben 3.6M farmers, launched in 3 weeks
- **Key dates:** as of July 2026

Read it when the question is whether voice is even the right channel and what to watch for regardless of which deployment you most resemble; read [MahaVISTAAR](mahavistaar.md) or [Bhili](bhili-language-enablement.md) for one deployment's own detail. It documents what recurred across teams deciding independently — which the pathway treats as a stronger signal that a lesson generalises. Related: [Voice AI Adoption Barriers](voice-ai-adoption-barriers.md) (named in the library copy).

## Effort

- **Cost anchor (as of Jul 2026):** ~$250K setup, ~$250K/year at MahaVISTAAR's scale — an order-of-magnitude anchor across the pattern, not a single deployment's precise figure. Per-minute telephony runs roughly ₹0.5–1.5/minute on an open self-hosted stack once earned at scale, ₹2.5–4.5/minute on a fully managed commercial platform (the realistic starting point for most adopters), and above ₹6/minute for a human-only call centre. Call duration and concurrency move the bill more than the per-minute rate; the number of languages barely moves it.
- **Build effort:** varies by deployment; the compression pattern is the finding — 9 months (MahaVISTAAR, from scratch) → 3 months (Ethiopia's ATI, drawing on MahaVISTAAR's architecture) → 3 weeks (Amul/Sarlaben, drawing on two full cycles of shared learning).
- **Downstream adoptions:** none documented for this pathway itself — the document describes it as downstream of the deployments it synthesises, written for a next, not-yet-started deployment to read before choosing an architecture.

## Coverage

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●●● | ● | ●● | ● |
| Solution | ●● | ●●● | ● | ● |
| Institution | ● | ●● | ●● | ● |
| Ecosystem | ○ | ● | ● | ●● |

## Gaps

- No single, precise per-deployment cost breakdown is given for most of the seven source deployments — the per-minute figures are a synthesised range across them, not a confirmed number for any one. (Solution/Explore)
- No documented method for confirming, rather than inferring, that a given deployment has genuinely reached the workforce-capability outcome described in Unit 5, versus dependency — the interview names the marker (who does daily QA) but not a scoring method. (Institution/Pilot)
- The India–Africa reverse-technology-transfer claim referenced in this pathway's own source material is explicitly unverified at the time of writing — carried through here as a direction worth testing, not a settled fact (see the African Voice AI pathway in this corpus for the fuller, appropriately-hedged treatment). (Ecosystem/Scale)
- No consolidated, single list of which of the seven source deployments have published their own reusable toolkits versus which remain internal-only. (Ecosystem/Scale)

## Where the reusable value is

According to EkStep Foundation's synthesis, the reusable value concentrates in the architecture and institutionalisation units. Eight units, one per micro-innovation in Section 3:

- **Persona × Explore** — [Name the excluded person precisely, not the demographic](../units/voice-ai-for-inclusion-name-the-excluded-person.md) (Strategic Decision)
- **Persona × Pilot** — [Two-bar prototype-to-pilot readiness test](../units/voice-ai-for-inclusion-two-bar-pilot-readiness-test.md) (Playbook — the technical bar, then the "reason to stay on the line" bar)
- **Solution × Explore** — [Price against the managed platform you will start on](../units/voice-ai-for-inclusion-price-against-managed-platform.md) (Strategic Decision)
- **Solution × Define** — [Shortlist and test multiple vendors in parallel during the pilot](../units/voice-ai-for-inclusion-parallel-multi-vendor-pilot.md) (Playbook, with the government sandbox pattern)
- **Solution × Define** — [Invest in open orchestration as shared infrastructure](../units/voice-ai-for-inclusion-open-orchestration-as-infrastructure.md) (Strategic Decision)
- **Institution × Define** — [Design for refusal, not just for response](../units/voice-ai-for-inclusion-design-for-refusal.md) (Strategic Decision)
- **Institution × Pilot** — [The sign of institutionalisation is who does the daily quality checks](../units/voice-ai-for-inclusion-who-does-daily-quality-checks.md) (Strategic Decision)
- **Ecosystem × Scale** — [Voice opens the door, other channels may complete the journey](../units/voice-ai-for-inclusion-voice-within-multichannel-service.md) (Strategic Decision)

Section 4's third row, the Voicera orchestration platform, is already in the brain as the MahaVISTAAR Toolkit Asset [Voiceera open-source orchestration platform](../units/mahavistaar-voiceera-orchestration-platform.md); it is linked from the orchestration unit rather than duplicated. The document has no Section 5, so no problem-solution pattern was extracted.

## Corpus copies

- `content/wiki/pathways/voice-ai-for-inclusion.md`
- `content/library-wiki/pathways/voice-ai-for-inclusion.md`

Exists in **both** in-repo corpora as independently maintained documents — same slug, different text.
