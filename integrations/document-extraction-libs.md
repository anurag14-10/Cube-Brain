---
name: Client-side document extraction libraries
type: integration
schema_version: 1
summary: Turns uploaded PDF, DOCX, XLSX/CSV and PPTX files into text in the browser before they go into
  a chat turn (`extractTextFromFile` in `lib/extract-text.ts`, used by `lib/adoption-conversation.ts`).
integration_kind: document-parsing
provider: Open-source libraries (in-browser)
sdk: pdfjs-dist@^4.10.38, mammoth@^1.12.0, xlsx@0.20.3 (SheetJS CDN tarball), jszip@^3.10.1
account_notes: No account; bundled npm packages. `xlsx` is installed from the SheetJS CDN URL, not the
  npm registry.
code_refs:
- lib/extract-text.ts
- lib/adoption-conversation.ts
- package.json
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/extract-text.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/adoption-conversation.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

Turns uploaded PDF, DOCX, XLSX/CSV and PPTX files into text in the browser before they go into a chat turn (`extractTextFromFile` in `lib/extract-text.ts`, used by `lib/adoption-conversation.ts`). pdf.js runs with a bundled worker. Images go to the model as image blocks instead.

## Configuration

None.

## Failure behaviour

An extraction failure is handled per file in the client. Nothing reaches the server for a file that fails to parse.

## Account

No account; bundled npm packages. `xlsx` is installed from the SheetJS CDN URL, not the npm registry.
