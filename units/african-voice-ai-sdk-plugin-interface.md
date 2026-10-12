---
name: African Voice AI SDK — Apache 2.0 plugin interface for ASR/TTS/LLM components
type: unit
schema_version: 2
summary: The open-source (Apache 2.0) African Voice AI SDK, whose plugin interface lets ASR, TTS and LLM
  components be registered without rebuilding orchestration — repository URL and interface specification
  are not documented in the source.
doc_refs:
- content/wiki/pathways/african-voice-ai.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-12'
  ref: content/wiki/pathways/african-voice-ai.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: dimension, sub_category and stage assigned by reading the Section 4 row against content/framework.md
    — Section 4 gives the type and reuse condition only, and the asset is unnumbered
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: african-voice-ai
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-c
stage: define
applies_when: Deploying voice AI in a language with existing or buildable ASR/TTS components and wanting
  to avoid rebuilding orchestration from scratch.
fails_when: A telephony-only deployment with reliable connectivity, where a bundled commercial provider
  would be faster.
purpose: An SDK with an Apache 2.0 plugin interface for ASR, TTS and LLM components, which partner startups
  integrate into their own field-agent workflows.
reuse_condition: Applies when deploying voice AI in a language with existing or buildable ASR/TTS components
  and wanting to avoid rebuilding orchestration from scratch; does not apply for a telephony-only deployment
  with reliable connectivity where a bundled commercial provider would be faster.
adopter_intents:
- How do we make one SDK work across sectors or languages?
- Can we reuse an existing voice orchestration stack instead of building one?
related_units:
- african-voice-ai-plugin-architecture-sector-agnostic
- african-voice-ai-public-good-needs-durable-maintainer
---

## Unit

According to Crane AI Labs and the UNDP AI Hub for Sustainable Development's African Voice AI pathway, the asset is: the African Voice AI SDK — an Apache 2.0 plugin interface for ASR, TTS and LLM components, delivered to partner startups who integrate it into their own field-agent workflows. The repository URL and the interface specification are not documented in the source, so no file or link is attached here.

**Purpose:** Lets ASR, TTS and LLM components be registered for a language without rebuilding orchestration from scratch.

**Reuse condition:** Applies when deploying voice AI in a language with existing or buildable ASR/TTS components and wanting to avoid rebuilding orchestration from scratch; does not apply for a telephony-only deployment with reliable connectivity where a bundled commercial provider would be faster.

## Condition

- **Applies when:** Deploying voice AI in a language with existing or buildable ASR/TTS components and wanting to avoid rebuilding orchestration from scratch.
- **Fails when:** A telephony-only deployment with reliable connectivity, where a bundled commercial provider would be faster.

## Why it is reusable

It is an openly licensed orchestration SDK an adopter could build on instead of starting from scratch, with a stated case where a bundled commercial provider is the better choice. Who maintains it after the programme ends is unresolved (see the maintainer unit).
