---
name: AxL — AI for Foundational Literacy and Numeracy
type: pathway
schema_version: 2
aliases:
- AxL — AI for Foundational Literacy and Numeracy
- AxL
- Assisted Language and Math Learning
summary: How EkStep Foundation's misconception-based adaptive learning system personalises foundational
  reading and math practice for struggling students across 18,000+ government schools in India
tags:
- Foundational Learning
- EdTech
- Adaptive Practice
- Public School Systems
title: AxL — AI for Foundational Literacy and Numeracy
pathway_kind: single-deployment
sector: Education
use_case_category: Foundational Literacy and Numeracy — adaptive practice in public-school systems
geography: India; active state-led deployments in Telangana, Karnataka (Kalika Deepa programme) and Delhi;
  broader footprint across Sikkim, Assam and 10+ states in total
population_served: Children in grades 3–8 in public-school systems who are below grade-level proficiency
  in foundational reading or numeracy, particularly in heterogeneous classrooms where grade-based instruction
  cannot reach them
stage_reached: scale
contributing_organisations:
- ekstep-foundation
partner_organisations:
- ai4bharat
- iisc
- bodhan-ai
key_dates: AML interview conducted September 2026; AxL for WB deck dated July 2026; Bodhan.ai partnership
  noted as established 2025–2026
scale_impact: 18,000+ schools across 10+ states (as of July 2026); ~70% of children flagged as lagging
  behind across 1,400 schools showed improvement after 8–10 sessions; AML entry-to-exit diagnostic scores
  improved from ~29% to ~52%; a teacher/headmaster survey of 617 respondents reported an average improvement
  of 5+ behavioural traits per student; 20 million+ question-answer pairs collected
cost_anchor: Under ₹10 per child per year running cost for AML (as of September 2026), excluding fixed
  product development cost borne by EkStep; no equivalent figure documented for ALL
build_effort: Three years from inception to current scale (as of September 2026); team size and partner
  count not documented in the source
coverage:
  persona:Explore: 2
  persona:Define: 2
  persona:Pilot: 2
  persona:Scale: 1
  solution:Explore: 2
  solution:Define: 2
  solution:Pilot: 2
  solution:Scale: 2
  institution:Explore: 2
  institution:Define: 2
  institution:Pilot: 1
  institution:Scale: 2
  ecosystem:Explore: 1
  ecosystem:Define: 2
  ecosystem:Pilot: 1
  ecosystem:Scale: 1
gaps:
- 'Ecosystem × Explore — precedent and alternative landscape (relates to Units 1, 11): The sources establish
  what AxL is and why EkStep built it, but do not document what other approaches were evaluated or attempted
  before AxL, or which precedent deployments the team examined. A new adopter cannot determine what distinguishes
  AxL''s approach from existing EdTech alternatives they may already know.'
- 'Institution × Pilot — first public failure and institutional response (relates to Unit 6): The sources
  describe what broke technically and pedagogically in early deployments, but do not document a specific
  instance of a public-facing failure, who owned it, and what the institutional response was. The insight
  form this cell requires — first public failure + institutional response (own vs. disown) — is not addressed.'
- 'Persona × Scale — new user segments appearing beyond the original design (relates to Unit 5): The Delhi
  CM SHRI finding (Unit 9) reveals schools adapting the programme in unexpected ways, but the sources
  do not document whether new learner populations, for example older students, different languages, or
  students with specific learning needs, have appeared at scale that the original design did not anticipate,
  or what design changes those required.'
- 'Ecosystem × Pilot — partner underperformance and contingency (relates to Unit 11): The sources name
  ecosystem partners but do not document whether any partner underperformed during the pilot phase, whether
  alternatives were considered, or what contingency exists if a key partner (e.g. ASR provider, infrastructure
  partner) exits or changes terms.'
- 'Ecosystem × Scale — FLN DPI and transferability conditions (relates to Unit 12): The FLN DPI effort
  with Bodhan.ai is described as early-stage, with two governing principles (minimal and interoperable),
  but what a future adopter would need to do differently to contribute to or draw from that infrastructure
  — versus building separately — is not documented.'
- 'Solution × Pilot — ASR failure taxonomy for ALL specifically (relates to Unit 6): The sources describe
  what broke in reading (ASR, noise, microphone variation, pronunciation) but do not provide the equivalent
  of AML''s misconception-error taxonomy for reading — specifically, how ASR errors were classified, which
  were recoverable by design change versus model improvement, and what the threshold was for switching
  to non-ASR pathways.'
