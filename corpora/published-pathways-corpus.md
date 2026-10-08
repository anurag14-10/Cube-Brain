---
name: Published pathways (database corpus)
type: corpus
schema_version: 1
aliases:
- published_pathways
summary: Community-contributed pathways made live by admin publish; merged into both in-repo corpora at
  read time.
corpus_kind: database
location: published_pathways
grounding_scope: merged into both corpora by slug
code_refs:
- supabase/migrations/0012_published_pathways.sql
- app/api/admin/pathways/publish/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0012_published_pathways.sql
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it is

Rows in the `published_pathways` table, public-read. The only place community content goes live —
written by `POST /api/admin/pathways/publish`, no redeploy needed.

## Who reads it

All three corpus loaders. A DB row overrides an in-repo file with the same slug.
