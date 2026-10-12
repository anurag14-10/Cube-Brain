---
name: MahaVISTAAR — start bundled to learn fast; design so you can unbundle later
type: unit
schema_version: 2
summary: Launch on a bundled commercial provider for speed while designing modularity in from day one;
  the later move to self-hosting cut cost per question about 180x.
tags:
- relevant-to-government
doc_refs:
- content/wiki/pathways/mahavistaar.md
sources:
- system: diffusion_cube_code
  method: document
  date: '2026-10-08'
  ref: content/wiki/pathways/mahavistaar.md
- system: diffusion_cube_code
  method: derived
  date: '2026-10-12'
  ref: content/wiki/pathways/mahavistaar.md — sub_category inferred; the document tags each unit with dimension, stage and type only
first_logged: '2026-10-12'
last_updated: '2026-10-12'
pathway: mahavistaar
unit_type: Strategic Decision
dimension: solution
sub_category: solution-c
stage: define
source_unit_id: Unit 9
applies_when: Speed of early deployment matters more than day-one cost or control.
fails_when: No deliberate unbundling decision is ever made once real users and stakes exist.
decision: Launch on a bundled commercial provider (GPT-4.1 / Azure OpenAI) for speed, while designing
  so it can later be unbundled to a self-hosted model.
alternative_considered: Build self-hosted and unbundled from day one.
reason: Speed of early deployment and learning outweighed day-one cost and control; the risk isn't starting
  bundled, it's staying bundled by accident once real users and stakes exist.
context: The pathway records the self-hosted target as a fine-tuned open-source model (Qwen3.5-27B); input
  tokens were 79.7% of spend.
before: ~₹9.4 per question on Azure OpenAI (Nov 2025).
after: ~₹0.05 per question self-hosted — a 180x reduction, achievable because modularity was designed
  in on day one.
adopter_intents:
- Should we build everything ourselves or start on a commercial API?
- How do we stop a single vendor from locking us in?
- What's actually driving our LLM costs, and can we bring them down?
related_units:
- mahavistaar-dual-provider-inference-stack
- mahavistaar-cost-modelling-framework
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the decision was: Launch on a bundled commercial provider (GPT-4.1 / Azure OpenAI) for speed, while designing so it can later be unbundled to a self-hosted model.

**Alternative considered:** Build self-hosted and unbundled from day one.

**Why:** Speed of early deployment and learning outweighed day-one cost and control; the risk isn't starting bundled, it's staying bundled by accident once real users and stakes exist.

**In this deployment:** The pathway records the self-hosted target as a fine-tuned open-source model (Qwen3.5-27B); input tokens were 79.7% of spend.

## Condition

- **Applies when:** Speed of early deployment matters more than day-one cost or control.
- **Fails when:** No deliberate unbundling decision is ever made once real users and stakes exist.

## Before → after

- **Before:** ~₹9.4 per question on Azure OpenAI (Nov 2025).
- **After:** ~₹0.05 per question self-hosted — a 180x reduction, achievable because modularity was designed in on day one.

## Why it is reusable

It separates two decisions adopters usually merge — where to start and whether you can leave — and shows the payoff of keeping the second open.
