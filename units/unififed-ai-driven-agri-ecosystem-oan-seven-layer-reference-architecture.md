---
name: OAN 7-layer open architecture (reference stack)
type: unit
schema_version: 2
summary: The open-source seven-layer OpenAgriNet stack — UI, language AI, AI module, registries, Beckn
  open network, provider services, data/ingestion pipeline — that every instance in the lineage runs on.
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
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: unififed-ai-driven-agri-ecosystem
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-c
stage: define
also_relevant_at:
- scale
source_unit_id: Section 4 — Unit 3 row
applies_when: Deploying AI advisory across multiple institutional data owners.
fails_when: A single institution controls all required data and can maintain it — the open network overhead
  is then unnecessary complexity.
purpose: 'An open-source, modular, federated reference architecture for multi-provider AI advisory with
  seven layers: user interface; language AI; AI module (moderation + intent classification + multi-step
  reasoning); registries; open network (Beckn); provider services; data/ingestion pipeline.'
reuse_condition: Use when deploying AI advisory across multiple institutional data owners; requires an
  open-source stack and a Beckn-compatible open network layer.
adopter_intents:
- How do we avoid building a system that locks us into one vendor or one data provider?
- Which architecture decisions will be hardest to reverse?
related_units:
- unififed-ai-driven-agri-ecosystem-oan-open-federated-architecture
---

## Unit

According to the Bharat Vistaar pathway contributed by COSS (Centre for Open Societal Systems), this is a toolkit asset from the deployment.

**What it is for.** An open-source, modular, federated reference architecture for multi-provider AI advisory with seven layers: user interface; language AI; AI module (moderation + intent classification + multi-step reasoning); registries; open network (Beckn); provider services; data/ingestion pipeline.

**Reuse condition.** Use when deploying AI advisory across multiple institutional data owners; requires an open-source stack and a Beckn-compatible open network layer.

No file or link is attached — the document names the asset but does not publish it.

## Condition

- **Applies when:** Deploying AI advisory across multiple institutional data owners.
- **Fails when:** A single institution controls all required data and can maintain it — the open network overhead is then unnecessary complexity.

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

It is an artifact the next adopter can adapt rather than rebuild, within the reuse condition above. It is a suggestion from another adoption's lived experience.
