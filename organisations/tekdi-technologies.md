---
name: Tekdi Technologies
type: organisation
schema_version: 2
aliases:
- Tekdi
- Tekdi Team
summary: 'Implementation partner on the Diffusion Cube: the ''Tekdi Team'' that, with Kamesh, forms the
  charter''s Solution Team which builds and maintains the web app.'
doc_refs:
- docs/wiki/diffusion-cube/business/business-overview.md
org_kinds:
- implementation-partner
sources:
- system: raw_documents
  method: document
  date: '2026-10-08'
  ref: docs/raw_documents/AI DIffusion Cube - Product Charter.docx (execution model)
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/business/business-overview.md § Execution model
- system: github_repo
  method: derived
  date: '2026-10-08'
  ref: git log author anurag14-10
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## Relationship to the Cube

The Product Charter's execution model names the **Solution Team** as "Kamesh + Tekdi Team". It owns solution functionality, UI/UX and the data and technical architecture, builds and maintains the web app and the planned Claude Skill integration, and handles product and technical user issues. See Solution Team.

## Notes

- [Anurag Goutam](../people/anurag-goutam.md) (git `anurag14-10`) is the Tekdi developer visible in the repository history. He built the Docker/AWS EC2 path, the Supabase Send Email hook (OTP over SMTP), self-serve account deletion, the Terms of Use / Privacy Notice work and toolkit asset files.
- The repository does not record which other committers, if any, are Tekdi staff. Affiliation is recorded here only where the charter or the brain's curated registry states it.
