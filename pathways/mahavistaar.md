---
name: MahaVISTAAR
type: pathway
schema_version: 2
aliases:
- MahaVISTAAR
- Voice AI for Farmer Advisory — Maharashtra
summary: Maharashtra's state-run AI voice advisory for smallholder farmers — federated data ownership,
  provider abstraction that paid for itself 180x over, and the institutional authorisation work that had
  to happen before any code was written.
tags:
- Voice AI
- Agriculture
- Government
title: MahaVISTAAR
pathway_kind: single-deployment
sector: Agriculture
use_case_category: voice-first government advisory (crop advisory, pest management, market pricing, government
  scheme access, grievance tracking)
geography: Maharashtra, India — federated nationally as Bharat-VISTAAR after state-level proof
population_served: Smallholder farmers in Maharashtra — primarily Marathi-speaking, feature-phone users
  with limited literacy and no reliable internet; specifically, women farmers in Marathwada whose land
  is titled to their husbands but who make the actual crop decisions, and who rely on small trust circles
  rather than agriculture offices
stage_reached: scale
contributing_organisations:
- maharashtra-department-of-agriculture
- ekstep-foundation
- openagrinet
deploying_organisations:
- maharashtra-department-of-agriculture
key_dates: 'Nov 2025: initial production deployment on Azure OpenAI (216,000 queries at ~₹9.4/question);
  later self-hosted migration brought cost to ~₹0.05/question; national federation (Bharat-VISTAAR) announced
  in the Union Budget 2026–27'
scale_impact: 'As of mid-2026: 342K+ unique users; 1.67M+ farmer questions answered; 791K+ sessions; 17
  lakh farmers reached daily via proactive voice alerts; 97–98.5% positive feedback'
cost_anchor: 'As of mid-2026: ~$250K setup and ~$250K/year run-rate at scale (an order-of-magnitude anchor,
  not a precise benchmark); inference cost fell 180x, ₹9.4 → ₹0.05 per question, after moving off Azure
  OpenAI to a self-hosted fine-tuned Qwen3.5-27B; the self-hosted 16-GPU build-out pencils at ~₹2 crore/year
  against a projected ₹18 crore/year on Azure at the same scale'
build_effort: Nine months from scratch with 30 partner organisations and a target population of 3 million
  farmers, with no prior pathway to draw on; data-sharing authorisation across the Department of Agriculture,
  four state agricultural universities, IMD, 307 APMC market committees and the MahaDBT scheme database
  came before any production code, sponsored at Agri-Secretary level with named nodal officers across agriculture,
  IT and field operations
downstream_adoptions:
- Ethiopia's ATI — three months, building on MahaVISTAAR's architecture without rediscovering which field
  choices work
- Amul/Sarlaben (dairy cooperative) — three weeks, drawing on two full cycles of shared learning, launching
  to 3.6 million farmers and 40 million cattle from day one
- Bharat-VISTAAR — the national federation of the same architecture, announced in the Union Budget 2026–27
related_pathways:
- voice-ai-for-inclusion
- bhili-language-enablement
- ai-advisory-for-dairy-farmers
coverage:
  persona:Explore: 3
  persona:Define: 2
  persona:Pilot: 0
  persona:Scale: 1
  solution:Explore: 2
  solution:Define: 3
  solution:Pilot: 3
  solution:Scale: 3
  institution:Explore: 1
  institution:Define: 3
  institution:Pilot: 1
  institution:Scale: 2
  ecosystem:Explore: 1
  ecosystem:Define: 3
  ecosystem:Pilot: 0
  ecosystem:Scale: 3
gaps:
- What did MahaVISTAAR's own pilot reveal about which user interactions succeeded or failed, as distinct
  from the general UX fixes documented later in production (Units 17–19)? (Persona × Pilot — Outcome and
  Success; Scope, Inclusion, and Trust)
- Beyond the raw session count, what decision was made about how to interpret engagement as a signal of
  success at Scale, and what would have changed that interpretation? (Persona × Scale — Outcome and Success)
- Which architecture or model choice actually broke or needed adjustment during the pilot itself, as distinct
  from the production-scale changes documented later (Units 21–25)? (Solution × Pilot — Model, Architecture,
  and Infrastructure)
- Which live data source was found stale, wrong or low-quality during the pilot, and how was it resolved?
  (Solution × Pilot — Data and Knowledge Readiness)
- Are there formal data SLAs or a data-currency governance process at Scale, beyond the four data relationships
  formalised before launch (Unit 38)? (Solution × Scale — Data and Knowledge Readiness)
