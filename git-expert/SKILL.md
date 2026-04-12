<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->
---
name: git-expert
description: >-
  Advanced Git operations including interactive rebasing, reflog recovery, bisecting,
  complex conflict resolution, and history manipulation.

---

# Advanced Git Operations

Expert-level guidance for executing complex Git operations safely and effectively.

## When to Activate

- User needs to rewrite commit history (e.g., squashing, reordering, editing).
- User has lost commits or needs to recover state using `git reflog`.
- User needs to find a regression using `git bisect`.
- User needs to recover a corrupted local repository (e.g., empty objects, bad object refs, `git fsck` failures).
- User requires assistance with complex merge conflicts or tree manipulations.
- User needs to manage Git submodules or advanced worktrees.

## Interactive Rebasing (`git rebase -i`)

- **Objective**: Clean up local commit history before pushing.
- **Process**:
  - Start rebase: `git rebase -i <base-commit-or-branch>`
  - Set `GIT_SEQUENCE_EDITOR=true` for non-interactive automated rewrites if scripted.
  - Actions: `pick`, `reword`, `edit`, `squash` (or `s`), `fixup` (or `f`), `drop`.
- **Safety**: NEVER rebase commits that have already been pushed to a shared public
  branch unless explicitly coordinating a force-push.
- **Abort**: `git rebase --abort`

## Reflog Recovery (`git reflog`)

- **Objective**: Recover lost commits, branches, or undo a destructive operation (like a bad hard reset).
- **Process**:
  - View history of HEAD movements: `git reflog`
  - Identify the target commit SHA (e.g., `HEAD@{2}`).
  - Restore state: `git reset --hard <sha>` or create a branch: `git branch <branch-name> <sha>`.

## Bisecting (`git bisect`)

- **Objective**: Use binary search to find the exact commit that introduced a bug.
- **Process**:
  - Start: `git bisect start`
  - Mark broken commit (usually current): `git bisect bad`
  - Mark known good commit: `git bisect good <good-commit-sha>`
  - Git will checkout intermediate commits. Test, then mark `git bisect good` or `git bisect bad`.
  - Conclude: `git bisect reset` to return to the original branch.

## Advanced Cherry-Picking

- **Objective**: Apply specific commits from one branch to another without merging the whole branch.
- **Process**: `git cherry-pick <commit-sha>`
- **Multiple commits**: `git cherry-pick <sha-A>^..<sha-B>`
- **No commit (stage only)**: `git cherry-pick -n <commit-sha>`

## Complex Troubleshooting

- **Corrupted Repository Recovery**: For errors like `fatal: bad object refs/heads/...`,
  `object file is empty`, or `git did not send all necessary objects`.
  - **Diagnose**: Run `git fsck --full` to identify missing/corrupted objects or refs.
  - **Backup first**: `cp -a repo repo.bak` before destructive commands.
  - **Empty Objects**: Delete zero-byte objects blocking pulls with
    `find .git/objects/ -type f -empty -delete`.
  - **Bad Refs/Heads**: Check for corrupted or duplicate branch refs (e.g., from cloud-sync
    like iCloud/Dropbox). Delete broken refs (e.g., `rm .git/refs/heads/dev` or
    `git update-ref -d refs/heads/dev`), then `git fetch -p` to restore.
  - **Finalize Repair**: If local index/HEAD is corrupted, `rm -rf .git/index` and
    `git reset --hard origin/<branch>`.
- **Detached HEAD**: If work is committed in a detached head, immediately create a branch
  before checking out anything else: `git branch backup-branch`.
- **Untracked files overwriting**: If a checkout/pull is blocked by untracked files, stash
  them (`git stash push -u`) or clean (`git clean -fd` - **destructive**).
- **Accidental Force Push**: Look for previous commit SHA in local terminal history, local
  `git reflog` (if same machine), or GitHub PR/Issue events to restore.

## Verification

- Always verify the workspace state with `git status` and history with `git log --oneline --graph -n 15` after altering history.
- Ensure all automated actions gracefully handle conflicts by checking exit codes.
