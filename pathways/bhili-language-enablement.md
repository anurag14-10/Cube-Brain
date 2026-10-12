---
name: Bhili Language Enablement for Voice AI
type: pathway
schema_version: 2
aliases:
- Bhili Language Enablement for Voice AI
- Project Astitva
- Voice AI for Tribal Language Inclusion — Nandurbar
summary: Bringing Dehwali Bhili, a zero-digital-resource tribal language, into ASR/NMT/TTS and into MahaVISTAAR's
  live voice bot — from a near-miss isolated data-collection effort to a district-to-state replication
  playbook.
tags:
- Voice AI
- Language
- Tribal Inclusion
title: Bhili Language Enablement for Voice AI
pathway_kind: single-deployment
sector: Agriculture
use_case_category: voice-first government advisory
geography: Nandurbar district, Maharashtra — extends to Bhili-speaking populations across Madhya Pradesh
  and Rajasthan
population_served: 10 million+ Dehwali Bhili speakers nationally; within Nandurbar, tribal community members
  — particularly women farmers with smaller advice networks, limited exposure to Marathi, and reduced
  access to government schemes reaching everyone else
stage_reached: pilot
contributing_organisations:
- ekstep-foundation
deploying_organisations:
- maharashtra-department-of-agriculture
- nandurbar-district-administration
key_dates: 'As of Aug 2026: data collection ~1 month from a standing start; models live in the MahaVISTAAR
  app ~26 May 2026; telephony/IVR field testing August 2026; full telephony rollout targeted before October
  2026'
scale_impact: 'As of Aug 2026: 25,000 agricultural + 15,000 non-agricultural translation sentences; 60,000+
  voice samples; ~60 hours spontaneous, ~6 hours studio and ~2 hours conversational speech; live inside
  MahaVISTAAR''s Vasudha voice bot and the MahaDBT-adjacent advisory channel; three further languages
  (Mathwadi Bhili, Mavchi, Pawari) queued on the same playbook'
cost_anchor: 'As of Jul 2026: Phase 1 roughly ₹27 lakh, fully government-funded, of which close to ₹20
  lakh went directly to community contributors paid per task; model training subsidised by AI4Bharat
  in exchange for open data access, not a cash cost to the district'
build_effort: ~1 month for the first data-collection phase with a 22–25 person field contributor team
  (from a ~70-person taluka agriculture staff pool), a small central studio team recording 10–12 hours
  a day in an existing community radio station, at least five named institutional partners and one lead
  district champion (the District Collector); ~100 days end to end from first recording to a live public
  feature
downstream_adoptions:
- None yet formally documented as live deployments by other adopters (as of Aug 2026)
- Same playbook committed to Mathwadi Bhili, Mavchi and Pawari, with Bodo and Garo named as later candidates
- The district has published its own four-step replication handbook for other districts to pick up
related_pathways:
- mahavistaar
coverage:
  persona:Explore: 2
  persona:Define: 0
  persona:Pilot: 1
  persona:Scale: 0
  solution:Explore: 0
  solution:Define: 3
  solution:Pilot: 1
  solution:Scale: 0
  institution:Explore: 2
  institution:Define: 2
  institution:Pilot: 2
  institution:Scale: 0
  ecosystem:Explore: 0
  ecosystem:Define: 2
  ecosystem:Pilot: 0
  ecosystem:Scale: 2
gaps:
- No stated Word Error Rate, BLEU, or Mean Opinion Score figures for the live ASR/NMT/TTS models, despite
  these being named as the standard evaluation yardsticks in the EkStep interview itself. (Solution/E,
  Pilot)
- No documented "current workaround" for the specifically excluded population (tribal women) before this
  service existed — barriers are named, the prior behaviour is not. (Persona/B, Explore)
- No named budget line or recurring funding commitment for Scale-stage operation, beyond the general statement
  that ownership has "transitioned to the state." (Institution/F, Scale)
- No documented formal data SLA (cadence, accountability) between the state agriculture department and
  any external data source feeding the live advisory answers, unlike the mandi-price SLA pattern documented
  in the related MahaVISTAAR pathway. (Ecosystem/B, Scale)
