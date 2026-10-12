---
name: Don't let parallel efforts on the same language run in isolation
type: unit
schema_version: 2
summary: The district's Bhili data collection with Karya ran unseen by the national model-building ecosystem
  until a separate team found it by chance; connecting it to AI4Bharat, Bhashini, Voicera and the state
  deployment channel showed discovery, not capability, was the constraint.
doc_refs:
- content/wiki/pathways/bhili-language-enablement.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/bhili-language-enablement.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against concepts/ecosystem.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: bhili-language-enablement
unit_type: Failure and Fix
dimension: ecosystem
sub_category: ecosystem-a
stage: define
source_unit_id: Unit 7
applies_when: Multiple institutions might plausibly already be working on pieces of the same low-resource-language
  problem without visibility into each other.
fails_when: A single institution already controls both the data-collection and model-building capability
  end to end.
failure: The district's own Bhili data-collection effort with Karya had already been running for some
  time, entirely independent of the national voice-AI model-building ecosystem (AI4Bharat, Bhashini) —
  a separate team building an unrelated agriculture advisory bot only discovered the Nandurbar effort
  by chance while working with the same state department.
fix: Once discovered, EkStep connected the district's data-collection track to the model-building side,
  bringing AI4Bharat/IIT Madras (six years and 10,000+ hours of prior language-model experience), Bhashini
  (national hosting and GPU access), Voicera (open-source voice-stack and telephony-integration expertise)
  and the state agriculture department's deployment channel into a single coordinated effort.
insight: A capable, well-intentioned local effort can still fail to produce a usable model simply because
  nobody who could build one knew it existed — discovery, not capability, was the actual constraint.
adopter_intents:
- We think another team might already be working on this — does it matter?
related_units:
- bhili-language-enablement-district-replication-handbook
---

## Unit

According to EkStep Foundation's Bhili Language Enablement pathway, this is a failure and the fix that followed.

**Failure.** The district's own Bhili data-collection effort with Karya had already been running for some time, entirely independent of the national voice-AI model-building ecosystem (AI4Bharat, Bhashini). A separate team, building an unrelated agriculture advisory bot with the same state department, discovered the Nandurbar effort only by chance.

**Fix.** Once it was discovered, EkStep connected the district's data-collection track to the model-building side — AI4Bharat/IIT Madras (six years and 10,000+ hours of prior language-model experience), Bhashini (national hosting and GPU access), Voicera (open-source voice-stack and telephony-integration expertise) and the state agriculture department's deployment channel — as one coordinated effort rather than two disconnected ones.

**Insight.** A capable, well-intentioned local effort can still fail to produce a usable model simply because nobody who could build one knew it existed. Discovery, not capability, was the actual constraint.

## Condition

- **Applies when:** Multiple institutions might plausibly already be working on pieces of the same low-resource-language problem without visibility into each other.
- **Fails when:** A single institution already controls both the data-collection and model-building capability end to end.

## Before → after

- **Before:** A district data-collection track and the national model-building ecosystem working on the same language without knowing of each other.
- **After:** One coordinated effort spanning data collection, model building, national hosting, voice-stack expertise and a state deployment channel.

## Why it is reusable

It tells the next adopter to look for existing efforts on the same language before starting — and that an orchestrator who can see both sides may matter more than another capability. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
