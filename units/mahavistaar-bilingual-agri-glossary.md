---
name: MahaVISTAAR — bilingual Marathi↔English agricultural glossary
type: unit
schema_version: 2
summary: A terminology bridge for crop, pest, scheme and mandi terms that keeps ASR/TTS accurate without
  translating the whole advisory corpus.
doc_refs:
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
sub_category: solution-d
stage: define
source_unit_id: Unit 16
applies_when: Marathi-language deployments.
fails_when: Not documented in the source
purpose: Keeps domain-specific terms accurate across ASR/TTS without needing to translate the entire advisory
  corpus.
reuse_condition: Via OpenAgriNet; applies for Marathi-language deployments.
---

## Unit

According to the MahaVISTAAR pathway contributed by the Department of Agriculture (Government of Maharashtra), EkStep Foundation and OpenAgriNet, the asset is: a terminology bridge supporting ASR/TTS accuracy for crop, pest, scheme, and mandi terms.

**Purpose:** Keeps domain-specific terms accurate across ASR/TTS without needing to translate the entire advisory corpus.

**Reuse condition:** Via OpenAgriNet; applies for Marathi-language deployments.

## Condition

- **Applies when:** Marathi-language deployments.
- **Fails when:** Not documented in the source

## Why it is reusable

A domain glossary is a cheap accuracy lever an adopter can lift directly for Marathi, or copy as a method for another language.