- What decision, with a real alternative behind it, was made about the operating model before launch, as
  distinct from the cost anchor figures on their own? (Institution × Define — Operating Model and Sustainability)
- What did MahaVISTAAR observe about its own workforce and extension officers during the pilot, as distinct
  from the general design principle set at Define or the farmer-facing onboarding finding (Unit 20)? (Institution
  × Pilot — Workforce and Change)
- Does frontline or extension-officer capability show signs of dependency rather than enhanced capacity
  at scale? (Institution × Scale — Workforce and Change)
- When a farmer receives a wrong answer, what is the actual path from that error to a fix, and who holds
  liability? Named as an open question in the source's own information-gaps list. (Institution × Scale
  — Accountability, Liability, and Compliance)
- Who reviews and refreshes data currency and stewardship on an ongoing cadence at Scale, distinct from
  who is accountable for accuracy at launch (Unit 29)? (Institution × Scale — Data Stewardship)
- Which ecosystem partner underperformed during the pilot, and was a contingency already identified? (Ecosystem
  × Pilot — Resilience, Portability, and Contingencies)
- Have the four Define-stage data relationships (Unit 38) been formalised into SLAs or renegotiated as
  usage scaled? (Ecosystem × Scale — External Data and Infrastructure Dependencies)
partner_organisations:
- voicera
- india-meteorological-department
- icar
- niphm
- microsoft
corpora:
- grounding-corpus
- library-corpus
doc_refs:
- content/wiki/pathways/mahavistaar.md
- content/library-wiki/pathways/mahavistaar.md
lifecycle: published
published_on: '2026-07-31'
contested:
- field: title
  readings:
  - 'grounding corpus: MahaVISTAAR'
  - 'library corpus: Voice AI for Farmer Advisory — Maharashtra'
  note: Same slug, different display titles; the library title is kept as an alias.
- field: document_date
  readings:
  - 'grounding corpus: timestamp 2026-08-31'
  - 'library corpus: timestamp 2026-07-26'
  note: The two copies are maintained independently; the grounding copy is the newer, framework-structured
    one. Recorded, not arbitrated.
- field: build_effort
  readings:
  - 'grounding corpus (Section 2): "a target population of 3 million farmers"'
  - 'library corpus (Overview): "30 partner organisations and 3 million farmers reached"'
  note: Target versus reached. build_effort carries the grounding wording; not arbitrated.
- field: units/mahavistaar-size-incremental-value-gap context
  readings:
  - 'grounding corpus (Unit 3): "Maharashtra''s ~1 field officer per 2,000 farmers"'
  - 'library corpus (Problem × Explore): "roughly one agriculture field officer for every 2,000 farmers in
    comparable states"'
  note: The copies disagree on whether the ratio is Maharashtra's own or that of comparable states. The
    unit follows the grounding copy.
- field: units/mahavistaar-openagrinet-seven-layer-architecture purpose
  readings:
  - 'grounding corpus (Unit 12): Knowledge Engine, Memory Layer, Trust Layer, Agent Core, Action Gateway,
    Reach Layer, Learning Layer'
  - 'library corpus (Technology × Explore): user layer, interface layer, moderation layer, AI decision engine,
    knowledge and scientific models, live data sources, DPI foundation'
  note: Both call it the seven-layer OpenAgriNet design but name different layers. The unit follows the grounding
    copy.
- field: stage (units)
  readings:
  - 'grounding corpus (Section 3 tags): dual-provider fallback routing (Unit 10), WebSocket over WebRTC (Unit
    14), the 500-pattern adversarial test set (Unit 28) and AI-extends-staff framing (Unit 31) at Define;
    the operating model as a staffing question (Unit 34) at Scale; OpenAgriNet architecture and Voiceera
    orchestration (Units 12–13) at Solution × Define; prove state-level, then federate (Unit 42) at Ecosystem
    × Scale'
  - 'library corpus (section placement): the dual-provider principle and WebSocket finding under Technology
    × Pilot; the adversarial test bank under Institution × Pilot; AI extends human capacity under Workforce
    × Pilot; the operating model as staffing under Operating Model × Define; OpenAgriNet and Voiceera under
    Ecosystem × Pilot; national federation under Institution × Scale'
  note: The library copy is organised under its own headings (Problem, Persona, Technology, Institution,
    Ecosystem, Workforce, Operating Model), not the framework's dimensions. The grounding copy is the stronger
    source for framework tags, and the units follow it.
