---
name: brainstorm-agent-runs
description: Activate agent-run brainstorming protocol to identify and analyze Cogni AI Agent CI/CD runs via GitHub API for a given Pull Request, avoiding the limitations of gh pr checks.
---

# Skill: brainstorm-agent-runs

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Analyze execution logs of agentic runs in CI/CD pipelines to extract insights about implementation status, challenges, and next steps for a Pull Request.

## Core Process

1. **Trigger Recognition**: Activate when an active Pull Request is associated with the runtime context or the user requests PR analysis.
2. **Identify Runs**: Use the GitHub API to query all runs matching either the PR branch OR title, bypassing `gh pr checks` limitations.
3. **Extract Insights**: Analyze the identified runs (successes, failures, missing facts) without checking detailed logs prematurely.
4. **Visualize**: Generate an `ishikawa-beta` diagram representing the findings.

## Commands / Usage Patterns

List all agent runs for a PR by matching both branch name and PR title:

```bash
branch_name=$(gh pr view <pr_number> --repo <owner>/<repo> --json headRefName -q .headRefName)
pr_title=$(gh pr view <pr_number> --repo <owner>/<repo> --json title -q .title)

gh api repos/<owner>/<repo>/actions/runs --paginate \
  -q ".workflow_runs[] | select((.head_branch == \"$branch_name\" or .display_title == \"$pr_title\") and .name == \"Cogni AI Agent\") | {id: .id, status: .status, conclusion: .conclusion, event: .event}"
```

## Examples

Visualize the identified runs using Mermaid `ishikawa-beta`:

```mermaid
%% This diagram visualizes the identification of agentic runs in the CI/CD pipeline for a PR.
ishikawa-beta
    Cogni AI Agent Runs
    issue_comment
        Agent Run (#<job_id>)
            success
    workflow_dispatch
        Agent Run (#<job_id>)
            failure
            Missing facts
```

## Related Skills

- **brainstorm-github-pr**:
  You MUST load this skill when asked to analyze or brainstorm a Pull Request.
- **mermaid-beta**:
  You MUST load this skill when creating or maintaining experimental Mermaid.js beta diagrams like `ishikawa-beta`.
- **gh-api**:
  You MUST load this skill when executing advanced GitHub CLI API queries.
