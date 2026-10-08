---
name: Resilience, Portability, and Contingencies
type: sub_category
schema_version: 1
aliases:
- Ecosystem E
- ecosystem:E
summary: 'Ecosystem sub-category E: Resilience, Portability, and Contingencies.'
dimension: ecosystem
code: E
weight_explore: dormant
weight_define: dormant
weight_pilot: primary
weight_scale: primary
questions:
- Which partner, vendor, data source, or infrastructure provider is mission-critical?
- What happens if a critical partner underperforms, changes terms, or exits?
- Which partners, components, or capabilities require alternatives or contingency plans?
- Can data, workflows, knowledge, and service history be transferred to another provider?
- Which dependencies can be modularised, diversified, or brought in-house over time?
- What would have to be rebuilt if a major partner changed at Pilot or Scale?
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

Ecosystem › **E. Resilience, Portability, and Contingencies** — part of "Can the required network of actors execute and support it?"

## Questions

- Which partner, vendor, data source, or infrastructure provider is mission-critical?
- What happens if a critical partner underperforms, changes terms, or exits?
- Which partners, components, or capabilities require alternatives or contingency plans?
- Can data, workflows, knowledge, and service history be transferred to another provider?
- Which dependencies can be modularised, diversified, or brought in-house over time?
- What would have to be rebuilt if a major partner changed at Pilot or Scale?

## Stage weighting

| Stage | Weight |
|---|---|
| Explore | dormant |
| Define | dormant |
| Pilot | primary |
| Scale | primary |

Primary at: Pilot, Scale. Primary = ask directly;
secondary = only if surfaced; dormant = never initiate.
