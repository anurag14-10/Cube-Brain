---
name: Supabase Storage
type: integration
schema_version: 1
summary: Only the private `toolkit-assets` bucket (toolkit asset files, added 2026-09-30).
integration_kind: object-storage
provider: Supabase
sdk: '@supabase/supabase-js@^2.110.0'
account_notes: Same Supabase project. The bucket limits are set by migration 0034.
config_vars:
- next-public-supabase-url
- supabase-service-role-key
code_refs:
- lib/toolkit-assets-server.ts
- supabase/migrations/0034_contribution_units_toolkit_assets.sql
- lib/adoption-conversation.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/toolkit-assets-server.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0034_contribution_units_toolkit_assets.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
contested:
- field: summary
  readings:
  - docs/wiki third-party-integrations.md lists Supabase as "Postgres + Auth" only
  - 'code + migration 0034: Supabase Storage (private toolkit-assets bucket) is also used'
  note: The doc predates 0034 (refreshed 2026-09-28). The code supports the second reading.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

Only the private `toolkit-assets` bucket (toolkit asset files, added 2026-09-30). The server mints signed upload URLs; the browser uploads with `uploadToSignedUrl`; downloads are streamed by the server through a 60-second signed URL. Objects are removed when their pathway or the uploader's account is deleted (unpublished files only for account deletion).

## Configuration

`NEXT_PUBLIC_SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`. The browser upload uses the anon client with a signed token.

## Failure behaviour

Upload or info failures return 400/500 to the contributor. Remove failures are logged and never block a delete, so orphan objects are possible.

## Account

Same Supabase project. The bucket limits are set by migration 0034.
