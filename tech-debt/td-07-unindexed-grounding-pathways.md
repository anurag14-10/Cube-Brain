---
name: TD-07 Six grounding-corpus pathway files not linked from index.md
type: tech_debt
schema_version: 1
aliases:
- TD-07
summary: lib/wiki-loader.ts and lib/wiki-content.ts discover pathways only through index.md links; six
  on-disk pathway files are not linked and are excluded from grounding and from the /wiki listing.
tags:
- content
- corpus
- silent-gap
td_id: TD-07
severity: P2
status: open
affected_modules:
- lib-wiki-loader
- lib-wiki-content
remediation: Link the six files from content/wiki/pathways/index.md, or confirm they are superseded by
  published_pathways rows and remove them.
code_refs:
- content/wiki/pathways/index.md
- lib/wiki-loader.ts#L88-L96
- lib/wiki-content.ts
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
  ref: content/wiki/pathways/index.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

Verified at `28068b6`: `index.md` links only african-voice-ai, bhili-language-enablement, blue-dots, mahavistaar, voice-ai-adoption-barriers and voice-ai-for-inclusion. These six files are on disk but unlinked: ai-advisory-for-dairy-farmers, ai-assisted-job-matching, ai-crop-diagnosis-advisory, assisted-language-math-learning, nivesh-suvidha and unififed-ai-driven-agri-ecosystem (the "unififed" typo is the real filename). Contributor "publish pathway:" commits added most of them between 2026-08-31 and 2026-09-18.

## Impact

The six pathways are left out of the companion's grounding corpus and the `/wiki` listing, although `/wiki/<slug>` still reads them directly by slug. Whether they also exist as `published_pathways` rows cannot be told from the repository. The gap is silent: matching quietly ignores them.

## Remediation

Link them or remove them. Either way, the decision should be recorded.
