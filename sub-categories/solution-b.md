---
name: UX, Channel, and Integration
type: sub_category
schema_version: 1
aliases:
- Solution B
- solution:B
summary: 'Solution sub-category B: UX, Channel, and Integration.'
dimension: solution
code: B
weight_explore: secondary
weight_define: primary
weight_pilot: primary
weight_scale: secondary
questions:
- 'Through what channel will the persona encounter the solution: phone, app, messaging, assisted interface,
  or an existing institutional system?'
- Why is that channel appropriate for this persona?
- Which existing systems, databases, workflows, and APIs must it integrate with?
- What happens when an upstream system, data source, or external service is unavailable?
- Where does a human enter, review, or take over the journey?
- How will the experience communicate uncertainty, delay, refusal, or failure to the user?
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

Solution › **B. UX, Channel, and Integration** — part of "Are we building the right system to solve it?"

## Questions

- Through what channel will the persona encounter the solution: phone, app, messaging, assisted interface, or an existing institutional system?
- Why is that channel appropriate for this persona?
- Which existing systems, databases, workflows, and APIs must it integrate with?
- What happens when an upstream system, data source, or external service is unavailable?
- Where does a human enter, review, or take over the journey?
- How will the experience communicate uncertainty, delay, refusal, or failure to the user?

## Stage weighting

| Stage | Weight |
|---|---|
| Explore | secondary |
| Define | primary |
| Pilot | primary |
| Scale | secondary |

Primary at: Define, Pilot. Primary = ask directly;
secondary = only if surfaced; dormant = never initiate.
