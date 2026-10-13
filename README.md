# Cube-Brain

The knowledge graph of the **Diffusion Cube / 100 Pathways** project
(repo `diffusion-cube`): the AI Diffusion Pathway Framework it operationalises,
the pathway corpus it is grounded in, the people and organisations around it,
and the decisions, risks and milestones that shape it — 8 entity types in
three layers, every entry linked by slug. The app's code level is out of
scope since schema v2 (last modelled at commit `0296ca8`).

| Start here | |
|---|---|
| [`CONVENTIONS.md`](CONVENTIONS.md) | Scope, entity types, slugs, edge directions, body templates, rules |
| [`SCHEMA.yml`](SCHEMA.yml) | The machine-readable model (types, fields, refs, rules) |
| [`MASTERS.md`](MASTERS.md) | Controlled vocabularies |
| [`SOURCES.md`](SOURCES.md) / [`SOURCE-SEMANTICS.md`](SOURCE-SEMANTICS.md) | What may corroborate an entry, and what each source means here |
| [`INDEX.md`](INDEX.md) | Every slug and alias (generated) |
| [`skills/cube-brain/`](skills/cube-brain/SKILL.md) | The agent skill that reads and writes this brain |

## Layers

| Layer | Folders | Variables (MASTERS.md) |
|---|---|---|
| Framework + corpus | `concepts/` `pathways/` `units/` | dimension, stage, sub-category, grid key, corpus |
| Actors | `organisations/` `people/` | team |
| Delivery | `decisions/` `risks/` `milestones/` | — |

Each dimension's concept page carries its sub-categories (weights and
questions) and its four grid cells; each stage has its own concept page.

## Everyday commands

```bash
pip install pyyaml                              # once
python3 scripts/validate_wiki.py .              # must exit 0 before every commit
python3 scripts/cube_report.py                  # project status: corpus coverage, risks, milestones
python3 scripts/check_corpus_drift.py            # pathways added/changed in diffusion-cube since they were ingested
python3 scripts/probe_published_pathways.py     # DB-only pathways in Supabase (needs SUPABASE_URL + SUPABASE_ANON_KEY in env)
python3 scripts/seed_from_repo.py --dry-run     # re-derive framework concepts / pathway stubs from the repo
python3 scripts/migrate_v1_to_v2.py . --check   # every entry is on schema v2
python3 scripts/build_skill.py                  # dist/cube-brain.skill for Claude Desktop / web upload
python3 scripts/build_index.py . && python3 scripts/build_backlinks.py . && python3 scripts/build_activity_log.py .
python3 scripts/add_site.py . && python3 scripts/build_site.py . && python3 -m http.server -d site 8000
```

Set `CUBE_REPO` if diffusion-cube is not checked out beside this repo.

## Contributing

Use the `cube-brain` skill with your own GitHub account (Claude Code, or the
GitHub connector on Claude Desktop / web). Admins push to `main`; everyone else
gets a pull request opened for them — from a branch here if you have write
access, from your fork if not — which an admin reviews and merges. CI
validates every PR and regenerates `INDEX.md` and the activity digest after
the merge. Details: [`skills/cube-brain/references/write-route.md`](skills/cube-brain/references/write-route.md).

## Rules in one breath

Trust the source document. Blank beats plausible. No secrets, no config values, no
personal data. One commit per capture, prefixed `cube-brain:`. A planned thing
is never cited as built; a pathway's content is its contributor's account.
