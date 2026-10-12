---
name: Name one accountable owner inside the organisation before selecting a vendor
type: unit
schema_version: 2
summary: Name a single person inside the adopting organisation who is accountable for the voice AI deployment
  before any vendor conversation — every organisation in the synthesis that reached a working deployment had
  this role filled early.
doc_refs:
- content/wiki/pathways/voice-ai-adoption-barriers.md
- content/library-wiki/pathways/voice-ai-adoption-barriers.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/voice-ai-adoption-barriers.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/voice-ai-adoption-barriers.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against concepts/<dimension>.md — the document tags dimension,
    stage and type only
contested:
- field: dimension
  readings:
  - 'Grounding copy: Persona × Explore (Unit 1).'
  - 'Library copy: "Assign a single accountable owner to lead the deployment end-to-end" sits under Operating
    Model × Define, alongside a PMU-style approach with regular vendor collaboration.'
  note: Tags follow the grounding copy, the framework-structured primary source.
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: voice-ai-adoption-barriers
unit_type: Strategic Decision
dimension: persona
sub_category: persona-a
stage: explore
source_unit_id: Unit 1
applies_when: An organisation is past the "should we try voice AI" stage and genuinely committing resources
  to a deployment.
fails_when: A very early, low-stakes exploratory test where formalising ownership this early would be premature.
decision: Identify a single person within the adopting organisation who is accountable for the voice AI deployment's
  success or failure, before any vendor conversation begins — not a committee, not "the tech team" generically,
  one named person.
reason: Every organisation in this synthesis that reached a working deployment had this role filled early;
  where it was missing, initial enthusiasm reliably stalled once the vendor demo phase ended and the harder,
  ongoing work began.
context: 'Ambak''s own framing of what closing their qualification-accuracy gap actually took: "You need one
  dedicated, smart resource who can monitor calls and run QA day in and day out. That''s the real cost" — not
  a one-time technology cost, a standing role.'
before: Across the organisations synthesised, where no single owner was named, initial enthusiasm stalled once
  the vendor demo phase ended and the ongoing work began.
after: Every organisation in the synthesis that reached a working deployment had this role filled early.
adopter_intents:
- We have a vendor and a budget but no one seems to own this internally
related_units:
- voice-ai-adoption-barriers-interest-is-not-readiness
---

## Unit

According to EkStep Foundation / People+AI's Voice AI Adoption Barriers pathway, this is a strategic decision drawn from the organisations it synthesises.

**Decision.** Identify a single person within the adopting organisation who is accountable for the voice AI deployment's success or failure, before any vendor conversation begins — not a committee, not "the tech team" generically, one named person.

**Why.** Every organisation in this synthesis that reached a working deployment had this role filled early; where it was missing, initial enthusiasm reliably stalled once the vendor demo phase ended and the harder, ongoing work began.

**Context.** Ambak's own framing of what closing their qualification-accuracy gap actually took: "You need one dedicated, smart resource who can monitor calls and run QA day in and day out. That's the real cost" — not a one-time technology cost, a standing role.

## Condition

- **Applies when:** An organisation is past the "should we try voice AI" stage and genuinely committing resources to a deployment.
- **Fails when:** A very early, low-stakes exploratory test where formalising ownership this early would be premature.

## Before → after

- **Before:** Across the organisations synthesised, where no single owner was named, initial enthusiasm stalled once the vendor demo phase ended and the ongoing work began.
- **After:** Every organisation in the synthesis that reached a working deployment had this role filled early.

## Why it is reusable

The condition tag says when this choice held across the organisations synthesised; the before→after shows what the other choice cost. It is a suggestion from other adoptions' lived experience, not a recommendation.
