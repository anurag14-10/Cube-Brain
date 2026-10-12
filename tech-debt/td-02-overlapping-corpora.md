---
name: TD-02 Two overlapping, separately maintained pathway corpora
type: tech_debt
schema_version: 1
aliases:
- TD-02
summary: content/wiki/pathways (grounding) and content/library-wiki/pathways (Library) both hold documents
  for the same deployments, and nothing keeps their facts in sync.
tags:
- content
- corpus
td_id: TD-02
severity: P2
status: open
affected_modules:
- lib-wiki-loader
- lib-library-wiki-loader
- lib-library-pathways
remediation: Consolidate to one corpus with per-surface rendering, or record explicitly that the two corpora
  are intentionally independent and assign an owner for keeping shared facts aligned.
code_refs:
- content/wiki/pathways
- content/library-wiki/pathways
- lib/wiki-loader.ts
- lib/library-wiki-loader.ts
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: content/library-wiki/pathways
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

Verified at `28068b6`: six deployments have a document in both directories: african-voice-ai, bhili-language-enablement, blue-dots, mahavistaar, voice-ai-adoption-barriers and voice-ai-for-inclusion. The Library corpus also holds ceew-climate-intelligence and data-dhara, which the grounding corpus no longer has. They were removed from it when the corpus was rebuilt on 2026-08-31 (`cdc0c55`). The two corpora differ in structure and voice by design, but nothing keeps their facts consistent.

## Impact

An update to one copy, for example MahaVISTAAR, does not reach the other. The public `/explore` chat and the signed-in `/analyse` companion can then tell different stories about the same deployment. See the risk [corpus-content-drift](../risks/corpus-content-drift.md).

## Remediation

Consolidate, or document the split as intentional and name who keeps them aligned.
