---
name: Ecosystem
type: concept
schema_version: 2
aliases:
- Ecosystem
- Ecosystem dimension
- ecosystem-a
- Ecosystem A
- Partner Architecture and Roles
- ecosystem-b
- Ecosystem B
- External Data and Infrastructure Dependencies
- ecosystem-c
- Ecosystem C
- Delivery, Distribution, and Trust
- ecosystem-d
- Ecosystem D
- Coordination, Procurement, and Incentives
- ecosystem-e
- Ecosystem E
- Resilience, Portability, and Contingencies
- ecosystem-f
- Ecosystem F
- Ecosystem Learning and Diffusion
- ecosystem:Explore
- ecosystem:Define
- ecosystem:Pilot
- ecosystem:Scale
summary: Can the required network of actors execute and support it?
concept_kind: dimension
definition: Ecosystem — Can the required network of actors execute and support it?
audience: public-vocabulary
broader: grid
central_question: Can the required network of actors execute and support it?
shift: From procuring inputs to coordinating a network of capabilities
thesis_group: enable-adoption
order: 4
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

Can the required network of actors execute and support it?

*From procuring inputs to coordinating a network of capabilities*

No population-scale AI deployment is delivered by one organisation alone. The Ecosystem Dimension examines the actors, capabilities, dependencies, agreements, and trust relationships that sit outside the deploying institution but are necessary for the service to work.

## Sub-categories

Units are tagged `sub_category: ecosystem-<letter>`. Weight per stage: primary =
ask directly, secondary = only if surfaced, dormant = never initiate. The
letters are internal-only.

| Code | Variable | Sub-category | Explore | Define | Pilot | Scale |
|---|---|---|---|---|---|---|
| A | `ecosystem-a` | Partner Architecture and Roles | secondary | primary | secondary | secondary |
| B | `ecosystem-b` | External Data and Infrastructure Dependencies | secondary | primary | secondary | primary |
| C | `ecosystem-c` | Delivery, Distribution, and Trust | dormant | secondary | secondary | secondary |
| D | `ecosystem-d` | Coordination, Procurement, and Incentives | dormant | secondary | secondary | secondary |
| E | `ecosystem-e` | Resilience, Portability, and Contingencies | dormant | dormant | primary | primary |
| F | `ecosystem-f` | Ecosystem Learning and Diffusion | dormant | dormant | secondary | primary |

### A. Partner Architecture and Roles

- Which external partners are required across technology, domain expertise, data, implementation, financing, research, and last-mile delivery?
- What precise role, output, and outcome is each partner responsible for?
- Which capabilities cannot be provided by the deploying institution itself?
- Are all critical dependencies and unnamed roles visible before building begins?
- Who is responsible for integrating the work of different partners into one functioning service?
- Which relationships are transactional vendor relationships, and which require long-term collaboration?

### B. External Data and Infrastructure Dependencies

- Which data sources, platforms, registries, models, networks, or infrastructure sit outside the deploying institution?
- Who owns, maintains, and is accountable for each external source or service?
- What permissions, contracts, APIs, standards, and service-level agreements are required?
- How quickly must external sources be updated, and what happens when they become stale or unavailable?
- How will conflicts between external sources and institutional sources be resolved?
- What external dependencies are currently informal and need to become durable agreements before scale?

### C. Delivery, Distribution, and Trust

- Who takes the solution to the end user?
- Which actors already have the user's trust and access?
- Which partners provide assisted access, local language support, human escalation, or grievance resolution?
- Which organisation represents the service in the eyes of the user?
- How will feedback from frontline and community partners reach the institution and technology teams?
- Can the delivery network reach the groups most likely to be excluded?

### D. Coordination, Procurement, and Incentives

- Who has the convening authority to resolve cross-organisational dependencies?
- What governance forum brings the institution and partners together to make decisions?
- Are partner incentives aligned with user outcomes and long-term service quality?
- What procurement and contracting arrangements support experimentation without creating permanent lock-in?
- How will changes in scope, cost, performance, or responsibility be negotiated?
- Who manages cross-partner performance and holds each actor to its commitments?

