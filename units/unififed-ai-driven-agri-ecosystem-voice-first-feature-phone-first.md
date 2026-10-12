---
name: Voice-first, feature-phone-first design as the non-negotiable inclusion constraint
type: unit
schema_version: 1
summary: Design the primary interface around a phone call rather than a smartphone app, so farmers without
  data, digital literacy or reading ability are included — voice improves on the channel they already
  use.
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
dimension: persona
sub_category: persona-d
stage: explore
also_relevant_at:
- define
- scale
source_unit_id: Unit 1
applies_when: Target population includes a significant proportion of feature-phone users, low-literacy
  users, or users for whom smartphone data costs are prohibitive.
fails_when: Not documented in the source
decision: Design the primary interface around the phone call — not the smartphone app — so the system
  is accessible to farmers without data connections, strong digital literacy, or reading ability.
alternative_considered: App-first design with voice as an add-on channel.
reason: 140M+ smallholder farmers include a large proportion relying on feature phones; app-first would
  replicate the exclusion already present in agricultural portals and extension services. Farmers' current
  workaround — calling an agrodealer, a relative or an extension officer — is itself a voice interaction,
  so voice AI improves an existing channel rather than demanding a new behaviour.
context: Phase 1 design prioritised Hindi and English, with 11 languages planned to follow.
before: Farmers relied on calling agrodealers, relatives or extension officers; existing agricultural
  portals and extension services excluded feature-phone and low-literacy users.
after: The toll-free helpline 155261 launched as the primary access point, with the app and web portal
  (chatbot 'Bharti') as secondary channels.
adopter_intents:
- Who is this platform actually built for, and how do they access it?
- Why voice and not an app?
related_units:
- unififed-ai-driven-agri-ecosystem-scope-by-farmer-decision-cycle
---

## Unit

According to the Bharat Vistaar pathway contributed by COSS (Centre for Open Societal Systems), this is a strategic decision from the deployment.

**Decision.** Design the primary interface around the phone call — not the smartphone app — so the system is accessible to farmers without data connections, strong digital literacy, or reading ability.

**Alternative considered.** App-first design with voice as an add-on channel.

**Why.** 140M+ smallholder farmers include a large proportion relying on feature phones; app-first would replicate the exclusion already present in agricultural portals and extension services. Farmers' current workaround — calling an agrodealer, a relative or an extension officer — is itself a voice interaction, so voice AI improves an existing channel rather than demanding a new behaviour.

**Context.** Phase 1 design prioritised Hindi and English, with 11 languages planned to follow.

## Condition

- **Applies when:** Target population includes a significant proportion of feature-phone users, low-literacy users, or users for whom smartphone data costs are prohibitive.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Farmers relied on calling agrodealers, relatives or extension officers; existing agricultural portals and extension services excluded feature-phone and low-literacy users.
- **After:** The toll-free helpline 155261 launched as the primary access point, with the app and web portal (chatbot 'Bharti') as secondary channels.

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
