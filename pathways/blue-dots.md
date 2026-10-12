---
name: Blue Dots — Local Job, Talent, and Service Discovery
type: pathway
schema_version: 2
aliases:
- Blue Dots — Local Job, Talent, and Service Discovery
- AI for Hyperlocal Job Discovery — National
summary: Open voice-AI discovery infrastructure making local jobs, talent, and services findable within a district,
  modelled on what UPI did for payments — from two district deployments and the open questions the next one
  still needs answered.
tags:
- Voice AI
- Livelihoods
- Digital Public Goods
title: Blue Dots — Local Job, Talent, and Service Discovery
pathway_kind: single-deployment
sector: Livelihoods
use_case_category: Local job, talent and service discovery (open voice-AI discovery infrastructure)
geography: Dharwad, Karnataka (pioneer district, 2024); Ghaziabad, Uttar Pradesh (second district); scaling
  now underway across multiple districts in Uttar Pradesh and Karnataka
population_served: Job seekers and citizens — especially women re-entering work, persons with disabilities,
  first-generation graduates, and daily-wage workers — SMBs and service providers, local ecosystem aggregators
  (ITIs, MSME associations, NGOs), district administrations, and private innovators
stage_reached: scale
contributing_organisations:
- ekstep-foundation
- dharwad-district-administration
- ghaziabad-district-administration
contributors:
- tushar
- gaurav-gupta
key_dates: 'Dharwad: 2024, pioneer deployment, ~10 months to a self-sustaining ecosystem. Ghaziabad: second
  district, ~4 months. As of July 2026.'
scale_impact: 'As of Jul 2026: in Ghaziabad, fewer than 10% of the district''s SMBs surfaced on the shared
  map made 10,000+ local job openings visible in under 60 days. In Dharwad, one MSME association onboarded
  300+ employers in two weeks and one ITI onboarded 500+ seekers in the same window.'
cost_anchor: 'As of Jul 2026: discovery cost drops from ₹500+ per field-survey interaction to ₹10 per voice
  interaction; telephony cost fell from roughly ₹6/minute to ₹1/minute over the rollout. A conservative 5%
  workforce-participation gain in one district is estimated at ₹1,050 crore additional annual GDP (₹87,500
  crore across India''s top 100 progressive districts) — order-of-magnitude anchors, not precise benchmarks.'
build_effort: 'Dharwad: 10 months from decision to a self-sustaining ecosystem, built while the playbook was
  being written. Ghaziabad: 4 months, drawing directly on Dharwad. A new district can configure the DPGs in
  about two weeks once the required information is collated — district readiness, not technology setup, is
  the constraint.'
downstream_adoptions:
- Scale-up underway across multiple districts in Uttar Pradesh and Karnataka
- The same local-discovery frame is being tested for tourism, local services and agriculture, and for other
  "Dots" initiatives beyond jobs (see Gap 3)
coverage:
  persona:Explore: 3
  persona:Define: 2
  persona:Pilot: 2
  persona:Scale: 1
  solution:Explore: 2
  solution:Define: 3
  solution:Pilot: 1
  solution:Scale: 1
  institution:Explore: 1
  institution:Define: 2
  institution:Pilot: 1
  institution:Scale: 1
  ecosystem:Explore: 0
  ecosystem:Define: 1
  ecosystem:Pilot: 2
  ecosystem:Scale: 1
gaps:
- What was reused from Dharwad when implementing Ghaziabad — technology, process, people, or partnerships —
  versus what had to be locally adapted, and which of those elements generalise to a third district? (Solution/Define)
- How does responsibility for a Blue Dots deployment actually transition from the initial implementation team
  to state or district institutions, and what specifically gets handed over? (Institution/Scale)
- How much of the Blue Dots approach has carried over into "Orange" or "Purple" Dots initiatives in other sectors,
  and what has that taught the team about adapting the model beyond jobs? (Ecosystem/Scale)
- How is a Blue Dots connection actually verified to have led to a useful outcome — an interview, a placement,
  a service delivered — rather than just a connection made? (Persona/Pilot)
- What are the biggest remaining barriers to making a new district deployment faster and more implementation-light
  than the current ~2-week configuration process? (Solution/Scale)
- Which parts of the user journey are handled by AI today, and where does human intervention remain essential?
  (Solution/Pilot)
corpora:
- grounding-corpus
- library-corpus
doc_refs:
- content/wiki/pathways/blue-dots.md
- content/library-wiki/pathways/blue-dots.md
lifecycle: published
published_on: '2026-07-31'
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/blue-dots.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/library-wiki/pathways/blue-dots.md
- system: github_repo
  method: derived
  date: '2026-10-08'
  ref: published_on = date content/wiki/pathways/blue-dots.md was first committed
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/blue-dots.md § 0–2 (identity, effort, contributors, coverage grid)
contested:
- field: coverage
  readings:
  - 'grounding (content/wiki/pathways/blue-dots.md): the 4×4 grid gives Persona × Pilot ●● (Unit 6) and Institution
    × Explore ●'
  - 'library (content/library-wiki/pathways/blue-dots.md): Persona × Pilot and Institution × Explore are marked
    n/a (persona validated at Explore/Define; institutional ownership belongs to Define)'
  note: coverage is taken from the grounding document's own grid, the framework-structured and stronger source.
    Kept, not arbitrated.
