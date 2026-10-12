---
name: Deploy before models and data are perfect, and let deployment improve the data
type: unit
schema_version: 1
summary: Deploy early with imperfect models and data, as iterative learning with feedback loops — for
  the dengue early-warning system this created incentives for government departments to strengthen their
  own disease surveillance and reporting.
code_refs:
- content/library-wiki/pathways/ceew-climate-intelligence.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/ceew-climate-intelligence.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: dimension, sub_category, stage and unit_type assigned by best reading against content/framework.md
    — the library document is a conversational overview, not framework-structured
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ceew-climate-intelligence
unit_type: Strategic Decision
dimension: institution
sub_category: institution-f
stage: define
also_relevant_at:
- pilot
applies_when: Current data quality is imperfect but can be assessed — the document advises assessing data
  quality without treating imperfection as a reason to delay indefinitely.
fails_when: Not documented in the source
decision: Deploy before models or data are perfect, design deployment as iterative learning rather than
  one-time implementation, and build feedback loops that improve data collection alongside model performance.
alternative_considered: Waiting for perfect models or perfect data before deploying.
reason: Waiting for perfect models or perfect data delays learning; early deployment lets users validate
  outputs and provide feedback.
context: For the early-warning system, health surveillance data, climate observations and geospatial information
  were all essential; climate and geospatial data were relatively accessible, but forecasting performance
  depended heavily on the availability and granularity of surveillance records, which were not.
before: Not documented in the source
after: Users validated outputs and fed back; for the early-warning system, early deployment created incentives
  for government departments to strengthen their own disease surveillance and reporting practices. Both
  systems kept evolving after launch as users requested new data and models were refined.
related_units:
- ceew-climate-intelligence-decision-support-before-workflow-embedding
---

## Unit

According to CEEW's Climate Intelligence pathway, this is a strategic decision from the deployment.

**Decision.** Deploy before models or data are perfect, design deployment as iterative learning rather than one-time implementation, and build feedback loops that improve data collection alongside model performance.

**Alternative considered.** Waiting for perfect models or perfect data before deploying.

**Why.** Waiting for perfect models or perfect data delays learning; early deployment lets users validate outputs and provide feedback.

**Context.** For the early-warning system, health surveillance data, climate observations and geospatial information were all essential; climate and geospatial data were relatively accessible, but forecasting performance depended heavily on the availability and granularity of surveillance records, which were not.

## Condition

- **Applies when:** Current data quality is imperfect but can be assessed — the document advises assessing data quality without treating imperfection as a reason to delay indefinitely.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Users validated outputs and fed back; for the early-warning system, early deployment created incentives for government departments to strengthen their own disease surveillance and reporting practices. Both systems kept evolving after launch as users requested new data and models were refined.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
