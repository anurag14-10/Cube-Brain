---
name: Design voice data for the phone call users will make, not the clean recording that is easy to collect
type: unit
schema_version: 2
summary: An earlier Bhili data effort collected clean studio-style audio with no deployment or deadline
  and performed poorly in real conditions; tying it to MahaVISTAAR shifted sampling to spontaneous, conversational
  speech including 8kHz phone-call audio.
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
unit_type: Failure and Fix
dimension: solution
sub_category: solution-d
stage: define
source_unit_id: Unit 2
applies_when: The end deployment is a voice channel real users will reach by phone, especially over variable-quality
  rural connections.
fails_when: The deployment is a controlled, high-bandwidth channel where studio-quality audio genuinely
  reflects real usage conditions.
failure: An earlier, separate attempt at Bhili data collection (before EkStep's involvement) gathered clean,
  studio-style audio without a specific deployment in mind and without a hard deadline. That data performed
  poorly once tested against real conditions.
fix: Once the effort was tied to MahaVISTAAR, sampling shifted deliberately toward spontaneous, conversational
  speech, including a meaningful share captured at 8kHz phone-call quality — matched to how a rural user
  actually reaches the service, by voice call, not through a clean microphone.
insight: A model trained only on clean, studio-style audio from careful readers fails the moment it meets
  a real, noisy phone call — telephony-grade sampling has to be designed in from session one, not bolted
  on once the first version underperforms.
adopter_intents:
- Our first data collection didn't produce a usable model — why?
related_units:
- bhili-language-enablement-fine-tune-from-related-language
- bhili-language-enablement-three-tier-quality-structure
- mahavistaar-telephony-protocol-local-network
---

## Unit

According to EkStep Foundation's Bhili Language Enablement pathway, this is a failure and the fix that followed.

**Failure.** An earlier, separate attempt at Bhili data collection (before EkStep's involvement) gathered clean, studio-style audio without a specific deployment in mind and without a hard deadline. That data performed poorly once tested against real conditions.

**Fix.** Once the effort was tied to MahaVISTAAR, sampling shifted deliberately toward spontaneous, conversational speech, including a meaningful share captured at 8kHz phone-call quality — matched to how a rural user actually reaches the service, by voice call rather than a clean microphone.

**Insight.** A model trained only on clean, studio-style audio from careful readers fails the moment it meets a real, noisy phone call. Telephony-grade sampling has to be designed in from session one, not bolted on once the first version underperforms.

**What it looked like.** The district's field studio still recorded under real constraints: the pathway reports an entire day's recording batch lost to background noise, after which the studio adopted a standing rule of always producing a rough draft, a rough-final and a final pass, and re-testing the full setup before any new recording block began.

## Condition

- **Applies when:** The end deployment is a voice channel real users will reach by phone, especially over variable-quality rural connections.
- **Fails when:** The deployment is a controlled, high-bandwidth channel where studio-quality audio genuinely reflects real usage conditions.

## Before → after

- **Before:** Clean, studio-style audio collected with no deployment target and no deadline; it performed poorly against real conditions.
- **After:** Sampling weighted toward spontaneous, conversational speech with a meaningful share at 8kHz phone-call quality, matched to the MahaVISTAAR voice channel.

## Why it is reusable

The failure is common and expensive: a data-collection budget spent on audio that does not resemble what the deployed model will hear. Naming the channel before recording starts tells the next adopter what to sample. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
