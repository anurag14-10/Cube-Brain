---
name: Scope the live assistant to answer only what the institution is prepared to stand behind
type: unit
schema_version: 2
summary: Limit a government-branded Bhili voice helpline strictly to farming questions, declining scheme,
  market-rate and other out-of-scope queries — every answer speaks in the department's name.
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
  ref: sub_category assigned by reading the unit against concepts/institution.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: bhili-language-enablement
unit_type: Strategic Decision
dimension: institution
sub_category: institution-c
stage: pilot
source_unit_id: Unit 6
applies_when: The deployment speaks with institutional authority (a government brand, a named department)
  and answering wrongly carries more cost than answering narrowly.
fails_when: The deployment is explicitly framed as general-purpose or experimental, where users expect
  and tolerate broader, less certain answers.
decision: Limit the deployed helpline's answers strictly to farming-related questions, explicitly declining
  market-rate, scheme, or other out-of-scope queries rather than attempting a general-purpose answer.
alternative_considered: Answering broadly across whatever the caller asked, using general capability rather
  than a scoped mandate.
reason: A government-branded voice service speaks in the department's name — every answer it gives is
  one the department has to be able to stand behind, so scope has to match what's actually been validated,
  not what the model happens to be able to generate.
before: Not documented in the source
after: In live field tests the helpline answered a cotton-pest question directly, stated "I will answer
  only farming-related questions" and declined a scheme question in the same call, and said a same-day
  mandi price was not available rather than approximating one.
adopter_intents:
- How do I get people to trust a government-branded voice AI enough to use it?
- Should our AI assistant try to answer anything a user asks?
- What did a real user's first live call with the system actually look like?
related_units:
- mahavistaar-speaks-as-the-institution
---

## Unit

According to EkStep Foundation's Bhili Language Enablement pathway, this is a strategic decision from the deployment.

**Decision.** Limit the deployed helpline's answers strictly to farming-related questions, explicitly declining market-rate, scheme, or other out-of-scope queries rather than attempting a general-purpose answer.

**Alternative considered.** Answering broadly across whatever the caller asked, using general capability rather than a scoped mandate.

**Why.** A government-branded voice service speaks in the department's name. Every answer it gives is one the department has to be able to stand behind, so scope has to match what has actually been validated, not what the model happens to be able to generate.

**What it looked like.** In a live field demonstration, a farmer asked about a cotton pest and a scheme in the same call; the system answered the farming question directly and stated plainly, "I will answer only farming-related questions," declining the scheme question rather than guessing. In a separate live test, asked for a same-day mandi price it had no current data for, it said the information wasn't available rather than approximating an answer. The pathway names these field tests as the only direct evidence of the live system's real-user behaviour, and notes as a gap that no mechanism is documented for a Bhili speaker to flag a wrong or unhelpful answer back to the model-building team.

## Condition

- **Applies when:** The deployment speaks with institutional authority (a government brand, a named department) and answering wrongly carries more cost than answering narrowly.
- **Fails when:** The deployment is explicitly framed as general-purpose or experimental, where users expect and tolerate broader, less certain answers.

## Before → after

- **Before:** Not documented in the source
- **After:** In live field tests the helpline answered a cotton-pest question directly, stated "I will answer only farming-related questions" and declined a scheme question in the same call, and said a same-day mandi price was not available rather than approximating one.

## Why it is reusable

It gives the next adopter a scoping rule tied to institutional accountability rather than model capability, with field evidence of what the refusal sounds like to a caller. It is a suggestion from another adoption's lived experience, to be checked against the condition tag above.
