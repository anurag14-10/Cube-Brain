---
name: 0027 — Allow draft doc_type
type: migration
schema_version: 1
aliases:
- 0027_design_documents_draft_type.sql
summary: Widens design_documents.doc_type to allow draft — fixing every Contributor draft insert silently
  failing the old check.
number: '0027'
file: supabase/migrations/0027_design_documents_draft_type.sql
tables_touched:
- design-documents
destructive: false
code_refs:
- supabase/migrations/0027_design_documents_draft_type.sql
- lib/design-documents.ts
- app/api/pathways/assemble/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0027_design_documents_draft_type.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Drops and re-adds `design_documents_doc_type_check` with `('analysis','plan','draft')`.

## Why

The Contributor flow stores drafts as `doc_type = 'draft'` (`lib/design-documents.ts`); until this ran no draft reached the DB and assemble never found one.

## Risk

None. It is the fix for a real production bug.
