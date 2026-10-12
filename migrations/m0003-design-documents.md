---
name: 0003 — Create design_documents
type: migration
schema_version: 1
aliases:
- 0003_design_documents.sql
summary: Creates the append-only versioned design_documents table for generated Analysis and Plan documents.
number: '0003'
file: supabase/migrations/0003_design_documents.sql
tables_touched:
- design-documents
- designs
- auth-users
destructive: false
code_refs:
- supabase/migrations/0003_design_documents.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0003_design_documents.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.design_documents` (`design_id` FK designs cascade, `user_id`, `doc_type` check in ('analysis','plan'), `version_number`, `content_hash`, `content`), an index on `(design_id, doc_type, version_number desc)` and owner select/insert policies.

## Why

Keep every generated version retrievable and let an unchanged content hash be a cache hit instead of a new model call.

## Risk

The narrow `doc_type` check later silently rejected every Contributor `draft` insert until 0027. No unique constraint on the version tuple.
