---
name: Anurag Goutam
type: person
schema_version: 2
summary: Tekdi developer on the Solution Team (git anurag14-10). Built the Docker/AWS EC2 path, the Supabase
  Send Email hook for OTP over SMTP, self-serve account deletion, the Terms of Use / Privacy Notice work
  and toolkit asset files.
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
last_updated: '2026-10-08'
---

## Involvement

Commits authored as `anurag14-10` in diffusion-cube, all reaching main through Swanand Kulkarni's fork PRs:

- **2026-09-22** `b8c9a9c`: Docker support and an AWS EC2 deployment path. The path is built but not wired to CI.
- **2026-09-24** `0f5aa10`: Supabase Auth Send Email hook. OTP and reset codes are delivered over SMTP via nodemailer (`app/api/auth/send-email/route.ts`). See OTP signup and reset.
- **2026-09-28** `1be6f71`: self-serve account deletion (migration 0033), in-app confirm dialogs and toasts. See Account deletion.
- **2026-09-28** `619aeff`: Terms and Conditions. See Terms and privacy.
- **2026-09-29 → 2026-10-06** (`e0ede1b`, `7ac843a`, `3ded7ae`, `e51e555`, `28068b6`): the toolkit asset files requirement, plan and task list, then the implementation (migration 0034, upload/register/download routes, consent cards, admin publish). See Toolkit asset files.

The toolkit-asset requirement records that he requested the work on 2026-09-29. `specs/TOOLKIT_ASSETS_SPEC.md` names him as owner.
