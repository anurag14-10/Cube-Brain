---
name: Chat won for advice, voice for transactions — channel preference is query-type-specific
type: unit
schema_version: 2
summary: Voice capacity was expanded two to three times on the assumption voice would dominate; farmers
  preferred chat for advisory (re-read, copy, share) and voice for transactions such as booking a vet
  visit.
doc_refs:
- content/wiki/pathways/ai-advisory-for-dairy-farmers.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/ai-advisory-for-dairy-farmers.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: sub_category assigned by reading the unit against content/framework.md — the document tags dimension,
    stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: ai-advisory-for-dairy-farmers
unit_type: Failure and Fix
dimension: persona
sub_category: persona-d
stage: pilot
source_unit_id: Unit 2
applies_when: Users have smartphones or WhatsApp access (not feature-phone-only); the advisory content
  is something a user wants to save, share, or re-read; transactions still benefit from voice confirmation.
fails_when: Not documented in the source
failure: The team designed and scaled voice capacity assuming voice would be the dominant channel. Farmers
  turned out to prefer chat for advisory and knowledge queries. Voice capacity was expanded two to three
  times before the pattern was understood.
fix: 'Recognised that the two channels serve different user needs: chat is preferred for advisory (farmers
  can re-read, copy, and share the answer; the record persists) while voice is preferred for transactions
  (booking a vet visit feels natural by phone call). Invested in chat quality and capacity accordingly.'
insight: '"Voice is easier for farmers" is an assumption, not a finding. Farmers who have mobile phones
  also have WhatsApp and app interfaces, and they choose chat when they want a record they can refer back
  to or share. The channel preference is query-type-specific, not user-type-specific.'
adopter_intents:
- We assumed voice would dominate — what actually happened?
- What's the right channel mix — voice, app, WhatsApp?
related_units:
- ai-advisory-for-dairy-farmers-design-for-the-woman-at-the-farm
- ai-advisory-for-dairy-farmers-landing-page-suggested-questions
- mahavistaar-voice-not-the-only-channel
---

## Unit

According to GCMMF (Amul) and EkStep Foundation's Amul AI / Sarla Ben pathway, this is a failure and fix from the deployment.

**Failure.** The team designed and scaled voice capacity assuming voice would be the dominant channel. Farmers turned out to prefer chat for advisory and knowledge queries. Voice capacity was expanded two to three times before the pattern was understood.

**Fix.** Recognised that the two channels serve different user needs: chat is preferred for advisory (farmers can re-read, copy, and share the answer; the record persists) while voice is preferred for transactions (booking a vet visit feels natural by phone call). Invested in chat quality and capacity accordingly.

**Insight.** "Voice is easier for farmers" is an assumption, not a finding. Farmers who have mobile phones also have WhatsApp and app interfaces, and they choose chat when they want a record they can refer back to or share. The channel preference is query-type-specific, not user-type-specific.

## Condition

- **Applies when:** Users have smartphones or WhatsApp access (not feature-phone-only); the advisory content is something a user wants to save, share, or re-read; transactions still benefit from voice confirmation.
- **Fails when:** Not documented in the source

## Before → after

Not documented in the source as a separate before→after.

## Why it is reusable

The reusable part is the insight the fix revealed, read together with the condition tag above. It is a suggestion from another adoption's lived experience, not a recommendation.
