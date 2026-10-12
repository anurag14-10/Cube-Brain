---
name: Amul AI / Sarla Ben
type: pathway
schema_version: 2
aliases:
- Amul AI / Sarla Ben
- Sarla Ben
- Amul AI
summary: Amul's AI advisory assistant for 3.6 million dairy farmer-members - built in one month on 50+
  years of cooperative data, with daily quality review and ongoing expansion into credit and IoT health
  alerts.
tags:
- Voice AI
- Agriculture
- Dairy
title: Amul AI / Sarla Ben
pathway_kind: single-deployment
sector: Agriculture / Dairy
use_case_category: AI advisory assistant for dairy cooperative farmer-members (animal husbandry advice, records
  and vet-visit booking over voice, app and WhatsApp)
geography: Gujarat, India (national and international expansion underway as of September 2026)
population_served: 3.6 million dairy farmer-members of GCMMF (Amul), primarily women responsible for daily
  milking and cattle care; feature-phone and smartphone users across Gujarati-speaking rural Gujarat
stage_reached: scale
contributing_organisations:
- gcmmf-amul
- ekstep-foundation
deploying_organisations:
- gcmmf-amul
related_pathways:
- mahavistaar
- unififed-ai-driven-agri-ecosystem
key_dates: 'PMO call to Amul MD: 2026-01-08 · First version live: approximately February 2026 (three weeks
  after project start, in time for the Global AI Summit) · CM launch of Amul AI: 2026-02-11 · Bharat Vistaar
  integration completed: approximately August 2026 · Interviews recorded: 2026-09-07 to 2026-09-09'
scale_impact: 'As of August 2026: ~1,000 inbound calls/day (40,000+ total); ~15,000 chats/day (500,000+
  total); 78,599 unique users and 360,871 message turns in August 2026 alone; 96.98% answer-delivery rate;
  41% returning users; 82.5% Gujarati-language share; 30,000 vet-visit transactions completed; peak single
  day 16,791 turns.'
cost_anchor: 'As of September 2026: GPU compute provided free by the Government of India and AI expertise
  pro bono by EkStep Foundation, so Amul''s direct cash outlay for setup was effectively zero; run-rate costs
  remain covered by these arrangements, and Amul states it can sustain the platform from its own resources
  if funding lapses. Cost per interaction not documented in the source.'
build_effort: 'One month from project start to first live version (first version in three weeks). Internal
  Amul team on a no-holiday, same-day delivery mandate plus the EkStep Foundation technical team led by
  its COO. Partners: EkStep Foundation (technical build, pro-bono AI expertise), NDDB (knowledge content),
  Government of Gujarat (knowledge content and GPU), veterinary colleges in Anand (knowledge content), 21
  district unions (champion teams, knowledge, field distribution).'
downstream_adoptions:
- Bharat Vistaar — integrated as the backend for agriculture queries (completed ~August 2026)
- NDDB — exploring integration or a parallel build
- New Zealand dairy sector — interest expressed at an International Dairy Federation event (November 2026
  planned)
- Ethiopia — interest expressed
- Multiple Indian state governments — in discussion
- The OAN / OpenAgriNet architecture underlying Sarla Ben also powers MahaVISTAAR (Maharashtra) and Bihar
  Krishi, with the same governance template applied locally each time
coverage:
  persona:Explore: 2
  persona:Define: 2
  persona:Pilot: 2
  persona:Scale: 2
  solution:Explore: 2
  solution:Define: 2
  solution:Pilot: 2
  solution:Scale: 2
  institution:Explore: 2
  institution:Define: 2
  institution:Pilot: 2
  institution:Scale: 2
  ecosystem:Explore: 1
  ecosystem:Define: 2
  ecosystem:Pilot: 2
  ecosystem:Scale: 2
gaps:
- 'Persona × Scale — unregistered-number users (relates to Unit 6): a large share of callers arrive on unregistered
  numbers (family members calling on behalf of a registered farmer) and secondary-number linking is being
  built; what the eventual design looks like, and what share of the 30-40 lakh target population it can
  reach, is not yet documented.'
