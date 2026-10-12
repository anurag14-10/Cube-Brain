---
name: Institution
type: concept
schema_version: 2
aliases:
- Institution
- Institution dimension
- institution-a
- Institution A
- Mandate, Ownership, and Decision Rights
- institution-b
- Institution B
- Workforce and Change
- institution-c
- Institution C
- Governance, Safety, and Redress
- institution-d
- Institution D
- Accountability, Liability, and Compliance
- institution-e
- Institution E
- Data Stewardship
- institution-f
- Institution F
- Operating Model and Sustainability
- institution-g
- Institution G
- Institutionalisation and Continuous Improvement
- institution:Explore
- institution:Define
- institution:Pilot
- institution:Scale
summary: Can the institution own, absorb, govern, and sustain it?
concept_kind: dimension
definition: Institution — Can the institution own, absorb, govern, and sustain it?
audience: public-vocabulary
broader: grid
central_question: Can the institution own, absorb, govern, and sustain it?
shift: From sponsoring a project to owning a sustainable service
thesis_group: enable-adoption
order: 3
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

Can the institution own, absorb, govern, and sustain it?

*From sponsoring a project to owning a sustainable service*

## Sub-categories

Units are tagged `sub_category: institution-<letter>`. Weight per stage: primary =
ask directly, secondary = only if surfaced, dormant = never initiate. The
letters are internal-only.

| Code | Variable | Sub-category | Explore | Define | Pilot | Scale |
|---|---|---|---|---|---|---|
| A | `institution-a` | Mandate, Ownership, and Decision Rights | primary | primary | secondary | secondary |
| B | `institution-b` | Workforce and Change | secondary | primary | primary | primary |
| C | `institution-c` | Governance, Safety, and Redress | dormant | primary | primary | secondary |
| D | `institution-d` | Accountability, Liability, and Compliance | dormant | secondary | secondary | primary |
| E | `institution-e` | Data Stewardship | dormant | primary | secondary | primary |
| F | `institution-f` | Operating Model and Sustainability | secondary | primary | secondary | primary |
| G | `institution-g` | Institutionalisation and Continuous Improvement | dormant | dormant | secondary | primary |

### A. Mandate, Ownership, and Decision Rights

- Which institution has the mandate to deploy and stand behind the solution?
- Who inside the institution must personally want this to succeed?
- Who is the named institutional owner?
- Who approves what the system is permitted to say or do?
- Which decisions require administrative, policy, legal, procurement, or technical approval?
- Has the institution formally authorised its knowledge, data, workflows, and public authority to be used in this way?
- Who has the authority to pause, change, or discontinue the service?

### B. Workforce and Change

- Which frontline and institutional roles will be affected?
- How will their work, authority, incentives, and responsibilities change?
- Do workers see the system as support, surveillance, additional work, or replacement?
- Who must test and approve the system before it reaches users?
- What capability-building is needed before, during, and after deployment?
- Are workers using the system as intended, or creating workarounds?
- Does the system leave people more capable, or more dependent?
- If the original project team or senior sponsor leaves, does the institution retain the capability?

### C. Governance, Safety, and Redress

- What decisions may the AI make, recommend, or support?
- Which decisions must always remain with a human?
- What are the known risks to users, institutions, and affected third parties?
- What safeguards, tests, approval gates, and monitoring mechanisms are required?
- Who monitors incidents and responds when failures occur?
- What is the escalation and redress mechanism for users?
- What records must be retained for auditability?
- How will the institution learn from incidents without disowning the service after the first public failure?

### D. Accountability, Liability, and Compliance

- Who is answerable when the system produces a harmful, incorrect, or inappropriate outcome?
- Who carries legal, regulatory, contractual, and reputational liability?
- What legal basis permits the collection, processing, and use of data?
- Which privacy, consent, accessibility, sectoral, and procurement obligations apply?
- How are responsibilities divided between the institution, vendors, and implementation partners?
- What assurance, documentation, and audit evidence must be maintained?
- Who signs off that the service is compliant before launch and after material changes?

### E. Data Stewardship

