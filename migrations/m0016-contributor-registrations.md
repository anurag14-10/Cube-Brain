---
name: 0016 — Create contributor_registrations
type: migration
schema_version: 1
aliases:
- 0016_contributor_registrations.sql
summary: Creates the one-time contributor registration table (profile, declaration, MOU and attribution
  consent).
number: '0016'
file: supabase/migrations/0016_contributor_registrations.sql
tables_touched:
- contributor-registrations
- auth-users
destructive: false
code_refs:
- supabase/migrations/0016_contributor_registrations.sql
- lib/contributor-registration.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0016_contributor_registrations.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.contributor_registrations` (unique `user_id`, organisation/POC/pathway fields, `declaration_accepted`, `mou_accepted`, four `consent_*` flags) with owner select/insert.

## Why

Gate the Contribute flow behind a one-time intake mirroring stages 1–4 of the Contributor Brief spec.

## Risk

Stores personal contact data. Several columns were later dropped, renamed or left unused.
