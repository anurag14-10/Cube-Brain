---
name: published_pathways
type: table
schema_version: 1
aliases:
- published_pathways
summary: 'The live community corpus: admin-published pathway documents, public-read, merged with the in-repo
  corpora at read time (DB wins by slug).'
table_name: published_pathways
store_kind: table
status: live
key_columns:
- id uuid PK
- slug text unique
- title
- description
- category
- content text
- sector (0014)
- contributor_org (0017)
- location, tags text[], stage (0030)
- published_by uuid → auth.users (set null since 0033)
- source_submission_id (inert)
- commit_message (inert)
- created_at
rls: Public select (using (true)); no insert/update/delete policy — writes via service-role client
references_tables:
- auth-users
created_in: m0012-published-pathways
code_refs:
- supabase/migrations/0012_published_pathways.sql
- supabase/migrations/0013_pathway_submission_versions.sql
- supabase/migrations/0014_published_pathways_sector.sql
- supabase/migrations/0017_published_pathways_contributor.sql
- supabase/migrations/0018_drop_retired_tables.sql
- supabase/migrations/0030_published_pathways_explore_fields.sql
- supabase/migrations/0033_account_deletion.sql
- app/api/admin/pathways/publish/route.ts
- lib/wiki-loader.ts
- lib/library-wiki-loader.ts
- lib/wiki-content.ts
- app/explore/page.tsx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0012_published_pathways.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0013_pathway_submission_versions.sql
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: supabase/migrations/0014_published_pathways_sector.sql
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Columns

| Column | Notes |
|---|---|
| `slug` | unique; the upsert key on publish |
| `title`, `description`, `category`, `content` | `category` defaults `From Adopters`; live publish sets it from the first two tags or `Community` |
| `sector` | 0014, nullable |
| `contributor_org` | 0017 — read by `lib/wiki-loader.ts` for a "Contributed by" line |
| `location`, `tags`, `stage` | 0030 — Explore card fields parsed from the document frontmatter at publish |
| `published_by` | FK auth.users; no ON DELETE action until 0033 made it `set null` |
| `source_submission_id` | FK to `pathway_submissions` dropped in 0018; column kept as an inert audit field |
| `commit_message` | 0013; written only by dead routes |

## RLS

`Anyone can view published pathways` (`using (true)`). No write policy. The single live writer is
`POST /api/admin/pathways/publish` (admin-only, service-role upsert on `slug`). Readers: `app/explore/page.tsx` and
`lib/library-wiki-loader.ts` (service-role, so anonymous visitors work), `lib/wiki-loader.ts` and `lib/wiki-content.ts`
(session client), `app/api/chat/route.ts`, `app/admin/page.tsx`.

## Lifecycle

Upserted on each admin publish (re-publish keeps the slug, so `created_at` keeps the first publish date). Nothing in the
app deletes a row: `POST /api/admin/pathways/delete` removes the `pathways` workspace but leaves the published copy live.
Survives account deletion of the publisher (`published_by` → null).

## Gotchas

- The live publish route never sets `contributor_org`, so the "Contributed by" attribution only appears for rows written
  by the retired `pathway_submissions` routes.
- Dead routes (`app/api/pathway-submissions/push`, `app/api/admin/pathway-submissions/publish`) still insert here, but
  they fail first on the dropped `pathway_submissions` table.
- Before 0033, deleting any user who had ever published was blocked by the `published_by` FK.
