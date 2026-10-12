---
name: Anurag Goutam
type: person
schema_version: 2
summary: Tekdi developer on the Solution Team (git anurag14-10). Owner of the Toolkit Asset Files work; also built the AWS deployment path, email delivery of sign-in codes, self-serve account deletion and the Terms of Use / Privacy Notice work.
doc_refs:
- specs/TOOLKIT_ASSETS_SPEC.md
- docs/tasks/toolkit-asset-files/requirement.md
affiliations:
- tekdi-technologies
teams:
- solution-team
project_roles:
- Developer, Solution Team
- Owner, Toolkit Asset Files spec (specs/TOOLKIT_ASSETS_SPEC.md)
github_handle: anurag14-10
sources:
- system: github_repo
  method: queried
  date: '2026-10-08'
  ref: git log --author=anurag14-10 (12 commits, 2026-09-22 → 2026-10-06)
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: 'specs/TOOLKIT_ASSETS_SPEC.md (Owner: Anurag Goutam)'
first_logged: '2026-10-08'
last_updated: '2026-10-12'
---

## Involvement

A Solution Team developer whose work reaches main through [Swanand Kulkarni](swanand-kulkarni.md)'s fork pull requests. Between 2026-09-22 and 2026-10-06 the work covered several charter requirements for [the web app milestone](../milestones/web-app-with-20-pathways.md):

- a Docker / AWS deployment path, built but not wired to CI (see [AWS account expiry](../risks/aws-account-expiry.md));
- delivery of sign-up and password-reset codes by email;
- self-serve account deletion;
- the Terms of Use and Privacy Notice;
- toolkit asset files, from requirement to implementation.

The toolkit-asset requirement records the request on 2026-09-29, and the spec names Anurag as owner. As owner, Anurag decided on 2026-09-30 that [third-party tools count as Toolkit Assets when the deployment built on them](../decisions/third-party-tools-count-as-toolkit-assets.md).