- 'Solution × Scale — per-cow yield data as the missing input for personalised advice (relates to Unit 5):
  farmer-level milk yield data exists but per-cow yield data does not exist at scale, which EkStep''s COO
  identifies as the binding constraint on moving from general knowledge retrieval to personalised health
  and breeding advice; how it will be closed (IoT collar belts, manual entry, or infrastructure change) is
  not yet resolved.'
- 'Solution × Explore — AI-fit justification for dairy versus simpler alternatives: given Amul''s significant
  prior digitisation and app infrastructure, what was blocking a non-AI solution (e.g. a well-structured
  FAQ or rule-based triage) from achieving the same outcome is not explicitly argued.'
- 'Institution × Scale — long-term funding and staffing model after the pro-bono period ends (relates to
  Unit 8): the specific arrangement for GPU costs, EkStep expert time, and Amul''s own dedicated staffing
  beyond the current shared-resource model is not documented.'
- 'Ecosystem × Explore — precedent deployments reviewed before starting: whether Amul or EkStep reviewed
  other voice AI or cooperative-AI deployments, including whether lessons from MahaVISTAAR (which preceded
  Amul AI) were formally reviewed at Explore stage, is not stated.'
contested:
- field: coverage
  readings:
  - 'Section 2 grid: every cell covered (●●) except Ecosystem × Explore (●); Section 0 names Institution ×
    Explore, Solution × Pilot and Ecosystem × Define as the highest-density cells'
  - 'Section 3 units: nine units, originating only in Persona × Explore, Persona × Pilot, Solution × Define
    (2), Solution × Pilot, Institution × Explore, Institution × Define, Institution × Scale and Ecosystem
    × Explore; no unit originates in Persona × Define/Scale, Solution × Explore/Scale, Institution × Pilot
    or Ecosystem × Define/Pilot/Scale'
  note: The coverage map transcribes the document's own grid as instructed; the unit evidence supports lower
    density in eight cells, including the Ecosystem × Define cell Section 0 calls high-density (its multi-source
    knowledge-ingestion process has no unit of its own).
contributors:
- jagadish
partner_organisations:
- nddb
- government-of-gujarat
corpora:
- grounding-corpus
doc_refs:
- content/wiki/pathways/ai-advisory-for-dairy-farmers.md
lifecycle: unindexed
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/ai-advisory-for-dairy-farmers.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-advisory-for-dairy-farmers.md Sections 0-6 (identity, effort, coverage grid,
    gaps, units)
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

Amul's AI advisory assistant for 3.6 million dairy farmer-members - built in one month on 50+ years of cooperative data, with daily quality review and ongoing expansion into credit and IoT health alerts.

Contributed by: GCMMF (Amul) / EkStep Foundation. Deployed by GCMMF (Amul).

According to the contributors, Sarla Ben serves GCMMF's dairy farmer-members across Gujarat — primarily the women responsible for daily milking and cattle care — via voice, app and WhatsApp in Gujarati, Hindi and English. It has become a declared permanent programme with daily quality review, ongoing feature expansion into credit and IoT health alerts, and interest from New Zealand, Ethiopia, NDDB and several state governments.

- **Sector / use case:** Agriculture / Dairy — advisory assistant for cooperative farmer-members.
- **Geography:** Gujarat, India (national and international expansion underway as of September 2026).
- **Stage reached:** Scale.
- **Key dates:** PMO call to the Amul MD 2026-01-08 · first version live ~February 2026 · CM launch 2026-02-11 · Bharat Vistaar integration ~August 2026.
- **Scale (as of August 2026):** ~1,000 inbound calls/day and ~15,000 chats/day; 78,599 unique users and 360,871 message turns in the month; 96.98% answer-delivery rate; 41% returning users; 30,000 vet-visit transactions.
- **Transfers when:** the deploying institution already holds per-farmer, per-cattle transactional data in digital form; a cooperative or farmer-trust structure exists that farmers already believe in; a senior institutional owner personally commits.
- **Does not transfer easily when:** farmer data is not digitised to individual-animal level; no pre-existing institution has the trust of target farmers; GPU and expert resources must be procured commercially rather than accessed through government or pro-bono arrangements.

## Effort

