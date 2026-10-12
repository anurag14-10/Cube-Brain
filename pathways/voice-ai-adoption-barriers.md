---
name: Voice AI Adoption Barriers
type: pathway
schema_version: 2
aliases:
- Voice AI Adoption Barriers
summary: Why voice AI pilots stall even when price and vendor access are no longer the obstacle — a synthesis
  of 40+ organisations, two subsidised EkStep programmes, and four named deployments (Ambak, Pradical
  Works, CIVIS, Karnataka AI Department) that did make it through.
tags:
- Voice AI
- Cross-Sector
- Adoption
title: Voice AI Adoption Barriers
pathway_kind: cross-deployment-synthesis
sector: Cross-Sector
use_case_category: Organisational readiness for voice AI adoption (HR & Hiring, Education, Health, Agriculture,
  Governance and others)
geography: India
population_served: Not end beneficiaries directly — the unit of analysis is the adopting organisation itself
  (NGOs, social enterprises, EdTech providers and government bodies attempting to bring voice AI into their
  own operations)
stage_reached: define
contributing_organisations:
- ekstep-foundation
- people-plus-ai
key_dates: 'Listen at Scale: Jan–Feb 2026 (1 month). Impact at Scale: Apr–Jul 2026 (3 months). Source material
  dated Jul 2026.'
scale_impact: 'As of Jul 2026: Listen at Scale 100 applicants → 20 selected; Impact at Scale 85 applicants
  → 75 selected. Utilisation sharply lopsided — the top 5 Listen at Scale organisations generated 86% of credits
  used, and roughly 30 of the 75 selected Impact at Scale organisations did not go ahead with any vendor.'
cost_anchor: 'As of Jul 2026: price was tested and found not to be the binding constraint — Listen at Scale
  gave roughly 100,000 free voice AI minutes per organisation (via Sarvam); Impact at Scale subsidised pricing
  to ₹1/minute against a market rate several times higher; uptake stayed low regardless.'
build_effort: Not a single build — a synthesis across dozens. In the organisations that succeeded, closing
  the gap between "the vendor works in a demo" and "the deployment works for us" reliably took three to four
  months of continuous in-house iteration, not outsourceable to the vendor or a one-time testing exercise.
related_pathways:
- voice-ai-for-inclusion
coverage:
  persona:Explore: 3
  persona:Define: 1
  persona:Pilot: 0
  persona:Scale: 0
  solution:Explore: 2
  solution:Define: 3
  solution:Pilot: 3
  solution:Scale: 1
  institution:Explore: 1
  institution:Define: 1
  institution:Pilot: 2
  institution:Scale: 1
  ecosystem:Explore: 1
  ecosystem:Define: 0
  ecosystem:Pilot: 0
  ecosystem:Scale: 3
gaps:
- No confirmed breakdown of the "three to four months of daily iteration" QA phase into person-hours or
  team size — the finding recurs across organisations but is not quantified into a staffing plan. (Solution/Pilot)
- No documented reason, organisation by organisation, for why roughly 30 of the 75 selected Impact at
  Scale organisations never went ahead with a vendor — only that organisational readiness emerged as the
  dominant pattern across the cohort as a whole, not a per-organisation breakdown of which readiness gap
  applied where. (Institution/Explore)
- The Karnataka AI Department pilot's core institutional gap — no path to continue voice AI spend once
  its grant ended, because government procurement cannot move at grant speed — is named directly in the
  source material as unresolved, not solved. (Institution/Scale)
- Whether the "organisational readiness is roughly 70% of the effort" split is a measured result or the
  interviewee's own working estimate is not stated precisely — carried through here as a strong practitioner
  judgment, not a quantified finding. (Institution/Explore)
- No documented account of behavioural (as opposed to technical or financial) resistance to adoption —
  the source material raises this as a real, unresolved open question (an organisation may know the ROI
  case and still not act, for reasons the interview does not claim to have identified) rather than answering
  it. (Persona/Explore)
deploying_organisations:
- ambak
- pradical-works
- civis
- karnataka-ai-department
partner_organisations:
- sarvam
corpora:
- grounding-corpus
- library-corpus
doc_refs:
- content/wiki/pathways/voice-ai-adoption-barriers.md
- content/library-wiki/pathways/voice-ai-adoption-barriers.md
lifecycle: published
published_on: '2026-07-31'
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/voice-ai-adoption-barriers.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/library-wiki/pathways/voice-ai-adoption-barriers.md
- system: github_repo
  method: derived
  date: '2026-10-08'
  ref: published_on = date content/wiki/pathways/voice-ai-adoption-barriers.md was first committed
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/voice-ai-adoption-barriers.md (Sections 1–2 — geography, population, key dates,
    scale, cost anchor, build effort; Section 0 — related pathway)
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: use_case_category worded from the document title and Section 1 sector line — the document names no
    use-case category
contested:
- field: stage_reached
  readings:
  - 'Grounding copy: frontmatter stage Define; Section 1 calls the synthesis a Define-stage diagnostic spanning
    organisations from Explore through Scale.'
  - 'Library copy: frontmatter stage Explore; says most of its content sits at the Explore stage.'
  note: Kept define, per the grounding copy (framework-structured, primary). Not arbitrated further.
- field: coverage
  readings:
  - 'Grounding copy: a 4×4 grid with Explore through Scale densities across all four dimensions.'
  - 'Library copy: no grid; most stage cells beyond Explore are "not distinctly documented", and it says
    the research covers organisations largely at or before the pilot stage.'
  note: Coverage is taken from the grounding copy's grid only.
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