### E. Resilience, Portability, and Contingencies

- Which partner, vendor, data source, or infrastructure provider is mission-critical?
- What happens if a critical partner underperforms, changes terms, or exits?
- Which partners, components, or capabilities require alternatives or contingency plans?
- Can data, workflows, knowledge, and service history be transferred to another provider?
- Which dependencies can be modularised, diversified, or brought in-house over time?
- What would have to be rebuilt if a major partner changed at Pilot or Scale?

### F. Ecosystem Learning and Diffusion

- What assets, decisions, standards, failure modes, and lessons can the next adopter reuse?
- What knowledge should remain proprietary, and what should be shared as ecosystem infrastructure?
- Under what conditions will the approach transfer to another institution, sector, geography, or population?
- Where will local trust, policy, data, language, or delivery conditions require adaptation?
- Who is responsible for documenting and sharing what the ecosystem has learned?
- How will the deployment contribute back to the wider AI diffusion ecosystem and enable the next adopter to start where this one stopped?

## Grid cells

Keyed `ecosystem:<Stage>` in a pathway's `coverage` and in the app's `designs.grid_state`.

### Ecosystem × Explore — `ecosystem:Explore`

- **Core question:** Who else has tried to solve this for this population, and what happened?
- **Listening for:** Precedent deployments, failed attempts, adjacent tools. Who do they trust as a reference peer?
- **Insight form:** Named precedent + what transferred + what didn't
- **Corpus example:** Voice AI for Inclusion: the same architecture went from 9 months (MahaVISTAAR, built from scratch) to 3 months (Ethiopia's ATI) to 3 weeks (Amul/Sarlaben). The build compressed each time; trust-building and data partnerships still had to be redone locally. ([pathway](../pathways/voice-ai-for-inclusion.md))
- **Primary sub-categories here:** none

### Ecosystem × Define — `ecosystem:Define`

- **Core question:** Which parts can you not build yourselves — and do you have a named partner for each?
- **Listening for:** Data owners, language models, telephony partners, integrators, field networks. Unnamed dependencies are unmanaged risk.
- **Insight form:** Dependency map: component × build-or-source × named partner
- **Corpus example:** Bhili Language Enablement: eight distinct ecosystem roles, all named before model work. Project stalled when the linguist role was unnamed for three months. ([pathway](../pathways/bhili-language-enablement.md))
- **Primary sub-categories here:** A, B

### Ecosystem × Pilot — `ecosystem:Pilot`

- **Core question:** Which partner is underperforming — and do you have an alternative?
- **Listening for:** Mid-pilot switching is painful but possible. Post-scale switching requires a rebuild.
- **Insight form:** Partner performance log + contingency plan
- **Corpus example:** Voice AI for Inclusion: running more than one vendor in parallel during the pilot revealed real comparative performance and added only a 2–5% cost premium in one deployment — far less than the lock-in risk it removed. ([pathway](../pathways/voice-ai-for-inclusion.md))
- **Primary sub-categories here:** E

### Ecosystem × Scale — `ecosystem:Scale`

- **Core question:** What from your deployment could the next adopter reuse — with what conditions?
- **Listening for:** Not "we did X." "X works when Y is true, fails when Z is true."
- **Insight form:** Transferable unit + condition tag (applies when / fails when)
- **Corpus example:** Nivesh Suvidha: schemas, pipelines, and governance approaches were designed from day one to be picked up by the next state or department — not one-off artefacts. Infrastructure built once and shared is a public good; built once and siloed is technical debt. ([pathway](../pathways/nivesh-suvidha.md))
- **Primary sub-categories here:** B, E, F

## Data and trust here

- **Data:** external sources, agreements, SLAs
- **Trust:** trust in delivery partners and distribution channels, independent of the institution itself

## How it is used

Every unit carries `dimension: ecosystem`; the dimension name is public
vocabulary, the sub-category letters are not.
