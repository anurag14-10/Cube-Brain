---
name: POST /api/chat
type: endpoint
schema_version: 1
aliases:
- chat route
- app/api/chat/route.ts
summary: 'The single LLM surface of the app: one POST handler that accepts eight `mode` values, builds
  the matching system prompt from lib/system-prompts.ts and streams claude-sonnet-4-6 output back as text/plain.'
tags:
- llm
- streaming
- core
path: /api/chat
methods:
- POST
file: app/api/chat/route.ts
access: role-gated
roles:
- adopter
- pathway-contributor
- admin
- general-user
- anonymous-visitor
tables_read:
- user-roles
- published-pathways
- contribution-units
- pathways-table
tables_written:
- adoption-queries
integrations:
- anthropic-claude
- supabase-postgres
- supabase-auth
- google-sheets
request_shape: 'JSON {messages: [{role, content: string | content-block[]}], mode: one of 8 MODES, grid?:
  GridState, meta?: CompanionMeta, versionNumber?: number, designId?: uuid, flow?: ''explorer''|''contributor'',
  existingPublishedDoc?: string, pathwayId?: slug (library only)}'
response_shape: 200 text/plain; charset=utf-8 stream of the model's text deltas (the trailing <grid_update>
  block is NOT stripped server-side). Errors are JSON {error}.
status: live
code_refs:
- app/api/chat/route.ts
- app/api/chat/route.ts#L27-L36
- app/api/chat/route.ts#L56-L80
- app/api/chat/route.ts#L90-L143
- app/api/chat/route.ts#L145-L219
- app/api/chat/route.ts#L233-L260
- proxy.ts#L19-L42
- lib/roles.ts
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
- docs/wiki/diffusion-cube/integrations/ai-llm.md
- ARCHITECTURE.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/chat/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: proxy.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: ARCHITECTURE.md
contested:
- field: access
  readings:
  - 'role-gated: every mode except library requires hasAnyRole (403 ''Your account is awaiting approval.'')'
  - 'public: /api/chat is in proxy.ts PUBLIC_PATHS and mode=library needs no session at all'
  note: Both are true per mode; `access` records the gate for 7 of 8 modes. The per-mode gate is recorded
    on each chat-modes/ entry.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

**Request** — `POST` JSON body, destructured at L50:
`{ messages, mode, grid, meta, versionNumber, designId, flow, existingPublishedDoc, pathwayId }`.

- `mode` must be one of `MODES` (L27-L36): `companion`, `analysis-doc`, `executive-summary`, `plan-document`, `extract-insights`, `pathway-draft`, `pathway-exec-summary`, `library`. Anything else → `400 {error:'Unknown mode.'}`.
- `grid` defaults to `EMPTY_GRID`, `meta` to `{}`, `versionNumber` to `1` (only read by `plan-document`).
- `existingPublishedDoc` (string) is read by `pathway-draft` and by `companion` when `flow==='contributor'`.
- `pathwayId` is read only by `library`; must pass `isValidSlug` (lib/slug.ts) because it becomes a file path in `readLibraryPathwayDocument`.

**Response** — always a streamed `text/plain; charset=utf-8` body built from `content_block_delta`/`text_delta` chunks of `anthropic.messages.stream`. No JSON envelope. The `<grid_update>` block (see [grid-update](../contracts/grid-update.md)) travels to the client inside the stream and is parsed/stripped client-side by lib/adoption-conversation.ts.

**Per-mode dispatch** (L145-L202): `analysis-doc` → `analysisDocSystemPrompt`, `executive-summary` → `executiveSummarySystemPrompt`, `plan-document` → `planDocumentSystemPrompt`, `extract-insights` → `documentInsightSystemPrompt`, `pathway-draft` → `pathwayDraftSystemPrompt` (+ `loadPathwayGenerationPrompt()`), `pathway-exec-summary` → `pathwaySubmissionExecutiveSummarySystemPrompt`, `companion`+`flow==='contributor'` → `contributorSystemPrompt`, everything else (companion with flow explorer/blank) → `explorerSystemPrompt` (+ `loadPublishedToolkitAssets()`). `library` is handled earlier (L90-L143) with `libraryPathwaySystemPrompt` / `libraryOverviewSystemPrompt` and `LIBRARY_KICKOFF_PROMPT`.

**max_tokens** (L216): companion 8192, extract-insights 1024, pathway-draft 9000, every other non-library mode 4096; library 1024 (L125). Model is hard-coded `claude-sonnet-4-6` at both call sites (L124, L205). No temperature override.

## Enforcement

1. `proxy.ts` lists `/api/chat` in `PUBLIC_PATHS`, so the middleware never 401s it — the route is the real gate.
2. `mode !== 'library'` → `hasAnyRole(supabase)` (lib/roles.ts; a `user_roles` read under the caller's own RLS). No role → `403 'Your account is awaiting approval.'` An anonymous caller has no rows, so also gets 403.
3. `mode === 'companion'`: `flow==='contributor'` requires `hasRole('pathway_contributor')`, `flow==='explorer'` requires `hasRole('adopter')` → 403 otherwise.
4. `mode === 'library'`: no auth at all; `pathwayId` slug-validated (404 'Unknown pathway.' on bad shape or no document).

**Gap:** a companion call with `flow` omitted or `''` skips the per-flow role check and falls through to `explorerSystemPrompt`, so any approved role (e.g. only `general_user` or `admin`) can run the Explorer companion. The other six modes check only `hasAnyRole` — e.g. any approved user can call `pathway-draft` directly.

## Side effects

- **Reads** (via loaders): the grounding corpus (`loadWikiContext` → `content/wiki/pathways/index.md` + linked files + every `published_pathways` row), `content/framework.md`, `content/resources.md`, `content/pathway-generation-prompt.md` (pathway-draft only); library mode reads `content/library-wiki/pathways/<id>.md`, falling back to `published_pathways` by slug; published toolkit assets from `contribution_units` joined to `pathways` (companion explorer branch and library-with-pathway only).
- **Google Sheets**: after every non-library stream completes, fire-and-forget `logConversation({mode, messages, response})` (lib/logger.ts) appends timestamp, mode, last user message, full response and full JSON history to the `logs!A:F` range. This includes uploaded document text. Library turns are not logged.
- **adoption_queries**: companion mode only, after the stream closes — inserts `{design_id: designId ?? null, content: <last user text>, pathway_slugs: parseGridUpdate(full).pathwaysReferenced ?? []}` via the caller's session client; failures only `console.error`.
- Dev-only (`NODE_ENV !== 'production'`): logs the contributor companion's raw `<grid_update>` to the server console (marked TEMPORARY, L236-L242).

## Errors

- `400 {error:'Unknown mode.'}` — bad mode.
- `403` — awaiting approval / wrong flow role.
- `404 {error:'Unknown pathway.'}` — library pathwayId invalid or not found in either source.
- No try/catch around `anthropic.messages.stream`: an Anthropic failure (missing `ANTHROPIC_API_KEY`, rate limit, account expiry) surfaces as an unhandled 500, or as a stream that errors mid-way. No retry anywhere.
