---
name: AI-assisted Job Matching for Rural Youth
type: pathway
schema_version: 2
aliases:
- AI-assisted Job Matching for Rural Youth
summary: A browser-based AI-assisted job-matching tool that surfaces and explains candidate recommendations
  from a large MIS-held pool for placement coordinators in a State Rural Livelihoods Mission. Coordinators
  decide, not the system. Piloting in two districts with staged activation and explicit human override.
tags:
- Livelihoods
- Job matching
title: AI-assisted Job Matching for Rural Youth
pathway_kind: single-deployment
sector: Livelihoods
use_case_category: skill development and employment support
geography: Two pilot districts (District A, District B) of one State Rural Livelihoods Mission; the state
  is not named in the source
population_served: Placement coordinators in a State Rural Livelihoods Mission, matching candidates from
  a large MIS-held pool of rural youth to vacancies that may span several trades or districts
stage_reached: pilot
contributing_organisations:
- ekstep-foundation
contributors:
- kamesh
key_dates: Document v2 dated 2026-08-21; pilot activation in progress as of August 2026
coverage:
  persona:Explore: 1
  persona:Define: 1
  persona:Pilot: 0
  persona:Scale: 0
  solution:Explore: 0
  solution:Define: 1
  solution:Pilot: 1
  solution:Scale: 0
  institution:Explore: 0
  institution:Define: 0
  institution:Pilot: 1
  institution:Scale: 0
  ecosystem:Explore: 0
  ecosystem:Define: 0
  ecosystem:Pilot: 0
  ecosystem:Scale: 0
gaps:
- Which coordinator interactions are failing in actual use, and are the failures scope problems (questions
  outside the mandate) or quality problems (poor in-mandate recommendations)? The contributor calls this
  the most important gap at the current stage. The answer decides whether the fix is better prompting, better
  data, or tighter scope boundaries. (Persona/Pilot)
- After the two-hour orientation, can coordinators correctly interpret match bands and stale-data signals,
  and tell eligibility exclusion apart from AI ranking? If not, the human-override guarantee does not
  work as intended. (Institution/Pilot)
- No Scale-stage knowledge exists in any dimension. Who owns the service operationally, what does the
  budget line look like, and how does it become part of the Mission without the founding team? (Institution/Scale,
  Ecosystem/Scale)
- The document records no know-how yet for Persona/Pilot, Persona/Scale, Solution/Explore, Solution/Scale,
  Institution/Explore, Institution/Define, Institution/Scale and Ecosystem/Explore.
corpora:
- grounding-corpus
doc_refs:
- content/wiki/pathways/ai-assisted-job-matching.md
lifecycle: unindexed
document_version: v2
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/ai-assisted-job-matching.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-assisted-job-matching.md (Sections 0–4, 6; coverage from its Section 2 grid)
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

According to EkStep Foundation's pathway, this is a browser-based AI-assisted job-matching tool for
placement coordinators in a State Rural Livelihoods Mission. For a given vacancy, it surfaces candidate
recommendations from a large MIS-held candidate pool and explains them. Coordinators decide; the system
does not.

**Problem it addresses:** large MIS-held candidate pools, coordinator-led placement processes, vacancies
that span several trades or districts, and newly assigned coordinators who do not personally know the
candidate pool.

**Stage reached:** [Pilot](../concepts/pilot.md). The tool is piloting in two districts with weekly MIS
data exports, staggered district activation, and explicit human override throughout.

- Sector: Livelihoods (skill development and employment support)
- Geography: two pilot districts of one State Rural Livelihoods Mission; the state is not named
- Contributed by: EkStep Foundation (Kamesh, Program Execution Partner)
- Document: v2, dated 2026-08-21

## Effort

Build effort, team size, cost and usage figures: Not documented in the source.

What the document does give about pilot effort:

- the pilot covers two districts;
- data arrives as weekly MIS exports;
- coordinators get a two-hour orientation;
- support issues are reviewed daily for the first four weeks.

## Coverage

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| [Persona](../concepts/persona.md) | ● | ● | ○ | ○ |
| [Solution](../concepts/solution.md) | ○ | ● | ● | ○ |
| [Institution](../concepts/institution.md) | ○ | ○ | ● | ○ |
| [Ecosystem](../concepts/ecosystem.md) | ○ | ○ | ○ | ○ |

Taken from the document's own coverage grid. The two extracted units sit at Solution × Pilot and
Institution × Pilot. The document marks Persona × Explore, Persona × Define and Solution × Define as
covered, but its Section 3 has no units at those cells.

## Gaps

- **Coordinator failures in actual use (Persona/Pilot).** Which coordinator interactions are failing, and are the failures scope problems (questions outside the mandate) or quality problems (poor in-mandate recommendations)? The contributor calls this the most important gap at the current stage, because the answer decides whether the fix is better prompting, better data, or tighter scope boundaries.
- **Coordinator training outcome (Institution/Pilot).** After the two-hour orientation, can coordinators correctly interpret match bands and stale-data signals, and tell eligibility exclusion apart from AI ranking? If they cannot do this reliably, the human-override guarantee does not work as intended.
- **Scale (Institution/Scale, Ecosystem/Scale).** No Scale-stage knowledge exists in any dimension. The open questions are who owns the service operationally, what the budget line looks like, and how it becomes part of the Mission without the founding team. The contributor expects this gap at Pilot stage.
- **Cells with no documented know-how:** Persona/Pilot, Persona/Scale, Solution/Explore, Solution/Scale, Institution/Explore, Institution/Define, Institution/Scale and Ecosystem/Explore.

## Where the reusable value is

Two pilot-operations units, both suggestions from this deployment's experience:

- [Staged district activation with a mandatory observation gap](../units/ai-assisted-job-matching-staged-district-activation.md) (Solution × Pilot, playbook). The sequence runs synthetic-data validation, then a privacy and security review gate, then a restricted real dataset, then coordinator training. After that, District A is activated alone, and District B goes live only once District A's operational problems are fixed.
- [Eight-category pilot issue taxonomy](../units/ai-assisted-job-matching-pilot-issue-taxonomy.md) (Institution × Pilot, strategic decision). Support issues are reviewed daily and logged by category, so that model failures, data failures and software defects are told apart when they are logged. This lets the post-pilot decision to invest in data or in the model rest on clean signals.

The document has no Section 5 problem-solution patterns.

## Corpus copies

- `content/wiki/pathways/ai-assisted-job-matching.md`

This copy is on disk in the grounding corpus but **not linked from `content/wiki/pathways/index.md`**, so it is excluded from grounding and from the /wiki listing. It may still be live via `published_pathways`; check the DB before calling it unpublished.
