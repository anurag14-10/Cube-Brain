---
name: POST /api/pathway-submissions/push
type: endpoint
schema_version: 1
summary: 'Dead code: the old contributor self-serve push of a pathway_submissions draft straight into
  published_pathways. Reads a table dropped in migration 0018 and has no caller.'
tags:
- contributor
- dead-code
- publish
path: /api/pathway-submissions/push
methods:
- POST
file: app/api/pathway-submissions/push/route.ts
access: role-gated
roles:
- pathway-contributor
- admin
tables_read:
- user-roles
- pathway-submissions
- designs
- published-pathways
- auth-users
tables_written:
- published-pathways
- pathway-submissions
integrations:
- supabase-postgres
- supabase-auth
request_shape: 'JSON {submission_id: string, commit_message?: string}'
response_shape: 'JSON {ok: true, slug} — unreachable; in practice 404 {error:''Submission not found.''}'
status: dead-code
code_refs:
- app/api/pathway-submissions/push/route.ts
- supabase/migrations/0018_drop_retired_tables.sql
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/pathway-submissions/push/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0018_drop_retired_tables.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
contested:
- field: status
  readings:
  - 'lib/grid-update.ts comment: pathwayAction ''publish'' ''triggers the push route directly from chat'''
  - 'code: handlePathwayAction(''publish'') calls publishPathwayDocument → POST /api/pathways/assemble;
    nothing calls /api/pathway-submissions/push'
  note: The grid-update.ts comment is stale; the code supports dead-code.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

`{submission_id, commit_message?}` → would load the submission, require caller ownership unless admin, derive title/description/sector from `designs.meta`, look up the submitter's `user_metadata.organization` via `auth.admin.getUserById` as `contributor_org`, then update-or-insert `published_pathways` keyed on `source_submission_id` (keeping the slug on re-push) and mark the submission `published`. This was a one-step contributor publish with no admin gate — the model the current two-step publish replaced.

## Enforcement

Session (401), then `hasRole('pathway_contributor')` OR `isAdmin` (403 `Pushing to the wiki requires the Contributor role.`), then own-submission check.

## Side effects

None. Queries `pathway_submissions`, dropped (with pathway_submission_versions and pathway_submission_exec_summaries) by migration 0018; any call fails at the first select. Also writes `commit_message` and `contributor_org` columns on `published_pathways` that nothing else writes.

## Errors

404 after auth. No file in app/, components/ or lib/ fetches this path.
