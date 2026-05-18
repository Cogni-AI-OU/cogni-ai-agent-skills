---
name: gh-issue
description: >-
  GitHub CLI (`gh issue`) operations for managing, viewing, and editing issues.
  You MUST load this skill when working with the `gh issue` command.
license: MIT
---

# gh-issue Skill

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- You need to create, view, edit, close, or reopen GitHub Issues from the command line or automation.
- You need to list and filter issues by state, label, assignee, or milestone for triage or reporting.
- You need to add comments to an existing issue thread in response to events or user requests.
- You are operating in a GitHub Actions runtime triggered by an `issue_comment` event and need to reply symmetrically.
- You need to bulk-modify issue metadata (labels, assignees, title, body) as part of a workflow.

## When Not to Use
- You need to modify issue templates or issue forms (`.github/ISSUE_TEMPLATE/`) — those are YAML/markdown files, not `gh issue` operations.
- You need to query issues with complex GraphQL joins (e.g., cross-repo searches, deep comment threading) — use **gh-api** for raw GraphQL access.
- You are working with GitHub Discussions — those require `gh api` GraphQL mutations, not `gh issue`.
- You need to perform operations that `gh issue` does not expose as subcommands (e.g., issue transfers, issue pinning) — fall back to **gh-api**.

## Common Pitfalls
- `gh issue create` without `--body-file` or `--body` opens an interactive editor — always provide content explicitly in non-interactive environments.
- When using `--body-file`, write the comment body to a temp file first using your file-writing tools; heredocs in the command can cause shell hangs if truncated.
- Response routing is critical in GitHub Actions: always check `github.event.issue.pull_request` to determine whether to reply via `gh issue comment` or `gh pr comment` — never cross-thread.
- The `--json` flag outputs selected fields only; if a field you need is missing from `gh issue view --json <field>`, you must use `gh api` with a custom GraphQL query instead.

Use `gh issue` to natively interact with GitHub Issues.
Prefer native fields and explicit routing over brittle shell
post-processing.

## Mindmap of Commands

```mermaid
mindmap
  root((gh-issue))
    create
      Create a new issue
    list
      List and filter issues
    view
      View issue details and comments
    edit
      Edit issue title, body, labels, etc.
    comment
      Add a comment to an issue
    close
      Close an issue
    reopen
      Reopen an issue
```

## Advanced Issue Workflows

- **Issue Creation**:
  Always prefer non-interactive creation in automated environments:

  ```bash
  gh issue create --title "bug: unexpected crash" --body-file /tmp/description.md --label "bug" --assignee "@me"
  ```

- **Listing Issues**:
  To quickly identify open issues with specific labels:

  ```bash
  gh issue list --state open --label "bug" --json number,title,createdAt --limit 10
  ```

- **Viewing Issue Details**:
  For quick structured review of an issue without leaving the terminal:

  ```bash
  gh issue view <number> --json title,body,state,labels,assignees,comments
  ```

- **Modifying Issues**:
  Be explicit about the modifications:

  ```bash
  gh issue edit <number> --add-label "in-progress" --add-assignee "@me"
  gh issue close <number> --reason "completed"
  ```

## Interaction & Comments

- For issue thread interactions, use `gh issue comment`.
- For long comments, avoid heredocs as they can cause shell hangs if truncated.
  Write the comment to a temporary file first, then use `--body-file`:

  ```bash
  # Use your file-writing tools to write the comment to /tmp/comment.md, then:
  gh issue comment <number> --body-file /tmp/comment.md
  ```

For high-level issue thread interactions, response routing, and workspace invariants in GitHub Actions,
refer to the **github-issue** skill.

## GitHub Actions Runtime

When executing autonomously within a GitHub Actions environment, adhere strictly to these interaction constraints:

### Response Detection & Routing

Check `github.event_name` and payload to identify trigger source:

- **Issue comment** (`issue_comment`):
  - Condition: `if: ${{ !github.event.issue.pull_request }}`
  - Reply Method: `gh issue comment`
- **General PR comment** (`issue_comment`):
  - Condition: `if: ${{ github.event.issue.pull_request }}`
  - Reply Method: `gh pr comment`

**Routing Invariants**:

- **Symmetric Routing**: ALWAYS reply via the exact originating channel. NEVER cross threads.
- **Direct API Responses ONLY**: Use `gh issue comment` to post directly. NEVER write comment text to files in the
  workspace.
- Parse `github.event.comment.id` to maintain thread continuity.

## Failure Signatures

- **"Could not resolve to an issue"**: Verify the issue number and ensure the repository context is correct.
- **"Permission denied"**: Check `gh auth status`. Ensure the token has `repo` and `issue` scopes.
- **"Issue is locked"**: Some repositories restrict comments on locked issues.

## What to Avoid

- Avoid using `gh api` for issue operations that have native `gh issue` subcommands.
- Do not use `gh issue comment` to provide large code blocks if they can be committed to a branch instead.

## Pre-Completion

Before finishing your session, you MUST ensure the workspace is in a valid state.

### Workspace Cleanliness (Non-Modifying Tasks)

If the runtime did not involve intended modification of files:

1. **Verify**: Run `git status` to confirm the workspace is clean.
2. **Clean**: If untracked or modified files exist (e.g., temporary analysis artifacts), run `git clean -fd` and
   `git checkout -- .`.
3. **Assert**: Ensure no PR or commit is triggered for purely informational tasks.

## Related Skills

- **gh-pr**:
  You MUST load this skill when working with the `gh pr` command.
