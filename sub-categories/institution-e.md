---
name: Data Stewardship
type: sub_category
schema_version: 1
aliases:
- Institution E
- institution:E
summary: 'Institution sub-category E: Data Stewardship.'
dimension: institution
code: E
weight_explore: dormant
weight_define: primary
weight_pilot: secondary
weight_scale: primary
questions:
- Who has the authority to permit the use of institutional data and knowledge?
- Who is accountable for the accuracy and continued maintenance of each internal source?
- What access, consent, licensing, residency, retention, and deletion rules apply?
- Who can update, correct, withdraw, or override institutional information?
- How will disputes between sources or departments be resolved?
- Is the AI layer presenting institutional knowledge, or unintentionally becoming the new source of truth?
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

Institution › **E. Data Stewardship** — part of "Can the institution own, absorb, govern, and sustain it?"

## Questions

- Who has the authority to permit the use of institutional data and knowledge?
- Who is accountable for the accuracy and continued maintenance of each internal source?
- What access, consent, licensing, residency, retention, and deletion rules apply?
- Who can update, correct, withdraw, or override institutional information?
- How will disputes between sources or departments be resolved?
- Is the AI layer presenting institutional knowledge, or unintentionally becoming the new source of truth?

## Stage weighting

| Stage | Weight |
|---|---|
| Explore | dormant |
| Define | primary |
| Pilot | secondary |
| Scale | primary |

Primary at: Define, Scale. Primary = ask directly;
secondary = only if surfaced; dormant = never initiate.
