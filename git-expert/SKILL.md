---
name: git-expert
description: >-
  Advanced Git operations including reflog recovery,
  bisecting, complex conflict resolution, and history manipulation.
  You MUST load this skill when performing advanced git operations or repository
  recovery.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

# Advanced Git Operations

Expert-level guidance for executing complex Git operations safely and effectively.

## When to Use

- User has lost commits or needs to recover state using `git reflog`.
- User needs to find a regression using `git bisect`.
- User is managing Git submodules or advanced worktrees.
- Local repository corruption requires recovery (e.g., empty objects, bad object refs, `git fsck` failures).
- Commit history rewriting is required (e.g., squashing, reordering, editing).
- User requires assistance with complex merge conflicts or tree manipulations.

Note: For specific guidance on Git rebase operations and interactive rebasing, see the **git-rebase** skill.

## When Not to Use

- For standard, day-to-day operations like simple commits, pulls, or merges (use the base `git` skill).
- When a graphical Git client or GitHub's web UI provides a safer, more transparent way to resolve a simple conflict.
- If you lack a fundamental understanding of Git's object model (attempting expert commands without knowledge often destroys history).

## Common Pitfalls

- **Panic Force-Pushing**: Running `git push --force` immediately after a bad rebase instead of calmly using `git reflog` to restore the previous state.
- **Detached HEAD Confusion**: Committing work in a detached HEAD state and then checking out another branch, instantly losing track of the new commits.
- **Corrupting the Index**: Manually deleting files inside the `.git/` directory to "fix" an error instead of using proper commands like `git fsck` or `git reset`.

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
  - **Backup first**: From the parent directory, back up the entire repository:
    `cp -a <repo-name> <repo-name>.bak` before destructive commands.
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

## Related Skills

- **git-rebase**:
  You MUST load this skill when performing Git rebase operations.
