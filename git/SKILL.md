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
- **Cherry-picking with editor bypass**: `GIT_EDITOR=true git cherry-pick --continue` (auto-accept commit message during conflict resolution)
- **Stashing partial work** (non-interactive): `git stash push -m "wip-description" -- path/to/file` (use pathspec for selective stashing; avoid `-p` as it is interactive)

### Bypassing Editor Prompts

Git commands that normally open an editor can be made non-interactive:

- **Set editor to true**: `GIT_EDITOR=true git <command>` (auto-accepts default message)
- **Use --no-edit flag**: `git commit --amend --no-edit`, `git merge --no-edit`, `git revert --no-edit`
- **Pre-set commit message**: `git commit -m "message"` (avoids editor entirely)
- **Cherry-pick continuation**: `GIT_EDITOR=true git cherry-pick --continue` (after resolving conflicts)
- **Revert with message**: `git revert <commit-sha> --no-edit` (uses default revert message)

**Important**: Automation tools (like `report_progress`) may fail if they encounter editor prompts.
Always use non-interactive patterns when preparing changes for automated tools.

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

## Integrating Changes from Target Branch (Avoiding Merge Commits)

**Problem**: When asked to "integrate changes from dev/main", using `git merge <target-branch>` creates a merge commit
that includes ALL commits from the target branch in your PR, making it impossible to review only your feature changes.

**Solution**: Rebase your commits on top of the target branch using the cherry-pick workflow.

### Step-by-Step Cherry-Pick Workflow

1. **Identify your feature commits**:

   ```bash
   # List commits in your branch not in target
   git log --oneline origin/<target-branch>..HEAD

   # Save commit SHAs for later
   git log --oneline origin/<target-branch>..HEAD | awk '{print $1}' | tac
   ```

2. **Fetch latest target branch**:

   ```bash
   git fetch origin <target-branch>
   ```

3. **Create backup before destructive operation**:

   ```bash
   git tag backup/before-rebase-$(date +%s)
   ```

4. **Reset branch to target** (creates clean starting point):

   ```bash
   git reset --hard origin/<target-branch>
   ```

5. **Cherry-pick your feature commits**:

   ```bash
   # Method 1: Individual commits
   git cherry-pick <commit-1> <commit-2> <commit-3>

   # Method 2: Range syntax (note the ^)
   git cherry-pick <first-commit>^..<last-commit>
   ```

6. **Handle conflicts during cherry-pick**:

   - Resolve conflicts in files (preserve target content, add your changes)
   - Stage resolved files: `git add <resolved-files>`
   - Continue non-interactively: `GIT_EDITOR=true git cherry-pick --continue`
   - Or skip commit: `git cherry-pick --skip`
   - Or abort: `git cherry-pick --abort`

7. **Verify only your changes are present**:

   ```bash
   # Check changed files
   git diff origin/<target-branch>..HEAD --name-status

   # Check stats
   git diff origin/<target-branch>..HEAD --stat

   # Verify commit count matches expectations
   git log --oneline origin/<target-branch>..HEAD | wc -l
   ```

   The diff should show ONLY files you created/modified for your feature, not unrelated files from target branch.

### Common Pitfalls

- **Merge commits in PR**: Indicates wrong approach was used. Start over with reset + cherry-pick workflow.
- **Too many changed files**: Verify you reset to correct target branch before cherry-picking.
- **Conflict resolution mistakes**: When resolving conflicts, don't remove existing target branch content—only add your feature changes.
- **Wrong commit order**: When cherry-picking multiple commits, maintain original chronological order.

### Working with Automation Tools

**CRITICAL**: Automation tools like `report_progress` automatically attempt to rebase your branch against the
remote tracking branch. **This causes session crashes** when:

- You've rewritten history (e.g., using reset + cherry-pick)
- Your branch has diverged from remote
- The remote has many commits that would trigger rebase conflicts

The crash sequence:

