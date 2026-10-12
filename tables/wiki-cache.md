---
name: wiki_cache
type: table
schema_version: 1
summary: Inert shared cache of wiki pages fetched from GitHub raw, from before the corpus moved into the
  repo; no code references it.
table_name: wiki_cache
store_kind: table
status: inert
key_columns:
- path text PK
- content text
- fetched_at
rls: Authenticated select/insert/update
created_in: m0004-wiki-cache
code_refs:
- supabase/migrations/0004_wiki_cache.sql
- lib/wiki-loader.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0004_wiki_cache.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/wiki-loader.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`path` PK, `content`, `fetched_at`.

## RLS

Any authenticated user may read, insert and update.

## Lifecycle

Replaced an in-memory cache when the corpus was fetched from GitHub. The corpus now ships in `content/` and is read
from the filesystem (`lib/wiki-loader.ts`), so nothing reads or writes this table.

## Gotchas

- Writable by any authenticated user though unused.
