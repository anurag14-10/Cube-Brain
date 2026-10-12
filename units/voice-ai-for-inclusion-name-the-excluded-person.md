---
name: Voice AI for Inclusion — name the excluded person precisely, not the demographic
type: unit
schema_version: 2
summary: Define the excluded user precisely enough to name the person and the specific constraint ("women
  farmers in remote districts who rely on small trust circles", not "farmers") — and treat reaching that
  precision as a resourced first milestone.
doc_refs:
- content/wiki/pathways/voice-ai-for-inclusion.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/voice-ai-for-inclusion.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: voice-ai-for-inclusion
unit_type: Strategic Decision
dimension: persona
sub_category: persona-a
stage: explore
source_unit_id: Unit 1
applies_when: A population genuinely exists that is excluded by language, literacy, device access, trust,
  or connectivity — the claim this pathway makes is specific to access problems, not automation or internal-efficiency
  use cases.
fails_when: Not documented in the source
decision: Define the excluded user precisely enough to name the person and the specific constraint — not
  "farmers," but "women farmers in remote districts who rely on small trust circles and cannot easily visit
  an agriculture office"; not "youth," but "interns across dispersed locations from whom fortnightly feedback
  is needed but two human callers cannot keep up."
reason: The sharper the user and problem, the easier every downstream decision becomes — channel, model,
  data, workflow, language, testing.
context: Across the deployments synthesised, this precision was sometimes itself a multi-round process
  requiring several stakeholder discussions before it converged.
before: The user named as a demographic — "farmers", "youth".
after: The user named as a person with a specific constraint — "women farmers in remote districts who rely
  on small trust circles and cannot easily visit an agriculture office"; "interns across dispersed locations
  from whom fortnightly feedback is needed but two human callers cannot keep up" — with the definition
  treated as an explicit, resourced first milestone rather than a formality to skip.
adopter_intents:
- How do I define who this is actually for?
related_units:
- voice-ai-for-inclusion-two-bar-pilot-readiness-test
---

## Unit

According to EkStep Foundation's Voice AI for Inclusion pathway — a synthesis across MahaVISTAAR, Bharat Vistaar, Amul/Sarlaben, Jal Jeevan Mission Assam, the Bhili effort, Lend A Hand and the India–Africa exchange — this is a strategic decision that recurred across the deployments.

**Decision.** Define the excluded user precisely enough to name the person and the specific constraint — not "farmers," but "women farmers in remote districts who rely on small trust circles and cannot easily visit an agriculture office"; not "youth," but "interns across dispersed locations from whom fortnightly feedback is needed but two human callers cannot keep up."

**Why.** The sharper the user and problem, the easier every downstream decision becomes — channel, model, data, workflow, language, testing.

**What this looked like.** In several of the synthesised deployments the precision was itself a multi-round process needing several stakeholder discussions before it converged — the pathway says to treat it as an explicit, resourced first milestone rather than a formality to skip.

## Condition

- **Applies when:** A population genuinely exists that is excluded by language, literacy, device access, trust, or connectivity — the claim this pathway makes is specific to access problems, not automation or internal-efficiency use cases.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** The user named as a demographic — "farmers", "youth".
- **After:** The user named as a person with a specific constraint, and the definition resourced as the first milestone.

## Why it is reusable

It recurred across several independent teams, which the pathway treats as a stronger signal that it generalises. It is a suggestion from other adoptions' lived experience, not a recommendation — check the condition tag first.
