---
name: toolkit-assets (storage bucket)
type: table
schema_version: 1
aliases:
- toolkit-assets
summary: 'Private Supabase Storage bucket holding toolkit asset files: 25 MB limit, a 14-type MIME allow-list
  (no ZIP), no client policies; every upload/download URL is minted server-side.'
table_name: toolkit-assets
store_kind: storage-bucket
status: live
key_columns:
- object path <pathway_id>/<uuid>/<sanitised file name>
- public = false
- file_size_limit 26214400 (25 MB)
- 'allowed_mime_types: pdf, doc/docx, ppt/pptx, xls/xlsx, csv, txt, md, png, jpeg, gif, webp'
rls: No storage.objects policies — anon and authenticated clients cannot read or write; service-role only
created_in: m0034-contribution-units-toolkit-assets
code_refs:
- supabase/migrations/0034_contribution_units_toolkit_assets.sql
- lib/toolkit-assets-server.ts
- lib/toolkit-assets.ts
- app/api/toolkit-assets/upload-url/route.ts
- app/api/toolkit-assets/[id]/download/route.ts
- app/api/account/delete/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0034_contribution_units_toolkit_assets.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/toolkit-assets-server.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/toolkit-assets.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

A storage bucket, not a table. Created by migration 0034 (`insert into storage.buckets … on conflict do update`).
Object paths are built server-side by `buildAssetStoragePath`: `<pathway_id>/<uuid>/<sanitised file name>`. Each file has
exactly one `contribution_units` row (`storage_path`).

## RLS

No policies on `storage.objects` for this bucket. Supabase itself enforces the size and MIME limits.

- Upload: `POST /api/toolkit-assets/upload-url` mints a signed upload URL (service role); the browser uploads with
  `uploadToSignedUrl`; `POST /api/toolkit-assets` then checks the object exists, its size, and that the path is under the
  pathway's own prefix.
- Download: `GET /api/toolkit-assets/[id]/download` mints a 60-second signed URL server-side and streams the file, so the
  storage URL never reaches the browser.

## Lifecycle

Files removed (best-effort, logged on failure) when an admin deletes the pathway (all statuses) or when the uploader
deletes their account (unpublished files only). Published files outlive their author.

## Gotchas

- ZIP is deliberately not allowed.
- Storage failures on delete never block the delete, so orphan objects are possible if removal fails.
