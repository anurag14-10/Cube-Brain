---
name: Federal-by-design — states and institutions plug in side by side, not stacked
type: unit
schema_version: 1
summary: Make the national instance one peer among state and institutional instances on a shared network,
  each with its own registry and two-way contracts, instead of a hub that sub-deployments inherit from.
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
dimension: ecosystem
sub_category: ecosystem-d
stage: scale
source_unit_id: Unit 8
applies_when: Multiple institutionally distinct deployments need to share data and services without centralising
  governance.
fails_when: Regulatory or data sovereignty requirements mandate a single point of control.
decision: Design the national instance so that states and institutions join as peers on a shared network,
  rather than as subordinate nodes reporting to a central platform.
alternative_considered: A hub-and-spoke model in which Bharat Vistaar is the central platform and state
  instances are sub-deployments that inherit configuration from the centre.
reason: Hub-and-spoke concentrates governance at the centre and creates dependency on central availability
  and policy choices. In the peer model each instance runs its own network registry with two-way contracts,
  so a state can update its knowledge base, add a language or change a data provider without central approval
  or rebuild.
context: The OAN diagram shows Bharat Vistaar, MahaVISTAAR, Amul AI and Bihar Krishi as co-equal instances
  — 'side by side, not stacked above it'.
before: Not documented in the source
after: A farmer querying on the national network can be answered by a provider registered on a state network
  with no re-onboarding on either side; the same peer model extends to Ethiopia, Kenya and Sri Lanka.
adopter_intents:
- We want to expand to other states — how do we federate without losing governance?
- What travels when this model is adopted in another country?
- How quickly can a new country instance be stood up?
related_units:
- unififed-ai-driven-agri-ecosystem-oan-open-federated-architecture
- unififed-ai-driven-agri-ecosystem-reuse-governance-template-not-just-code
---

## Unit

According to the Bharat Vistaar pathway contributed by COSS (Centre for Open Societal Systems), this is a strategic decision from the deployment.

**Decision.** Design the national instance so that states and institutions join as peers on a shared network, rather than as subordinate nodes reporting to a central platform.

**Alternative considered.** A hub-and-spoke model in which Bharat Vistaar is the central platform and state instances are sub-deployments that inherit configuration from the centre.

**Why.** Hub-and-spoke concentrates governance at the centre and creates dependency on central availability and policy choices. In the peer model each instance runs its own network registry with two-way contracts, so a state can update its knowledge base, add a language or change a data provider without central approval or rebuild.

**Context.** The OAN diagram shows Bharat Vistaar, MahaVISTAAR, Amul AI and Bihar Krishi as co-equal instances — 'side by side, not stacked above it'.

## Condition

- **Applies when:** Multiple institutionally distinct deployments need to share data and services without centralising governance.
- **Fails when:** Regulatory or data sovereignty requirements mandate a single point of control.

## Before → after

- **Before:** Not documented in the source
- **After:** A farmer querying on the national network can be answered by a provider registered on a state network with no re-onboarding on either side; the same peer model extends to Ethiopia, Kenya and Sri Lanka.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
