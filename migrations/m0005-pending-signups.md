---
name: 0005 — Create pending_signups
type: migration
schema_version: 1
aliases:
- 0005_pending_signups.sql
summary: Creates the pending_signups queue for the old admin-approval signup flow; RLS with no policies.
  Now inert.
number: '0005'
file: supabase/migrations/0005_pending_signups.sql
tables_touched:
- pending-signups
destructive: false
code_refs:
- supabase/migrations/0005_pending_signups.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0005_pending_signups.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.pending_signups` (`name`, `email`, `organization`, `status`, unique `approval_token`, timestamps), an email index, and enables RLS with zero policies.

## Why

Hold not-yet-verified signup requests and a single-use approval token server-side only, before any auth user existed.

## Risk

Holds personal data and tokens; the flow it served is gone, so it is retained data with no owner.
