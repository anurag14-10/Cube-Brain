---
name: AI-assisted Job Matching — eight-category pilot issue taxonomy to separate model failures from data failures
type: unit
schema_version: 2
summary: In the first four weeks of the pilot, support issues are reviewed daily and logged into eight categories,
  so that recommendation-quality problems, software defects and data-quality problems are attributed at
  the point of logging rather than retrospectively.
doc_refs:
- content/wiki/pathways/ai-assisted-job-matching.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-assisted-job-matching.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ai-assisted-job-matching
unit_type: Strategic Decision
dimension: institution
sub_category: institution-c
stage: pilot
source_unit_id: Unit 5
applies_when: Recommendation quality is one of several possible failure modes; pilot evaluation depends
  on distinguishing model performance from data quality; the institution needs to decide after the pilot
  whether to invest in data improvement, model improvement, or both.
fails_when: Not documented in the source
decision: During the first four weeks of the pilot, review support issues daily and categorise them into
  eight types (software, data, vacancy input, recommendation quality, workflow, user access, training,
  unknown). Matching-quality issues are tagged separately from software defects, and data-quality issues
  are logged separately from model errors.
alternative_considered: A single issue queue where all problems are logged together and triaged reactively.
reason: A poor recommendation can come from at least three causes (a software bug, a data-quality problem,
  or a genuine model-quality problem), and each needs a different fix. Conflating them gives misleading
  signals. If data errors are counted as model errors, the model looks worse than it is. If model errors
  are logged as data issues, data investment is misdirected. The taxonomy forces the attribution question
  at the point of logging, not retrospectively.
context: The taxonomy is defined in the architecture document as a pilot support process requirement,
  not as an optional logging convention. Daily review in the first four weeks is specified as an operational
  commitment, not a fallback.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- When something breaks in the pilot, how do I figure out if it's the AI or our data?
- How do we set up support so we can tell the difference between a model problem and a bad data problem?
- How do we structure pilot support so issues don't all get lumped together?
related_units:
- ai-assisted-job-matching-staged-district-activation
---

## Unit

According to EkStep Foundation's AI-assisted Job Matching for Rural Youth pathway, this is a strategic
decision about how pilot support is run.

**Decision.** During the first four weeks of the pilot, support issues are reviewed daily and categorised
into eight types: software, data, vacancy input, recommendation quality, workflow, user access, training,
and unknown. Matching-quality issues are tagged separately from software defects, and data-quality
issues are logged separately from model errors.

**Alternative considered.** A single issue queue where all problems are logged together and triaged
reactively.

**Why.** A poor recommendation can come from at least three causes: a software bug, a data-quality
problem, or a genuine model-quality problem. Each needs a different fix. Conflating them gives misleading
signals. If data errors are counted as model errors, the model looks worse than it is. If model errors are
logged as data issues, data investment is misdirected. The taxonomy forces the attribution question at
the point of logging, not retrospectively.

**Context.** The taxonomy is defined in the architecture document as a pilot support process
requirement, not as an optional logging convention. Daily review in the first four weeks is specified as
an operational commitment, not a fallback.

## Condition

- **Applies when:** Recommendation quality is one of several possible failure modes; pilot evaluation depends on distinguishing model performance from data quality; the institution needs to decide after the pilot whether to invest in data improvement, model improvement, or both.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

The pathway also says that no failure taxonomy from actual coordinator use has been recorded yet.

## Why it is reusable

The alternative shows the trade-off. With a single reactive queue, the post-pilot choice between
investing in data and investing in the model rests on mixed-up signals. It is a suggestion from another
adoption's lived experience, not a recommendation.
