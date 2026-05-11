---
name: github-pr-review
description: >-
  Comprehensive PR review workflow for verifying code quality, metadata accuracy, and merge readiness.
  You MUST load this skill when reviewing, auditing, or verifying a GitHub Pull Request.
---

# GitHub PR Review

Elite autonomous PR review workflow for ensuring structural integrity, metadata accuracy, and zero-defect deployments.

## Core Review Checkpoints

Execute these checks systematically using `gh` and `git` tools:

- **Discovery & Scope Alignment**:
  - **Branch State**: Verify if the PR branch is up-to-date with the base branch.
  - **Comments Resolution**: Check for any existing unresolved comments or threads on the PR to ensure previous feedback
    has been integrated.
  - **Metadata Accuracy**: Ensure PR Title follows Conventional Commits and Description accurately reflects all changes.
- **Deep Code Inspection**:
  - **Inspection Framework**: Apply the `code-review` skill's cognitive framework to evaluate code quality dimensions.
  - **Atomic File Analysis**: Step through the diff file-by-file or component-by-component.
  - **Scope Control**: Ensure the PR does strictly what it claims. Flag any drive-by changes or unrelated refactoring.
  - **Integration Check**: Verify that new code correctly integrates with existing patterns and dependencies.
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

Refer to the `code-review` skill for the deep inspection framework and hygiene check patterns.

```bash
# List comments to ensure resolution
gh api repos/:owner/:repo/pulls/<pr-number>/comments
```

### 3. Agent Delegation

For a comprehensive PR review, delegate specialized reviews to relevant project agents
using the `task` tool to ensure thorough coverage:

- **Architectural Alignment**: Delegate to `cogni-ai-plan-reviewer` to validate structural changes against project patterns.
- **Code Quality**: Delegate to `cogni-ai-code-reviewer` for exhaustive idiomatic inspection and quality enforcement.
- **Security Audit**: Delegate to `cogni-ai-security-auditor` for deep vulnerability tracing and threat modeling.
- **Verification**: Delegate to `cogni-ai-tester` to execute tests and verify edge-case behavior.

### 4. Verification

- Run local tests if applicable.
- Perform a "Design-It-Twice" comparison if the PR implements a complex architectural change.
- Synthesize results from delegated agents (if any) into the final review summary.

## What to Avoid

- **Blanket Approvals**: Never approve without verifying EVERY checkpoint.
- **Ignoring Checks**: Never skip checking the status of CI/CD pipelines.
- **Missing Context**: Always read the PR description and linked issues before reviewing code.

## Related Skills

- **tester**:
  You MUST load this skill when designing or suggesting new tests to cover identified gaps.
- **code-review**:
  You MUST load this skill when performing deep inspection of code changes.
- **gh-pr**:
  You MUST load this skill when working with the `gh pr` command.
- **subagent-task**:
  You MUST load this skill when delegating specialized review tasks to other agents.
