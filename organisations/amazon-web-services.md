---
name: Amazon Web Services
type: organisation
schema_version: 2
aliases:
- AWS
summary: Cloud vendor for the Cube's Docker / EC2 deployment path, on a free account the Product Charter says expires in December 2026.
doc_refs:
- docs/raw_documents/AI DIffusion Cube - Product Charter.docx
- docs/wiki/diffusion-cube/operations/deployment.md
org_kinds:
- vendor
website: https://aws.amazon.com
sources:
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: Product Charter, Dependencies section (AWS server account free, expiring December)
- system: diffusion_cube_docs
  method: document
  date: '2026-10-12'
  ref: docs/wiki/diffusion-cube/operations/deployment.md
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Relationship to the Cube

AWS hosts the Docker / EC2 deployment path of the app. That path is built but not wired to CI; the live path is Vercel. The Product Charter lists the AWS server account as a dependency on a free account.

## Notes

- The charter says the account expires "this December" and that a replacement must be planned by November 2026. The dated threat is tracked as the risk [AWS account expiry](../risks/aws-account-expiry.md).
