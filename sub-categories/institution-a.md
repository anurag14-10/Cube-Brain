---
name: Mandate, Ownership, and Decision Rights
type: sub_category
schema_version: 1
aliases:
- Institution A
- institution:A
summary: 'Institution sub-category A: Mandate, Ownership, and Decision Rights.'
dimension: institution
code: A
weight_explore: primary
weight_define: primary
weight_pilot: secondary
weight_scale: secondary
questions:
- Which institution has the mandate to deploy and stand behind the solution?
- Who inside the institution must personally want this to succeed?
- Who is the named institutional owner?
- Who approves what the system is permitted to say or do?
- Which decisions require administrative, policy, legal, procurement, or technical approval?
- Has the institution formally authorised its knowledge, data, workflows, and public authority to be used
  in this way?
- Who has the authority to pause, change, or discontinue the service?
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

Institution › **A. Mandate, Ownership, and Decision Rights** — part of "Can the institution own, absorb, govern, and sustain it?"

## Questions

- Which institution has the mandate to deploy and stand behind the solution?
- Who inside the institution must personally want this to succeed?
- Who is the named institutional owner?
- Who approves what the system is permitted to say or do?
- Which decisions require administrative, policy, legal, procurement, or technical approval?
- Has the institution formally authorised its knowledge, data, workflows, and public authority to be used in this way?
- Who has the authority to pause, change, or discontinue the service?

## Stage weighting

| Stage | Weight |
|---|---|
| Explore | primary |
| Define | primary |
| Pilot | secondary |
| Scale | secondary |

Primary at: Explore, Define. Primary = ask directly;
secondary = only if surfaced; dormant = never initiate.
