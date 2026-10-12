---
name: TD-15 No rate limiting, PII screening or security hardening
type: tech_debt
schema_version: 1
aliases:
- TD-15
summary: No rate limiting on /api/chat (including the anonymous library mode) or on uploads and public
  toolkit-asset downloads, and no PII or malware screening of uploaded documents or shared asset files.
tags:
- security
- privacy
- cost
td_id: TD-15
severity: P3
status: open
affected_endpoints:
- chat
- toolkit-assets-download
- toolkit-assets-upload-url
requirement: security-and-privacy-hardening
remediation: Add per-user/IP rate limits and concurrency caps on /api/chat and the public toolkit-asset
  routes; add a PII screening step before uploaded text is folded into prompts or drafts; scan shared
  files before publish.
code_refs:
- proxy.ts#L19-L42
- app/api/chat/route.ts
- app/api/toolkit-assets/[id]/download/route.ts
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
- specs/TOOLKIT_ASSETS_SPEC.md
- docs/tasks/toolkit-asset-files/requirement.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: proxy.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: specs/TOOLKIT_ASSETS_SPEC.md
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: docs/raw_documents/AI DIffusion Cube - Product Charter.docx
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

Verified at `28068b6`:
- `/api/chat` is in `PUBLIC_PATHS`. Its `library` mode needs no session, so anonymous visitors can drive Anthropic calls without limit.
- Grepping app/lib/proxy finds no app-level rate limiting at all. The only "rate limit" handling is the Supabase Auth limits surfaced on `/login` and on account deletion.
- Uploaded documents are text-extracted in the browser and sent to the model with no PII check.

The toolkit-assets release widened the surface. Published asset files are publicly downloadable with no rate limit (an egress-cost risk), and the files are "not scanned for malware or PII". `TOOLKIT_ASSETS_SPEC.md` §8 accepts both points for that release. The spec cites security findings #2, #4 and #6 as fixed, from `docs/security/security-review-2026-09-30.md`, a file that is not in the repository at `28068b6`.

## Impact

See [unbounded-llm-spend](../risks/unbounded-llm-spend.md) and [pii-in-uploaded-documents](../risks/pii-in-uploaded-documents.md).

## Remediation

This is the charter's [security-and-privacy-hardening](../requirements/security-and-privacy-hardening.md) requirement (Not started).
