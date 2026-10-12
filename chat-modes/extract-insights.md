---
name: extract-insights mode
type: chat_mode
schema_version: 1
aliases:
- silent document extraction
summary: Silent one-shot pass over one uploaded document that returns only a <grid_update> (cells + basic
  meta) to seed the workspace grid before the user's next message.
tags:
- upload
- grid
prompt: document-insight-system-prompt
max_tokens: 1024
access: role-gated
roles:
- adopter
- pathway-contributor
- admin
- general-user
contract: grid-update
produces_doc_type: none
triggered_by: extractInsightsForAttachment in lib/adoption-conversation.ts when a text-extractable attachment
  (or a contributor CSV) finishes reading into an already-open conversation
status: live
mode_key: extract-insights
endpoint: chat
model: claude-sonnet-4-6
streaming: true
code_refs:
- app/api/chat/route.ts#L170-L171
- app/api/chat/route.ts#L216
- lib/system-prompts.ts#L500-L537
- lib/adoption-conversation.ts#L1178-L1232
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
  ref: lib/adoption-conversation.ts
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Purpose

Seeds the 4×4 grid the moment a file lands, instead of waiting for the first chat turn. Best-effort: any failure is silently ignored, because the document text still reaches the companion in the user's next message.

## Grounding

Framework only (`frameworkBlock(content/framework.md)`) plus the current grid as the floor ("do not lower any density"). No corpus. The single user message is the document's extracted text.

## Output

Only a reduced [grid-update](../contracts/grid-update.md): `cells` (only cells the document evidences, density 1–3) and `meta` {name, sector, geography, stage (only if the document states it), summary}. No prose, no flowStep or actions. The client merges non-empty meta values and changed cells into the conversation and persists to `designs`. The route also writes the full document text to the Google Sheets log via `logConversation`.

## Triggered when

An attachment finishes text extraction and `conversationRef.current` exists (not on the welcome screen — the row is no longer created eagerly). Request carries only `{messages:[{role:'user', content: text}], mode, grid}` — no `flow`/`meta`, so only `hasAnyRole` gates it.
