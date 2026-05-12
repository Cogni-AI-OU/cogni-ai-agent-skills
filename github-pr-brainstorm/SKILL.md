---
name: github-pr-brainstorm
description: Activate PR brainstorming protocol to analyze and visualize commit history, review threads, and CI pipeline checks using Mermaid diagrams.
---

# Skill github-pr-brainstorm

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Analyze and visualize GitHub Pull Requests by mapping commit history, reviewer feedback, and CI/CD status into structured Mermaid diagrams to establish context before deep analysis.

## Core Process

1. **Commit History Visualization**: Map out the historical context of the PR by generating a list of commits into a Mermaid `gitGraph` diagram.
2. **PR Review Kanban Diagram**: Map active, outdated, and resolved review threads or comments into a Mermaid `kanban` diagram.
3. **CI Checks State Visualization**: Visualize the current state of Continuous Integration (CI) checks (passing, failing, pending) using a Mermaid `flowchart` diagram.
4. **CI Failures Summarization**: Categorize and summarize the root causes and affected jobs of any CI failures using a Mermaid `ishikawa-beta` diagram.

## Core Principles

- **Visual State Mapping**: Always translate raw PR data (commits, reviews, checks) into Mermaid diagrams before diving into code or detailed logs.
- **Progressive Disclosure**: Map high-level structure (commits, reviews, pipeline topology) first, then drill down into detailed logs only if needed.
- **Native Tooling**: Rely on native CLI commands like `gh pr view`, `gh pr checks`, `gh run view`, and `gh api graphql` for fast data extraction.

## Commands / Usage Patterns

**Extract Commit History:**

```bash
gh pr view <pr_number> --json baseRefName,headRefName,commits
```

*Use output to map the structural history into a `gitGraph` diagram before deep fact-finding.*

**Extract Review Threads:**

```bash
gh api graphql -F owner="<owner>" -F repo="<repo>" -F number=<pr_number> -f query='
  query($owner: String!, $repo: String!, $number: Int!) {
    repository(owner: $owner, name: $repo) {
      pullRequest(number: $number) {
        reviewThreads(first: 100) { nodes { isResolved comments(first: 1) { nodes { body } } } }
      }
    }
  }'
```

*Use output to populate a `kanban` diagram tracking Active, Outdated, and Resolved issues.*

**Extract CI Checks State:**

```bash
gh pr checks <pr_number> --repo <owner>/<repo>
```

*Use output to build a `flowchart` categorized by check states (pass, fail, pending).*

**Summarize CI Failures:**

```bash
gh run view --job <run_id>
```

*Use output to create an `ishikawa-beta` diagram grouping failures by logical categories and root causes.*

## What to Avoid

- Diving into detailed job logs or codebase checks before visualizing the overall CI state and PR history.
- Attempting to map commit history without identifying the base and head branch structure.
- Rendering diagrams that include invalid Mermaid syntax or overly complex elements that break rendering.

## Related Skills

- **gh**: You MUST load this skill when executing standard `gh` CLI commands.
- **gh-api**: You MUST load this skill when executing `gh api` queries.
- **gh-models**: You MUST load this skill when running and evaluating AI models.
- **gh-pr**: You MUST load this skill for Pull Request operations and metadata.
- **gh-run**: You MUST load this skill when extracting workflow run and job details.
- **git**: You MUST load this skill when executing native git operations.
- **mermaid**: You MUST load this skill when constructing `gitGraph`, `kanban`, and `flowchart` diagrams.
- **mermaid-beta**: You MUST load this skill when building `ishikawa-beta` diagrams.
