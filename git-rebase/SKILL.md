---
name: git-rebase
description: >-
  Advanced git rebase operations including interactive history cleanup and
  non-interactive scripted rewrites. You must load this skill when performing
  git rebase operations.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

# Git Rebase

Expert-level guidance for executing git rebase operations safely, particularly distinguishing between interactive manual usage and automated environments.

## Interactive Rebasing (`git rebase -i`)

- **Objective**: Clean up local commit history before pushing.
- **Process**:
  - **WARNING**: Interactive modes (`-i`) are FORBIDDEN in runtime automation. Ensure `-i` is strictly scoped to local manual-only usage or fixing in the non-github runtime (like in local agent or devcontainer runtime).
  - Start manual rebase: `git rebase -i <base-commit-or-branch>`
  - Automated rewrites: Set `GIT_SEQUENCE_EDITOR=true` for non-interactive execution if scripted.
  - Actions: `pick`, `reword`, `edit`, `squash` (or `s`), `fixup` (or `f`), `drop`.

## Safety Principles

- NEVER rebase commits that have already been pushed to a shared public branch unless explicitly coordinating a force-push.
- **Abort**: Execute `git rebase --abort` to safely cancel an ongoing rebase operation.

## What to Avoid

- Interactive command execution (`git rebase -i`) in automated runtime pipelines.

## Limitations

- Cannot autonomously perform interactive rebasing in restricted runtime environments.

## Related Skills

- **git-expert**:
  Must be loaded when performing other advanced git operations or repository recovery.
