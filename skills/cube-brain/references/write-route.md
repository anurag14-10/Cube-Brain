# Write route — who pushes where

Admins push to `branch` directly. Everyone else writes through a pull request
an admin reviews and merges. Decide the route once per session, before the
first write, and keep it.

## 1. Identify the writer

The GitHub login, never a display name:

- Connector: its own identity call (`get_me` or equivalent).
- Shell: `gh api user --jq .login` if `gh` is installed and signed in;
  otherwise ask the user once. `git config user.name` is a display name, not
  a login.

## 2. Pick the route

| Writer | Route |
|---|---|
| Listed in `admins` (Configuration in `SKILL.md`) | **Direct** — commit to `branch` and push, as Mode B describes |
| Has write access to `repo` | **Branch** — a branch in `repo`, then a PR |
| Anyone else | **Fork** — a branch in the writer's fork of `repo`, then a PR |

Write access, checked without guessing:

- Connector: try to create the branch in `repo`. Success → Branch route. A
  403, 404 or "permission" refusal → Fork route.
- Shell: `gh api repos/<repo> --jq .permissions.push` → `true` is Branch
  route. Without `gh`, push the branch to `repo`'s remote and fall back to the
  Fork route on "Permission denied" / 403.

Branch name, one per logging event, always cut from the latest `branch` of
`repo`: `<pr_branch_prefix><login>/<YYYY-MM-DD>-<short-slug>`, e.g.
`capture/priya-k/2026-10-13-pilot-weighting`.

## 3. What a PR commit holds

The entity files you wrote or changed, plus the one new activity entry file
under `activities/entries/<YYYY-MM>/`. **Never** `INDEX.md`, a monthly digest
`activities/<YYYY-MM>.md`, or backlink-only edits to pages you did not
otherwise touch. CI regenerates all of them after the merge, and committing
them makes every two open PRs conflict.

## 4. Shell (Claude Code, a local clone)

`<brain>` is the remote whose URL is `repo`; `<fork>` is the one pointing to
`<login>/Cube-Brain`. Start from a clean tree: if `git status --porcelain` is
not empty, stop and ask, because step 4 below discards regenerated files.

```bash
git fetch <brain>
git switch -c capture/<login>/<date>-<slug> <brain>/main
# Mode B steps 5–7: write, log the entry, regenerate + validate (must exit 0)
git add <your entity files> activities/entries/<YYYY-MM>/<your entry>.md
git commit -m "cube-brain: <summary>"
git restore .                       # drop regenerated derived pages
git push -u <brain or fork> HEAD
```

Fork, set up once:

- With `gh`: `gh repo fork <repo> --remote --remote-name fork` (keeps
  `origin` as is).
- Without `gh`: ask the user to press **Fork** on `github.com/<repo>` once,
  then `git remote add fork git@github.com:<login>/Cube-Brain.git`.

Open the PR:

- With `gh`: `gh pr create --repo <repo> --base main --head <login>:<branch>
  --title "cube-brain: <summary>" --body-file -` (body below).
- With GitHub connector tools in the session: their create-pull-request call.
- Otherwise hand the user the link to press **Create pull request** on:
  `https://github.com/<repo>/compare/main...<login>:Cube-Brain:<branch>?expand=1`
  (Branch route: `.../compare/main...<branch>?expand=1`) and the body to paste.

Then `git switch main`.

## 5. Connector (Claude Desktop chat, web, mobile)

1. Identity call → login. Admin → the adapter's direct push; stop here.
2. Create the branch in `repo` from `branch`. Refused → fork `repo` (the fork
   call returns the existing fork if there is one).
3. Fork route: the fork's `main` must be at the same commit as `repo`'s
   before you branch — compare the latest commit SHA of each. If it is behind,
   use the connector's sync tool if it has one; otherwise ask the user to press
   **Sync fork** on `github.com/<login>/Cube-Brain`, and wait. A branch cut
   from a stale fork drags other people's merged work into the PR diff. Then
   create the branch in the fork.
4. Fetch every file you change fresh **from `repo`** (not the fork), merge,
   and write them with the activity entry in **one multi-file push** to the
   branch.
5. Create the pull request on `repo`: base `branch`, head `<login>:<branch>`
   (Fork) or `<branch>` (Branch). If that call is refused (403 "Resource not
   accessible by integration" — the connector's GitHub App is not installed
   on `repo`'s owner), the branch is already pushed: give the user the compare
   link from §4 and the PR body to paste, and say the PR is not open until
   they press **Create pull request**.

A 403 on step 2's fork, or on writing to the fork, means the connector's
GitHub App cannot reach the writer's own account or the new fork: they open
GitHub → Settings → Applications → the connector's app → Repository access
→ **All repositories** (a fork created later is not in a "selected" list),
then ask again. Never tell a non-admin to become a collaborator — the PR route
exists so they do not have to.

## 6. PR body

```markdown
**What:** new decision `decisions/<slug>.md`; update `pathways/<slug>.md` (+6 units)
**Rests on:** <each source and its method — document / queried / stated / derived>
**Activity entry:** `activities/entries/<YYYY-MM>/<file>.md`

Captured with the cube-brain skill by @<login>.
```

## 7. Report it as pending

A PR is not the brain. Say: "PR #N opened — <link>. It lands in the brain when
an admin merges it." Never say it was saved or logged. In Mode A, do not cite
an unmerged PR as brain content. If the push or the PR call failed, say so,
claim nothing, and give the drafted markdown inline.

## For the admin reviewing

The PR's **Validate wiki** check must be green. Merge with the PR title as the
commit message (it carries the `cube-brain:` prefix). After the merge CI
regenerates `INDEX.md`, backlinks and the activity digest on `main`.
