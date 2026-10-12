---
name: 0029 — Create library_conversations
type: migration
schema_version: 1
aliases:
- 0029_library_conversations.sql
summary: Creates library_conversations for saved /explore chats of signed-in users, with full owner CRUD.
number: '0029'
file: supabase/migrations/0029_library_conversations.sql
tables_touched:
- library-conversations
- auth-users
destructive: false
code_refs:
- supabase/migrations/0029_library_conversations.sql
- app/explore/ExploreLibrary.tsx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0029_library_conversations.sql
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/database.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it does

Creates `public.library_conversations` with an index `(user_id, updated_at desc)` and four owner policies.

## Why

Signed-in visitors can resume library chats; anonymous chats stay in memory.

## Risk

None.
