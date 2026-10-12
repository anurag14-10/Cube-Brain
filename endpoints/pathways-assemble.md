---
name: POST /api/pathways/assemble
type: endpoint
schema_version: 1
aliases:
- contributor publish
- Send for review
summary: 'Step one of two-step publish: commits the caller''s latest pathway draft (plus the regenerated
  toolkit-asset block) to GitHub as content/wiki/pathways/<slug>.md and caches it on the pathway with
  review_requested=true.'
tags:
- contributor
- publish
- github
path: /api/pathways/assemble
methods:
- POST
file: app/api/pathways/assemble/route.ts
access: role-gated
roles:
- pathway-contributor
tables_read:
- user-roles
- pathway-contributors
- designs
- pathways-table
- design-documents
- contribution-units
tables_written:
- pathways-table
integrations:
- github-contents-api
- supabase-postgres
- supabase-auth
request_shape: 'JSON {pathwayId: uuid, designId: uuid, commitMessage?: string (sent by the client, ignored
  by the route)}'
response_shape: 'JSON {content: <draft markdown without asset block>, slug, assembled_design_doc_id}'
status: live
code_refs:
- app/api/pathways/assemble/route.ts
- app/api/pathways/assemble/route.ts#L41-L63
- app/api/pathways/assemble/route.ts#L83-L120
- lib/github.ts
- lib/toolkit-assets.ts#L217-L237
- lib/adoption-conversation.ts#L555-L596
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/pathways/assemble/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/adoption-conversation.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

Body `{pathwayId, designId}` (both required, 400 otherwise). Called by `publishPathwayDocument` in lib/adoption-conversation.ts when the contributor companion emits `pathwayAction: {type:'publish'}`, and from components/AdoptionWorkspace.tsx. The client also sends `commitMessage`; the route never reads it — the commit message is always `publish pathway: <slug>`.

Response `{content, slug, assembled_design_doc_id}` — `content` is the raw draft (the client syncs its pane to it).

## Enforcement

1. Session (401), `hasAnyRole` (403 `Account not approved`), `hasRole('pathway_contributor')` (403).
2. Membership: a `pathway_contributors` row for (pathwayId, caller) via the session client (403 `Not a contributor to this pathway`).
3. Ownership: `designs` row for `designId` must be visible to the caller (RLS: own designs only) and have `pathway_id === pathwayId` (403 `Not your workspace for this pathway`) — prevents publishing another member's private draft.
4. `isValidSlug(pathway.slug)` before the slug becomes a GitHub path (400).

## Side effects

1. Latest draft: `design_documents` where `design_id`, `user_id = caller`, `doc_type='draft'`, ordered by `version_number desc`, limit 1 (400 `No draft found…` if none).
2. `loadPathwayToolkitAssets(pathwayId)` (all consented assets, published or not) → `applyToolkitAssetBlock(draft, assets.map(toBlockEntry))` inserts the `<!-- toolkit-assets:start -->…<!-- toolkit-assets:end -->` block with `<!-- asset-id: … -->` markers at the end of Section 4.
3. `ghReadFile` then `ghWriteFile('content/wiki/pathways/<slug>.md', assembled, 'publish pathway: <slug>', sha)` — a whole-document GitHub commit, verbatim; no reformatting or unit extraction.
4. Best-effort `pathways` update: `content_cache = assembled`, `review_requested = true`, `assembled_design_doc_id = draft.id`.

The pathway is **not** live after this: it only reaches `published_pathways` via [admin-pathways-publish](admin-pathways-publish.md). Because the commit lands in `content/wiki/pathways/` but `index.md` is not updated, the file is not picked up by `loadWikiContext` grounding until indexed.

## Errors

Any throw in steps 2–3 → 500 `{error:'Publish failed', detail}`. The pathways update result is not checked.
