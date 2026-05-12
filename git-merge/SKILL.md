---
name: git-merge
description: >-
  Guide and safety rules for performing git merges, ensuring no conflict markers and no duplicate lines are present.
  You MUST load this skill before performing a git merge.
---
# Skill: git-merge

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Execute safe and verified git merges. This skill enforces pre-merge checks, explicit conflict resolution,
and strict post-merge validation to prevent duplicate lines or lingering conflict markers.

## Core Process

1. **Pre-Flight Check**: Ensure the working directory is perfectly clean (`git status`)
   and the repository is not shallowed. Otherwise you need to unshallow it.
2. **Execute Merge**: Perform the merge (e.g., `git merge <branch> --no-edit --no-ff`).
3. **Inspect Conflicts**: If conflicts occur, resolve them explicitly file by file.
4. **Clean File Verification**: Check every resolved file to ensure absolutely
   no Git conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) remain.
5. **Deduplication Check**: Review the resolved sections to ensure no logical duplicates
   (e.g., duplicate imports, repeated variable declarations, or duplicate lines) were introduced.
6. **Commit and Validate**: Finalize the merge commit, run local tests, and check the log.

## Core Principles

- **Clean State**: Always begin a merge from a clean working tree. If there are uncommitted changes, stash or commit them first.
- **Deep History**:
  Ensure the repository is not shallow. Merging in a shallow repository can lead to unexpected results or failures.
- **No Duplicate Lines**: Merging can often result in duplicated logic if both branches added similar lines.
   You must manually verify that no duplicate imports, definitions, or statements exist post-merge.
- **Non-Interactive**: Prefer non-interactive commands. Do not launch `git mergetool` or GUI merge tools,
   and use `--no-edit` or `GIT_EDITOR=true` to avoid editor prompts during merge and commit steps.
- **Zero Conflict Markers**: A merge must never be committed if standard Git conflict markers remain in the file.

## Commands / Usage Patterns

- **Check Working Directory**:
  `git status --short`
- **Check for Shallow Repository**:
  `git rev-parse --is-shallow-repository`
  (must return `false` before merging to ensure full history is available)
- **Review Differences Before Merge**:
  `git diff HEAD..<target-branch> --name-only`
- **Perform Merge**:
  `git merge <target-branch> --no-ff --no-edit -m "Merge <target-branch> into HEAD"`
- **Find Conflict Markers**:
  `grep -rnE "<<<<<<<|=======|>>>>>>>" .`
  (Must return no output before finalizing the merge).
- **Find Duplicate Lines (heuristic)**:
  Use tools like `sort | uniq -d` on specific regions or manually inspect imports and declarations.
- **Finalize Merge**:
  `git commit --no-edit` (if conflicts were manually resolved and added).
- **Unshallow Repository**:
  `git fetch origin master --unshallow || git fetch origin master`

## Diagnostics and Troubleshooting

- **Accidental Bad Merge**: If the merge went wrong and you haven't pushed, use `git merge --abort` (if in progress)
  or `git reset --hard HEAD~1` (if already committed).
- **Merge Stuck in Conflict**: Use `git status` to identify unmerged paths.
  Edit them, run `git add <file>`, and then `git commit --no-edit`.
- **Process Stuck**: If git process hangs, ensure no interactive prompt was launched. Abort and rerun non-interactively.

## What to Avoid

- Avoid using interactive merge tools that stall the agent process.
- Do not commit if `git status` shows unmerged files.
- Do not push a merge without first verifying the application builds and tests pass locally.
- Never blindly `git add .` without checking the contents of resolved files.
- Never leave `<<<<<<< HEAD` or `>>>>>>>` markers in the codebase.

## Limitations

- The agent cannot use graphical merge conflict tools (e.g., `kdiff3`, `meld`).
  All conflict resolution must be done via text editing tools or by fully rewriting the file content.
