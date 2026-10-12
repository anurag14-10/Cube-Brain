---
name: Google Sheets logging
type: integration
schema_version: 1
summary: After each `/api/chat` stream it appends one row (timestamp, mode, pathway slug, last user message,
  response, full history JSON) to the `logs` tab.
integration_kind: spreadsheet-logging
provider: Google
sdk: googleapis@^173.0.0
account_notes: A service account owns access; the target sheet and account are not recorded in the repo.
config_vars:
- google-service-account-json
- google-sheet-id
code_refs:
- lib/logger.ts
- app/api/chat/route.ts
- package.json
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/logger.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/chat/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

After each `/api/chat` stream it appends one row (timestamp, mode, pathway slug, last user message, response, full history JSON) to the `logs` tab. This sends full conversation content to a spreadsheet.

## Configuration

`GOOGLE_SERVICE_ACCOUNT_JSON`, `GOOGLE_SHEET_ID`.

## Failure behaviour

Silent soft-fail: errors are caught and `console.error`'d, never retried, and never affect the response.

## Account

A service account owns access; the target sheet and account are not recorded in the repo.
