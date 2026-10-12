---
name: Anthropic Claude API
type: integration
schema_version: 1
summary: Every model call in the app, all to `claude-sonnet-4-6`.
integration_kind: llm
provider: Anthropic
sdk: '@anthropic-ai/sdk@^0.106.0'
account_notes: Free account per the Product Charter (summarised in docs/wiki ai-context.md), expiring
  2026-10-28; the charter says a new account/licence must be planned before then. Expiry is not tracked
  anywhere in code or CI.
config_vars:
- anthropic-api-key
code_refs:
- app/api/chat/route.ts
- app/api/pathways/check-similar/route.ts
- package.json
doc_refs:
- docs/raw_documents/AI DIffusion Cube - Product Charter.docx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/chat/route.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/pathways/check-similar/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
- system: raw_documents
  method: document
  date: '2026-10-08'
  ref: docs/raw_documents/AI DIffusion Cube - Product Charter.docx
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/ai-context.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

Every model call in the app, all to `claude-sonnet-4-6`:

- `POST /api/chat` — eight modes, all streamed with `messages.stream`; `max_tokens` is set per mode (companion 8192, pathway-draft 9000, extract-insights 1024, library 1024, others 4096).
- `POST /api/pathways/check-similar` — one non-streaming forced tool-use call (`report_match`, `max_tokens` 512) for duplicate-pathway detection.

## Configuration

`ANTHROPIC_API_KEY` only.

## Failure behaviour

There are no retries, no fallback model and no cached response. Chat modes hard-fail (no try/catch around the stream). `check-similar` catches the error and returns `{matchId: null}`, so pathway creation goes ahead unchecked.

## Account

Free account per the Product Charter (summarised in docs/wiki ai-context.md), expiring 2026-10-28; the charter says a new account/licence must be planned before then. Expiry is not tracked anywhere in code or CI.
