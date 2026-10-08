---
name: Library corpus
type: corpus
schema_version: 1
aliases:
- content/library-wiki/pathways
- Diffusion Library
summary: In-repo, conversational-tone pathway documents behind the public /explore library, grounded one
  document at a time.
corpus_kind: static-repo
location: content/library-wiki/pathways
grounding_scope: one document at a time
voice: conversational, no grid
merges_with:
- published-pathways-corpus
code_refs:
- content/library-wiki/pathways
- lib/library-wiki-loader.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/library-wiki-loader.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it is

Overview-style pathway documents for the public, no-login Diffusion Library (`/explore`).

## How it is loaded

`lib/library-wiki-loader.ts`; no index file. Merged with `published_pathways` by slug (DB wins).

## Divergence from other corpora

Not the same documents as the grounding corpus even where slugs match (TD-02).
