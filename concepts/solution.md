---
name: Solution
type: concept
schema_version: 2
aliases:
- Solution
- Solution dimension
- solution-a
- Solution A
- AI Fit and Comparative Advantage
- solution-b
- Solution B
- UX, Channel, and Integration
- solution-c
- Solution C
- Model, Architecture, and Infrastructure
- solution-d
- Solution D
- Data and Knowledge Readiness
- solution-e
- Solution E
- Performance, Reliability, and Scale
- solution:Explore
- solution:Define
- solution:Pilot
- solution:Scale
summary: Are we building the right system to solve it?
concept_kind: dimension
definition: Solution — Are we building the right system to solve it?
audience: public-vocabulary
broader: grid
central_question: Are we building the right system to solve it?
shift: From choosing a model to designing a reliable and adaptable system
thesis_group: build-the-right-thing
order: 2
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/dimensions.ts
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/framework.md
doc_refs:
- lib/dimensions.ts
- content/framework.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Definition

Are we building the right system to solve it?

*From choosing a model to designing a reliable and adaptable system*

## Sub-categories

Units are tagged `sub_category: solution-<letter>`. Weight per stage: primary =
ask directly, secondary = only if surfaced, dormant = never initiate. The
letters are internal-only.

| Code | Variable | Sub-category | Explore | Define | Pilot | Scale |
|---|---|---|---|---|---|---|
| A | `solution-a` | AI Fit and Comparative Advantage | primary | secondary | dormant | dormant |
| B | `solution-b` | UX, Channel, and Integration | secondary | primary | primary | secondary |
| C | `solution-c` | Model, Architecture, and Infrastructure | secondary | primary | primary | primary |
| D | `solution-d` | Data and Knowledge Readiness | secondary | primary | primary | primary |
| E | `solution-e` | Performance, Reliability, and Scale | dormant | secondary | primary | primary |

### A. AI Fit and Comparative Advantage

- What capability is required: language understanding, speech, vision, prediction, recommendation, generation, or autonomous action?
- Why is AI appropriate for this problem?
- What was the pre-AI approach?
- What outcome can AI improve that could not be improved sufficiently through process redesign, digitisation, rules, or conventional software?
- What evidence would show that AI is materially moving the needle?

### B. UX, Channel, and Integration

- Through what channel will the persona encounter the solution: phone, app, messaging, assisted interface, or an existing institutional system?
- Why is that channel appropriate for this persona?
- Which existing systems, databases, workflows, and APIs must it integrate with?
- What happens when an upstream system, data source, or external service is unavailable?
- Where does a human enter, review, or take over the journey?
- How will the experience communicate uncertainty, delay, refusal, or failure to the user?

### C. Model, Architecture, and Infrastructure

- What level of model capability is adequate for the problem?
- What constraints determine the model choice: quality, language support, latency, cost, privacy, or sovereignty?
- What are the choices of compute, hosting, and deployment environment?
- Which architecture decisions would be difficult or expensive to reverse?
- Which components must remain modular and replaceable?
- What is the vendor posture, and how will lock-in be avoided or managed?
- What must remain within the institution, and what may travel to an external model or service?

### D. Data and Knowledge Readiness

- What data and institutional knowledge does the system require?
- Does each source exist in a usable, machine-readable form?
- How current, complete, and representative must each source be?
- How will stale, conflicting, incomplete, or incorrect data be detected?
- Who maintains the technical pipeline that keeps the data available and current?
- What data is collected from users, and is all of it necessary?
- What data stays with the institution, and what is shared with models, vendors, or partners?

### E. Performance, Reliability, and Scale

- What does "good enough" performance mean for this particular use case?
- How will quality be evaluated before and during deployment?
- Which failures are model failures, data failures, integration failures, scope failures, or experience failures?
- What are the latency, availability, and cost-per-interaction requirements?
- Which component is currently causing the most pain, and can it be replaced independently?
- How does performance change across languages, user groups, environments, and scale?
- How will the system be monitored, evaluated, and improved after launch?

## Grid cells

Keyed `solution:<Stage>` in a pathway's `coverage` and in the app's `designs.grid_state`.

### Solution × Explore — `solution:Explore`

- **Core question:** What channel or system are you replacing, what does it fail at, and is AI actually the right tool for that failure?
- **Listening for:** Two human callers, paper forms, nothing — plus honest reasoning on AI-fit vs simpler fixes.
- **Insight form:** Current channel + failure mode + AI-fit justification
- **Corpus example:** Blue Dots: an ITI field visit in Dharwad found four in five job seekers had no resume, and employers advertised on posters, poles, and auto-rickshaws — not portals. That redirected the team to voice before a line of code was written. ([pathway](../pathways/blue-dots.md))
- **Primary sub-categories here:** A

### Solution × Define — `solution:Define`

- **Core question:** Which architecture choices, if wrong, would take six months to undo — and is every data source named, with an accountable owner for each?
- **Listening for:** Residency, vendor lock-in, sovereignty, orchestration ownership. Not "government data" — ICAR, IMD, APMC, named humans.
- **Insight form:** Irreversible decisions list + data source registry (source × owner × cadence × accountability)
- **Corpus example:** Blue Dots: building open, UPI-style shared rails instead of a platform any one organisation owns is named directly as the single most consequential, hardest-to-reverse decision in the pathway. ([pathway](../pathways/blue-dots.md))
- **Primary sub-categories here:** B, C, D

### Solution × Pilot — `solution:Pilot`

- **Core question:** Which component is causing the most pain, is it replaceable, and which data source is going stale or wrong?
- **Listening for:** Bundled-vs-unbundled plays out here. Data quality failures at Pilot look like AI failures to users.
- **Insight form:** Component failure + replaceability + data quality issue + owner response time
- **Corpus example:** MahaVISTAAR: mandi price 48hr lag caused wrong harvest-timing advice. Fix: governance call with APMC to 6-hr cadence — not a technical fix. ([pathway](../pathways/mahavistaar.md))
- **Primary sub-categories here:** B, C, D, E

### Solution × Scale — `solution:Scale`

- **Core question:** Which components are you now unbundling, what triggered it — and which data sources are breaking under scale, do formal SLAs exist?
- **Listening for:** Cost/control arguments become concrete numbers at scale.
- **Insight form:** Unbundling decision (component × trigger × gain) + data SLA map
- **Corpus example:** Voice AI for Inclusion: Bharat-VISTAAR required formal data SLAs with 12 state agriculture departments. Each became an accountable node, not just a data source. ([pathway](../pathways/voice-ai-for-inclusion.md))
- **Primary sub-categories here:** C, D, E

## Data and trust here

- **Data:** is data usable/reliable/current
- **Trust:** is trust conveyed through channel/UX choices — tone, disclosure, voice vs. text

## How it is used

Every unit carries `dimension: solution`; the dimension name is public
vocabulary, the sub-category letters are not.
