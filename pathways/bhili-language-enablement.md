---
name: Bhili Language Enablement for Voice AI
type: pathway
schema_version: 2
aliases:
- Bhili Language Enablement for Voice AI
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
stage_reached: pilot
contributing_organisations:
- ekstep-foundation
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
corpora:
- grounding-corpus
- library-corpus
doc_refs:
- content/wiki/pathways/bhili-language-enablement.md
- content/library-wiki/pathways/bhili-language-enablement.md
lifecycle: published
published_on: '2026-07-31'
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
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Identity

Bringing Dehwali Bhili, a zero-digital-resource tribal language, into ASR/NMT/TTS and into MahaVISTAAR's live voice bot — from a near-miss isolated data-collection effort to a district-to-state replication playbook.

Contributed by: EkStep Foundation.

## Coverage

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●● | ○ | ● | ○ |
| Solution | ○ | ●●● | ● | ○ |
| Institution | ●● | ●● | ●● | ○ |
| Ecosystem | ○ | ●● | ○ | ●● |

## Gaps

- No stated Word Error Rate, BLEU, or Mean Opinion Score figures for the live ASR/NMT/TTS models, despite these being named as the standard evaluation yardsticks in the EkStep interview itself. (Solution/E, Pilot)
- No documented "current workaround" for the specifically excluded population (tribal women) before this service existed — barriers are named, the prior behaviour is not. (Persona/B, Explore)
- No named budget line or recurring funding commitment for Scale-stage operation, beyond the general statement that ownership has "transitioned to the state." (Institution/F, Scale)
- No documented formal data SLA (cadence, accountability) between the state agriculture department and any external data source feeding the live advisory answers, unlike the mandi-price SLA pattern documented in the related MahaVISTAAR pathway. (Ecosystem/B, Scale)
- No account of what happened to the roughly 5–8 of the original 22–25 field contributors who did not complete the work — attrition is mentioned by the Taluka Agriculture Officer but not why, or what (if anything) was done about it. (Ecosystem/E, Pilot)
- No documented mechanism for a Bhili speaker to flag a wrong or unhelpful helpline answer back to the model-building team — the interview describes model-side monitoring, not a user-facing feedback path. (Institution/C, Pilot)
- No stated criteria for when the standalone telephony/IVR line — still in field testing as of August 2026 — will be judged ready for full public rollout, beyond a target date. (Solution/E, Pilot)

## Where the reusable value is

Not yet extracted — run the cube-brain skill's *ingest pathway* operation to
create its `units/`.

## Corpus copies

- `content/wiki/pathways/bhili-language-enablement.md`
- `content/library-wiki/pathways/bhili-language-enablement.md`

Exists in **both** in-repo corpora as independently maintained documents — same slug, different text.