- field: title
  readings:
  - 'grounding (content/wiki/pathways/blue-dots.md): Blue Dots — Local Job, Talent, and Service Discovery'
  - 'library (content/library-wiki/pathways/blue-dots.md): AI for Hyperlocal Job Discovery — National'
  note: Same slug, different titles; the library title is kept as an alias.
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

Open voice-AI discovery infrastructure making local jobs, talent, and services findable within a district, modelled on what UPI did for payments — from two district deployments and the open questions the next one still needs answered.

According to EkStep Foundation's Blue Dots pathway, the deployment is a set of shared, open digital rails that make local jobs, talent and services visible to each other within a district via a 2–3 minute voice call, built as reusable Digital Public Goods rather than a platform any one organisation owns. It started in Dharwad, Karnataka (pioneer district, 2024), went to Ghaziabad, Uttar Pradesh (second district), and is now scaling across multiple districts in both states. It serves job seekers and citizens (especially women re-entering work, persons with disabilities, first-generation graduates and daily-wage workers), SMBs and service providers, local aggregators (ITIs, MSME associations, NGOs), district administrations and private innovators.

Contributed by: EkStep Foundation, with the Dharwad and Ghaziabad district administrations and local aggregators (ITIs, MSME associations). [Tushar](../people/tushar.md)'s material is the primary source; [Gaurav Gupta](../people/gaurav-gupta.md) (Chief Growth Officer, EkStep Foundation, and Lead Architect of Blue Dots) contributed the Gaps.

Scale (as of Jul 2026): in Ghaziabad, fewer than 10% of the district's SMBs on the shared map made 10,000+ local job openings visible in under 60 days; in Dharwad, one MSME association onboarded 300+ employers and one ITI 500+ seekers in two weeks.

## Effort

- **Cost anchor (as of Jul 2026):** discovery cost falls from ₹500+ per field-survey interaction to ₹10 per voice interaction; telephony fell from about ₹6/minute to ₹1/minute over the rollout (the cost-optimisation flow behind it is not documented in the source). The GDP estimates (₹1,050 crore for one district at a 5% workforce-participation gain; ₹87,500 crore across 100 districts) are order-of-magnitude anchors.
- **Build effort:** Dharwad took 10 months with no prior pathway to draw on; Ghaziabad 4 months, drawing on Dharwad. A new district can configure the DPGs in about two weeks once the required information is collated. Technology setup is rarely the constraint; district readiness is.
- **Downstream:** multi-district scale-up in Uttar Pradesh and Karnataka; the same frame is being tested for tourism, local services, agriculture and other "Dots" initiatives.

## Coverage

From the document's own 4×4 grid:

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●●● | ●● | ●● | ● |
| Solution | ●● | ●●● | ● | ● |
| Institution | ● | ●● | ● | ● |
| Ecosystem | ○ | ● | ●● | ● |

## Gaps

Contributed by Gaurav Gupta as open questions the pathway does not yet answer:

- What was reused from Dharwad when implementing Ghaziabad — technology, process, people, or partnerships — versus what had to be locally adapted, and which of those elements generalise to a third district? (Solution/Define)
- How does responsibility for a Blue Dots deployment actually transition from the initial implementation team to state or district institutions, and what specifically gets handed over? (Institution/Scale)
- How much of the Blue Dots approach has carried over into "Orange" or "Purple" Dots initiatives in other sectors, and what has that taught the team about adapting the model beyond jobs? (Ecosystem/Scale)
- How is a Blue Dots connection actually verified to have led to a useful outcome — an interview, a placement, a service delivered — rather than just a connection made? (Persona/Pilot)
- What are the biggest remaining barriers to making a new district deployment faster and more implementation-light than the current ~2-week configuration process? (Solution/Scale)
- Which parts of the user journey are handled by AI today, and where does human intervention remain essential? (Solution/Pilot)

## Where the reusable value is

According to the pathway, the reusable value is concentrated in its architecture decisions and its toolkit. The open-rails and DPG decisions are the most consequential and the hardest to reverse.

- **Architecture:** [open shared rails, not an owned platform](../units/blue-dots-open-shared-rails.md) · [reusable DPGs, not a closed application](../units/blue-dots-reusable-dpg-building-blocks.md) · the [DPG stack itself](../units/blue-dots-dpg-stack-toolkit.md) (toolkit asset)
- **Framing the problem:** [the paradox of proximity](../units/blue-dots-paradox-of-proximity.md) · [meet existing behaviour with voice](../units/blue-dots-meet-existing-behaviour.md)
- **Trust and institutions:** [three-layer trust sequence](../units/blue-dots-three-layer-trust-sequence.md) (playbook) · [District Champion and State Sponsor before activation](../units/blue-dots-district-champion-state-sponsor.md)
- **What broke at pilot:** [district-by-district dialect adaptation](../units/blue-dots-district-dialect-adaptation.md) · [density and freshness decay](../units/blue-dots-density-freshness-decay.md)

The document has no Section 5, so no problem→solution pattern was recorded.

## Corpus copies

- `content/wiki/pathways/blue-dots.md`
- `content/library-wiki/pathways/blue-dots.md`

Exists in **both** in-repo corpora as independently maintained documents — same slug, different text.