- field: units/mahavistaar-federated-data-ownership context
  readings:
  - 'grounding corpus (Unit 38): four relationships formalised before launch — ICAR, IMD, APMC, NIPHM'
  - 'library corpus (Technology × Define): sources that stay with their owners are ICAR, IMD, APMC, NIPHM
    and the AgriStack farmer registry'
  note: Possibly not a conflict (formalised relationships versus sources left with their owners), but the
    library copy names AgriStack and the grounding copy does not.
- field: coverage persona:Pilot
  readings:
  - 'grounding corpus: Persona × Pilot is empty in the grid and named as a gap'
  - 'library corpus (Persona × Pilot): persona validation happened through the staged testing plan rather
    than as a separate workstream'
  note: coverage is carried from the grounding grid only.
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/library-wiki/pathways/mahavistaar.md
- system: github_repo
  method: derived
  date: '2026-10-08'
  ref: published_on = date content/wiki/pathways/mahavistaar.md was first committed
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/mahavistaar.md — Sections 1–2 (identity, effort, downstream adoptions, coverage
    grid, gaps), Sections 3–4 audited against units
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/mahavistaar.md — compared for the contested readings, the "where this
    pathway doesn't apply" note and its related-pathway line
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: deploying_organisations = maharashtra-department-of-agriculture, from "state-run" / "government-run"
    in Sections 0–1 and Unit 27 (the bot speaks as the Department); related_pathways ai-advisory-for-dairy-farmers
    = the Amul/Sarlaben downstream adoption named in Section 2
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

According to the pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, MahaVISTAAR is a voice line (155313) that gives Maharashtra's smallholder farmers crop advisory, weather, mandi prices and scheme access in Marathi. It does this by federating data from seven institutions behind one government-backed voice. The bot, Vasudha, speaks as the Department of Agriculture. Ethiopia's ATI and the Amul/Sarlaben dairy cooperative have since replicated it, each faster than the one before.

- **Geography:** Maharashtra, India, federated nationally as Bharat-VISTAAR after state-level proof.
- **Who it serves:** smallholder farmers in Maharashtra, mostly Marathi-speaking feature-phone users with limited literacy and no reliable internet. The pathway names one group in particular: women farmers in Marathwada whose land is titled to their husbands but who make the crop decisions, and who rely on small trust circles rather than agriculture offices.
- **Stage reached:** [Scale](../concepts/scale.md). The service is live and government-run, and the Union Budget 2026–27 announced national federation.
- **Use case:** crop advisory, pest management, market pricing, government scheme access and grievance tracking, all through a voice call on any phone.
- **Where it applies (library copy):** strongest where users depend on feature phones and speak Indic languages, institutional credibility is a trust asset, and the data already exists in fragmented institutional form. Weaker where users already have smartphones and text literacy, government credibility is contested, or the goal is internal efficiency rather than last-mile inclusion.

Contributed by: Department of Agriculture, Government of Maharashtra; EkStep Foundation; OpenAgriNet (OAN).

## Effort

- **Cost anchor (as of mid-2026):** about $250K to set up and about $250K a year at scale, an order-of-magnitude figure rather than a precise benchmark. Inference cost fell 180× (₹9.4 → ₹0.05 per question) after moving off Azure OpenAI to a self-hosted, fine-tuned Qwen3.5-27B. Input tokens were 79.7% of spend, so prefix caching was the real cost lever. The self-hosted 16-GPU build-out comes to roughly ₹2 crore a year, against a projected ₹18 crore a year on Azure at the same scale.
- **Build effort:** nine months from scratch, with 30 partner organisations and a target population of 3 million farmers. It was the first deployment of its kind in this ecosystem. Data-sharing authorisation came before any production code, across the Department of Agriculture, four state agricultural universities, IMD, 307 APMC market committees and MahaDBT. An Agri-Secretary-level sponsor and named nodal officers drove it.
- **Vendor strategy:** three voice-AI vendors ran in parallel on a configurable traffic split. The better vendor emerged from live competition rather than from a one-time evaluation, at 2–5% above single-vendor pricing. The same discipline helped when, after about six months, the department realised it also needed outbound calling, which needed different technology (one-way IVR rather than a two-way conversational stack). The original RFP had missed this.
- **Scale (as of mid-2026):** 342K+ unique users, 1.67M+ questions answered, 791K+ sessions, 17 lakh farmers reached daily by proactive voice alerts, and 97–98.5% positive feedback.
- **Key dates:** the first production deployment on Azure OpenAI in November 2025 (216,000 queries at ~₹9.4 a question), then the self-hosted migration (~₹0.05 a question), then the national federation announced in the Union Budget 2026–27.
- **Downstream:** Ethiopia's ATI took three months, building on the architecture. Amul/Sarlaben ([pathway](ai-advisory-for-dairy-farmers.md)) took three weeks, drawing on two cycles of shared learning, and launched to 3.6 million farmers and 40 million cattle. Bharat-VISTAAR federates the same architecture nationally.

