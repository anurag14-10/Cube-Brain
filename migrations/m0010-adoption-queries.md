---
name: 0010 — Create adoption_queries
type: migration
schema_version: 1
aliases:
- 0010_adoption_queries.sql
summary: Creates adoption_queries, an insert-only log of companion-mode user messages.
number: '0010'
file: supabase/migrations/0010_adoption_queries.sql
tables_touched:
- adoption-queries
- designs
- auth-users
destructive: false
code_refs:
- supabase/migrations/0010_adoption_queries.sql
- app/api/chat/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0010_adoption_queries.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.adoption_queries` (`design_id` nullable FK, `user_id`, `content`) with an insert-own policy only.

## Why

Start capturing raw material for a deferred cross-adoption "what have others asked" feature.

## Risk

Low. Grows with every companion turn; nothing reads it.