- No account of what happened to the roughly 5–8 of the original 22–25 field contributors who did not
  complete the work — attrition is mentioned by the Taluka Agriculture Officer but not why, or what (if
  anything) was done about it. (Ecosystem/E, Pilot)
- No documented mechanism for a Bhili speaker to flag a wrong or unhelpful helpline answer back to the
  model-building team — the interview describes model-side monitoring, not a user-facing feedback path.
  (Institution/C, Pilot)
- No stated criteria for when the standalone telephony/IVR line — still in field testing as of August
  2026 — will be judged ready for full public rollout, beyond a target date. (Solution/E, Pilot)
partner_organisations:
- karya
- bhashini
- ai4bharat
- voicera
- pocra
corpora:
- grounding-corpus
- library-corpus
doc_refs:
- content/wiki/pathways/bhili-language-enablement.md
- content/library-wiki/pathways/bhili-language-enablement.md
lifecycle: published
published_on: '2026-07-31'
contested:
- field: scale_impact
  readings:
  - 'grounding corpus: 25,000 agricultural + 15,000 non-agricultural translation sentences (40,000 in all)'
  - 'library corpus: 60,000 Bhili–Marathi translation pairs'
  note: The grounding document is framework-structured and newer (timestamp 2026-08-31 vs 2026-07-06);
    the brain records its figure in scale_impact but does not arbitrate.
- field: scale_impact
  readings:
  - 'grounding corpus: ~6 hours studio speech and ~2 hours conversational speech, per the booklet''s later
    count'
  - 'library corpus: 2 hours of studio-quality voice (~2 hours per artist)'
  note: The two copies disagree on studio-speech hours; the grounding copy cites the Astitva booklet's
    later count. Not arbitrated.
- field: title
  readings:
  - 'grounding corpus: Bhili Language Enablement for Voice AI'
  - 'library corpus: Voice AI for Tribal Language Inclusion — Nandurbar'
  note: Same slug, different display titles; the library title is kept as an alias.
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/bhili-language-enablement.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/library-wiki/pathways/bhili-language-enablement.md
- system: github_repo
  method: derived
  date: '2026-10-08'
  ref: published_on = date content/wiki/pathways/bhili-language-enablement.md was first committed
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/bhili-language-enablement.md — Sections 1–2 (identity, effort, coverage
    grid, gaps) and Section 3 units 1–8
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/bhili-language-enablement.md — compared only, for the contested readings
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: deploying_organisations = maharashtra-department-of-agriculture, from Section 1's role "State Agriculture
    Department & POCRA (deployment into MahaVISTAAR)" — the document lists all actors under contributing
    organisations
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

According to EkStep Foundation's pathway, Project Astitva brought Dehwali Bhili — a tribal language with no prior ASR, NMT or TTS resource — into a voice AI stack and into the Vasudha voice bot of [MahaVISTAAR](mahavistaar.md), Maharashtra's agricultural advisory. A district-run data-collection effort, discovered running in isolation from the national model-building ecosystem and then connected to it, became a live (still-tuning) feature and an explicit replication playbook for the next language.

- **Geography:** Nandurbar district, Maharashtra; Bhili-speaking populations also span Madhya Pradesh and Rajasthan.
- **Who it serves:** 10 million+ Dehwali Bhili speakers nationally; within Nandurbar, tribal community members — particularly women farmers with smaller advice networks, limited Marathi and reduced access to government schemes.
- **Stage reached:** [Pilot](../concepts/pilot.md). Text and voice chat live inside Vasudha since ~26 May 2026; a standalone telephony/IVR line was in field testing in August 2026, targeted for full rollout before October 2026.
- **Actors named in the document:** the District Administration, Nandurbar (convening authority); Karya (data-collection platform); Bhashini/ULCA (national hosting); AI4Bharat/IIT Madras (model building); Voicera (voice stack and telephony-integration learnings); the State Agriculture Department and POCRA (deployment into MahaVISTAAR); EkStep Foundation (cross-stakeholder orchestration).

Contributed by: EkStep Foundation.

## Effort

