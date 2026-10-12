---
name: TD-05 No app-level retry or graceful degradation on Anthropic calls
type: tech_debt
schema_version: 1
aliases:
- TD-05
summary: /api/chat streams with no surrounding try/catch and check-similar swallows failures; no app-level
  retry, backoff, timeout or fallback exists for any Anthropic call.
tags:
- reliability
- llm
td_id: TD-05
severity: P2
status: open
affected_endpoints:
- chat
- pathways-check-similar
requirement: error-handling-graceful-degradation
remediation: Wrap anthropic.messages.stream / .create in explicit error handling with a user-facing failure
  message, set an explicit timeout and maxRetries policy, and add concurrency limits per the charter's
  reliability requirement.
code_refs:
- app/api/chat/route.ts#L25
- app/api/chat/route.ts#L123
- app/api/chat/route.ts#L204
- app/api/pathways/check-similar/route.ts#L76-L90
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: app/api/chat/route.ts
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: docs/raw_documents/AI DIffusion Cube - Product Charter.docx
contested:
- field: summary
  readings:
  - 'wiki: ''No retry logic on any Anthropic API call anywhere in the app'''
  - 'derived from code: the clients are built as `new Anthropic({ apiKey })` with no maxRetries override,
    so the SDK''s own default retry behaviour still applies; what is missing is app-level handling'
  note: 'Derived from SDK defaults, not tested here. The debt stands either way: there is no graceful
    degradation, no timeout policy and no user-facing error.'
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

Verified at `28068b6`: `app/api/chat/route.ts` creates one module-level client (`new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY })`) and calls `anthropic.messages.stream(...)` at two sites with no try/catch around them. `app/api/pathways/check-similar/route.ts` wraps its single `messages.create` call in try/catch, returns a default value on failure, and does not retry.

## Impact

An intermittent API error, or the [account expiring](../risks/anthropic-account-expiry.md), reaches users as a raw failure in every chat mode: the companion, the library, document generation and pathway drafts. Nothing tells the user the AI is unavailable.

## Remediation

This is the charter's [error-handling-graceful-degradation](../requirements/error-handling-graceful-degradation.md) requirement, together with [reliability-serving-architecture](../requirements/reliability-serving-architecture.md) for the defined timeout/retry policy. Both are recorded as Not started.
