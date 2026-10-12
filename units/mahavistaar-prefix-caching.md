---
name: MahaVISTAAR — prefix caching to avoid re-paying for conversation history
type: unit
schema_version: 1
summary: Serving-stack prefix caching so repeated system prompt and prior-turn context aren't recomputed
  — input tokens were 79.7% of spend.
code_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Toolkit Asset
dimension: solution
sub_category: solution-e
stage: scale
source_unit_id: Unit 22
applies_when: Turns share a large repeated prefix — ~37% of notional input compute is skipped on a three-turn
  conversation.
fails_when: Not documented in the source
purpose: Cuts redundant compute on the largest share of cost — input tokens — for conversations that share
  a long, repeated prefix.
reuse_condition: A serving-stack configuration; any vLLM-style deployment with multi-turn, tool-heavy
  conversations can enable the equivalent.
adopter_intents:
- What's actually driving our LLM costs, and can we bring them down?
related_units:
- mahavistaar-cost-modelling-framework
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the asset is: prefix caching on the self-hosted stack so a multi-turn conversation's repeated system prompt and prior-turn context isn't recomputed each turn.

**Purpose:** Cuts redundant compute on the largest share of cost — input tokens — for conversations that share a long, repeated prefix.

**Reuse condition:** A serving-stack configuration; any vLLM-style deployment with multi-turn, tool-heavy conversations can enable the equivalent.

## Condition

- **Applies when:** Turns share a large repeated prefix — ~37% of notional input compute is skipped on a three-turn conversation.
- **Fails when:** Not documented in the source

## Why it is reusable

It points adopters at the real cost lever (input tokens) rather than output-token efficiency, with a configuration change they can lift directly.
