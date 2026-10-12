---
name: TD-16 Free-trial Anthropic and AWS accounts with fixed expiry
type: tech_debt
schema_version: 1
aliases:
- TD-16
summary: The Anthropic API account behind every AI feature is a free grant expiring 2026-10-28, and the
  AWS account a free grant expiring December 2026; nothing in code or CI tracks either.
tags:
- operational
- time-sensitive
td_id: TD-16
severity: P1
status: open
remediation: Arrange a paid Anthropic account/key before 2026-10-28 and rotate ANTHROPIC_API_KEY in every
  environment; plan the AWS replacement by November 2026. Tracked as risks anthropic-account-expiry and
  aws-account-expiry.
code_refs:
- app/api/chat/route.ts#L25
- app/api/pathways/check-similar/route.ts#L6
- Dockerfile
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
- docs/wiki/diffusion-cube/operations/deployment.md
- docs/wiki/diffusion-cube/ai-context.md
- docs/raw_documents/AI DIffusion Cube - Product Charter.docx
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: docs/raw_documents/AI DIffusion Cube - Product Charter.docx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: app/api/chat/route.ts
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

The Product Charter's Dependencies section says the Claude API licence/access is a free account that "will expire by 28th of October", with a new account to be planned before then. It says the AWS server account is a free account expiring "this December", with a new one to be planned by November. As of 2026-10-12 the Anthropic deadline is 16 days away. No fallback model or provider is configured anywhere in code; all three call sites use `claude-sonnet-4-6` with `ANTHROPIC_API_KEY`.

## Impact

If the Anthropic account lapses, every AI-backed feature stops: the companion, the library chat, document generation, pathway drafts, the duplicate check and toolkit-asset identification. Uploading, publishing and downloading keep working, because they do not call the model.

## Remediation

This is an account and procurement action with a hard date, not a code task. The live dates and ownership are tracked on the risks [anthropic-account-expiry](../risks/anthropic-account-expiry.md) and [aws-account-expiry](../risks/aws-account-expiry.md).
