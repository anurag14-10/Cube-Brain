---
name: GET|POST /api/toolkit-assets
type: endpoint
schema_version: 1
summary: GET (public) returns card metadata for published toolkit assets by id; POST (pathway member contributor,
  after explicit share consent) registers an uploaded file or https link as an unpublished contribution_units
  row.
tags:
- toolkit-assets
- contributor
- public
path: /api/toolkit-assets
methods:
- GET
- POST
file: app/api/toolkit-assets/route.ts
access: role-gated
roles:
- pathway-contributor
- anonymous-visitor
- adopter
- admin
- general-user
tables_read:
- contribution-units
- pathways-table
- user-roles
- pathway-contributors
- designs
- toolkit-assets-bucket
tables_written:
- contribution-units
integrations:
- supabase-postgres
- supabase-auth
- supabase-storage
request_shape: 'GET: ?ids=asset-<uuid>,… (max 20, invalid ids dropped). POST: JSON {pathwayId, designId?,
  shareConsent: true, name, purpose?, reuseCondition?, dimension?, stage?, kind: ''file''|''link'', storagePath
  + fileName (file) | linkUrl (link)}'
response_shape: 'GET: JSON {assets: ToolkitAssetSummary[]} (never a storage path or URL). POST: 201 JSON
  {id: ''asset-<uuid>'', status: ''awaiting_pathway_review''}'
status: live
code_refs:
- app/api/toolkit-assets/route.ts
- app/api/toolkit-assets/route.ts#L31-L35
- app/api/toolkit-assets/route.ts#L44-L134
- lib/toolkit-assets-server.ts#L97-L167
- lib/adoption-conversation.ts#L746-L802
- supabase/migrations/0034_contribution_units_toolkit_assets.sql
doc_refs:
- specs/TOOLKIT_ASSETS_SPEC.md
- docs/tasks/toolkit-asset-files/plan.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/toolkit-assets/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/toolkit-assets-server.ts
contested:
- field: path
  readings:
  - 'docs/wiki api-specification.md: does not list any /api/toolkit-assets route'
  - 'code: three toolkit-asset routes exist (this one, upload-url, [id]/download)'
  note: The generated wiki predates migration 0034; trust the code.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

- **GET** `?ids=a,b` — dedupe, keep only `isAssetId` (`asset-<uuid v4 shape>`), cap 20 → `loadPublishedToolkitAssets({ids})` → `toSummary` (`{id, name, purpose, kind, fileName, sizeBytes, linkDomain, pathwaySlug, pathwayTitle, publishedAt}`). Unknown/unpublished ids silently omitted, so the client can pass whatever ids the model emitted (`toolkitAssetsReferenced` / `<toolkit_assets>` tag). Callers: components/ToolkitAssetCards.tsx, ToolkitAssetStatusList.tsx, AdminPathwayRowCard.tsx.
- **POST** — step 2 of attaching an asset (after the consent card's Yes and, for files, after the browser uploaded to the signed URL from [toolkit-assets-upload-url](toolkit-assets-upload-url.md)). Called by the consent handler in lib/adoption-conversation.ts.

## Enforcement

- GET: none — `/api/toolkit-assets` prefix is in proxy.ts `PUBLIC_PATHS` (published assets are public by contributor consent + admin approval).
- POST: `authorizePathwayContributor(supabase, body.pathwayId)` — session (401), `pathway_contributor` role (403), `pathwayId` present (400), `pathway_contributors` membership (403). Then `shareConsent === true` (400 `Public-sharing consent is required.`) and non-empty `name` (≤200 chars).
- File: `storagePath` must start with `<pathwayId>/`, contain no `..`, and the file extension must be in `ASSET_MIME_BY_EXTENSION`; object must exist (`assetObjectSize`) and be ≤ `MAX_ASSET_BYTES` (25 MB).
- Link: must parse as a URL with protocol `https:` and length ≤ 2000.

## Side effects

POST inserts via the service-role client (0034 removed every client write policy on `contribution_units`): `unit_internal_id='asset-<uuid>'`, `pathway_id`, `design_id` (only if the caller's own design for this pathway), `user_id`, `section='micro-innovation'`, `unit_type='toolkit-asset'`, `dimension`/`stage` (validated lowercase codes else null), `asset_name`, `purpose`, `reuse_condition` (≤1000 each), `share_consent=true`, `share_consented_at=now`, plus file columns (`asset_kind='file'`, `storage_path`, `file_name`, `mime_type` from extension, `size_bytes` from storage, `source_doc`) or link columns (`asset_kind='link'`, `link_url`, `source_doc`). `published_at` stays null until [admin-pathways-publish](admin-pathways-publish.md) publishes the document that lists it.

## Errors

POST: 400 validation messages (`kind must be file or link`, `Invalid file.`, `Uploaded file not found.`, `File is over 25 MB.`, `Links must be valid https:// URLs.`), 401/403 from authorisation, 500 `Could not save the asset. Try again.` GET never errors (load failures return `[]`).
