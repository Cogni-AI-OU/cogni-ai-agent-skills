---
name: github-pr-review
license: MIT
description: >-
  Comprehensive PR review workflow for verifying code quality, metadata accuracy, and merge readiness.
  You MUST load this skill when reviewing, auditing, or verifying a GitHub Pull Request.
license: MIT
---

# GitHub PR Review

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- A user explicitly asks you to review, audit, or verify a GitHub Pull Request.
- Performing a pre-merge quality gate to ensure the PR meets code quality, testing, and metadata standards.
- Reviewing a complex PR that benefits from delegated reviews (architectural, security, testing).
- Ensuring PR title follows Conventional Commits and description accurately reflects all changes.
- Checking build/CI status and mergeability before approving or requesting changes.
- The PR review is part of a CI/CD pipeline gate before merging is permitted.

## When Not to Use
- The user simply needs to comment on or reply to a PR thread without a full review — load `github-pr` for lightweight PR interactions.
- The task involves making code changes to the PR branch — this skill is for review/audit only, not implementation.
- The user needs general GitHub Actions troubleshooting (load `github-actions`) or workflow run analysis (load `gh-run`).
- The changes are trivial (typo fix, dependency bump) that don't warrant deep architectural or security review.

## Common Pitfalls
- Never approve a PR without verifying EVERY checkpoint — blanket approvals bypass critical quality gates and erode trust in the review process.
- Always read the PR description AND linked issues before reviewing code — reviewing in isolation misses context, design decisions, and trade-offs documented elsewhere.
- Delegated reviews via `task` tool run asynchronously; you MUST synthesize results from all sub-agents into a single coherent review summary — don't post multiple disjointed reviews.
- CI/CD checks may be pending or in-progress — wait for them to complete (using `gh run watch` if needed) rather than approving before verification.
- The `code-review` skill provides the deep inspection framework — this skill orchestrates the full review workflow, but the actual code-level analysis uses the cognitive framework from `code-review`.

Elite autonomous PR review workflow for ensuring structural integrity, metadata accuracy, and zero-defect deployments.

## Core Review Checkpoints

Execute these checks systematically using `gh` and `git` tools:

- **Discovery & Scope Alignment**:
  - **Intent & Purpose**: Verify the PR clearly articulates the WHY (goals/user value),
    WHAT (scope/deliverables), and HOW (implementation strategy).
  - **Branch State**: Verify if the PR branch is up-to-date with the base branch.
  - **Comments Resolution**: Check for any existing unresolved comments or threads on the PR to ensure previous feedback
    has been integrated.
  - **Metadata Accuracy**: Ensure PR Title follows Conventional Commits and Description accurately reflects all changes.
- **Deep Code Inspection**:
  - **Inspection Framework**: Apply the `code-review` skill's cognitive framework to evaluate code quality dimensions.
  - **Atomic File Analysis**: Step through the diff file-by-file or component-by-component.
  - **Hygiene & Style**: Check for trailing whitespace, debugger statements, and other hygiene issues.
  - **Scope Control**: Ensure the PR does strictly what it claims. Flag any drive-by changes or unrelated refactoring.
  - **Overengineering Check**: Aggressively apply YAGNI. Question "nice to have" features,
    premature optimizations, and abstractions that exceed core requirements.
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

# Check for trailing whitespace and conflict markers in the diff
git diff <base-branch>...HEAD --check
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

- **critical-thinking**:
  You MUST load this skill when applying deep analytical reasoning to complex changes.
- **tester**:
  You MUST load this skill when designing or suggesting new tests to cover identified gaps.
- **code-review**:
  You MUST load this skill when performing deep inspection of code changes.
- **gh-pr**:
  You MUST load this skill when working with the `gh pr` command.
- **subagent-task**:
  You MUST load this skill when delegating specialized review tasks to other agents.
