---
name: git-rebase
description: >-
  Advanced Git rebase operations including interactive history cleanup and
  non-interactive scripted rewrites.
  You MUST load this skill before performing Git rebase operations.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

# Git Rebase

Expert-level guidance for executing Git rebase operations safely, particularly distinguishing between interactive manual usage and automated environments.

## When to Use

- When updating a feature branch with the latest changes from `main` to maintain a linear history.
- To squash or fix up messy, intermediate commits before opening a Pull Request (using `git rebase -i --autosquash` locally).
- When moving a branch's base from one commit to another to untangle dependency chains.

## When Not to Use

- On shared or public branches where other developers have already pulled the commits (doing so rewrites history and causes severe integration headaches).
- For simple feature integrations where a standard merge commit is explicitly requested or preferred by the team's workflow.
- In fully automated CI/CD environments unless strictly using non-interactive scripting to handle specific autosquash patterns.

## Common Pitfalls

- **Interactive Terminal Hangs**: Using `-i` in an automated agent environment, causing the system to freeze while waiting for a VIM editor input that will never happen.
- **Force-Pushing Blindly**: Running `git push --force` after a rebase instead of `git push --force-with-lease`, potentially destroying a teammate's recent commits.
- **Conflict Panic**: Encountering a merge conflict during a rebase and running chaotic commands instead of methodically resolving the files, adding them, and running `git rebase --continue` (or `--abort` if hopelessly stuck).

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