- 'Institution × Pilot — content authority and approval process (relates to Unit 8): Who approves what
  the system is permitted to say or recommend at the pilot stage — specifically, which SCERT/NCERT role
  has sign-off authority on the misconception taxonomy and question content — is not documented beyond
  a general statement that state instances can be customised.'
- 'Ecosystem × Explore — AI4Bharat / IISc / Bodhan.ai relationship (relates to Unit 11): The sources name
  three distinct technical and research partners but do not explain how their roles are divided or how
  overlaps are managed. A new adopter cannot replicate the partner architecture without knowing which
  capability each partner actually supplies.'
corpora:
- grounding-corpus
doc_refs:
- content/wiki/pathways/assisted-language-math-learning.md
lifecycle: unindexed
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/assisted-language-math-learning.md
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/assisted-language-math-learning.md — Sections 1–2 (identity, effort, coverage
    grid, gaps)
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Identity

According to EkStep Foundation's AxL pathway, AxL (Assisted Language and Math Learning) is an AI-powered foundational literacy and numeracy programme made of three parts: ALL (Assisted Language Learning, for foundational reading), AML (Assisted Math Learning, for foundational numeracy) and the AxL Companion for teachers. It runs one repeating loop, Measure → Diagnose → Personalise → Practise → Assess → Adapt → Intervene, around a single AI question asked fresh for every learner in every session: *what should this specific learner practise next?*

- **Sector:** Education — Foundational Literacy and Numeracy
- **Geography:** India; active state-led deployments in Telangana, Karnataka (Kalika Deepa programme) and Delhi; broader footprint across Sikkim, Assam and 10+ states in total
- **Population served:** Children in grades 3–8 in public-school systems who are below grade-level proficiency in foundational reading or numeracy, particularly in heterogeneous classrooms where grade-based instruction cannot reach them
- **Stage reached:** [Scale](../concepts/scale.md)
- **Key dates:** AML interview September 2026; AxL for WB deck July 2026; Bodhan.ai partnership established 2025–2026

Contributed by: EkStep Foundation. Key partners named in the document: AI4Bharat (Dhruva infrastructure), IISc Centre for Neuroscience (learning-task design) and Bodhan.ai (FLN AI research and scale, Government of India AI CoE for Education). State education departments own implementation after deployment.

The document is written for state education departments and SCERT/NCERT stakeholders, for technology teams deciding what to build, integrate or reuse in an adaptive learning system, and for implementation partners and school leaders who need the deployment sequence and teacher workflow.

**Scope — applies when.** Children are several learning levels apart within the same classroom; instruction is organised by grade rather than demonstrated proficiency; teachers cannot provide continuous one-to-one diagnosis; schools have functioning computer labs with internet access.

**Does not transfer when.** Learners are already grouped by demonstrated ability; the content gap is not foundational literacy or numeracy; schools lack functioning computer labs or internet connectivity; no state-level leadership buy-in exists.

## Effort

- **Scale / impact achieved:** 18,000+ schools across 10+ states (as of July 2026). About 70% of children flagged as lagging behind across 1,400 schools improved after 8–10 sessions; AML entry-to-exit diagnostic scores rose from about 29% to about 52%; a teacher/headmaster survey of 617 respondents reported an average improvement of 5+ behavioural traits per student; 20 million+ question-answer pairs collected.
- **Cost anchor:** Under ₹10 per child per year running cost for AML (as of September 2026), excluding the fixed product development cost borne by EkStep. No equivalent figure is documented for ALL.
- **Build effort:** Three years from inception to current scale (as of September 2026). Team size and partner count are not documented in the source.
- **Downstream adoptions:** Not documented in the source.

## Coverage

From the document's own coverage grid (Section 2):

| | Explore | Define | Pilot | Scale |
|---|---|---|---|---|
| Persona | ●● | ●● | ●● | ● |
| Solution | ●● | ●● | ●● | ●● |
| Institution | ●● | ●● | ● | ●● |
| Ecosystem | ● | ●● | ● | ● |

