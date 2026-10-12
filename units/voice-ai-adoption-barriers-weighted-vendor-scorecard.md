---
name: Weighted vendor-scoring rubric — score vendors on your own use case, not their demo
type: unit
schema_version: 2
summary: A five-criterion weighted scorecard (ease of adoption 15%, conversation quality 30%, domain knowledge
  and operational support 30%, compliance 10%, pricing 20%), each owned by a named function, under which a
  technically weaker vendor with stronger domain support can win.
doc_refs:
- content/wiki/pathways/voice-ai-adoption-barriers.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/voice-ai-adoption-barriers.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against concepts/<dimension>.md — the document tags dimension,
    stage and type only
contested:
- field: unit_type
  readings:
  - 'Grounding copy, Section 3 Unit 3: Playbook.'
  - 'Grounding copy, Section 4 row 3: Toolkit Asset (weighted vendor-scoring rubric).'
  note: Recorded as Toolkit Asset — the content is a weighted rubric (an artifact), not a gated sequence; one
    unit covers both the Section 3 unit and the Section 4 row.
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: voice-ai-adoption-barriers
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-c
stage: define
source_unit_id: Unit 3
applies_when: Selecting a vendor for any deployment expected to run past a short demo.
fails_when: The use case is trivial enough (Level 0 or 1 on the use-case complexity ladder) that vendor differentiation
  barely matters.
purpose: 'Evaluate voice AI vendors against your own use case and language rather than a demo or a referral,
  on a weighted scorecard: ease of adoption and integration (default 15%, owned by IT/Engineering/Ops — weight
  higher for lean tech teams); conversation quality (30%, owned by IT/Engineering — sub-1500ms latency, accuracy,
  TTS naturalness, blind listening tests on your own use case); domain knowledge and operational support (30%,
  owned by Ops/CX — reliability at scale, SLAs, dashboards, vendor track record); compliance and data protection
  (10%, owned by Legal — weight higher for regulated or government use cases); pricing/commercials (20%, owned
  by Finance — transparent pricing, ROI versus current process, fully loaded cost).'
reuse_condition: Applies to any organisation evaluating multiple voice AI vendors; default weights are a starting
  point, adjust per organisational context (lean tech teams weight ease-of-adoption higher; regulated or government
  use cases weight compliance higher).
adopter_intents:
- How do we choose between voice AI vendors?
related_units:
- voice-ai-adoption-barriers-use-case-complexity-ladder
- voice-ai-adoption-barriers-use-case-before-vendor
---

## Unit

According to EkStep Foundation / People+AI's Voice AI Adoption Barriers pathway, the asset is: evaluate voice AI vendors against your own use case and language rather than a demo or a referral, on a weighted scorecard: ease of adoption and integration (default 15%, owned by IT/Engineering/Ops — weight higher for lean tech teams); conversation quality (30%, owned by IT/Engineering — sub-1500ms latency, accuracy, TTS naturalness, blind listening tests on your own use case); domain knowledge and operational support (30%, owned by Ops/CX — reliability at scale, SLAs, dashboards, vendor track record); compliance and data protection (10%, owned by Legal — weight higher for regulated or government use cases); pricing/commercials (20%, owned by Finance — transparent pricing, ROI versus current process, fully loaded cost).

**Reuse condition:** Applies to any organisation evaluating multiple voice AI vendors; default weights are a starting point, adjust per organisational context (lean tech teams weight ease-of-adoption higher; regulated or government use cases weight compliance higher).

**Worked example.** A vendor with superior raw conversation quality can still lose on total score to a vendor with weaker technology but stronger domain experience and operational support — in one sample scoring exercise, a technically stronger vendor (5/5 on conversation quality but 2/5 on domain/ops support) scored 3.2 overall against a technically weaker vendor's 3.6.

**What skipping it cost.** Digital Labour Chowk chose a vendor for its analytics dashboard and discovered only after deployment that it could not handle the dialects of the workers it needed to reach; Haqdarshak chose a vendor based on responsiveness during the discovery call, without ever running an accuracy test on the Hindi-English-Marathi code-switching its real users actually speak.

## Condition

- **Applies when:** Selecting a vendor for any deployment expected to run past a short demo.
- **Fails when:** The use case is trivial enough (Level 0 or 1 on the use-case complexity ladder) that vendor differentiation barely matters.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

It is an artifact a next adopter can lift and adapt directly, within the reuse condition above. It is a suggestion from other adoptions' lived experience, not a recommendation.
