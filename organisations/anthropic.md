---
name: Anthropic
type: organisation
schema_version: 2
summary: Vendor of the Claude API, the Cube's only LLM provider — every conversational and AI-assisted feature depends on one Anthropic account, which the charter records as a free account expiring 2026-10-28.
doc_refs:
- docs/raw_documents/AI DIffusion Cube - Product Charter.docx
- docs/tasks/toolkit-asset-files/requirement.md
org_kinds:
- vendor
website: https://www.anthropic.com
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: the app's chat and duplicate-check routes call a single Claude model; no second provider is configured
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: Product Charter, Dependencies (Claude API licence free, expiring 28 October)
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/tasks/toolkit-asset-files/requirement.md (AI account expires 28-Oct-2026)
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Relationship to the Cube

Anthropic is the Cube's only LLM vendor. The companion, the library chat, document generation, pathway drafting, the duplicate check and toolkit-asset identification all call the Claude API. The charter also names a Claude Chat channel (see [Web app and Claude Chat channels](../decisions/web-app-and-claude-chat-channels.md)).

## Notes

- The Product Charter and the toolkit-asset requirement record that the account is a free one expiring 28-Oct-2026. If it lapses, every conversational feature stops; uploading, approving and downloading keep working. Tracked as [Anthropic API account expiry](../risks/anthropic-account-expiry.md).
- No second provider is configured, so a lapse or an outage has no fallback.
