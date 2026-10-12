---
name: 0032 — Add assembled/published design doc ids to pathways
type: migration
schema_version: 1
aliases:
- 0032_pathways_design_doc_ids.sql
summary: Adds assembled_design_doc_id and published_design_doc_id FKs from pathways to design_documents.
number: '0032'
file: supabase/migrations/0032_pathways_design_doc_ids.sql
tables_touched:
- pathways-table
- design-documents
destructive: false
code_refs:
- supabase/migrations/0032_pathways_design_doc_ids.sql
- app/api/pathways/assemble/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0032_pathways_design_doc_ids.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Adds two uuid columns referencing `design_documents(id)` with no ON DELETE action.

## Why

Record which draft version was assembled and which was published. The migration has no comment.

## Risk

The missing ON DELETE action would block deleting a user whose drafts were referenced (fixed in 0033).
