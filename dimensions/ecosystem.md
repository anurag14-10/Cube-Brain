---
name: Ecosystem
type: dimension
schema_version: 1
aliases:
- ecosystem
summary: Can the required network of actors execute and support it?
code: ecosystem
central_question: Can the required network of actors execute and support it?
shift: From procuring inputs to coordinating a network of capabilities
thesis_group: enable-adoption
ui_color: '#feda09'
data_concern: external sources, agreements, SLAs
trust_concern: trust in delivery partners and distribution channels, independent of the institution itself
order: 4
code_refs:
- lib/dimensions.ts
- content/framework.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/dimensions.ts
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/framework.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it asks

Can the required network of actors execute and support it?

*From procuring inputs to coordinating a network of capabilities*

No population-scale AI deployment is delivered by one organisation alone. The Ecosystem Dimension examines the actors, capabilities, dependencies, agreements, and trust relationships that sit outside the deploying institution but are necessary for the service to work.

## Sub-categories

- [A. Partner Architecture and Roles](../sub-categories/ecosystem-a.md)
- [B. External Data and Infrastructure Dependencies](../sub-categories/ecosystem-b.md)
- [C. Delivery, Distribution, and Trust](../sub-categories/ecosystem-c.md)
- [D. Coordination, Procurement, and Incentives](../sub-categories/ecosystem-d.md)
- [E. Resilience, Portability, and Contingencies](../sub-categories/ecosystem-e.md)
- [F. Ecosystem Learning and Diffusion](../sub-categories/ecosystem-f.md)

## Data and trust here

- **Data:** external sources, agreements, SLAs
- **Trust:** trust in delivery partners and distribution channels, independent of the institution itself

## How the companion uses it

Grid cells for this dimension are keyed `ecosystem:<Stage>` in `designs.grid_state`.
Which sub-categories the companion probes at a given stage is set by each
sub-category's stage weight. The dimension name is public vocabulary; the
sub-category letters are internal-only.
