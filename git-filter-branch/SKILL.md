---
name: git-filter-branch
description: >-
  Extract a specific subdirectory with history using git filter-branch when modern tools like filter-repo are unavailable.
  You MUST load this skill when extracting a subdirectory with history using `git filter-branch`.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

# Git Filter Branch

Extract a specific subdirectory from an external repository and merge it into another repository's root,
permanently preserving the git commit history of those files, using `git filter-branch` as a built-in fallback.

## When to Use

- To extract a specific subdirectory from a repository while completely preserving its commit history.
- When migrating a mono-repo folder into its own standalone repository.
- As a fallback when modern tools like `git filter-repo` or `git subtree` are unavailable in the environment.

## When Not to Use

- For standard merges, rebases, or cherry-picks within the same repository (use standard `git` commands).
- When the environment supports `git filter-repo`, which is significantly faster and safer than `filter-branch`.
- For simply copying files without needing to preserve their git history.

## Common Pitfalls

- **Ignoring Root Conflicts**: Merging the filtered branch and blindly accepting conflicts on root files (like `README.md` or `.gitignore`), accidentally overwriting the target repo's core files.
- **Slow Execution**: Running `filter-branch` on a massive, decade-old repository without realizing it can take hours to process every commit.
- **Pre-Commit Hook Crashes**: Attempting the final merge without using `--no-verify`, causing pre-commit hooks to trigger on thousands of old files and timing out the environment.

## Core Process

1. **Clone Source**: Clone the external repository into a temporary directory:

   ```bash
   git clone <url> temp-repo
   cd temp-repo
   ```

2. **Rewrite History**: Isolate the target subdirectory so it becomes the root of the temporary repository:

   ```bash
   export FILTER_BRANCH_SQUELCH_WARNING=1
   git filter-branch -f --subdirectory-filter <path> HEAD
   ```

3. **Add Remote**: Navigate back to your main repository and add the temporary clone as a new remote:

   ```bash
   cd /path/to/main
   git remote add temp-repo /path/to/temp-repo
   ```

4. **Merge**: Fetch and merge the isolated history into your main repository (replace `<branch>` with the source repo's default branch if different):

   ```bash
   git fetch temp-repo
   git merge temp-repo/<branch> --allow-unrelated-histories
   ```

## Challenges & Solutions

- **Root File Conflicts**:
  Files pulled from the target subdirectory may conflict with your main repository if they share generic names (e.g., `README.md`, `AGENTS.md`).
  Handle these deliberately (e.g., `git checkout --ours README.md`).
- **Hook Interference**:
  Pre-commit hooks might trigger heavily on the newly merged files. Use `--no-verify` on the merge commit if the upstream is already trusted,
  followed by independent linting to avoid timeout crashes in constrained environments.

## Limitations

- **Tool Availability**: Modern tools (`filter-repo`, `subtree`) may be missing. `filter-branch` provides a built-in albeit older solution.