- **Build:** one month from project start to first live version (first version in three weeks), by an internal Amul team on a no-holiday, same-day delivery mandate plus the EkStep Foundation technical team.
- **Partners:** EkStep Foundation (technical build, pro-bono AI expertise); NDDB, the Government of Gujarat and the veterinary colleges in Anand (knowledge content; Gujarat also GPU); 21 district unions (champion teams, knowledge, field distribution).
- **Cost (as of September 2026):** GPU compute free from the Government of India and AI expertise pro bono from EkStep Foundation; Amul's direct setup outlay effectively zero; cost per interaction not documented in the source.
- **Downstream:** Bharat Vistaar uses it as the backend for agriculture queries; NDDB, New Zealand's dairy sector, Ethiopia and several state governments have expressed interest. The same OAN architecture powers [MahaVISTAAR](mahavistaar.md) and Bihar Krishi.

## Coverage

From the document's own Section 2 grid:

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●● | ●● | ●● | ●● |
| Solution | ●● | ●● | ●● | ●● |
| Institution | ●● | ●● | ●● | ●● |
| Ecosystem | ● | ●● | ●● | ●● |

The nine units extracted from Section 3 originate in only eight of these cells; the grid's uniform density is recorded as `contested` against the unit evidence.

## Gaps

- Persona × Scale — unregistered-number users: family members calling on behalf of a registered farmer arrive on unregistered numbers; the secondary-number linking design, and the share of the 30–40 lakh target population it can reach, is not yet documented.
- Solution × Scale — per-cow yield data as the missing input for personalised advice: farmer-level yield data exists, per-cow yield data does not at scale; how that gap will be closed (IoT collar belts, manual entry, infrastructure change) is unresolved.
- Solution × Explore — AI-fit justification: what was blocking a non-AI solution (a structured FAQ, rule-based triage) given Amul's prior digitisation is not argued.
- Institution × Scale — long-term funding and staffing after the pro-bono period: the arrangement for GPU costs, EkStep expert time and Amul's own dedicated staffing is not documented.
- Ecosystem × Explore — precedent deployments: whether other voice AI or cooperative-AI deployments (including MahaVISTAAR, which preceded it) were reviewed before starting is not stated.

## Where the reusable value is

Nine units, all from Section 3 (Section 4's five toolkit rows restate Units 3, 4, 5, 7 and 9; Section 5 is marked omitted, so there are no problem-solution patterns):

- **Persona** — [design for the woman who milks, not the registered account](../units/ai-advisory-for-dairy-farmers-design-for-the-woman-at-the-farm.md) (Explore); [chat won for advice, voice for transactions](../units/ai-advisory-for-dairy-farmers-chat-for-advice-voice-for-transactions.md) (Pilot, failure and fix).
- **Solution** — [staged open-source model migration](../units/ai-advisory-for-dairy-farmers-staged-open-source-migration.md) and [API retrieval, not data custody](../units/ai-advisory-for-dairy-farmers-api-retrieval-not-data-custody.md) (Define); [landing page with rotating suggested questions](../units/ai-advisory-for-dairy-farmers-landing-page-suggested-questions.md) (Pilot — usage doubled).
- **Institution** — [the MD's personal ownership as precondition](../units/ai-advisory-for-dairy-farmers-md-personal-ownership.md) (Explore); [no-holiday same-day delivery team](../units/ai-advisory-for-dairy-farmers-same-day-delivery-team.md) (Define); [permanent programme declared](../units/ai-advisory-for-dairy-farmers-permanent-programme-declared.md) (Scale).
- **Ecosystem** — [the three-tier cooperative structure as distribution and feedback channel](../units/ai-advisory-for-dairy-farmers-cooperative-tiers-as-distribution.md) (Explore).

The contributors single out the per-cow data gap (Gap 2) as the most important forward-looking insight for adopters planning personalised advisory rather than general knowledge retrieval.

## Corpus copies

- `content/wiki/pathways/ai-advisory-for-dairy-farmers.md`

On disk in the grounding corpus but **not linked from `content/wiki/pathways/index.md`**, so excluded from grounding and the /wiki listing. It may still be live via `published_pathways` — check the DB before calling it unpublished.
