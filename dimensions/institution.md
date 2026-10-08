---
name: Institution
type: dimension
schema_version: 1
aliases:
- institution
summary: Can the institution own, absorb, govern, and sustain it?
code: institution
central_question: Can the institution own, absorb, govern, and sustain it?
shift: From sponsoring a project to owning a sustainable service
thesis_group: enable-adoption
ui_color: '#1b1b42'
data_concern: who owns/authorises/corrects it
trust_concern: 'accountability: who the user blames when it''s wrong, who stands behind the answer'
order: 3
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

Can the institution own, absorb, govern, and sustain it?

*From sponsoring a project to owning a sustainable service*



## Sub-categories

- [A. Mandate, Ownership, and Decision Rights](../sub-categories/institution-a.md)
- [B. Workforce and Change](../sub-categories/institution-b.md)
- [C. Governance, Safety, and Redress](../sub-categories/institution-c.md)
- [D. Accountability, Liability, and Compliance](../sub-categories/institution-d.md)
- [E. Data Stewardship](../sub-categories/institution-e.md)
- [F. Operating Model and Sustainability](../sub-categories/institution-f.md)
- [G. Institutionalisation and Continuous Improvement](../sub-categories/institution-g.md)

## Data and trust here

- **Data:** who owns/authorises/corrects it
- **Trust:** accountability: who the user blames when it's wrong, who stands behind the answer

## How the companion uses it

Grid cells for this dimension are keyed `institution:<Stage>` in `designs.grid_state`.
Which sub-categories the companion probes at a given stage is set by each
sub-category's stage weight. The dimension name is public vocabulary; the
sub-category letters are internal-only.
