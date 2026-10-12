---
name: Define the problem as heterogeneity, not content scarcity
type: unit
schema_version: 2
summary: Frame foundational-learning failure as unaddressed proficiency heterogeneity within one classroom,
  not a shortage of content, devices or teachers — the framing decided what to build and what not to build.
doc_refs:
- content/wiki/pathways/assisted-language-math-learning.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/assisted-language-math-learning.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: assisted-language-math-learning
unit_type: Strategic Decision
dimension: persona
sub_category: persona-a
stage: explore
source_unit_id: Unit 1
applies_when: The school system already has teachers, curriculum, and digital content; the limiting factor
  is the system's inability to continuously identify which content or skill each specific learner needs
  next.
fails_when: Not documented in the source
decision: Frame the foundational learning problem as continuous, unaddressed heterogeneity within the
  same classroom — not as a shortage of content, devices, or teachers — before deciding whether AI is
  the right intervention.
alternative_considered: Treating the gap as a content or device problem and addressing it through more
  digital worksheets, additional teaching hours, or device procurement.
reason: Schools already had teachers, textbooks, worksheets, and large libraries of digital content. The
  problem was that children in the same classroom could be several learning levels apart, and the system
  had no continuous ability to identify those differences and respond individually.
context: ASER data showed only ~1/3 of grade 3 children could perform basic two-digit subtraction with
  borrowing, and only ~50% of grade 8 students could answer basic math questions — proficiency-heterogeneity
  statistics, not content-availability statistics.
before: Schools had teachers, textbooks, worksheets and digital content libraries, yet children in the
  same classroom could be several learning levels apart with no continuous way to identify and respond
  to those differences.
after: The heterogeneity framing drove the decision to build a personalisation system rather than a content
  library.
adopter_intents:
- How do I explain to a state government why they need this before any AI exists?
- What is the right way to frame what this product actually does?
related_units:
- assisted-language-math-learning-personalise-on-proficiency-not-grade
---

## Unit

According to EkStep Foundation's AxL pathway, this is a strategic decision from the deployment.

**Decision.** Frame the foundational learning problem as continuous, unaddressed heterogeneity within the same classroom — not as a shortage of content, devices, or teachers — before deciding whether AI is the right intervention.

**Alternative considered.** Treating the gap as a content or device problem and addressing it through more digital worksheets, additional teaching hours, or device procurement.

**Why.** Schools already had teachers, textbooks, worksheets, and large libraries of digital content. The problem was that children in the same classroom could be several learning levels apart, and the system had no continuous ability to identify those differences and respond individually.

**Context.** ASER data showed only ~1/3 of grade 3 children could perform basic two-digit subtraction with borrowing, and only ~50% of grade 8 students could answer basic math questions — proficiency-heterogeneity statistics, not content-availability statistics.

## Condition

- **Applies when:** The school system already has teachers, curriculum, and digital content; the limiting factor is the system's inability to continuously identify which content or skill each specific learner needs next.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Schools had teachers, textbooks, worksheets and digital content libraries, yet children in the same classroom could be several learning levels apart with no continuous way to identify and respond to those differences.
- **After:** The heterogeneity framing drove the decision to build a personalisation system rather than a content library.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
