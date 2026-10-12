---
name: Wiki pathway page (/wiki/[slug])
type: page
schema_version: 1
aliases:
- wiki pathway page
summary: Renders one grounding-corpus pathway, or a published_pathways row as a fallback, with frontmatter and the
  contributor-only Source Trace / Provenance appendix stripped.
route: /wiki/[slug]
file: app/(app)/wiki/[slug]/page.tsx
access: role-gated
roles:
- general-user
- adopter
- pathway-contributor
- admin
components:
- app-app-group-layout
- components-wiki-markdown
status: live
code_refs:
- app/(app)/wiki/[slug]/page.tsx
- lib/wiki-content.ts
- components/WikiMarkdown.tsx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/(app)/wiki/[slug]/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/wiki-content.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: components/WikiMarkdown.tsx
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it renders

`getWikiPathway(slug)` reads `content/wiki/pathways/<slug>.md` first and falls back to `published_pathways`
when there is no static file. **Static wins** here, which is the opposite of /explore, where the DB row wins.
It strips the frontmatter and cuts everything from the first heading that mentions "Source Trace" or
"Provenance", then renders the rest with [WikiMarkdown](../modules/components-wiki-markdown.md) (tables
supported, links shown as plain text). A missing slug gives `notFound()`.

The back link depends on `?from=`. With `from=contribute` it returns to `/contribute` (or
`/contribute?open=<designId>`, labelled "Back to Contributions"); otherwise to `/wiki`.

## Access behaviour

Same as [/wiki](wiki.md): session required by proxy.ts, any role required by the `(app)` layout. Stripping the
Source Trace keeps the provenance-contributor-only rule on this browsing surface. It is enforced in code here,
unlike in prompts.
