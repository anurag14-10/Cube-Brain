---
name: External Data and Infrastructure Dependencies
type: sub_category
schema_version: 1
aliases:
- Ecosystem B
- ecosystem:B
summary: 'Ecosystem sub-category B: External Data and Infrastructure Dependencies.'
dimension: ecosystem
code: B
weight_explore: secondary
weight_define: primary
weight_pilot: secondary
weight_scale: primary
questions:
- Which data sources, platforms, registries, models, networks, or infrastructure sit outside the deploying
  institution?
- Who owns, maintains, and is accountable for each external source or service?
- What permissions, contracts, APIs, standards, and service-level agreements are required?
- How quickly must external sources be updated, and what happens when they become stale or unavailable?
- How will conflicts between external sources and institutional sources be resolved?
- What external dependencies are currently informal and need to become durable agreements before scale?
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

## What it covers

Ecosystem › **B. External Data and Infrastructure Dependencies** — part of "Can the required network of actors execute and support it?"

## Questions

- Which data sources, platforms, registries, models, networks, or infrastructure sit outside the deploying institution?
- Who owns, maintains, and is accountable for each external source or service?
- What permissions, contracts, APIs, standards, and service-level agreements are required?
- How quickly must external sources be updated, and what happens when they become stale or unavailable?
- How will conflicts between external sources and institutional sources be resolved?
- What external dependencies are currently informal and need to become durable agreements before scale?

## Stage weighting

| Stage | Weight |
|---|---|
| Explore | secondary |
| Define | primary |
| Pilot | secondary |
| Scale | primary |

Primary at: Define, Scale. Primary = ask directly;
secondary = only if surfaced; dormant = never initiate.
