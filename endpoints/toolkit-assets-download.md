---
name: GET /api/toolkit-assets/[id]/download
type: endpoint
schema_version: 1
summary: Streams a published toolkit-asset file to anyone (or 302s to a link asset's https URL) without
  exposing the storage URL; unpublished assets only to their uploader or an admin.
tags:
- toolkit-assets
- public
- storage
path: /api/toolkit-assets/[id]/download
methods:
- GET
file: app/api/toolkit-assets/[id]/download/route.ts
access: public
roles:
- anonymous-visitor
- adopter
- pathway-contributor
- admin
- general-user
tables_read:
- contribution-units
- user-roles
- toolkit-assets-bucket
integrations:
- supabase-storage
- supabase-postgres
- supabase-auth
request_shape: Path param id = 'asset-<uuid>'
response_shape: 200 file stream (Content-Type from mime_type, Content-Disposition attachment with RFC
  5987 filename, Cache-Control no-store, X-Content-Type-Options nosniff) | 302 to link_url | 404 JSON
status: live
code_refs:
- app/api/toolkit-assets/[id]/download/route.ts
- lib/toolkit-assets-server.ts#L134-L143
- lib/toolkit-assets-server.ts#L196-L211
doc_refs:
- specs/TOOLKIT_ASSETS_SPEC.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/toolkit-assets/[id]/download/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/toolkit-assets-server.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`GET /api/toolkit-assets/asset-<uuid>/download`. File assets: the route creates a 60-second signed URL server-side, fetches it, and pipes the body through as an attachment — the browser never sees the project host, bucket path or token. Link assets: `302` to `link_url` (must start `https://`), `Cache-Control: no-store`.

## Enforcement

Public via the proxy prefix. `isAssetId(id)` else 404. If `published_at` is null, only a signed-in user who is the row's `user_id` or `isAdmin` may download (owner preview / admin review); everyone else receives the same 404 as a nonexistent id (no existence leak).

## Side effects

Read-only. `loadToolkitAsset` uses the service-role client (anonymous visitors have no session for RLS).

## Errors

404 `Not found` (bad id, missing, unpublished-and-not-allowed, non-https link); 404 `This file is no longer available.` if the storage object is gone or the fetch fails.
