---
name: Design for the woman who milks, not the registered farmer account
type: unit
schema_version: 2
summary: Define the primary user as the woman who milks twice daily, at 4-5am, with no trusted expert
  available at that hour or in her language — not the household's registered farmer; usage peaks at the
  6-9am and 6-9pm milking windows confirmed the fit.
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
unit_type: Strategic Decision
dimension: persona
sub_category: persona-a
stage: explore
source_unit_id: Unit 1
applies_when: The care worker and the registered cooperative member are different people in the same household;
  the primary care window is early morning and evening when formal channels are unavailable.
fails_when: Not documented in the source
decision: Define the primary user not as "the farmer" in the abstract but as the woman who milks twice
  daily regardless of circumstances — who is the one the cattle recognise, who is up at 4am, and who has
  no trusted expert available at that hour or in her language.
alternative_considered: Not documented in the source. The framing emerged from Amul's existing cooperative
  model, which already tracked that women are the primary cattle-care workers.
reason: Animal husbandry advice delivered to someone other than the person actually performing the care
  is likely to be ignored or misapplied. Designing for the woman at the farm at 5am — available on any
  phone, in local Gujarati dialect, at any hour — is a different product than designing for a household's
  registered farmer account.
context: Sarla Ben is accessible on voice (any phone), app and WhatsApp; it recognises users by mobile
  number; it answers at any hour; it uses a female persona that farmers report feeling comfortable with.
  Usage peaks at 6-9am and 6-9pm — the milking windows — confirming the design matched the actual use
  moment. The document's retrieval guide also points here for dialect variation, citing a 2,000-word glossary
  and a farmer-contributed feedback loop for new terms.
before: Not documented in the source
after: Not documented in the source
adopter_intents:
- Who is this actually built for — the registered farmer or the woman doing the work?
- Farmers use the system at what times of day — how should we size infrastructure?
- How do we handle dialect variation within a single state language?
related_units:
- ai-advisory-for-dairy-farmers-chat-for-advice-voice-for-transactions
- mahavistaar-registered-farmer-not-decision-maker
---

## Unit

According to GCMMF (Amul) and EkStep Foundation's Amul AI / Sarla Ben pathway, this is a strategic decision from the deployment.

**Decision.** Define the primary user not as "the farmer" in the abstract but as the woman who milks twice daily regardless of circumstances — who is the one the cattle recognise, who is up at 4am, and who has no trusted expert available at that hour or in her language.

**Alternative considered.** Not documented in the source. The framing emerged from Amul's existing cooperative model, which already tracked that women are the primary cattle-care workers.

**Why.** Animal husbandry advice delivered to someone other than the person actually performing the care is likely to be ignored or misapplied. Designing for the woman at the farm at 5am — available on any phone, in local Gujarati dialect, at any hour — is a different product than designing for a household's registered farmer account.

**In this deployment.** Sarla Ben is accessible on voice (any phone), app and WhatsApp; it recognises users by mobile number; it answers at any hour; it uses a female persona that farmers report feeling comfortable with. Usage peaks at 6-9am and 6-9pm — the milking windows — confirming the design matched the actual use moment. The document's retrieval guide also points here for dialect variation, citing a 2,000-word glossary and a farmer-contributed feedback loop for new terms.

## Condition

- **Applies when:** The care worker and the registered cooperative member are different people in the same household; the primary care window is early morning and evening when formal channels are unavailable.
- **Fails when:** Not documented in the source

## Before → after

- **Before:** Not documented in the source
- **After:** Not documented in the source

## Why it is reusable

The condition tag says when this choice held in the source deployment; the alternative and the before→after show what a different choice would trade away. It is a suggestion from another adoption's lived experience, not a recommendation.
