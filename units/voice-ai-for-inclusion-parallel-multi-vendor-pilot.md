---
name: Voice AI for Inclusion — shortlist and test multiple vendors in parallel during the pilot
type: unit
schema_version: 2
summary: Run more than one voice-AI vendor in parallel during the pilot (a closed sandbox where government
  empanelment blocks it) before committing — usage-based pricing put the premium at roughly 2–5% in one
  deployment; start bundled, unbundle only after the pilot.
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
    stage and type only; the step order is read from the unit's note text, which the document does not number
first_logged: '2026-10-12'
last_updated: '2026-10-12'
contested:
- field: stage
  readings:
  - 'grounding corpus (content/wiki/pathways/voice-ai-for-inclusion.md): Solution × Define'
  - 'library corpus (content/library-wiki/pathways/voice-ai-for-inclusion.md): placed under Technology
    × Pilot ("Shortlist multiple vendors and test in parallel during the pilot")'
  note: The grounding copy is framework-structured and is the primary source; the unit keeps define. Library
    placement recorded, not arbitrated.
pathway: voice-ai-for-inclusion
unit_type: Playbook
dimension: solution
sub_category: solution-c
stage: define
also_relevant_at:
- pilot
source_unit_id: Unit 3
applies_when: A pilot is genuinely still deciding on a long-term vendor, and usage-based pricing makes parallel
  testing affordable.
fails_when: Procurement rules make any parallel testing genuinely infeasible even in a sandbox, or the vendor
  decision is already fixed by an existing institutional relationship.
steps:
- 1. Teams starting from zero with limited in-house capability start on a single bundled end-to-end provider
  (India's ecosystem has dozens active in Indic languages).
- 2. During the pilot, shortlist and run more than one vendor in parallel, splitting call volume across
  providers — compare under similar conditions, watch which adapts fastest to feedback, and use the competition
  on cost and quality.
- 3. In government procurement, where single-vendor empanelment makes formal multi-vendor testing difficult,
  run a closed sandbox test ahead of formal procurement instead.
- 4. 'Gate: commit to a long-term vendor only once real comparative data exists.'
- 5. Once past pilot and wanting more control, unbundle — procure and evaluate telephony, speech and language
  model separately.
common_failure_mode: Committing to one vendor before real comparative data exists — picked from a demo
  — and getting stuck mid-way (the lock-in risk parallel testing removes).
adopter_intents:
- Should we commit to one vendor now, or test several?
related_units:
- voice-ai-for-inclusion-open-orchestration-as-infrastructure
---

## Unit

According to EkStep Foundation's Voice AI for Inclusion pathway, this is a playbook (Section 4 lists it as "Parallel multi-vendor pilot testing, including the government sandbox pattern").

**Steps (in order):**

1. Teams starting from zero with limited in-house capability start on a single bundled end-to-end provider — India's ecosystem has dozens active in Indic languages.
2. During the pilot, shortlist and run more than one vendor in parallel, splitting call volume across providers: real comparison under similar conditions, visibility of which vendor adapts fastest to feedback, competitive pressure on cost and quality.
3. In government procurement, where single-vendor empanelment makes formal multi-vendor testing difficult, run a closed sandbox test ahead of formal procurement — the pattern several source deployments used.
4. **Gate:** commit to a long-term vendor only once real comparative data exists.
5. Once past pilot and wanting more control, unbundle — telephony, speech and language model procured and evaluated separately. Unbundling is not the starting point.

**Cost.** Because voice AI is usually priced by usage, splitting volume may not meaningfully increase total cost relative to the lock-in risk removed — one deployment in the synthesis measured the premium at roughly 2–5% over a single-vendor commitment.

**Common failure mode.** Committing to one vendor before real comparative data exists and getting stuck mid-way.

## Condition

- **Applies when:** A pilot is genuinely still deciding on a long-term vendor, and usage-based pricing makes parallel testing affordable.
- **Fails when:** Procurement rules make any parallel testing genuinely infeasible even in a sandbox, or the vendor decision is already fixed by an existing institutional relationship.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

The sequencing (bundled first, parallel during pilot, unbundle after) and the sandbox workaround for single-vendor empanelment are what a next adopter can lift. The document labels this a Playbook; its order is read from the unit's own text and the gates other than the commit gate are not documented. A suggestion, not a recommendation.