- Who has the authority to permit the use of institutional data and knowledge?
- Who is accountable for the accuracy and continued maintenance of each internal source?
- What access, consent, licensing, residency, retention, and deletion rules apply?
- Who can update, correct, withdraw, or override institutional information?
- How will disputes between sources or departments be resolved?
- Is the AI layer presenting institutional knowledge, or unintentionally becoming the new source of truth?

### F. Operating Model and Sustainability

- Who pays for design, setup, integration, and initial deployment?
- Who pays in year two and beyond?
- What is the actual cost per interaction, transaction, or beneficiary?
- Who operates the service day to day?
- Who handles failures, user support, vendor management, and escalation?
- Who updates internal data, approves model changes, and maintains institutional integrations?
- What staffing and capabilities must remain permanently within the institution?
- Is there a recurring budget line, or does the deployment still depend on project funding?
- What must be true for the institution to commit to long-term operation?

### G. Institutionalisation and Continuous Improvement

- Has the solution become an institutional service, or is it still treated as an external project?
- Is there a named owner, permanent team, budget, service standard, and governance mechanism?
- Can the service survive a leadership change, staff transfer, vendor change, or funding transition?
- How will user feedback, incidents, performance evidence, and policy changes lead to service improvements?
- What signals show that the institution is adopting the service rather than merely hosting a pilot?
- How will the institution periodically reassess whether the solution remains necessary, safe, and effective?

## Grid cells

Keyed `institution:<Stage>` in a pathway's `coverage` and in the app's `designs.grid_state`.

### Institution × Explore — `institution:Explore`

- **Core question:** Who inside the institution has to personally want this to work — and do they know yet?
- **Listening for:** Not procurement sign-off. The person whose professional stake is tied to success.
- **Insight form:** Named champion + their specific stake
- **Corpus example:** Bhili Language Enablement: the Nandurbar District Collector personally convened the effort and chaired the language-prioritisation meeting — a prior tribal posting had already shown her what changes when a service speaks someone's own language. ([pathway](../pathways/bhili-language-enablement.md))
- **Primary sub-categories here:** A

### Institution × Define — `institution:Define`

- **Core question:** Who approves what the system says, have they agreed to own that, and what testing/timeline has the institution committed to before real users?
- **Listening for:** Content authority, not technical sign-off. Staged testing with named gate criteria.
- **Insight form:** Content authority + approval process + testing progression
- **Corpus example:** African Voice AI: testing runs through a named, gated sequence — internal team, then partner staff, then field agents, then real farmers — with no stage advancing until its own criterion is actually met, not just scheduled. ([pathway](../pathways/african-voice-ai.md))
- **Primary sub-categories here:** A, B, C, E, F

### Institution × Pilot — `institution:Pilot`

- **Core question:** What has the institution seen fail publicly — and did they own it or disown it?
- **Listening for:** How the institution responds to the first failure is the strongest signal about whether this scales.
- **Insight form:** First public failure + institutional response (own vs disown)
- **Corpus example:** Bhili Language Enablement: in a live field demo, the helpline answered a farmer's cotton-pest question directly and declined a scheme question outright — "I will answer only farming-related questions" — rather than guessing to seem more capable. ([pathway](../pathways/bhili-language-enablement.md))
- **Primary sub-categories here:** B, C

### Institution × Scale — `institution:Scale`

- **Core question:** Has the institution absorbed this — budget line, named owner, review cadence — and does the system leave people more capable or more dependent?
- **Listening for:** Absorption vs "still the project team's problem." Workforce agency outcome.
- **Insight form:** Absorption indicators (budget + owner + review cadence) + agency outcome (capability vs dependency)
- **Corpus example:** African Voice AI: every contract in the programme ends in 2026 and the compute allocation expires that November — the team names "who maintains this SDK in three years" as a still-open funding and governance question, not a technical one. ([pathway](../pathways/african-voice-ai.md))
- **Primary sub-categories here:** B, D, E, F, G

## Data and trust here

- **Data:** who owns/authorises/corrects it
- **Trust:** accountability: who the user blames when it's wrong, who stands behind the answer

## How it is used

Every unit carries `dimension: institution`; the dimension name is public
vocabulary, the sub-category letters are not.
