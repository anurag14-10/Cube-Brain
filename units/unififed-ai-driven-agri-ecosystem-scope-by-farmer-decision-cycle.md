---
name: Scope defined by the farmer's decision cycle, not by departmental boundaries
type: unit
schema_version: 2
summary: Scope advisory around every decision a smallholder actually faces — crops, weather, pests, prices,
  schemes — rather than one department's remit, which in turn requires a governance model that can hold
  many data relationships.
doc_refs:
- content/wiki/pathways/unififed-ai-driven-agri-ecosystem.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/unififed-ai-driven-agri-ecosystem.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: before taken from Unit 2's Why paragraph (the unit has no explicit Before → After line)
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: unififed-ai-driven-agri-ecosystem
unit_type: Strategic Decision
dimension: persona
sub_category: persona-d
stage: define
source_unit_id: Unit 2
applies_when: Target population faces decisions that cut across multiple institutional data owners, and
  a governance model can hold multiple data relationships simultaneously.
fails_when: A single-institution deployment cannot execute this scope — it requires a governance model
  able to hold multiple data relationships simultaneously.
decision: Scope the advisory system around the full range of decisions a smallholder farmer actually faces
  — crop guidance, weather, pest and disease, market prices, scheme eligibility — rather than limiting
  scope to a single department's remit.
alternative_considered: Single-department scope (e.g. crop advisory only from ICAR) to simplify governance
  and data integration.
reason: Farmers do not experience decisions as departmentally siloed — a farmer asking about pest control
  also needs to know whether a scheme covers the recommended input. Artificial scope limits would reproduce
  the fragmentation the system exists to solve and push farmers back to agrodealers and relatives.
context: The OAN architecture routes each query to the appropriate data provider via the AI agent layer.
before: Advice was split by departmental remit, a fragmentation that pushed farmers to the informal networks
  (agrodealers, relatives) they relied on.
after: The platform integrates crop advisory, weather (IMD), mandi prices, soil health and government
  schemes (including PM Fasal Bima Yojana) into a single interface.
adopter_intents:
- Who is this platform actually built for, and how do they access it?
related_units:
- unififed-ai-driven-agri-ecosystem-oan-open-federated-architecture
- unififed-ai-driven-agri-ecosystem-ai-layer-retrieves-not-owns-data
---

## Unit

According to the Bharat Vistaar pathway contributed by COSS (Centre for Open Societal Systems), this is a strategic decision from the deployment.

**Decision.** Scope the advisory system around the full range of decisions a smallholder farmer actually faces — crop guidance, weather, pest and disease, market prices, scheme eligibility — rather than limiting scope to a single department's remit.

**Alternative considered.** Single-department scope (e.g. crop advisory only from ICAR) to simplify governance and data integration.

**Why.** Farmers do not experience decisions as departmentally siloed — a farmer asking about pest control also needs to know whether a scheme covers the recommended input. Artificial scope limits would reproduce the fragmentation the system exists to solve and push farmers back to agrodealers and relatives.

**Context.** The OAN architecture routes each query to the appropriate data provider via the AI agent layer.

## Condition

- **Applies when:** Target population faces decisions that cut across multiple institutional data owners, and a governance model can hold multiple data relationships simultaneously.
- **Fails when:** A single-institution deployment cannot execute this scope — it requires a governance model able to hold multiple data relationships simultaneously.

## Before → after

- **Before:** Advice was split by departmental remit, a fragmentation that pushed farmers to the informal networks (agrodealers, relatives) they relied on.
- **After:** The platform integrates crop advisory, weather (IMD), mandi prices, soil health and government schemes (including PM Fasal Bima Yojana) into a single interface.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
