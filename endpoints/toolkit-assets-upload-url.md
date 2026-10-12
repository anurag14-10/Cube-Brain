---
name: POST /api/toolkit-assets/upload-url
type: endpoint
schema_version: 1
summary: 'Step 1 of attaching a toolkit-asset file: for a pathway-member contributor, mints a one-time
  signed upload URL for a server-built path in the private toolkit-assets bucket.'
tags:
- toolkit-assets
- contributor
- storage
path: /api/toolkit-assets/upload-url
methods:
- POST
file: app/api/toolkit-assets/upload-url/route.ts
access: role-gated
roles:
- pathway-contributor
tables_read:
- user-roles
- pathway-contributors
tables_written:
- toolkit-assets-bucket
integrations:
- supabase-storage
- supabase-auth
- supabase-postgres
request_shape: 'JSON {pathwayId: string, fileName: string, size: number (bytes)}'
response_shape: 'JSON {path: ''<pathwayId>/<uuid>/<sanitised name>'', token: string, contentType: string}'
status: live
code_refs:
- app/api/toolkit-assets/upload-url/route.ts
- lib/toolkit-assets-server.ts#L173-L182
- lib/toolkit-assets.ts#L23-L71
- lib/adoption-conversation.ts#L762-L779
doc_refs:
- specs/TOOLKIT_ASSETS_SPEC.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/toolkit-assets/upload-url/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/toolkit-assets-server.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`{pathwayId, fileName, size}` → `{path, token, contentType}`. The browser then calls `supabase.storage.from('toolkit-assets').uploadToSignedUrl(path, token, file, {contentType})` directly (bypassing Vercel's request-size limit) and registers the object with `POST /api/toolkit-assets`. Path layout: [toolkit-asset-storage-path](../contracts/toolkit-asset-storage-path.md).

## Enforcement

Under the public `/api/toolkit-assets` prefix in proxy.ts, so the route does its own gate: `authorizePathwayContributor` (session, `pathway_contributor`, membership). Then `fileName` non-empty, `assetExtension(fileName)` in the allow-list (400 mentions ZIP is unsupported), `0 < size ≤ 25 MB`. The bucket's own `file_size_limit` / `allowed_mime_types` (migration 0034) are the real enforcement; these checks only fail early.

## Side effects

`createSignedUploadUrl(buildAssetStoragePath(pathwayId, fileName))` via the service-role client — the bucket has no client storage policies. Nothing is written until the browser uploads; an uploaded object with no subsequent register call is orphaned in the bucket.

## Errors

400 validation, 401/403 auth, 500 `Could not prepare the upload. Try again.`
