# Write route — who pushes where

Admins push to `branch` directly. Everyone else writes through a pull request
an admin reviews and merges — nobody needs collaborator access. Settle the
route **before drafting anything**, so a write that cannot happen is said up
front, not after the work.

## 1. Identify the writer

The GitHub login, never a display name:

- Connector: its identity call (`get_me` or equivalent).
- Shell: `gh api user --jq .login` if `gh` is installed and signed in;
  otherwise ask the user once.

Never infer it — not from `repo`'s owner, the `admins` list, `git config
user.name`, a commit author or CODEOWNERS. No identity call and no answer →
no write. Compare against `admins` case-insensitively; use the login in
**lowercase** in branch names and activity filenames.

## 2. Pick the route — GitHub has the last word

| Writer | First try | If GitHub refuses (403 / 404 / "Permission denied" / "Resource not accessible by integration") |
|---|---|---|
| In `admins` | **Direct** — commit to `branch`, push | Not a PR fallback: the admin's own setup is wrong. Connector: the connector's GitHub App must be installed on `repo` with write. Shell: the SSH key or credential. Stop and say which. |
| Anyone else | **Branch** — a capture branch in `repo`, then a PR | **Fork** — the same branch in the writer's fork, then a PR. Expected for most people; not an error to report. |

A refusal on `repo` is never a reason to ask for collaborator access. A
refusal on the writer's **own fork** is a setup fault — see §5.

Branch name, one per logging event, always cut from the latest `branch` of
`repo`:
`<pr_branch_prefix><login>/<YYYY-MM-DD>-<short-slug>` (e.g.
`capture/swanandai/2026-10-13-pilot-weighting`). If it already exists (a
retry), append `-2`, `-3`.

## 3. What a PR commit holds

The entity files you wrote or changed, plus the one new activity entry file
under `activities/entries/<YYYY-MM>/`. **Never** `INDEX.md`, a monthly digest
`activities/<YYYY-MM>.md`, or backlink-only edits to pages you did not
otherwise touch. CI regenerates all of them after the merge; committing them
makes every two open PRs conflict.

## 4. Shell (Claude Code, the user's own clone)

Remotes: `<brain>` is the remote whose URL ends in `<repo>` (`git remote -v`).
If none does — the user cloned their fork — add it, in the same protocol
(ssh/https) as the existing remote: `git remote add upstream
https://github.com/<repo>.git`. `<fork>` is the remote ending in
`<login>/Cube-Brain`, if any.

**Admin (Direct):** on `main`, after the Mode B commit:

```bash
git pull --rebase <brain> main && git push <brain> main
```

CI commits regenerated pages to `main` after every push, so a plain push is
often rejected as non-fast-forward. Pull-rebase and push again **once**; if it
still fails, report it. Never force-push.

**Anyone else:** start from a clean tree — if `git status --porcelain` is not
empty, stop and ask (the `git restore .` below would discard it).

```bash
git fetch <brain>
git switch -c capture/<login>/<date>-<slug> <brain>/main
# Mode B steps 5–7: write, log the entry, regenerate + validate (must exit 0)
git add <your entity files> activities/entries/<YYYY-MM>/<your entry>.md
git commit -m "cube-brain: <summary>"
git restore .                                  # drop regenerated derived pages
git push -u <brain> HEAD  ||  git push -u <fork> HEAD   # Branch, else Fork
git switch main
```

No `<fork>` remote when the Branch push is refused:

- With `gh`: `gh repo fork <repo> --remote --remote-name fork`, then push.
- Without `gh`: ask the user to press **Fork** on `github.com/<repo>` once,
  then add it in the existing remote's protocol —
  `git remote add fork git@github.com:<login>/Cube-Brain.git` (ssh) or
  `https://github.com/<login>/Cube-Brain.git` (https) — and push.

Open the PR:

- With `gh`: `gh pr create --repo <repo> --base main --head <login>:<branch>
  --title "cube-brain: <summary>" --body-file -` (body in §6). Branch route:
  `--head <branch>`.
- Else with GitHub connector tools in the session: their create-pull-request
  call.
- Else hand the user the link to press **Create pull request** on, plus the
  body to paste:
  Fork `https://github.com/<repo>/compare/main...<login>:Cube-Brain:<branch>?expand=1`,
  Branch `https://github.com/<repo>/compare/main...<branch>?expand=1`.

## 5. Connector (Claude Desktop chat, web, mobile)

**Tool check first** (adapter §0): identity, read file, create branch, push
files / create-or-update file, fork, create pull request. Missing tools change
the route, not the outcome:

| Missing | Do instead |
|---|---|
| identity | ask for the login (§1) |
| create branch, or push/update file | cannot write — say so before drafting; offer the draft inline |
| fork | ask the user to press **Fork** on `github.com/<repo>` once, then continue |
| create pull request | after the push, give the compare link (§4) and the body |

Steps:

1. Identity → login. Admin → the adapter's direct push to `branch`; stop here.
2. Create the capture branch in `repo` from `branch`. Refused → step 3.
   Created → skip to step 5 (Branch route).
3. Fork `repo` (returns the existing fork if there is one). A just-created
   fork is built asynchronously: if the next call returns 404 / "not found",
   wait a few seconds and retry up to three times.
4. The fork's `main` must be at the same commit as `repo`'s — compare the
   latest commit SHA of each. Behind → use a sync tool if the connector has
   one; otherwise ask the user to press **Sync fork** on
   `github.com/<login>/Cube-Brain`, and wait. (A branch cut from a stale fork
   drags other people's merged work into the PR diff.) Then create the capture
   branch in the fork.
5. Fetch every file you change fresh **from `repo`** (not the fork), merge,
   and write them with the activity entry in **one multi-file push** to the
   capture branch.
6. Create the pull request on `repo`: base `branch`, head `<login>:<branch>`
   (Fork) or `<branch>` (Branch). Refused or no tool → the branch is already
   pushed: give the compare link (§4) and the body, and say the PR is not open
   until they press **Create pull request**.

Refused on the writer's own fork (steps 3 to 5): the connector's GitHub App
cannot reach their account or the new fork. Fix to name: GitHub → Settings →
Applications → the connector's app → Repository access → **All
repositories** (a fork created later is never in a "selected" list); or
re-authorise the connector with write scope. Then ask again.

## 6. PR body

```markdown
**What:** new decision `decisions/<slug>.md`; update `pathways/<slug>.md` (+6 units)
**Rests on:** <each source and its method — document / queried / stated / derived>
**Activity entry:** `activities/entries/<YYYY-MM>/<file>.md`

Captured with the cube-brain skill v<metadata.version> by @<login>.
```

## 7. Report only what happened

- Direct push succeeded → "Logged to the Cube-Brain — commit `<sha>`".
- PR opened → "PR #N opened — <link>. It lands in the brain when an admin
  merges it." Never "saved" or "logged". In Mode A, never cite an unmerged PR
  as brain content.
- Branch pushed, PR not opened → the compare link, "not open until you press
  Create pull request".
- Anything failed → say which step and the error, claim nothing, give the
  drafted markdown inline. Never retry the same refused call in a loop.

## For the admin reviewing

A contributor's **first** PR from a fork waits for **Approve and run
workflows** on the PR page before CI runs. Then the **Validate wiki** check
must be green. Merge with the PR title as the commit message (it carries the
`cube-brain:` prefix); after the merge CI regenerates `INDEX.md`, backlinks and
the activity digest on `main`. Close test PRs instead of merging them.
