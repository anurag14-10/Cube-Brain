# Cube-Brain

The knowledge graph of the **Diffusion Cube / 100 Pathways** project
(repo `diffusion-cube`): the AI Diffusion Pathway Framework it operationalises,
the pathway corpus it is grounded in, the app that delivers it, and the
decisions, debt, risks and milestones that shape it — 34 entity types in six
layers, every entry linked by slug.

| Start here | |
|---|---|
| [`CONVENTIONS.md`](CONVENTIONS.md) | Scope, entity types, slugs, edge directions, body templates, rules |
| [`SCHEMA.yml`](SCHEMA.yml) | The machine-readable model (types, fields, refs, rules) |
| [`MASTERS.md`](MASTERS.md) | Controlled vocabularies |
| [`SOURCES.md`](SOURCES.md) / [`SOURCE-SEMANTICS.md`](SOURCE-SEMANTICS.md) | What may corroborate an entry, and what each source means here |
| [`INDEX.md`](INDEX.md) | Every slug and alias (generated) |
| [`skills/cube-brain/`](skills/cube-brain/SKILL.md) | The agent skill that reads and writes this brain |

## Layers

| Layer | Folders |
|---|---|
| Framework | `dimensions/` `sub-categories/` `stages/` `cells/` `concepts/` |
| Corpus | `pathways/` `units/` `patterns/` `corpora/` |
| Actors | `organisations/` `people/` `teams/` `roles/` |
| Product | `features/` `workflows/` `pages/` `endpoints/` `chat-modes/` `prompts/` `contracts/` `tables/` `migrations/` `modules/` `integrations/` `config/` `environments/` |
| Knowledge | `rules/` `decisions/` |
| Delivery | `requirements/` `milestones/` `releases/` `tech-debt/` `risks/` `incidents/` |

## Everyday commands

```bash
pip install pyyaml                              # once
python3 scripts/validate_wiki.py .              # must exit 0 before every commit
python3 scripts/cube_report.py                  # project status: coverage, risks, debt, milestones, freshness
python3 scripts/cube_sync_plan.py               # what changed in diffusion-cube since the brain was verified
python3 scripts/seed_from_repo.py --dry-run     # re-derive framework/corpus stubs from the code
python3 scripts/build_index.py . && python3 scripts/build_backlinks.py . && python3 scripts/build_activity_log.py .
python3 scripts/add_site.py . && python3 scripts/build_site.py . && python3 -m http.server -d site 8000
```

Set `CUBE_REPO` if diffusion-cube is not checked out beside this repo.

## Rules in one breath

Trust the code. Blank beats plausible. No secrets, no config values, no
personal data. One commit per capture, prefixed `cube-brain:`. A planned thing
is never cited as built; a pathway's content is its contributor's account.