Coverage is even across [Persona](../concepts/persona.md) and [Solution](../concepts/solution.md). The thinnest cells are [Institution](../concepts/institution.md) at Pilot and [Ecosystem](../concepts/ecosystem.md) at Explore, Pilot and Scale.

## Gaps

The document names eight gaps:

1. **Precedent and alternative landscape (Ecosystem × Explore).** What other approaches were evaluated or attempted before AxL, and which precedent deployments the team examined, is not documented.
2. **First public failure and institutional response (Institution × Pilot).** No specific public-facing failure, who owned it, or how the institution responded is documented.
3. **New user segments at scale (Persona × Scale).** Schools adapted the programme in unexpected ways (the Delhi CM SHRI finding), but whether new learner populations appeared, and what design changes they required, is not documented.
4. **Partner underperformance and contingency (Ecosystem × Pilot).** Whether any partner underperformed, whether alternatives were considered, and what happens if a key partner such as the ASR provider exits, is not documented.
5. **FLN DPI and transferability (Ecosystem × Scale).** The FLN DPI effort with Bodhan.ai is early-stage (minimal and interoperable); what a future adopter must do to contribute to or draw from it is not documented.
6. **ASR failure taxonomy for ALL (Solution × Pilot).** There is no reading equivalent of AML's misconception-error taxonomy: how ASR errors were classified, which were fixed by design versus model improvement, and when to switch to non-ASR pathways.
7. **Content authority and approval (Institution × Pilot).** Which SCERT/NCERT role signs off the misconception taxonomy and question content is not documented.
8. **Division of roles among AI4Bharat, IISc and Bodhan.ai (Ecosystem × Explore).** How the three partners' roles are divided and overlaps managed is not documented.

## Where the reusable value is

Twelve units, one per micro-innovation in the document. Section 4's toolkits and playbooks (the state deployment sequence, the pen-and-paper misconception data collection, the connectivity-aware batching architecture and the pseudonymous identifier architecture) are covered by units 9, 5, 7 and 12. The document's Section 5 is marked as omitted (its Failure-and-Fix units cover the material), so there are no patterns.

- **Frame the problem correctly.** [Define the problem as heterogeneity, not content scarcity](../units/assisted-language-math-learning-heterogeneity-not-content-scarcity.md) (Persona × Explore) and [Personalise on demonstrated proficiency, not grade](../units/assisted-language-math-learning-personalise-on-proficiency-not-grade.md) (Persona × Define).
- **Design around the teacher and measure the right outcome.** [Design teacher workflow as a constraint, not a feature](../units/assisted-language-math-learning-teacher-workflow-as-constraint.md) (Persona × Define) and [Reintegration into the classroom as the measured outcome](../units/assisted-language-math-learning-reintegration-as-measured-outcome.md) (Persona × Pilot).
- **Data architecture before models.** [Build the misconception taxonomy before building the product](../units/assisted-language-math-learning-misconception-taxonomy-before-product.md) (Solution × Explore) and [Treat the learner-data architecture as harder to recover from than any model](../units/assisted-language-math-learning-learner-data-architecture-first.md) (Solution × Define).
- **Engineer for real schools.** [Batch API calls to survive intermittent connectivity, and run on CPUs](../units/assisted-language-math-learning-batched-calls-cpu-first.md) (Solution × Define), the source of the under-₹10 running cost.
- **The key failure and fix.** [The smallest unit of failure is the learner interaction, not the model call](../units/assisted-language-math-learning-learner-interaction-failure-unit.md) (Solution × Pilot).
- **Deploy through the state and hand it over.** [The state deployment sequence is fixed and largely non-compressible](../units/assisted-language-math-learning-state-deployment-sequence.md) (Institution × Define) and [Ownership transfers fully to the state](../units/assisted-language-math-learning-full-state-ownership-narrow-role.md) (Institution × Scale).
- **Partners and children's data.** [Name a partner for every capability you cannot supply](../units/assisted-language-math-learning-named-partner-per-capability.md) (Ecosystem × Explore) and [Separate the learner's identity from the learner's data](../units/assisted-language-math-learning-separate-identity-from-learner-data.md) (Ecosystem × Define).

## Corpus copies

- `content/wiki/pathways/assisted-language-math-learning.md`

On disk in the grounding corpus but **not linked from `content/wiki/pathways/index.md`**, so excluded from grounding and the /wiki listing. It may still be live via `published_pathways` — check the DB before calling it unpublished.
