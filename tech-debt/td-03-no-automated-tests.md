---
name: TD-03 No automated tests
type: tech_debt
schema_version: 1
aliases:
- TD-03
summary: The repository has no test files, no test runner config, no `test` script and no CI test job;
  regressions such as the 0027 draft-insert failure ship silently.
tags:
- testing
- quality
td_id: TD-03
severity: P1
status: open
requirement: test-cases-all-flows
remediation: Start with unit tests for pure lib/ modules (grid-update, toolkit-assets, slug, strip-frontmatter),
  then integration tests for app/api routes, and add a test job to .github/workflows/deploy.yml.
code_refs:
- package.json
- .github/workflows/deploy.yml
doc_refs:
- docs/wiki/diffusion-cube/knowledge/technical-debt.md
- docs/wiki/diffusion-cube/architecture/testing.md
- specs/TOOLKIT_ASSETS_SPEC.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/knowledge/technical-debt.md
- system: diffusion_cube_code
  method: queried
  date: '2026-10-12'
  ref: package.json
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: docs/raw_documents/AI DIffusion Cube - Product Charter.docx
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Problem

Verified at `28068b6`: `package.json` scripts are only `dev`, `build`, `start` and `lint`. No `*.test.*` / `*.spec.*` files and no jest/vitest/playwright config exist, and the only workflow is the Vercel `deploy.yml`. The toolkit-assets work (2026-09-30 to 2026-10-05) was checked only by `tsc`, `eslint`, `npm run build`, scratch scripts kept outside the repo, and manual live tests by the owner.

## Impact

Silent regressions are the expected failure mode. The [doc_type constraint incident](../incidents/contributor-draft-inserts-failing-doc-type.md) went unnoticed for the whole multi-contributor rework window. The behaviour rules for toolkit assets are prompt instructions, so they can only be checked with live model calls.

## Remediation

This matches the charter's non-functional requirement [test-cases-all-flows](../requirements/test-cases-all-flows.md), which is recorded as Not started.
