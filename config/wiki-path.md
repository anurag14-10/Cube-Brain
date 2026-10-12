---
name: WIKI_PATH
type: config_var
schema_version: 1
summary: Optional override of the grounding-corpus root directory.
var_name: WIKI_PATH
required: false
secret: false
browser_exposed: false
read_by:
- lib-wiki-loader
- lib-wiki-content
environments:
- local-development
code_refs:
- lib/wiki-loader.ts
- lib/wiki-content.ts
verified_at_commit: 28068b6d0667507325fa862f700089d4e91a1731
sources:
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/wiki-loader.ts
- system: diffusion_cube_code
  method: queried
  date: '2026-10-08'
  ref: lib/wiki-content.ts
- system: diffusion_cube_docs
  method: document
  date: '2026-10-08'
  ref: docs/wiki/diffusion-cube/architecture/configuration.md
first_logged: '2026-10-08'
last_updated: '2026-10-08'
---

## What it controls

Optional override of the grounding-corpus root directory. It defaults to the in-repo `content/wiki` folder under `process.cwd()`. Useful to point local development at another checkout.

## Where it is read

- `lib/wiki-loader.ts` — the model's prompt corpus.
- `lib/wiki-content.ts` — /wiki browsing.

Both read the same variable, so they stay pointed at the same corpus.
