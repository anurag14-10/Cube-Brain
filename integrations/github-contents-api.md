---
name: GitHub Contents API
type: integration
schema_version: 1
summary: Contributor assemble (`POST /api/pathways/assemble`) commits the pathway document to `content/wiki/pathways/<slug>.md`
  on the configured branch.
integration_kind: version-control
provider: GitHub
account_notes: Repo, branch and token come from env; which account owns the token is not recorded in the
  repo.
config_vars:
- github-token
- github-repo
- github-branch
code_refs:
- lib/github.ts
- app/api/pathways/assemble/route.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/github.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/api/pathways/assemble/route.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/integrations/third-party-integrations.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Used for

Contributor assemble (`POST /api/pathways/assemble`) commits the pathway document to `content/wiki/pathways/<slug>.md` on the configured branch. It uses a hand-rolled fetch client in `lib/github.ts` (no SDK) that reads, writes and lists files. `ghListFiles` has no caller.

## Configuration

`GITHUB_TOKEN`, `GITHUB_REPO`, `GITHUB_BRANCH` (has a default).

## Failure behaviour

Any non-404 error throws, and assemble returns 500 with no retry. The `pathways` cache update after a successful commit is best-effort. If the branch is `main`, each assemble triggers a production deploy.

## Account

Repo, branch and token come from env; which account owns the token is not recorded in the repo.
