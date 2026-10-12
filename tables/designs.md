---
name: designs
type: table
schema_version: 1
summary: 'One row per adoption workspace (Explorer analysis or Contributor pathway workspace): conversation
  messages, grid_state and meta jsonb, owner-only RLS.'
table_name: designs
store_kind: table
status: live
key_columns:
- id uuid PK
- user_id uuid → auth.users (cascade)
- meta jsonb
- grid_state jsonb (renamed from cube_state in 0008)
- messages jsonb
- pathway_id uuid → pathways (set null, 0024)
- created_at
- updated_at
rls: Owner-only select/insert/update/delete (auth.uid() = user_id)
references_tables:
- auth-users
- pathways-table
created_in: m0001-designs
code_refs:
- supabase/migrations/0001_designs.sql
- supabase/migrations/0008_grid_revamp.sql
- supabase/migrations/0024_designs_pathway_fk.sql
- lib/adoption-conversation.ts
- lib/adoptions-cache.ts
- app/(app)/adoptions/page.tsx
- app/api/pathways/assemble/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0001_designs.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0008_grid_revamp.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0024_designs_pathway_fk.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

| Column | Notes |
|---|---|
| `id` | uuid PK |
| `user_id` | defaults to `auth.uid()`; FK `auth.users` on delete cascade |
| `meta` | jsonb — flow, intent, flowStep, stage and the rest of the adoption meta (see the `designs-meta` contract) |
| `grid_state` | jsonb — the 16-cell 4×4 coverage grid; was `cube_state` (7-dimension cube) until migration 0008 |
| `messages` | jsonb — the conversation |
| `pathway_id` | FK `pathways` on delete set null (0024). Set only for Contributor workspaces; always null for Explorer adoptions |
| `document_review_turns_left`, `typed_intro_turns_left` | integers from 0001 — nothing in current code reads or writes them |
| `created_at`, `updated_at` | timestamps |

## RLS

Four owner-scoped policies (select, insert, update, delete) on `auth.uid() = user_id`. The app writes it from the
browser client (`lib/adoption-conversation.ts` insert/update, `app/(app)/adoptions/page.tsx` delete), so RLS is the
real enforcement here. Server routes (`/api/pathways/assemble`, `/api/toolkit-assets`) deliberately read it through the
caller's session client so RLS proves the design belongs to the caller.

## Lifecycle

Created when a user starts an adoption; updated every chat turn (`persist` in `lib/adoption-conversation.ts`); deleted by
the owner from /adoptions or by cascade when the auth user is deleted (account deletion). Deleting a design cascades
`design_documents` and `adoption_queries`; `contribution_units.design_id` is set null.

## Gotchas

- Migration 0008 deleted every row (old 7-dimension shape, confirmed test data) before renaming `cube_state` → `grid_state`.
- Two dead integer columns survive from 0001.
- Deleting a `pathways` row leaves the contributor's design intact but unlinked (`pathway_id` → null).
