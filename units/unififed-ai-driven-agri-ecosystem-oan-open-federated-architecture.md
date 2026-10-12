---
name: OAN 7-layer open architecture as the non-reversible foundation choice
type: unit
schema_version: 1
summary: Build on an open-source, modular, federated seven-layer architecture where provider institutions
  register independently on an open network, rather than a centralised platform owned by one institution
  — named as the hardest decision to reverse.
code_refs:
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
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: unififed-ai-driven-agri-ecosystem
unit_type: Strategic Decision
dimension: solution
sub_category: solution-c
stage: define
also_relevant_at:
- scale
source_unit_id: Unit 3
applies_when: Multiple data owners with different update cadences, different accountability structures,
  and different institutional mandates.
fails_when: A single institution controls all required data and can maintain it — the open network overhead
  is then unnecessary complexity.
decision: Build on the Open AgriNet (OAN) 7-layer architecture — user interface, language AI, AI module
  (moderation + intent + reasoning), registries, open network (Beckn), provider services, and data/ingestion
  pipeline — as open-source, modular and federated, rather than a closed platform owned by any single
  organisation.
alternative_considered: A centralised platform architecture in which one institution owns the stack and
  others plug in as data suppliers.
reason: A centralised platform creates a single point of control, a single point of failure, and a governance
  problem over which institution owns what the system says. On the open network each provider registers
  independently and is discovered by class — no re-onboarding when a provider joins, no shared directory,
  no neutral third party. Switching to a centralised model after federated deployment would require renegotiating
  every provider relationship.
context: The AI Module — moderation, intent classification and multi-step reasoning — runs as a single
  module; provider services (ICAR, IMD, mandi data, scheme databases) register on the network independently.
before: Not documented in the source
after: A peer-network capability lets a farmer querying on one network be answered by a provider on another,
  with no re-onboarding on either side.
adopter_intents:
- How do we avoid building a system that locks us into one vendor or one data provider?
- Which architecture decisions will be hardest to reverse?
related_units:
- unififed-ai-driven-agri-ecosystem-ai-layer-retrieves-not-owns-data
- unififed-ai-driven-agri-ecosystem-federal-by-design-peer-instances
- unififed-ai-driven-agri-ecosystem-oan-seven-layer-reference-architecture
---

## Unit

According to the Bharat Vistaar pathway contributed by COSS (Centre for Open Societal Systems), this is a strategic decision from the deployment.

**Decision.** Build on the Open AgriNet (OAN) 7-layer architecture — user interface, language AI, AI module (moderation + intent + reasoning), registries, open network (Beckn), provider services, and data/ingestion pipeline — as open-source, modular and federated, rather than a closed platform owned by any single organisation.

**Alternative considered.** A centralised platform architecture in which one institution owns the stack and others plug in as data suppliers.

**Why.** A centralised platform creates a single point of control, a single point of failure, and a governance problem over which institution owns what the system says. On the open network each provider registers independently and is discovered by class — no re-onboarding when a provider joins, no shared directory, no neutral third party. Switching to a centralised model after federated deployment would require renegotiating every provider relationship.

**Context.** The AI Module — moderation, intent classification and multi-step reasoning — runs as a single module; provider services (ICAR, IMD, mandi data, scheme databases) register on the network independently.

## Condition

- **Applies when:** Multiple data owners with different update cadences, different accountability structures, and different institutional mandates.
- **Fails when:** A single institution controls all required data and can maintain it — the open network overhead is then unnecessary complexity.

## Before → after

- **Before:** Not documented in the source
- **After:** A peer-network capability lets a farmer querying on one network be answered by a provider on another, with no re-onboarding on either side.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
