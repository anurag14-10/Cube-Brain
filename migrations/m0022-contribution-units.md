---
name: 0022 — Create contribution_units
type: migration
schema_version: 1
aliases:
- 0022_contribution_units.sql
summary: Creates contribution_units — individually tagged content atoms (identity and micro-innovation
  units) with an author-only edit boundary in RLS.
number: '0022'
file: supabase/migrations/0022_contribution_units.sql
tables_touched:
- contribution-units
- pathways-table
- designs
- auth-users
destructive: false
code_refs:
- supabase/migrations/0022_contribution_units.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0022_contribution_units.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.contribution_units` (`unit_internal_id`, `pathway_id`, `design_id`, `user_id` cascade, `section`, `unit_type`, `dimension`/`stage`/`density` checks, `source_doc`, `git_commit_sha`, `published_at`) with select (published or own), insert-own and update-own policies.

## Why

Store each authored unit's index and metadata with text in per-contributor GitHub draft files; assembly would bucket Section 3 by dimension and stage.

## Risk

The design was never wired up for content; the cascading `user_id` would later have deleted published units with their author (fixed in 0033).