- **Cost anchor (as of Jul 2026):** Phase 1 roughly ₹27 lakh, fully government-funded; close to ₹20 lakh of it paid directly to community contributors per task. Model training was subsidised by AI4Bharat in exchange for open data access.
- **Build effort:** about one month for the first data-collection phase — a 22–25 person field contributor team drawn from a ~70-person taluka agriculture staff pool, a small studio team recording 10–12 hours a day in an existing community radio station, at least five institutional partners and one district champion. About 100 days from first recording to a live public feature.
- **Scale (as of Aug 2026):** 25,000 agricultural and 15,000 non-agricultural translation sentences; 60,000+ voice samples; ~60 hours of spontaneous, ~6 hours of studio and ~2 hours of conversational speech.
- **Downstream:** no other adopter's live deployment is documented yet; the same playbook is committed to Mathwadi Bhili, Mavchi and Pawari, with Bodo and Garo named later, and the district has published a four-step replication handbook.

The library copy gives different counts for translation pairs and studio hours — see `contested`.

## Coverage

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●● | ○ | ● | ○ |
| Solution | ○ | ●●● | ● | ○ |
| Institution | ●● | ●● | ●● | ○ |
| Ecosystem | ○ | ●● | ○ | ●● |

From the document's own grid. Two cells credit evidence that has no numbered unit of its own: Persona × Pilot (the live helpline field test) and Solution × Pilot (validator and dialect friction, folded into the three-tier quality structure).

## Gaps

- No stated Word Error Rate, BLEU, or Mean Opinion Score figures for the live ASR/NMT/TTS models, despite these being named as the standard evaluation yardsticks in the EkStep interview itself. (Solution/E, Pilot)
- No documented "current workaround" for the specifically excluded population (tribal women) before this service existed — barriers are named, the prior behaviour is not. (Persona/B, Explore)
- No named budget line or recurring funding commitment for Scale-stage operation, beyond the general statement that ownership has "transitioned to the state." (Institution/F, Scale)
- No documented formal data SLA (cadence, accountability) between the state agriculture department and any external data source feeding the live advisory answers, unlike the mandi-price SLA pattern documented in the related MahaVISTAAR pathway. (Ecosystem/B, Scale)
- No account of what happened to the roughly 5–8 of the original 22–25 field contributors who did not complete the work — attrition is mentioned by the Taluka Agriculture Officer but not why, or what (if anything) was done about it. (Ecosystem/E, Pilot)
- No documented mechanism for a Bhili speaker to flag a wrong or unhelpful helpline answer back to the model-building team — the interview describes model-side monitoring, not a user-facing feedback path. (Institution/C, Pilot)
- No stated criteria for when the standalone telephony/IVR line — still in field testing as of August 2026 — will be judged ready for full public rollout, beyond a target date. (Solution/E, Pilot)

## Where the reusable value is

Eight units, one per Section 3 micro-innovation; the document has no Section 5, so no problem-solution pattern was extracted.

- **Who it is for** — centre the population digital infrastructure keeps invisible, not the language in the abstract ([unit](../units/bhili-language-enablement-center-the-excluded-population.md)).
- **What to collect and build** — design voice data for the phone call users will make, after a clean-studio first attempt failed ([unit](../units/bhili-language-enablement-design-for-telephony-audio.md)); fine-tune a full ASR/NMT/TTS stack from a related higher-resource language, accepting the cost of including speech recognition ([unit](../units/bhili-language-enablement-fine-tune-from-related-language.md)).
- **Who owns and governs it** — anchor the effort to one personally invested administrative champion ([unit](../units/bhili-language-enablement-personal-administrative-champion.md)); a three-tier contributor → checker → validator structure staffed through local administration, the deployment's reusable toolkit ([unit](../units/bhili-language-enablement-three-tier-quality-structure.md)); scope the live helpline to what the department will stand behind ([unit](../units/bhili-language-enablement-scope-to-what-institution-stands-behind.md)).
- **Who else has to show up** — don't let parallel efforts on the same language run in isolation; discovery, not capability, was the constraint ([unit](../units/bhili-language-enablement-connect-parallel-language-efforts.md)); the district's four-step replication handbook for the next language ([unit](../units/bhili-language-enablement-district-replication-handbook.md)).

## Corpus copies

- `content/wiki/pathways/bhili-language-enablement.md`
- `content/library-wiki/pathways/bhili-language-enablement.md`

Exists in **both** in-repo corpora as independently maintained documents — same slug, different text.
