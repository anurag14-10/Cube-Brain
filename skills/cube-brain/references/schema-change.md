# Changing the Cube-Brain's model

A schema change alters the shape everyone writes against. Do it with a person
present, never as a side effect of a capture. Commits follow
`write-route.md`: anyone not in `admins` proposes it as a PR, and
`SCHEMA.yml`, `CONVENTIONS.md` and `MASTERS.md` always need the admin's
review (CODEOWNERS).

## Adding a vocabulary term (no version bump)

A new term in `MASTERS.md` changes meaning, not shape. Add it as
`- term — one-line meaning` under the right numbered section, in the same
commit as the first entry that uses it, and say why in the commit message.

## Adding an optional field (no version bump)

Declare it under the type in `SCHEMA.yml` (respect "one folder per ref
field"; refs point from the more specific/volatile entity to the more
stable one), document it in `CONVENTIONS.md` (edge-direction table if it is a
reference), and validate. Existing files stay valid.

## Adding an entity type (no version bump)

First ask whether it is a closed set. Dimensions, stages, sub-categories,
grid keys, corpora and teams are MASTERS variables, not folders — a small
fixed list belongs there, with its definition on a concept page. Schema v2
exists because v1 made folders of them.

1. `SCHEMA.yml`: new key under `entities:` with `folder`, a load-bearing
   `description:` (what it MEANS and what it may be cited as), `<<: *common`
   fields, its own fields, and any rules.
2. `CONVENTIONS.md`: entity-type table, "choosing the right type" row if it
   could be confused with an existing type, slug form, edge directions, body
   skeleton.
3. `mkdir <folder> && touch <folder>/.gitkeep`.
4. Validate; the site picks the new type up automatically.

## Bumping the schema version (a field renamed, removed, or changes shape)

1. Write `scripts/migrate_v<n>_to_v<n+1>.py` that rewrites every affected file
   mechanically, with a `--check` mode for CI (`migrate_v1_to_v2.py` is the
   worked example). A bump without its migrator is not finished — opportunistic
   migration never converges.
2. Update `SCHEMA.yml` `schema_version`, `CONVENTIONS.md` "Current schema
   version" AND add a version-history entry with the field-level mapping.
3. Keep a retired field as an alias for one version before removing it.
4. Commit the schema change and the data migration as **separate commits** so
   each can be reviewed.
5. Update `metadata.brain_schema` in `skills/cube-brain/SKILL.md` and point the
   CI "Schema version drift" step at the new migrator.
