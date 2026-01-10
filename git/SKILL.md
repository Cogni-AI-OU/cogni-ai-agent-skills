<!-- markdownlint-disable MD003 MD013 MD022 MD026 MD041 -->
---
name: git
description: Guide for using git
license: MIT
---

Expert in advanced git usage for repository agents. Prioritize non-interactive, safe, reproducible operations that maintain clean history and respect repository conventions.

## Core Principles

- **Non-interactive execution**: Commands must run without prompting. Never use interactive modes (`-i`, `--interactive`, default editors).
- **Linear history**: Prefer rebase over merge for feature branches to keep history clean and bisectable.
- **Atomic changes**: Favor small, focused commits. Use amend/fixup patterns for corrections.
- **Safety**: Never perform destructive operations without explicit reasoning and user confirmation.
- **Hook handling**: Aim to satisfy pre-commit/pre-push hooks. Use `--no-verify` only as a last resort when hooks are non-critical or environment-specific.
- **Conventional Commits**: Always use the format `<type>[optional scope]: <description>` with a blank line and detailed body if needed.

## Non-Interactive Patterns

- **Amending last commit** (preserve author date): `git commit --amend --no-edit --date="$(git log -1 --format=%aD)"`
- **Fixup previous commits** (non-interactive preparation):
- Create fixup: `git commit --fixup <commit-sha>`
- Later autosquash (requires interactive rebase—propose to user or defer to PR squash if agent cannot handle `-i`): `git rebase -i --autosquash origin/main`
- **Rebasing feature branches**: `git fetch origin && git rebase origin/main --no-verify` (add `--no-verify` only if hooks block)
- **Cherry-picking without conflicts**: `git cherry-pick -x <commit-sha>` (`-x` records original SHA for traceability)
- **Stashing partial work** (non-interactive): `git stash push -m "wip-description" -- path/to/file` (use pathspec for selective stashing; avoid `-p` as it is interactive)

## Working with Shallow Clones

GitHub Actions and other CI environments often check out repositories as shallow clones (limited history).

- **Detect shallow clone**:
  - `test -f .git/shallow && echo "Shallow clone" || echo "Full clone"`
  - `git rev-parse --is-shallow-repository` (outputs `true` or `false`)
- **Unshallow repository**: `git fetch --unshallow` (retrieves complete history)
- **Find commits not in current branch**:
  - Check if commit exists: `git cat-file -e <commit-sha> 2>/dev/null && echo "Exists" || echo "Not found"`
  - Search across all branches: `git log --all --oneline | grep <commit-sha-prefix>`
  - Fetch specific PR: `git fetch origin pull/<pr-number>/head:pr-<pr-number>`
  - List all branches containing commit: `git branch -a --contains <commit-sha>`

## Safety & Recovery

- **Check repository state non-interactively**:
- Clean working tree: `git diff --quiet && git diff --cached --quiet`
- Current branch: `git rev-parse --abbrev-ref HEAD`
- Unpushed commits: `git log origin/$(git rev-parse --abbrev-ref HEAD)..HEAD`
- **Reflog for recovery**: Reference `git reflog` before history-rewriting operations to enable rollback.
- **Backup before destructive ops**: Create temp tag: `git tag backup/pre-op-$(date +%s)`
- **Force push only when required** (e.g., after approved history rewrite): `git push --force-with-lease origin <branch>`

## Useful Diagnostic Commands

- Verify identity: `git config user.name && git config user.email`
- Remote tracking status: `git status -sb`
- Commit template check: `git config commit.template`
- Signed commit verification: `git log --show-signature -1`

## Resolving Merge Conflicts with Minimal Changes

When a merge introduces too many unrelated changes, maintain PR focus with selective conflict resolution:

- **Reset to clean state**: `git reset --hard <commit-sha>` (reset to commit before problematic merge)
- **Revert merge commit**: `git revert -m 1 <merge-commit-sha> --no-edit` (revert merge keeping first parent)
- **Remove lock files**: `rm -f .git/index.lock` (if git operations fail due to lock)
- **Clean untracked files**: `git clean -fd` (remove untracked files from working directory)
- **Check file state in commit**: `git ls-tree -r <commit-sha>:.github/workflows/ --name-only` (list files at specific commit)
- **Verify changes**: `git diff <commit-sha> HEAD --name-status` (compare commits to see what changed)

Strategy for focused PRs:

- Avoid merging large changesets when PR has single purpose
- Use `git reset --hard` to target commit with desired changes only
- Document resolution approach for future reference
- Keep PR changes minimal and reviewable

## What to Avoid

- Interactive operations (`git rebase -i`, `git add -p` without scripting, editor prompts).
- Direct pushes to protected branches (main/master).
- `git pull` in scripts—prefer explicit `fetch` + `rebase` or `merge --no-edit`.
- `--force` pushes without `--force-with-lease`.
- Unqualified `git reset --hard` (prefer `git reset --hard origin/main` with backup tag).

Always explain proposed git operations step-by-step, quote exact commands, and confirm irreversible actions with the user.
