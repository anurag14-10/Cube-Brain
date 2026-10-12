---
name: Anthropic API account expiry
type: risk
schema_version: 2
aliases:
- TD-16
- Claude API licence expiry
summary: The Anthropic API account behind every AI feature of the Cube is a free grant expiring 2026-10-28; if it lapses, every conversational feature stops.
tags:
- time-sensitive
- vendor-account
doc_refs:
- docs/raw_documents/AI DIffusion Cube - Product Charter.docx
- docs/tasks/toolkit-asset-files/requirement.md
- docs/wiki/diffusion-cube/ai-context.md
status: open
likelihood: high
impact: critical
due_date: 2026-10-28
mitigation: Arrange a paid Anthropic account or key before 2026-10-28 and rotate the API key in every environment where the app runs.
organisation: anthropic
sources:
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: Product Charter, Dependencies section (Claude API licence free, expiring 28 October)
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/tasks/toolkit-asset-files/requirement.md (AI account expires 28-Oct-2026)
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Risk

The Product Charter's Dependencies section says the Claude API licence is a free account that "will expire by 28th of October", and that a new account must be planned before then. No fallback model or second provider is configured in the app, and nothing in code or CI tracks the expiry date.

## Impact if it happens

Every AI-backed feature stops: the companion, the library chat, document generation, pathway drafts, the duplicate check and toolkit-asset identification. Uploading, publishing and downloading keep working, because they do not call the model.

## Mitigation

This is an account and procurement action with a hard date, not a code task. The `likelihood` reads high because no replacement is recorded as of 2026-10-12, 16 days before the deadline.
