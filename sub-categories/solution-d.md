---
name: Data and Knowledge Readiness
type: sub_category
schema_version: 1
aliases:
- Solution D
- solution:D
summary: 'Solution sub-category D: Data and Knowledge Readiness.'
dimension: solution
code: D
weight_explore: secondary
weight_define: primary
weight_pilot: primary
weight_scale: primary
questions:
- What data and institutional knowledge does the system require?
- Does each source exist in a usable, machine-readable form?
- How current, complete, and representative must each source be?
- How will stale, conflicting, incomplete, or incorrect data be detected?
- Who maintains the technical pipeline that keeps the data available and current?
- What data is collected from users, and is all of it necessary?
- What data stays with the institution, and what is shared with models, vendors, or partners?
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

Solution › **D. Data and Knowledge Readiness** — part of "Are we building the right system to solve it?"

## Questions

- What data and institutional knowledge does the system require?
- Does each source exist in a usable, machine-readable form?
- How current, complete, and representative must each source be?
- How will stale, conflicting, incomplete, or incorrect data be detected?
- Who maintains the technical pipeline that keeps the data available and current?
- What data is collected from users, and is all of it necessary?
- What data stays with the institution, and what is shared with models, vendors, or partners?

## Stage weighting

| Stage | Weight |
|---|---|
| Explore | secondary |
| Define | primary |
| Pilot | primary |
| Scale | primary |

Primary at: Define, Pilot, Scale. Primary = ask directly;
secondary = only if surfaced; dormant = never initiate.
