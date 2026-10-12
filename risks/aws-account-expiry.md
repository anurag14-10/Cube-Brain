---
name: AWS account expiry
type: risk
schema_version: 2
summary: The AWS account behind the Docker / EC2 deployment path is a free account expiring in December 2026; the charter says plan a replacement by November.
tags:
- time-sensitive
- vendor-account
doc_refs:
- docs/raw_documents/AI DIffusion Cube - Product Charter.docx
- docs/wiki/diffusion-cube/operations/deployment.md
status: open
likelihood: medium
impact: medium
due_date: 2026-11-30
mitigation: Plan the replacement AWS account by November 2026, as the charter asks, or retire the EC2 path in favour of the live Vercel path.
organisation: amazon-web-services
sources:
- system: raw_documents
  method: document
  date: '2026-10-12'
  ref: Product Charter, Dependencies section (AWS server account free, expiring December, plan by November)
first_logged: '2026-10-12'
last_updated: '2026-10-12'
---

## Risk

The Product Charter lists the AWS server account as a free account expiring "this December", with a new account to be planned by November 2026.

## Impact if it happens

The Docker / EC2 deployment path stops. That path is built but not wired to CI, and the live app runs on Vercel, so the immediate user impact is limited. It matters if the charter's "Deployment in AWS environment" requirement is still the target.

## Mitigation

`due_date` is the charter's planning deadline (end of November), not the expiry itself. The charter gives no exact expiry day.
