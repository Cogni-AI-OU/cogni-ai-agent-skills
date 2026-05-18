---
name: git-rebase
description: >-
  Advanced Git rebase operations including interactive history cleanup and
  non-interactive scripted rewrites.
  You MUST load this skill before performing Git rebase operations.
license: MIT
---

# Git Rebase

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- You need to rebase a feature branch onto a target branch to maintain a linear, clean commit history.
- You need to clean up local commit history before pushing (squashing fixups, reordering commits, dropping WIP commits).
- You need to automate rebase operations with scripted `GIT_SEQUENCE_EDITOR` for non-interactive todo list manipulation.
- You need to use `git rebase --autosquash` with pre-created `fixup!` / `squash!` commits to automate history cleanup.
- You need to recover from a rebase that has gone wrong using `git rebase --abort`.

## When Not to Use
- You need to perform a standard merge (with merge commit) to preserve branch topology — use the **git-merge** skill instead.
- You need to integrate changes from a target branch into your feature branch while avoiding history rewrites — use the **git** skill's merge workflow or cherry-pick approach.
- You have already pushed commits to a shared/public branch — rebasing shared commits rewrites history and causes divergence for all collaborators.
- You are operating in a GitHub Actions runtime where the auto-PR/push logic requires compatible remote branch history — rebasing will change commit SHAs and break post-run push workflows.

## Common Pitfalls
- `GIT_SEQUENCE_EDITOR=true` only skips opening the editor during `git rebase -i`; it does **not** rewrite the todo list — you need a script or command as the editor value to perform automated todo manipulation.
- Interactive mode (`git rebase -i`) is **FORBIDDEN** in automated runtime environments — it will hang waiting for user input with no fallback.
- Rebasing commits that have already been pushed requires `--force-with-lease` to push the rewritten history, which is destructive to any collaborator's work based on the original commits.
- After a rebase, an automation tool that automatically syncs with the remote tracking branch will attempt a `git rebase` as part of its workflow — if your branch has diverged due to history rewriting, this secondary rebase will crash. Use a new branch name to prevent this.
- Always run `git rebase --abort` at the first sign of unresolvable conflicts or unexpected behavior during a rebase — continuing with conflicts unresolved will leave the repository in a broken state.

Expert-level guidance for executing Git rebase operations safely, particularly distinguishing between interactive manual usage and automated environments.

## Interactive Rebasing (`git rebase -i`)

- **Objective**: Clean up local commit history before pushing.
- **Process**:
  - **WARNING**: Interactive modes (`-i`) are FORBIDDEN in runtime automation. Ensure `-i` is strictly scoped to local manual-only usage or fixing in the non-GitHub runtime (like in local agent or devcontainer runtime).
  - Start manual rebase: `git rebase -i <base-commit-or-branch>`
  - Non-interactive note: `GIT_SEQUENCE_EDITOR=true` only skips opening the editor; it does **not** rewrite the rebase todo list.
  - Scripted rewrites: For automation, set `GIT_SEQUENCE_EDITOR` to a script or command that edits the todo file, or prefer `git rebase -i --autosquash` with `fixup!` / `squash!` commits when appropriate.
  - Actions in the todo list: `pick`, `reword`, `edit`, `squash` (or `s`), `fixup` (or `f`), `drop`.

## Safety Principles

- NEVER rebase commits that have already been pushed to a shared public branch unless explicitly coordinating a force-push.
- **Abort**: Execute `git rebase --abort` to safely cancel an ongoing rebase operation.

## What to Avoid

- Interactive command execution (`git rebase -i`) in automated runtime pipelines.

## Limitations

- Cannot autonomously perform interactive rebasing in restricted runtime environments.

## Related Skills

- **git**:
  You MUST load this skill when performing standard Git operations.
- **git-expert**:
  You MUST load this skill when performing advanced Git operations beyond rebasing.
