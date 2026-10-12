---
name: library_conversations
type: table
schema_version: 1
summary: Saved /explore library chats for signed-in users (one row per conversation), full owner CRUD.
table_name: library_conversations
store_kind: table
status: live
key_columns:
- id uuid PK
- user_id → auth.users (cascade, default auth.uid())
- pathway_slug
- pathway_title
- messages jsonb
- created_at
- updated_at
rls: Owner-only select/insert/update/delete
references_tables:
- auth-users
created_in: m0029-library-conversations
code_refs:
- supabase/migrations/0029_library_conversations.sql
- app/explore/ExploreLibrary.tsx
- components/Sidebar.tsx
- app/explore/page.tsx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0029_library_conversations.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/explore/ExploreLibrary.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: components/Sidebar.tsx
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

`pathway_slug` / `pathway_title` are set when the chat started from a pathway card, null for a general question.
Index `(user_id, updated_at desc)`.

## RLS

Four owner policies. Written from the browser client (`app/explore/ExploreLibrary.tsx` insert/update,
`components/Sidebar.tsx` list/delete); read server-side in `app/explore/page.tsx`.

## Lifecycle

Anonymous visitors' library chats stay in memory only; signed-in users' chats are saved and resumable. Cascades with
the auth user.

## Gotchas

- Not an adoption: no grid or meta, separate from `designs`.
