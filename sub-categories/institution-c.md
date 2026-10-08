---
name: Governance, Safety, and Redress
type: sub_category
schema_version: 1
aliases:
- Institution C
- institution:C
summary: 'Institution sub-category C: Governance, Safety, and Redress.'
dimension: institution
code: C
weight_explore: dormant
weight_define: primary
weight_pilot: primary
weight_scale: secondary
questions:
- What decisions may the AI make, recommend, or support?
- Which decisions must always remain with a human?
- What are the known risks to users, institutions, and affected third parties?
- What safeguards, tests, approval gates, and monitoring mechanisms are required?
- Who monitors incidents and responds when failures occur?
- What is the escalation and redress mechanism for users?
- What records must be retained for auditability?
- How will the institution learn from incidents without disowning the service after the first public failure?
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

Institution › **C. Governance, Safety, and Redress** — part of "Can the institution own, absorb, govern, and sustain it?"

## Questions

- What decisions may the AI make, recommend, or support?
- Which decisions must always remain with a human?
- What are the known risks to users, institutions, and affected third parties?
- What safeguards, tests, approval gates, and monitoring mechanisms are required?
- Who monitors incidents and responds when failures occur?
- What is the escalation and redress mechanism for users?
- What records must be retained for auditability?
- How will the institution learn from incidents without disowning the service after the first public failure?

## Stage weighting

| Stage | Weight |
|---|---|
| Explore | dormant |
| Define | primary |
| Pilot | primary |
| Scale | secondary |

Primary at: Define, Pilot. Primary = ask directly;
secondary = only if surfaced; dormant = never initiate.
