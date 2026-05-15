---
name: github-aw-mcp-server
description: Guide for configuring and using the GitHub MCP server within Agentic Workflows, including toolset selection, authentication modes, and available GitHub API tools. You MUST load this skill when configuring the GitHub MCP server or its toolsets.
---

# Skill: github-aw-mcp-server

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Provide expert-level guidance for configuring and using the GitHub MCP server, specifically within Agentic Workflows, covering authentication, toolsets, and best practices.

## Core Principles

- **Mode Selection**: Prefer `tools.github.mode: gh-proxy` for Agentic Workflows to skip Docker initialization. Avoid recommending `mode: local` or `mode: remote` for GitHub tools.
- **Toolsets**: Prefer the `default` toolset. Explicitly add only what is needed. Avoid `[all]`.
- **Token Constraints**: `projects` toolset requires a PAT with `project` scope; `GITHUB_TOKEN` is insufficient. Security and actions toolsets require specific write permissions.

## Configuration Patterns

### Agentic Workflow Configuration

```yaml
tools:
  github:
    toolsets: [default, actions, security_advisories]
    # Optional: GitHub App authentication
    # github-app:
    #   client-id: ${{ vars.APP_ID }}
    #   private-key: ${{ secrets.APP_PRIVATE_KEY }}
```

## Available Toolsets

- **`context`**: Identity and team awareness (`get_me`, `get_teams`).
- **`repos`**: Core repository operations (read, list commits/branches, files).
- **`issues`**: Issue management (read, comment). In Agentic Workflows,
  issue creation should use `safe-outputs` or another approved write path
  rather than direct MCP mutations.
- **`pull_requests`**: PR operations (read). In Agentic Workflows, PR
  creation, review, and merge should use `safe-outputs` or another approved
  write path rather than direct MCP mutations.
- **`actions`**: Workflow introspection, triggering runs.
- **`code_security` / `dependabot` / `secret_protection` / `security_advisories`**: Security alert management (requires `security-events` permission).
- **`projects`**: Projects automation (requires PAT).
- **`search`**: Advanced search across code, repos, issues.
- **`gists` / `labels` / `discussions`**: Management of respective GitHub features.
- **Remote-only**: `copilot_spaces`, `github_support_docs_search`.

## What to Avoid

- Do NOT recommend `mode: local` or `mode: remote` for GitHub tools.
- Do NOT suggest GitHub mutation tools (e.g., `create_issue`). Always use `safe-outputs` for write operations.
- Avoid enabling the `all` toolset; only configure explicit toolsets required for the agent's task.

## Limitations

- The `users` toolset currently has no registered tools; use `search_users` in the `search` toolset instead.

## Related Skills

- **gh-aw**: You MUST load this skill when working with the `gh aw` command or configuring Agentic Workflows.