The library copy differs on a few figures and placements (see `contested`).

## Coverage

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●●● | ●● | ○ | ● |
| Solution | ●● | ●●● | ●●● | ●●● |
| Institution | ● | ●●● | ● | ●● |
| Ecosystem | ● | ●●● | ○ | ●●● |

From the document's own grid. Solution is dense at every stage after Explore. Persona × Pilot and Ecosystem × Pilot are empty, and both are named in the gaps.

## Gaps

The document names twelve open questions. They fall into four groups:

- **Pilot-stage evidence is thin:** what the pilot itself showed about which interactions worked; which architecture, model or live data source broke during the pilot; what was seen in the workforce during the pilot; and which ecosystem partner underperformed.
- **Scale-stage stewardship:** formal data SLAs or a data-currency process; whether the four Define-stage data relationships became SLAs; who refreshes data on a regular cadence; and whether extension officers show dependency rather than added capacity.
- **Accountability:** the path from a wrong answer to a fix, and who holds liability. The source's own information-gaps list names this.
- **Decisions not documented:** how engagement was read as a success signal at Scale, and an operating-model decision made before launch that had a real alternative behind it.

The full list is in `gaps`.

## Where the reusable value is

43 units: the 42 numbered Section 3 micro-innovations, plus one for the Section 4 transferable-asset bundle. The document has no Section 5, so no problem-solution pattern was extracted.

- **Who it is for:** define the excluded user precisely ([unit](../units/mahavistaar-precise-excluded-user.md)); the registered farmer is not always the decision-maker ([unit](../units/mahavistaar-registered-farmer-not-decision-maker.md)); size the value gap against the current state ([unit](../units/mahavistaar-size-incremental-value-gap.md)); scope to one answerable question ([unit](../units/mahavistaar-scope-to-single-answerable-question.md)); design inbound and outbound together ([unit](../units/mahavistaar-inbound-and-outbound-together.md)); plan for languages beyond the first ([unit](../units/mahavistaar-anticipate-multilingual-demand.md)).
- **What to build:** start bundled and design so you can unbundle later ([unit](../units/mahavistaar-start-bundled-design-to-unbundle.md)); the dual-provider inference stack ([unit](../units/mahavistaar-dual-provider-inference-stack.md)); decoupled moderation ([unit](../units/mahavistaar-decoupled-moderation-endpoint.md)); open architecture and orchestration to start from ([OpenAgriNet](../units/mahavistaar-openagrinet-seven-layer-architecture.md), [Voiceera](../units/mahavistaar-voiceera-orchestration-platform.md)); voice UX fixes from the pilot ([dead silence](../units/mahavistaar-dead-silence-hold-message.md), [short introduction](../units/mahavistaar-short-opening-introduction.md), [no commercial nudging](../units/mahavistaar-no-commercial-follow-up-nudging.md)); and the scale economics ([moderation GPU for TP=8](../units/mahavistaar-isolate-moderation-gpu-tp8.md), [prefix caching](../units/mahavistaar-prefix-caching.md), [cost model](../units/mahavistaar-cost-modelling-framework.md)).
- **Who owns and governs it:** institutional authorisation is the critical path ([unit](../units/mahavistaar-institutional-authorisation-critical-path.md)); the system speaks as the institution ([unit](../units/mahavistaar-speaks-as-the-institution.md)); name the data owner first ([unit](../units/mahavistaar-name-data-owner-first.md)); staged, gated institutional testing ([unit](../units/mahavistaar-staged-gated-institutional-testing.md)); the operating model is a staffing question ([unit](../units/mahavistaar-operating-model-as-staffing.md)), with a named owner for continuous improvement ([unit](../units/mahavistaar-named-owner-continuous-improvement.md)).
- **Who else has to show up:** inventory what exists before specifying ([unit](../units/mahavistaar-inventory-before-specifying.md)); federate data rather than centralise it ([unit](../units/mahavistaar-federated-data-ownership.md)); what transfers to the next adopter and what doesn't ([unit](../units/mahavistaar-architecture-transfers-trust-doesnt.md)); the published asset bundle ([unit](../units/mahavistaar-transferable-asset-bundle.md)); prove at state level, then federate ([unit](../units/mahavistaar-prove-state-then-federate.md)).

## Corpus copies

- `content/wiki/pathways/mahavistaar.md`
- `content/library-wiki/pathways/mahavistaar.md`

Exists in **both** in-repo corpora as independently maintained documents — same slug, different text.
