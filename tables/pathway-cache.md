---
name: pathway_cache
type: table
schema_version: 1
summary: Inert shared cache of AI-generated pathway outputs keyed by slug and content hash; no code references
  it.
table_name: pathway_cache
store_kind: table
status: inert
key_columns:
- slug text PK
- content_hash
- cube_state jsonb
- card
- summary
- updated_at
rls: Authenticated select/insert/update
created_in: m0002-pathway-cache
code_refs:
- supabase/migrations/0002_pathway_cache.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0002_pathway_cache.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`slug` PK, `content_hash`, `cube_state` (old 7-dimension shape), `card`, `summary`, `updated_at`.

## RLS

Any authenticated user may read, insert and update.

## Lifecycle

Built for the old explore-init/explore-copy flows; those are gone. A repo-wide grep finds no reader or writer.

## Gotchas

- Still writable by any authenticated user through the REST API although nothing uses it.
