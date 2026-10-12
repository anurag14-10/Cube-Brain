---
name: Manage account (/account)
type: page
schema_version: 1
aliases:
- Account
- Manage Account
summary: Self-service account page for any signed-in user, with or without a role. It covers profile editing (user_metadata),
  contact-sharing level (approved contributors only) and permanent account deletion.
route: /account
file: app/account/page.tsx
access: signed-in
components:
- components-app-shell
- app-account-manage-account
- components-organisation-input
- components-delete-account-button
calls_endpoints:
- account-contact-sharing
- account-delete
- organisations
status: live
code_refs:
- app/account/page.tsx
- app/account/ManageAccount.tsx
- components/DeleteAccountButton.tsx
doc_refs:
- docs/wiki/diffusion-cube/application/frontend.md
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/account/page.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: app/account/ManageAccount.tsx
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: components/DeleteAccountButton.tsx
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/application/frontend.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it renders

A server component. It reads the user, their `designs` (for the Sidebar), `isAdmin`, and their
`contributor_registrations` row (`access_status`, `share_name`, `share_contact`), then renders AppShell around
[ManageAccount](../modules/app-account-manage-account.md):

1. **Profile:** name and organisation. Saved with `auth.updateUser({data})` straight from the browser, merging
   into the same `user_metadata` keys sign-up wrote.
2. **Contact sharing:** shown only when the registration is `approved`. Three levels (none / name / name and
   email) are saved through `POST /api/account/contact-sharing`, which applies the same approved-only rule.
3. **Danger zone:** [DeleteAccountButton](../modules/components-delete-account-button.md). The user confirms
   with their password, `POST /api/account/delete` re-verifies it server-side, then the browser signs out and
   goes to `/login`. Published pathways stay live.

The Sidebar links here as "Account", next to the email.

## Access behaviour

- **Anonymous:** `/account` is not public, so proxy.ts redirects to `/login?next=/account`. The page also
  redirects there itself if `getUser()` returns nobody.
- **Signed in, any role or none:** full page. It lives outside the `(app)` group on purpose, so a pending
  account can still edit or delete itself.
- **Contact sharing:** hidden unless the contributor registration is approved.
