---
name: git-filter-branch
description: 'Extract a specific subdirectory with history using git filter-branch when modern tools like filter-repo are unavailable. You MUST load this skill when extracting a subdirectory with history using `git filter-branch`.'
license: MIT
---

# Git Filter Branch

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- You need to extract a specific subdirectory from an external repository and import it into your repository while preserving the full git history of those files.
- You are splitting a monorepo into smaller repositories or migrating a component from one repository to another.
- You need to merge code from an upstream repository that is organized differently (files are in a subdirectory) into your root-level project structure.
- Modern tools like `git filter-repo` or `git subtree` are not available in your environment, and you need a built-in git solution.

## When Not to Use
- You need to extract a directory without preserving history — a simple file copy (`cp -r`) or `git checkout` with path-specific commands is faster and less risky.
- `git filter-repo` or `git subtree` is available in your environment — prefer those tools as they are faster, safer, and have better documentation.
- You need to simply merge two repositories at the root level (no subdirectory filtering) — use standard `git merge --allow-unrelated-histories` instead.
- You are working in a shared repository where rewriting history would disrupt other contributors — `filter-branch` rewrites all affected commits, changing SHAs.

## Common Pitfalls
- `git filter-branch` **rewrites commit SHAs** for every commit that touched the target subdirectory — this is a destructive history rewrite that will cause divergence from any forks or clones.
- The `FILTER_BRANCH_SQUELCH_WARNING=1` environment variable is recommended to suppress verbose warnings, but it does not silence all output — expect significant terminal output for large repositories.
- When merging filtered history with `--allow-unrelated-histories`, files with generic names (e.g., `README.md`, `AGENTS.md`, `LICENSE`) will conflict — handle these deliberately with `git checkout --ours` or `--theirs` per file.
- Pre-commit hooks can trigger heavily on the newly merged files, potentially causing timeouts in constrained environments — use `--no-verify` on the merge commit if the upstream is already trusted.

Extract a specific subdirectory from an external repository and merge it into another repository's root,
permanently preserving the git commit history of those files, using `git filter-branch` as a built-in fallback.

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