Why voice AI pilots stall even when price and vendor access are no longer the obstacle — a synthesis of 40+ organisations, two subsidised EkStep programmes, and four named deployments (Ambak, Pradical Works, CIVIS, Karnataka AI Department) that did make it through.

Contributed by: EkStep Foundation / People+AI (Voice AI Ecosystem team).

According to EkStep Foundation / People+AI's account, this is not a single deployment but a cross-organisation synthesis of why voice AI pilots stall, drawn from 40+ deep-dive conversations, a 16+-respondent survey across six sectors, and two subsidised EkStep programmes — Listen at Scale (Sarvam, 20 organisations, Jan–Feb 2026) and Impact at Scale (three vendors, 75 selected organisations, Apr–Jul 2026). Four organisations that reached a working deployment (Ambak, Pradical Works, CIVIS, Karnataka AI Department) anchor what success looks like; named organisations that stalled (Sesame Workshop India, Digital Labour Chowk, Randstad India, Sustainable Living Lab, Haqdarshak, Rite Water and others) anchor what failure looks like.

- **Sector:** Cross-Sector (HR & Hiring, Education, Health, Agriculture, Governance, and others)
- **Geography:** India
- **Population served:** the adopting organisation itself — NGOs, social enterprises, EdTech providers and government bodies — not end beneficiaries
- **Key dates:** Listen at Scale Jan–Feb 2026; Impact at Scale Apr–Jul 2026; source material dated Jul 2026
- **Scale (as of Jul 2026):** 100 applicants → 20 selected (Listen at Scale); 85 applicants → 75 selected (Impact at Scale); the top 5 Listen at Scale organisations used 86% of credits, and roughly 30 of 75 Impact at Scale organisations never went ahead with a vendor

It is an *ecosystem* pathway — how an organisation gets to the decision to build — meant to be read before [Voice AI for Inclusion](voice-ai-for-inclusion.md), the *implementation* pathway for after that decision is made.

## Effort

- **Cost anchor (as of Jul 2026):** price was tested and was not the binding constraint — roughly 100,000 free minutes per organisation in Listen at Scale, ₹1/minute subsidised pricing in Impact at Scale against a market rate several times higher, and uptake stayed low regardless.
- **Build effort:** in the organisations that succeeded, getting from "works in a demo" to "works for us" reliably took three to four months of continuous in-house iteration that could not be outsourced to the vendor or a one-time test.

## Coverage

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●●● | ● | ○ | ○ |
| Solution | ●● | ●●● | ●●● | ● |
| Institution | ● | ● | ●● | ● |
| Ecosystem | ● | ○ | ○ | ●●● |

## Gaps

- No confirmed breakdown of the "three to four months of daily iteration" QA phase into person-hours or team size — the finding recurs across organisations but is not quantified into a staffing plan. (Solution/Pilot)
- No documented reason, organisation by organisation, for why roughly 30 of the 75 selected Impact at Scale organisations never went ahead with a vendor — only that organisational readiness emerged as the dominant pattern across the cohort as a whole, not a per-organisation breakdown of which readiness gap applied where. (Institution/Explore)
- The Karnataka AI Department pilot's core institutional gap — no path to continue voice AI spend once its grant ended, because government procurement cannot move at grant speed — is named directly in the source material as unresolved, not solved. (Institution/Scale)
- Whether the "organisational readiness is roughly 70% of the effort" split is a measured result or the interviewee's own working estimate is not stated precisely — carried through here as a strong practitioner judgment, not a quantified finding. (Institution/Explore)
- No documented account of behavioural (as opposed to technical or financial) resistance to adoption — the source material raises this as a real, unresolved open question (an organisation may know the ROI case and still not act, for reasons the interview does not claim to have identified) rather than answering it. (Persona/Explore)

## Where the reusable value is

According to the contributors, the reusable value concentrates in the use-case-definition, vendor-evaluation and QA units and in the toolkit — the vendor-scoring rubric, the use-case complexity ladder and the two-phase QA process are built to be picked up directly.

- **Before choosing a vendor:** [name one accountable owner](../units/voice-ai-adoption-barriers-one-accountable-owner.md); [define the use case and success metric first](../units/voice-ai-adoption-barriers-use-case-before-vendor.md); [size the build on the complexity ladder](../units/voice-ai-adoption-barriers-use-case-complexity-ladder.md), which also filters out use cases that need no voice AI.
- **Choosing a vendor:** the [weighted vendor-scoring rubric](../units/voice-ai-adoption-barriers-weighted-vendor-scorecard.md), where domain support weighs as much as raw conversation quality.
- **Running the pilot:** the [three-month pilot timeline](../units/voice-ai-adoption-barriers-three-month-pilot-timeline.md); the [conversation-design pattern library](../units/voice-ai-adoption-barriers-conversation-design-pattern-library.md); [two-pass call QA](../units/voice-ai-adoption-barriers-two-pass-call-qa.md).
- **Diagnosing a stalled pilot:** [low connect rates are an operations problem](../units/voice-ai-adoption-barriers-connect-rate-is-operations.md); [integration plumbing gets blamed on the AI](../units/voice-ai-adoption-barriers-integration-plumbing-not-the-ai.md).
- **Designing an adoption programme:** [subsidies do not convert interest into readiness](../units/voice-ai-adoption-barriers-interest-is-not-readiness.md).

The document has no Section 5, so no problem-solution pattern was extracted.

## Corpus copies

- `content/wiki/pathways/voice-ai-adoption-barriers.md`
- `content/library-wiki/pathways/voice-ai-adoption-barriers.md`

Exists in **both** in-repo corpora as independently maintained documents — same slug, different text.
