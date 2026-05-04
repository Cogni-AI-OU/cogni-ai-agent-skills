---
name: github-pr-review
description: >-
  Comprehensive PR review workflow for verifying code quality, metadata accuracy, and merge readiness.
  You must load this skill when reviewing, auditing, or verifying a GitHub Pull Request.
---

# GitHub PR Review

Elite autonomous PR review workflow for ensuring structural integrity, metadata accuracy, and zero-defect deployments.

## When to Activate

- Triggered when asked to review, audit, or verify a GitHub Pull Request.
- Loaded automatically during the final verification phase of a PR lifecycle.

## Core Review Checkpoints

Execute these checks systematically using `gh` and `git` tools:

- **Discovery & Scope Alignment**:
  - **Branch State**: Verify if the PR branch is up-to-date with the base branch.
  - **Comments Resolution**: Check for any existing unresolved comments or threads on the PR to ensure previous feedback
    has been integrated.
  - **Metadata Accuracy**: Ensure PR Title follows Conventional Commits and Description accurately reflects all changes.
- **Deep Code Inspection**:
  - **Atomic File Analysis**: Step through the diff file-by-file or component-by-component.
  - **Code Hygiene**: Scan for temporary/debug statements (`console.log`, `print`, `TODO`, `FIXME`, debugger breakpoints)
    and unintended files (`.env`, logs).
  - **Scope Control & Drive-by Prevention**: Ensure the PR does strictly what it claims. Flag any drive-by changes or
    unrelated refactoring that expand the PR's impact.
  - **Vulnerability Tracing**: Check for hardcoded secrets, injection flaws, inadequate input sanitization, and
    unchecked authorization gates.
  - **Regression Detection**: Uncover unintended side-effects and logically dead code introduced by changing
    dependencies.
- **Verification & Merge Readiness**:
  - **Build & CI Status**: Verify that all CI/CD checks (status checks) are passing.
  - **Test-Driven Audit**: Validate that adequate unit and integration tests accompany the changed vectors. Flag
    untested edge cases that were overlooked.
  - **Mergeability**: Check mergeability status for conflicts.

## Workflow Execution

### 1. Context Gathering

```bash
# Get PR metadata and mergeability
gh pr view <pr-number> --json title,body,mergeable,state,baseRefName,headRefName

# List all files changed
gh pr view <pr-number> --json files --jq '.files[].path'

# Get status checks
gh pr checks <pr-number>
```

### 2. Deep Inspection

```bash
# Check for debug statements in diff
git diff $(gh pr view <pr-number> --json baseRefName --jq .baseRefName)...HEAD | grep -E "console\.log|debugger|print\(|TODO|FIXME"

# List comments to ensure resolution
gh api repos/:owner/:repo/pulls/<pr-number>/comments
```

### 3. Verification

- Run local tests if applicable.
- Perform a "Design-It-Twice" comparison if the PR implements a complex architectural change.

## What to Avoid

- **Blanket Approvals**: Never approve without verifying EVERY checkpoint.
- **Ignoring Checks**: Never skip checking the status of CI/CD pipelines.
- **Missing Context**: Always read the PR description and linked issues before reviewing code.

## Related Skills

- **github-pr**:
  Must be loaded when working with changes on a GitHub Pull Request.
- **gh-pr**:
  Must be loaded when working with `gh pr` command.
- **github**:
  Must be loaded when working with GitHub-specific features or web-based PR interactions.
