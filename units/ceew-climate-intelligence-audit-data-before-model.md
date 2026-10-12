---
name: Audit the data before selecting a model
type: unit
schema_version: 2
summary: Across both CEEW systems data quality decided success more than model sophistication; for the dengue
  early-warning system, health surveillance data — not climate or geospatial data — was the binding constraint.
doc_refs:
- content/library-wiki/pathways/ceew-climate-intelligence.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/library-wiki/pathways/ceew-climate-intelligence.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: dimension, sub_category, stage and unit_type assigned by best reading against content/framework.md —
    the library document is a conversational overview, not framework-structured
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ceew-climate-intelligence
unit_type: Strategic Decision
dimension: solution
sub_category: solution-d
stage: define
also_relevant_at:
- explore
applies_when: Not documented in the source
fails_when: Not documented in the source
decision: Audit the availability, quality and granularity of each required data category before selecting a
  model.
reason: A sophisticated model cannot compensate for fragmented, poorly governed or unreliable data; across
  both projects, data quality determined success more than model sophistication.
context: 'For the early-warning system, three data categories proved essential: health surveillance data, climate
  observations and geospatial information. Climate and geospatial data were relatively accessible (weather
  stations, satellite imagery); health data was not, and forecasting performance depended heavily on surveillance-record
  availability and granularity.'
before: Not documented in the source
after: Not documented in the source
related_units:
- ceew-climate-intelligence-deploy-before-data-is-perfect
---

## Unit

According to CEEW's Climate Intelligence pathway, this is a strategic decision from the deployment.

**Decision.** Audit the availability, quality and granularity of each required data category before selecting a model.

**Why.** A sophisticated model cannot compensate for fragmented, poorly governed or unreliable data; across both projects, data quality determined success more than model sophistication.

**Context.** For the early-warning system, three data categories proved essential: health surveillance data, climate observations and geospatial information. Climate and geospatial data were relatively accessible (weather stations, satellite imagery); health data was not, and forecasting performance depended heavily on surveillance-record availability and granularity.

## Condition

- **Applies when:** Not documented in the source
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
