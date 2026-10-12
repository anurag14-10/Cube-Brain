---
name: pathway-exec-summary mode
type: chat_mode
schema_version: 1
summary: 'Dead mode: still dispatched by /api/chat to an internal reviewer summary prompt, but its only
  caller (generateSubmissionExecutiveSummary) and its storage (pathway_submission_exec_summaries) are
  gone.'
tags:
- dead-code
- admin
- document
prompt: pathway-submission-executive-summary-system-prompt
max_tokens: 4096
access: role-gated
roles:
- adopter
- pathway-contributor
- admin
- general-user
produces_doc_type: none
triggered_by: Formerly generateSubmissionExecutiveSummary in lib/adoption-conversation.ts alongside every
  draft; that function no longer exists and nothing sends this mode
status: dead-code
mode_key: pathway-exec-summary
endpoint: chat
model: claude-sonnet-4-6
streaming: true
code_refs:
- app/api/chat/route.ts#L182-L183
- lib/system-prompts.ts#L833-L883
- supabase/migrations/0018_drop_retired_tables.sql
- lib/pathway-submission-versions.ts
doc_refs:
- docs/wiki/diffusion-cube/integrations/ai-llm.md
- ARCHITECTURE.md
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
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
  method: derived
  date: '2026-10-08'
  ref: grep for generateSubmissionExecutiveSummary and 'pathway-exec-summary'
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/ai-llm.md
contested:
- field: status
  readings:
  - 'ARCHITECTURE.md: live mode, ''exec summary of a pathway submission'''
  - 'ai-llm.md: the prompt is dead code with no caller'
  - 'code: the route still dispatches the mode; no client sends it and its stored destination was dropped
    in 0018'
  note: Code supports dead-code (reachable only by a direct API call, output has nowhere to go).
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Purpose

Was an internal-only executive summary of a contributor's pathway submission, generated automatically with every draft and shown only to admins in PathwaySubmissionsPanel to help decide whether to publish.

## Grounding

No corpus and no framework — the single message was the drafted pathway document itself; prompt also gets `meta` (name/sector/geography) and the generation time.

## Output

`## <name> — Executive Summary (internal)` with `### The Deployment` and `### Coverage & Gaps`. Previously stored in `pathway_submission_exec_summaries`, which migration 0018 dropped together with `pathway_submissions`.

## Triggered when

Never. The documented trigger (`generateSubmissionExecutiveSummary`) is absent from lib/adoption-conversation.ts; the comments in lib/system-prompts.ts and lib/pathway-submission-versions.ts that name it are stale. Any approved user could still invoke it directly (hasAnyRole only).
