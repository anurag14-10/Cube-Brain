---
name: 0025 — Move unit content into contribution_units
type: migration
schema_version: 1
aliases:
- 0025_contribution_units_content.sql
summary: Adds contribution_units.content and drops git_commit_sha, abandoning per-contributor GitHub draft
  files.
number: '0025'
file: supabase/migrations/0025_contribution_units_content.sql
tables_touched:
- contribution-units
destructive: true
code_refs:
- supabase/migrations/0025_contribution_units_content.sql
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0025_contribution_units_content.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

`add column content text`; `drop column git_commit_sha`.

## Why

Keep unit text in the DB next to its metadata instead of in a GitHub draft file.

## Risk

Drops a column (destructive, though nothing was writing it).
