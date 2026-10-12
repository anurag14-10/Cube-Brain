---
name: design_documents
type: table
schema_version: 1
summary: Append-only versioned generated documents per design — Analysis Document, Executive Summary/Plan,
  and the Contributor pathway draft (doc_type analysis | plan | draft).
table_name: design_documents
store_kind: table
status: live
key_columns:
- id uuid PK
- design_id uuid → designs (cascade)
- user_id uuid → auth.users (cascade)
- doc_type text check in (analysis, plan, draft)
- version_number int
- content_hash text
- content text
- created_at
rls: Owner select and insert only (auth.uid() = user_id); no update/delete policy — append-only
references_tables:
- designs
- auth-users
created_in: m0003-design-documents
code_refs:
- supabase/migrations/0003_design_documents.sql
- supabase/migrations/0027_design_documents_draft_type.sql
- supabase/migrations/0032_pathways_design_doc_ids.sql
- supabase/migrations/0033_account_deletion.sql
- lib/design-documents.ts
- app/api/pathways/assemble/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0003_design_documents.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0027_design_documents_draft_type.sql
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

## Columns

`id`, `design_id` (FK designs, cascade), `user_id` (default `auth.uid()`, FK auth.users cascade), `doc_type`,
`version_number`, `content_hash`, `content`, `created_at`. Index `(design_id, doc_type, version_number desc)` — an
index, **not** a unique constraint.

## RLS

Owner select + insert. No update or delete policy: every regeneration inserts a new version; an unchanged
`content_hash` is meant to be a cache hit. Written from the browser client in `lib/design-documents.ts`; the assemble
route reads the latest `draft` row with the service-role client (filtered to the caller's design and user id).

## Lifecycle

Inserted on every Analysis / Plan generation and every Contributor draft generate/revise. `pathways.assembled_design_doc_id`
and `pathways.published_design_doc_id` point at draft rows (0032; on delete set null since 0033). Removed by cascade
when the design or the auth user is deleted.

## Gotchas

- `doc_type` originally allowed only `analysis` and `plan`. Every Contributor `draft` insert silently failed the check
  constraint until migration 0027 widened it — so assemble could never find a draft before then.
- No uniqueness on `(design_id, doc_type, version_number)`: two concurrent generations could write the same version number.
- For `analysis`/`plan` only the latest version is read back; `draft` versions are all browsable (version picker).
