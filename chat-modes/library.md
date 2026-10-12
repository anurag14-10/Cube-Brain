---
name: library mode
type: chat_mode
schema_version: 1
aliases:
- Diffusion Library chat
- /explore chat
summary: 'The public, no-login /explore chat: grounded in one library pathway document (or the library-wide
  overview when no pathway is chosen), conversational voice, no grid and no grid_update.'
tags:
- library
- public
- explore
prompt: library-pathway-system-prompt
max_tokens: 1024
access: public
roles:
- anonymous-visitor
- adopter
- pathway-contributor
- admin
- general-user
corpora:
- library-corpus
- published-pathways-corpus
produces_doc_type: none
triggered_by: app/explore/ExploreLibrary.tsx streams {messages, mode:'library', pathwayId} when a visitor
  opens a pathway tile (empty history → kickoff turn) or sends a message
status: live
mode_key: library
endpoint: chat
model: claude-sonnet-4-6
streaming: true
code_refs:
- app/api/chat/route.ts#L90-L143
- lib/system-prompts.ts#L897-L952
- lib/library-wiki-loader.ts
- lib/toolkit-assets.ts#L257-L280
- app/explore/ExploreLibrary.tsx
- proxy.ts#L19-L42
doc_refs:
- docs/wiki/diffusion-cube/integrations/ai-llm.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/chat/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/system-prompts.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/library-wiki-loader.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/ai-llm.md
contested:
- field: prompt
  readings:
  - library-pathway-system-prompt (pathwayId given)
  - library-overview-system-prompt (no pathwayId)
  note: Selected per request; library-kickoff-prompt replaces an empty message history in both cases.
- field: contract
  readings:
  - 'docs/wiki ai-llm.md: no <grid_update> at all, nothing structured in the output'
  - 'code: with published toolkit assets the reply may end with a <toolkit_assets>["asset-…"]</toolkit_assets>
    tag that ExploreLibrary strips and renders as download cards'
  note: The toolkit_assets tag arrived with migration 0034; not a registry contract, described here in
    prose.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Purpose

Lets anyone (no session, no registration) explore a single pathway conversationally on /explore, or ask about the library as a whole. Ported verbatim from the standalone Diffusion Library app's FastAPI backend (PATHWAY_SYSTEM_TEMPLATE / LIBRARY_SYSTEM_TEMPLATE) — its voice and rules deliberately do not share the companion's grounding/speaking rules.

## Grounding

- `pathwayId` given (must pass `isValidSlug`): `readLibraryPathwayDocument(id)` from `content/library-wiki/pathways/<id>.md`; if absent, `published_pathways.content` by slug (session client; RLS makes published rows public) prefixed with `datedLine(content, created_at)`. Plus that pathway's published toolkit assets (`loadPublishedToolkitAssets({pathwaySlug})`). → [library-pathway-system-prompt](../prompts/library-pathway-system-prompt.md).
- No `pathwayId`: `buildLibraryOverview()` — every library file's frontmatter plus every `published_pathways` row's title/description/sector/stage/location/tags (DB wins by slug). → [library-overview-system-prompt](../prompts/library-overview-system-prompt.md).

The grounding corpus (`content/wiki/pathways/`) is NOT used — the library corpus is a separate, independently maintained set of documents.

## Output

Short conversational prose (1–2 short paragraphs, contractions, sparing bold, no headers/lists), always ending with a question that invites going deeper. Optional trailing `<toolkit_assets>[ids]</toolkit_assets>` tag (only on a reply that offered assets). Nothing is persisted by the route; no Google Sheets log and no adoption_queries row for this mode. max_tokens 1024.

## Triggered when

ExploreLibrary opens a pathway (empty history → the route substitutes [library-kickoff-prompt](../prompts/library-kickoff-prompt.md) as the invisible first user turn) and on every visitor message. No auth check in the route; `/api/chat` is in proxy.ts PUBLIC_PATHS.
