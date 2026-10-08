---
name: Grounding corpus
type: corpus
schema_version: 1
aliases:
- content/wiki/pathways
- wiki corpus
summary: In-repo pathway documents the Explorer and Contributor flows are grounded in, whole-corpus.
corpus_kind: static-repo
location: content/wiki/pathways
index_file: content/wiki/pathways/index.md
grounding_scope: whole corpus (~22K tokens with framework)
voice: advisory, framework-tagged, drives <grid_update>
merges_with:
- published-pathways-corpus
code_refs:
- content/wiki/pathways
- lib/wiki-loader.ts
- lib/wiki-content.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/wiki-loader.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/ai-llm.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it is

The framework-structured pathway documents (Sections 0–6 + Source Trace) committed in the repo.

## How it is loaded

`lib/wiki-loader.ts` reads files linked from `index.md` (the sole discovery path), merges
`published_pathways` rows by slug (DB wins). `lib/wiki-content.ts` is a second read path for
`/wiki` browsing, stripping frontmatter and the Source Trace appendix.

## Divergence from other corpora

Shares several slugs with the library corpus but the documents are maintained independently (TD-02).