1. Tool switches to your branch
2. Tool runs `git rebase origin/<your-branch>` automatically
3. Rebase encounters conflicts from diverged history
4. Tool cannot resolve conflicts interactively → crash

### Prevention Strategies

#### Strategy 1: Use New Branch Name (Safest after history rewrite)

```bash
# After reset + cherry-pick workflow is complete
git checkout -b <feature>-v2
# or
git checkout -b <feature>-rebased

# Now report_progress won't attempt rebase - no remote tracking branch exists yet
```

#### Strategy 2: Manual Push Before Automation

If you must reuse the same branch:

```bash
# Complete all operations manually
git fetch origin <target-branch>
git reset --hard origin/<target-branch>
git cherry-pick <commits...>

# Verify changes
git diff origin/<target-branch>..HEAD --stat

# DON'T call report_progress here - ask user to push instead
# Explain: "Branch ready, needs force-push: git push --force-with-lease origin <branch>"
```

#### Strategy 3: Fresh Branch from Clean State

```bash
# If you haven't pushed anything yet
git checkout -b <new-feature-branch> origin/<target-branch>
# Do your work
# Call report_progress - safe because no divergence
```

### Detection: When You've Hit This Issue

Error patterns indicating auto-rebase crash:

- `Rebasing (1/NNN)` where NNN is very large (e.g., 113 commits)
- `error: could not apply <commit-sha>...`
- `CONFLICT (content): Merge conflict in <file>`
- `warning: skipped previously applied commit`
- Session terminates with `GitError: rebase git error`

### Recovery Steps

If automation tool fails with rebase errors:

1. **Abort the rebase**: `git rebase --abort`
2. **Verify your local state**: `git log --oneline -5` and `git diff origin/<target-branch>..HEAD --stat`
3. **Choose recovery path**:
   - Create new branch: `git checkout -b <branch>-v2 && git push origin <branch>-v2`
   - Or explain to user: "Branch ready at commit `<sha>`, needs manual push: `git push --force-with-lease origin <branch>`"

**Best Practice**: Complete all git operations manually (fetch, reset, cherry-pick, verify) BEFORE calling
automation tools. The tool will then simply push your clean, prepared commits.

### Example: Rebasing Feature Branch on Dev

```bash
# 1. Identify your commits
git log --oneline origin/dev..HEAD
# Output: abc123 Feature commit 3
#         def456 Feature commit 2
#         ghi789 Feature commit 1

# 2. Fetch latest dev
git fetch origin dev

# 3. Backup and reset
git tag backup/before-dev-$(date +%s)
git reset --hard origin/dev

# 4. Cherry-pick in original order
git cherry-pick ghi789 def456 abc123

# 5. Verify only your 3 commits on top of dev
git log --oneline origin/dev..HEAD
git diff origin/dev..HEAD --stat

# 6. Branch is now clean and ready for automation tools or manual push
```

## Troubleshooting tips

- Always use non-interactive git commands (e.g., git commit -m) to prevent editor locks in automation.
- Never trust only success messages—verify branches exist on the remote using git ls-remote or the GitHub UI after any push.
- For rewritten or rebased branches, use git push -f or push to a new branch; never attempt a normal push.
- Check for merge conflicts (git status) before any push, and abort (git rebase --abort) and clean up on conflict.
- Inspect all push/rebase failures in logs—manual intervention may be required if you see non-fast-forward or remote rejection errors.
- Use unique branch names if retrying after failure or history rewrite.
- Ensure your automation accounts have the correct GitHub permissions to create and push branches.

## What to Avoid

- Interactive operations (`git rebase -i`, `git add -p` without scripting, editor prompts).
- Direct pushes to protected branches (main/master).
- `git pull` in scripts—prefer explicit `fetch` + `rebase` or `merge --no-edit`.
- `--force` pushes without `--force-with-lease`.
- Unqualified `git reset --hard` (prefer `git reset --hard origin/main` with backup tag).

Always explain proposed git operations step-by-step, quote exact commands, and confirm irreversible actions with the user.
