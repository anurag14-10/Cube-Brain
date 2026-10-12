---
name: 0001 — Create designs
type: migration
schema_version: 1
aliases:
- 0001_designs.sql
summary: Creates the designs table (one row per adoption) with meta / cube_state / messages jsonb and
  owner-only RLS.
number: '0001'
file: supabase/migrations/0001_designs.sql
tables_touched:
- designs
- auth-users
destructive: false
code_refs:
- supabase/migrations/0001_designs.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0001_designs.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.designs` (`id`, `user_id` default `auth.uid()` FK auth.users cascade, `meta`, `cube_state`, `messages` jsonb, two turn-counter integers, timestamps), enables RLS and adds owner select/insert/update/delete policies.

## Why

The base persistence for a user's adoption conversation — the first table of the app.

## Risk

None at creation. The two turn-counter columns became dead; `cube_state` was later renamed and its data wiped (0008).
