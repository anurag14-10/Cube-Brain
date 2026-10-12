---
name: pathway-draft mode
type: chat_mode
schema_version: 1
aliases:
- pathway document generation
summary: Generates or revises the contributor's pathway document (frontmatter + Sections 0–6 + Source
  Trace appendix) from the conversation, merging into the pathway's existing published document when there
  is one; stored as design_documents doc_type 'draft'.
tags:
- contributor
- document
prompt: pathway-draft-system-prompt
max_tokens: 9000
access: role-gated
roles:
- adopter
- pathway-contributor
- admin
- general-user
contract: pathway-frontmatter
produces_doc_type: draft
triggered_by: contributor companion grid_update pathwayAction 'generate' or 'revise' → handlePathwayAction
  → generatePathwayDraft in lib/adoption-conversation.ts
status: live
mode_key: pathway-draft
endpoint: chat
model: claude-sonnet-4-6
streaming: true
code_refs:
- app/api/chat/route.ts#L172-L181
- app/api/chat/route.ts#L216
- lib/system-prompts.ts#L560-L622
- content/pathway-generation-prompt.md
- lib/adoption-conversation.ts#L465-L548
- lib/design-documents.ts
doc_refs:
- docs/wiki/diffusion-cube/integrations/ai-llm.md
- CLAUDE.md
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
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/ai-llm.md
contested:
- field: max_tokens
  readings:
  - 'CLAUDE.md (older revision, as quoted by ai-llm.md): 6144'
  - 'code: 9000'
  note: Code at L216 sets 9000.
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Purpose

Turns the contributor's conversation and uploaded material into the corpus-format pathway document they review, revise and eventually send for review (assemble). Generating never publishes anything.

## Grounding

`content/framework.md` (raw, not `frameworkBlock`) + `content/pathway-generation-prompt.md` (the exact output-structure rules, injected at runtime despite that file's header claiming otherwise) + `standingContext(grid, meta)` + the pathway's current `pathways.content_cache` as `existingPublishedDoc` (fetched fresh before every generate/revise). **Not** grounded in the corpus. Messages = conversation + prior draft as an assistant turn (when one exists) + "Draft my adoption as a pathway page now." or "Please revise the pathway draft as follows: <instruction>…".

## Output

The full document only: YAML [frontmatter](../contracts/pathway-frontmatter.md), Sections 0–6, Source Trace appendix keyed to "Adoption Companion conversation" as of the generation time. Must omit the `<!-- toolkit-assets:start/end -->` block (the app regenerates it at assemble). With an existing published doc it must return an updated version of that document (continue unit numbering, update superseded facts in place, never revert filled fields). Fallback line when too little is established. The client stores each run with `insertDraftVersion` (a new `version_number` every time — backs the version picker), extracts Section 2 gaps for the first-draft card (`lib/pathway-gaps.ts`) and appends a `<pathway_doc/>` card message.

## Triggered when

The contributor companion emits `pathwayAction` 'generate' (the turn the stage is confirmed) or 'revise' (a change request, or a new document after a draft exists). The route only checks `hasAnyRole` — not `pathway_contributor` — so any approved user could call it directly; the role gate exists only on the companion turn and on assemble.
