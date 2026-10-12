---
name: POST /api/pathways/check-similar
type: endpoint
schema_version: 1
summary: 'Contributor-only duplicate check: sends the candidate pathway plus every existing `pathways`
  row to claude-sonnet-4-6 with a forced `report_match` tool call and returns {matchId}.'
tags:
- llm
- contributor
- dedupe
path: /api/pathways/check-similar
methods:
- POST
file: app/api/pathways/check-similar/route.ts
access: role-gated
roles:
- pathway-contributor
tables_read:
- user-roles
- pathways-table
integrations:
- anthropic-claude
- supabase-postgres
- supabase-auth
request_shape: 'JSON {title: string (required), sector?: string, description: string (required)}'
response_shape: 'JSON {matchId: string | null}'
status: live
code_refs:
- app/api/pathways/check-similar/route.ts
- app/api/pathways/check-similar/route.ts#L11-L25
- app/api/pathways/check-similar/route.ts#L66-L91
- components/PathwaySelector.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/api-specification.md
- docs/wiki/diffusion-cube/integrations/ai-llm.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/pathways/check-similar/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/api-specification.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Contract

Request `{title, sector?, description}`; `title` and `description` must be non-blank (400 `title and description required`). Response is always `200 {matchId: string|null}` once auth passes — the id of an existing `pathways` row the model judged to be the same underlying deployment, else `null`. Called from `components/PathwaySelector.tsx` before a contributor creates a new pathway.

Prompt and tool: see [check-similar-tool-prompt](../prompts/check-similar-tool-prompt.md) and [check-similar-report-match](../contracts/check-similar-report-match.md). `anthropic.messages.create` (the app's only non-streaming Anthropic call), `max_tokens: 512`, `tools: [MATCH_TOOL]`, `tool_choice: {type:'tool', name:'report_match'}`.

## Enforcement

Session required (401) and `hasRole('pathway_contributor')` (403 `Contributor role required`). Not in proxy PUBLIC_PATHS, so anonymous calls are 401'd by the middleware first.

## Side effects

Reads `pathways (id, title, sector, description)` ordered by `created_at desc` via the session client — the whole table goes into one prompt (unbounded as pathways grow). No writes. Empty table → `{matchId:null}` without calling the model.

## Errors

- Any Anthropic failure is caught and swallowed to `{matchId: null}` (console.error only) — a failed check reads as "no duplicate".
- A `tool_use` block missing from the response also yields `null`.
- 500 only if the `pathways` select fails.
- The file comment says this mirrors "EXTRACT_TOOL in app/api/pathways/assemble/route.ts"; assemble no longer calls the model at all, so that reference is stale.
