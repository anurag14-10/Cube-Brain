---
name: Pathway lifecycle (workspace → assembled → published)
type: concept
schema_version: 2
aliases:
- pathway workspace
- two-step publish
- assemble vs publish
- published_pathways
summary: A contributed pathway moves from a `pathways` workspace row, through an assembled document committed to GitHub and awaiting review, to live only when an admin publishes it into `published_pathways`.
concept_kind: method
definition: The path a contributed pathway takes from draft to live. The `pathways` table is the contributor's workspace (drafting, then an assembled document cached on the row and committed to GitHub, with review requested); `published_pathways` is the live community corpus. Assembling never makes a pathway live — only an admin publish copies the assembled document into `published_pathways`.
audience: internal-only
broader: pathway-document
see_also:
- pathway-document
doc_refs:
- app/api/pathways/assemble/route.ts
- app/api/admin/pathways/publish/route.ts
- lib/wiki-loader.ts
- lib/wiki-content.ts
- lib/library-wiki-loader.ts
- supabase/migrations/0012_published_pathways.sql
- supabase/migrations/0020_pathways.sql
- supabase/migrations/0031_pathways_review_requested.sql
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: app/api/pathways/assemble/route.ts, app/api/admin/pathways/publish/route.ts at 28068b6
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: lib/wiki-loader.ts, lib/wiki-content.ts, lib/library-wiki-loader.ts at 28068b6 (how published rows merge with in-repo files)
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: supabase/migrations/0012_published_pathways.sql, 0020_pathways.sql (read policies)
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Definition

Two different tables hold two different things:

| | `pathways` | `published_pathways` |
|---|---|---|
| What it is | The contributor's **workspace** for one pathway | The **live** community corpus |
| Written by | The contributor (create), then assemble | Admin publish only (service role) |
| Who can read it | Signed-in users | Anyone (public read policy) |
| Holds | slug, title, sector, description, `content_cache` (the assembled document), `review_requested`, design-doc pointers | slug, title, description, category, content, sector, location, tags, stage, `contributor_org` |

The steps, and the brain's `lifecycle` value (MASTERS 11) at each:

1. **Create** — a contributor starts a workspace row in `pathways`. → `drafting`
2. **Assemble** — `POST /api/pathways/assemble` commits the drafted document to GitHub, then (best-effort) caches it in `pathways.content_cache` and sets `review_requested: true`. **Nothing is live yet.** → `assembled`
3. **Publish** — an admin calls `POST /api/admin/pathways/publish`, which upserts `content_cache` into `published_pathways` (on conflict by slug, so re-publishing replaces the live copy), clears `review_requested`, and publishes the toolkit assets named in that document. → `published`

The rule this enforces: **assembling is never publishing.** A pathway goes live only after a person reviews it.

## How it is used

Where a live community pathway is read, at commit `28068b6`:

| Reader | How `published_pathways` combines with the in-repo files |
|---|---|
| Grounding corpus (`lib/wiki-loader.ts`, Explorer + Contributor flows) | **Appended** after the indexed in-repo pathways. No de-duplication: a slug in both appears twice. |
| `/wiki` listing (`lib/wiki-content.ts`) | **Appended** after the static list. A shared slug is listed twice. |
| Library (`lib/library-wiki-loader.ts`, public `/explore`) | **The database copy wins by slug.** The static file of the same slug is dropped. |

In the brain, a pathway whose live copy is a `published_pathways` row carries `published-pathways-corpus` in `corpora` (MASTERS 13). `lifecycle: published` alone does not say which: it also covers in-repo documents linked from the grounding index. Read `corpora` to tell the two apart.

## What the brain does not hold yet

Every pathway in `pathways/` so far was seeded from the in-repo corpora. Community pathways that exist only as `published_pathways` rows, and drafts that exist only as `pathways` rows, are not in the brain. The seeder reads repo files only. Bringing them in needs a read of `published_pathways` (public data) or an export of it. Workspace drafts are not public, and they stay out unless their contributor's document is supplied.

## Not to be confused with

- The brain's `pathways/` folder. That folder holds entries describing pathways, whatever corpus their copy lives in. It is not the `pathways` table.
- `pathway_submissions`, the older submission table. Migration 0018 dropped it, and the `pathways` workspace replaces it.
