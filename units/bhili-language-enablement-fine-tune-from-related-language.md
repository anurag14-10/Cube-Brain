---
name: Fine-tune a full ASR/NMT/TTS stack from a related higher-resource language model
type: unit
schema_version: 2
summary: Build Dehwali Bhili's speech stack by fine-tuning an existing Marathi model rather than training
  from scratch — and insist on a full model including speech recognition, which raised the training estimate
  roughly 2.5x.
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
  ref: sub_category assigned by reading the unit against concepts/solution.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: bhili-language-enablement
unit_type: Tactical Decision
dimension: solution
sub_category: solution-c
stage: define
source_unit_id: Unit 3
applies_when: A genuinely low-resource language has a linguistically related, higher-resource neighbour
  language with existing model infrastructure to bootstrap from.
fails_when: No related higher-resource language model exists to fine-tune from, or the target language's
  structure diverges too far from any available base model.
decision: Build Dehwali Bhili's ASR/NMT/TTS stack by fine-tuning an existing Marathi model rather than
  training new architecture from scratch.
alternative_considered: An earlier working assumption budgeted for only a translation (NMT) and text-to-speech
  (TTS) model, leaving out a full speech-recognition (ASR) component.
reason: A technical reviewer insisted the effort "will not have anything that's not a full model" — meaning
  ASR had to be included for the system to be genuinely usable by voice, not just text.
before: An earlier working assumption budgeted for only NMT and TTS models, with no ASR component.
after: A full ASR/NMT/TTS stack fine-tuned from an existing Marathi model. Adding ASR raised the model-training
  cost estimate roughly 2.5x, which briefly stalled budget approval until the data-collection partner
  (Karya) agreed to help absorb the difference.
adopter_intents:
- Should we train our own model from scratch for a low-resource language?
related_units:
- bhili-language-enablement-design-for-telephony-audio
---

## Unit

According to EkStep Foundation's Bhili Language Enablement pathway, this is a tactical decision from the deployment.

**Decision.** Build Dehwali Bhili's ASR/NMT/TTS stack by fine-tuning an existing Marathi model rather than training new architecture from scratch.

**Alternative considered.** An earlier working assumption budgeted for only a translation (NMT) and text-to-speech (TTS) model, leaving out a full speech-recognition (ASR) component.

**Why.** A technical reviewer insisted the effort "will not have anything that's not a full model" — ASR had to be included for the system to be genuinely usable by voice, not just text.

**What it looked like.** Adding the ASR component raised the model-training cost estimate by roughly 2.5×. That briefly stalled budget approval until the data-collection partner, Karya, agreed to help absorb the difference — in the district collector's account, "if there's extra money, we'll pitch in — it's important that it be done." The pathway's cost section adds that model training was subsidised by AI4Bharat in exchange for open data access, not a cash cost to the district.

## Condition

- **Applies when:** A genuinely low-resource language has a linguistically related, higher-resource neighbour language with existing model infrastructure to bootstrap from.
- **Fails when:** No related higher-resource language model exists to fine-tune from, or the target language's structure diverges too far from any available base model.

## Before → after

- **Before:** An earlier working assumption budgeted for only NMT and TTS models, with no ASR component.
- **After:** A full ASR/NMT/TTS stack fine-tuned from an existing Marathi model; adding ASR raised the training estimate roughly 2.5× and briefly stalled approval until Karya helped absorb the difference.

## Why it is reusable

Two choices an adopter faces early are made here together: bootstrap from a related language rather than build from zero, and do not drop speech recognition to save money if users will reach the service by voice. The cost consequence is stated so it can be planned for. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
