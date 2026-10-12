---
name: TD-08 Stale root documentation
type: tech_debt
schema_version: 1
aliases:
- TD-08
summary: Root docs (conversation_design.md, specs/SIGNUP_APPROVAL_OPTIONS.md, README.md, AGENTS.md) describe
  superseded states; CLAUDE.md has since been rewritten as a short pointer to the generated wiki.
tags:
- docs
- partially-resolved
td_id: TD-08
severity: P2
status: in-progress
remediation: Replace README.md and AGENTS.md boilerplate with project onboarding; mark conversation_design.md
  and SIGNUP_APPROVAL_OPTIONS.md as historical (dated, with what superseded them).
code_refs:
- CLAUDE.md
- README.md
- AGENTS.md
- conversation_design.md
- specs/SIGNUP_APPROVAL_OPTIONS.md
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
- docs/wiki/diffusion-cube/architecture/architecture-overview.md
- docs/wiki/diffusion-cube/business/business-overview.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: CLAUDE.md
- system: github_repo
  method: queried
  date: '2026-10-12'
  ref: d37f3bc
contested:
- field: status
  readings:
  - open — wiki register lists CLAUDE.md as substantially stale
  - in-progress — at 28068b6 CLAUDE.md is a 54-line file deferring to the generated wiki (rewritten in
    d37f3bc, 2026-09-28)
  note: CLAUDE.md is no longer stale. README.md and AGENTS.md are still create-next-app boilerplate. conversation_design.md
    (1,797 lines) and SIGNUP_APPROVAL_OPTIONS.md, moved to specs/ on 2026-09-28, still describe superseded
    designs.
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

At `28068b6`:
- `README.md` is unmodified create-next-app boilerplate.
- `AGENTS.md` holds only the Next.js agent-rules block.
- `conversation_design.md` predates the removal of the intent menu and the whole pathways/organisations/registration schema.
- `specs/SIGNUP_APPROVAL_OPTIONS.md` still presents email-based admin approval as "current, already built". Signup became self-serve instead; see [otp-self-serve-signup-over-admin-approval](../decisions/otp-self-serve-signup-over-admin-approval.md).

`CLAUDE.md`, the worst offender in the original register, was rewritten on 2026-09-28 (`d37f3bc`) into a short index into the generated wiki.

## Impact

Anyone, human or agent, who reads these files first forms a wrong mental model. The trust order is code > migrations > ARCHITECTURE.md > generated wiki > older root docs.

## Remediation

Retire or clearly date the stale files. The generated wiki has drifted as well; see [TD-17](td-17-generated-wiki-stale.md).
