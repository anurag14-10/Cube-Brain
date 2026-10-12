---
name: AI-assisted Job Matching — staged district activation with a mandatory observation gap
type: unit
schema_version: 2
summary: A ten-step pilot deployment sequence — synthetic data first, a privacy and security review gate,
  a restricted real dataset, coordinator training — that activates District A alone and turns District
  B on only after District A's operational problems are fixed.
doc_refs:
- content/wiki/pathways/ai-assisted-job-matching.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-assisted-job-matching.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ai-assisted-job-matching
unit_type: Playbook
dimension: solution
sub_category: solution-e
stage: pilot
source_unit_id: Unit 4
applies_when: Multi-district or multi-geography pilot; operational problems discovered at the first site
  can be fixed before the second site goes live; pilot volume is sufficient to observe usage patterns
  within one week.
fails_when: Not documented in the source
steps:
- 1. Configure pilot infrastructure and load synthetic candidate data.
- 2. Validate the vacancy workflow end-to-end with synthetic data.
- 3. Validate eligibility rules against known test cases.
- 4. Test the matching service with synthetic candidates.
- '5. Conduct a privacy and security review. Gate: do not proceed until cleared.'
- 6. Load the restricted pilot dataset (real candidate data, limited geography).
- 7. Run internal acceptance tests.
- 8. Train placement coordinators (two-hour orientation).
- '9. Activate District A only. Gate: observe first-week usage before any further activation.'
- '10. Activate District B. Gate: only after the operational problems from District A have been addressed.'
- 'Gates between the other steps: Not documented in the source.'
common_failure_mode: Skipping the observation window to accelerate the second district's activation, which
  removes the only mechanism for catching operational problems before they affect both districts simultaneously.
adopter_intents:
- In what order should we turn on features during the pilot?
- How long should we wait between rollout stages before expanding?
- Should we launch everything at once or phase it in gradually?
related_units:
- ai-assisted-job-matching-pilot-issue-taxonomy
---

## Unit

According to EkStep Foundation's AI-assisted Job Matching for Rural Youth pathway, this is the playbook
used to sequence the pilot of a browser-based job-matching tool for placement coordinators in a State
Rural Livelihoods Mission.

**Steps (in order):**

1. Configure pilot infrastructure and load synthetic candidate data.
2. Validate the vacancy workflow end-to-end with synthetic data.
3. Validate eligibility rules against known test cases.
4. Test the matching service with synthetic candidates.
5. Conduct a privacy and security review. **Gate:** do not proceed until cleared.
6. Load the restricted pilot dataset (real candidate data, limited geography).
7. Run internal acceptance tests.
8. Train placement coordinators (two-hour orientation).
9. Activate District A only. **Gate:** observe first-week usage before any further activation.
10. Activate District B. **Gate:** only after the operational problems from District A have been addressed.

Gates between the other steps: Not documented in the source.

The contributor names the gap between District A and District B as the critical gate.

**Common failure mode.** Skipping the observation window to accelerate the second district's activation.
That removes the only mechanism for catching operational problems before they affect both districts
simultaneously.

## Condition

- **Applies when:** Multi-district or multi-geography pilot; operational problems discovered at the first site can be fixed before the second site goes live; pilot volume is sufficient to observe usage patterns within one week.
- **Fails when:** Not documented in the source

## Before → after

Not documented in the source. Pilot activation was still in progress as of August 2026.

## Why it is reusable

Two things carry over. Real candidate data is loaded only after synthetic-data validation and a privacy
and security review. The second site goes live only after the first has been observed and fixed. It is a
suggestion from another adoption's lived experience, to be checked against the condition tag above.
