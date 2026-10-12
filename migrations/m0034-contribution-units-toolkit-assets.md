---
name: 0034 — Toolkit assets in contribution_units
type: migration
schema_version: 1
aliases:
- 0034_contribution_units_toolkit_assets.sql
summary: Adds toolkit asset columns and a shape check to contribution_units, drops its client insert/update
  policies, and creates the private toolkit-assets storage bucket.
number: '0034'
file: supabase/migrations/0034_contribution_units_toolkit_assets.sql
tables_touched:
- contribution-units
- toolkit-assets-bucket
destructive: true
decision: toolkit-assets-in-contribution-units-service-role-only
code_refs:
- supabase/migrations/0034_contribution_units_toolkit_assets.sql
- lib/toolkit-assets-server.ts
- app/api/toolkit-assets/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0034_contribution_units_toolkit_assets.sql
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Adds `asset_kind`, `asset_name`, `purpose`, `reuse_condition`, `storage_path`, `file_name`, `mime_type`, `size_bytes`, `link_url` (https-only check), `share_consent`, `share_consented_at`; adds `contribution_units_toolkit_asset_shape`; adds a partial index for toolkit assets; drops the two client write policies; upserts the private `toolkit-assets` bucket (25 MB, 14 MIME types, no ZIP).

## Why

Contributors can attach the real file or link behind a Toolkit Asset after explicit public-sharing consent; assets go live only when an admin publishes the pathway. The old write policies let a user self-publish by setting `published_at`. See docs/tasks/toolkit-asset-files/plan.md.

Not covered by the generated `docs/wiki` database page, which stops at 0032.

## Risk

Not purely additive: dropping the policies means any client-side write to the table now fails (the file says nothing used them). This makes contribution_units live again, contradicting the generated wiki's "inert" label.
