---
name: github-mcp-server
description: Guide for configuring and using the GitHub MCP server within Agentic Workflows, including toolset selection, authentication modes, and available GitHub API tools. You MUST load this skill when configuring the GitHub MCP server or its toolsets.
---

# Skill: github-mcp-server

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Provide expert-level guidance for configuring and using the GitHub MCP server, specifically within Agentic Workflows, covering authentication, toolsets, and best practices.

## Core Principles

- **Mode Selection**: Prefer `tools.github.mode: gh-proxy` for Agentic Workflows to skip Docker initialization. Avoid recommending `mode: local` or `mode: remote` for GitHub tools.
- **Toolsets**: Prefer the `default` toolset. Explicitly add only what is needed. Avoid `[all]`.
- **Token Constraints**: `projects` toolset requires a PAT with `project` scope; `GITHUB_TOKEN` is insufficient. Security and actions toolsets require specific write permissions.

## Overview

The GitHub MCP server provides AI agents with programmatic access to GitHub's API through the Model Context Protocol. It supports two modes of operation:

### Local Mode (Docker-based)

- Runs as a Docker container on the GitHub Actions runner
- Uses `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable for authentication
- Configurable toolsets via `GITHUB_TOOLSETS` environment variable
- Supports read-only mode via `GITHUB_READ_ONLY` environment variable

### Remote Mode (Hosted)

- Connects to hosted GitHub MCP server at `https://api.githubcopilot.com/mcp/`
- Uses Bearer token authentication in HTTP headers
- Supports read-only mode via `X-MCP-Readonly` header
- No Docker container required

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
## Configuration

### Basic Configuration

**Local Mode (Docker)**:
```yaml
tools:
  github:
    mode: "local"
    toolsets: [default]  # or [repos, issues, pull_requests]
```

**Remote Mode (Hosted)**:
```yaml
tools:
  github:
    mode: "remote"
    toolsets: [default]  # or [repos, issues, pull_requests]
```

### Read-Only Mode

To restrict the GitHub MCP server to read-only operations:

```yaml
tools:
  github:
    mode: "remote"
    read-only: true
    toolsets: [repos, issues]
```

### Custom Authentication

Use a custom GitHub token instead of the default:

```yaml
tools:
  github:
    mode: "remote"
    github-token: "${{ secrets.CUSTOM_GITHUB_PAT }}"
    toolsets: [repos, issues]
```

## Available Toolsets

The GitHub MCP server organizes tools into logical toolsets. You can enable specific toolsets, use `[default]` for the recommended defaults, or use `[all]` to enable everything.

:::note[Why Use Toolsets?]
The `allowed:` pattern for listing individual GitHub tools is **not recommended for new workflows**. Individual tool names may change between GitHub MCP server versions, but toolsets provide a stable API. Always use `toolsets:` instead. See [Migration from Allowed to Toolsets](#migration-from-allowed-to-toolsets) for guidance on updating existing workflows.
:::

:::tip[Best Practice]
**Always use `toolsets:` for GitHub tools.** Toolsets provide:
- **Stability**: Tool names may change between MCP server versions, but toolsets remain stable
- **Better organization**: Clear groupings of related functionality
- **Complete functionality**: Get all related tools automatically
- **Reduced verbosity**: Cleaner configuration
- **Future-proof**: New tools are automatically included as they're added
:::

### Recommended Default Toolsets

The following toolsets are enabled by default when `toolsets:` is not specified:
- `context` - User and environment context (strongly recommended)
- `repos` - Repository management
- `issues` - Issue management
- `pull_requests` - Pull request operations

**Note**: The `users` toolset is not included by default and must be explicitly specified if needed.

### All Available Toolsets

| Toolset | Description | Common Tools |
|---------|-------------|--------------|
| `context` | User and environment context | `get_teams`, `get_team_members` |
| `repos` | Repository management | `get_repository`, `get_file_contents`, `search_code`, `list_commits` |
| `issues` | Issue management | `issue_read`, `list_issues`, `create_issue`, `search_issues` |
| `pull_requests` | Pull request operations | `pull_request_read`, `list_pull_requests`, `create_pull_request` |
| `actions` | GitHub Actions/CI/CD | `list_workflows`, `list_workflow_runs`, `download_workflow_run_artifact` |
| `code_security` | Code scanning and security | `list_code_scanning_alerts`, `get_code_scanning_alert` |
| `dependabot` | Dependency management | Dependabot alerts and updates |
| `discussions` | GitHub Discussions | `list_discussions`, `create_discussion` |
| `experiments` | Experimental features | Unstable/preview APIs |
| `gists` | Gist operations | `create_gist`, `list_gists` |
| `labels` | Label management | `get_label`, `list_labels`, `create_label` |
| `notifications` | Notifications | `list_notifications`, `mark_notifications_read` |
| `orgs` | Organization management | `get_organization`, `list_organizations` |
| `projects` | GitHub Projects | Project board operations |
| `secret_protection` | Secret scanning | Secret detection and management |
| `security_advisories` | Security advisories | Advisory creation and management |
| `stargazers` | Repository stars | Star-related operations |
| `users` | User profiles | `get_me`, `get_user`, `list_users` |
| `search` | Advanced search | Search across repos, code, users |

## Available Tools by Toolset

This section maps individual tools to their respective toolsets to help with migration from `allowed:` to `toolsets:`.

### Context Toolset
- `get_teams` - List teams the user belongs to
- `get_team_members` - List members of a specific team

### Repos Toolset
- `get_repository` - Get repository information
- `get_file_contents` - Read file contents from repository
- `search_code` - Search code across repositories
- `list_commits` - List commits in a repository
- `get_commit` - Get details of a specific commit
- `get_latest_release` - Get the latest release
- `list_releases` - List all releases

### Issues Toolset
- `issue_read` - Read issue details
- `list_issues` - List issues in a repository
- `create_issue` - Create a new issue
- `update_issue` - Update an existing issue
- `search_issues` - Search issues across repositories
- `add_reaction` - Add reaction to an issue or comment
- `create_issue_comment` - Add a comment to an issue

### Pull Requests Toolset
- `pull_request_read` - Read pull request details
- `list_pull_requests` - List pull requests in a repository
- `get_pull_request` - Get details of a specific pull request
- `create_pull_request` - Create a new pull request
- `search_pull_requests` - Search pull requests across repositories

### Actions Toolset
- `list_workflows` - List GitHub Actions workflows
- `list_workflow_runs` - List workflow runs
- `get_workflow_run` - Get details of a specific workflow run
- `download_workflow_run_artifact` - Download workflow artifacts

### Code Security Toolset
- `list_code_scanning_alerts` - List code scanning alerts
- `get_code_scanning_alert` - Get details of a specific alert
- `create_code_scanning_alert` - Create a code scanning alert

### Discussions Toolset
- `list_discussions` - List discussions in a repository
- `create_discussion` - Create a new discussion

### Labels Toolset
- `get_label` - Get label details
- `list_labels` - List labels in a repository
- `create_label` - Create a new label

### Users Toolset
- `get_me` - Get current authenticated user information
- `get_user` - Get user profile information
- `list_users` - List users

### Notifications Toolset
- `list_notifications` - List user notifications
- `mark_notifications_read` - Mark notifications as read

### Organizations Toolset
- `get_organization` - Get organization details
- `list_organizations` - List organizations

### Gists Toolset
- `create_gist` - Create a new gist
- `list_gists` - List user's gists

## Authentication Details

### Remote Mode Authentication

The remote mode uses Bearer token authentication:

**Headers**:
- `Authorization: Bearer <token>` - Required for authentication
- `X-MCP-Readonly: true` - Optional, enables read-only mode

**Token Source**:
- Default: `${{ secrets.GH_AW_GITHUB_TOKEN }}` or `${{ secrets.GITHUB_TOKEN }}`
- Custom: Configure via `github-token` field

### Local Mode Authentication

The local mode uses environment variables:

**Environment Variables**:
- `GITHUB_PERSONAL_ACCESS_TOKEN` - Required for authentication
- `GITHUB_READ_ONLY=1` - Optional, enables read-only mode
- `GITHUB_TOOLSETS=<comma-separated-list>` - Optional, specifies enabled toolsets

## Best Practices

### Toolset Selection

1. **Start with defaults**: For most workflows, the recommended default toolsets provide sufficient functionality
2. **Enable specific toolsets**: Only enable additional toolsets when you need their specific functionality
3. **Security consideration**: Be mindful of write operations - consider using read-only mode when possible
4. **Performance**: Using fewer toolsets reduces initialization time and memory usage

### Token Permissions

Ensure your GitHub token has appropriate permissions for the toolsets you're enabling:

- `repos` toolsets: Requires repository read/write permissions
- `issues` toolsets: Requires issues read/write permissions
- `pull_requests` toolsets: Requires pull requests read/write permissions
- `actions` toolsets: Requires actions read/write permissions
- `discussions` toolsets: Requires discussions read/write permissions

### Remote vs Local Mode

**Use Remote Mode when**:
- You want faster initialization (no Docker container to start)
- You're running in a GitHub Actions environment with internet access
- You want to use the latest version without specifying Docker image tags

**Use Local Mode when**:
- You need a specific version of the MCP server
- You want to use custom arguments
- You're running in an environment without internet access
- You want to test with a local build of the MCP server

## Migration from Allowed to Toolsets

If you have existing workflows using the `allowed:` pattern, we recommend migrating to `toolsets:` for better maintainability and stability. Individual tool names may change between MCP server versions, but toolsets provide a stable API that won't break your workflows.

### Migration Examples

**Using `allowed:` (not recommended):**
```yaml
tools:
  github:
    allowed:
      - get_repository
      - get_file_contents
      - list_commits
      - list_issues
      - create_issue
      - update_issue
```

**Using `toolsets:` (recommended):**
```yaml
tools:
  github:
    toolsets: [repos, issues]
```

### Tool-to-Toolset Mapping

Use this table to identify which toolset contains the tools you need:

| `allowed:` Tools | Migrate to `toolsets:` |
|------------------|------------------------|
| `get_me` | `users` |
| `get_teams`, `get_team_members` | `context` |
| `get_repository`, `get_file_contents`, `search_code`, `list_commits` | `repos` |
| `issue_read`, `list_issues`, `create_issue`, `update_issue`, `search_issues` | `issues` |
| `pull_request_read`, `list_pull_requests`, `create_pull_request` | `pull_requests` |
| `list_workflows`, `list_workflow_runs`, `get_workflow_run` | `actions` |
| `list_code_scanning_alerts`, `get_code_scanning_alert` | `code_security` |
| `list_discussions`, `create_discussion` | `discussions` |
| `get_label`, `list_labels`, `create_label` | `labels` |
| `get_user`, `list_users` | `users` |
| Mixed repos/issues/PRs tools | `[default]` |
| All tools | `[all]` |

### Quick Migration Steps

1. **Identify tools in use**: Review your current `allowed:` list
2. **Map to toolsets**: Use the table above to find corresponding toolsets
3. **Replace configuration**: Change `allowed:` to `toolsets:`
4. **Test**: Run `gh aw mcp inspect <workflow>` to verify tools are available
5. **Compile**: Run `gh aw compile` to update the lock file

## Using Allowed Pattern with Custom MCP Servers

:::note[When to Use Allowed]
The `allowed:` pattern is appropriate for:
- Custom MCP servers (non-GitHub)
- Gradual migration of existing workflows
- Fine-grained restriction of specific tools within a toolset

For GitHub tools, always use `toolsets:` instead of `allowed:`.
:::

The `allowed:` field can still be used to restrict tools for custom MCP servers:

```yaml
mcp-servers:
  notion:
    container: "mcp/notion"
    allowed: ["search_pages", "get_page"]  # Fine for custom MCP servers
```

For GitHub tools, `allowed:` can be combined with `toolsets:` to further restrict access, but this pattern is not recommended for new workflows.

## GitHub API Limitations

Not all GitHub data is accessible through the GitHub MCP server or the GitHub REST API. Be aware of these limitations when designing workflows to avoid silent failures or incomplete results at runtime.

### Billing and Cost Data

**❌ Not available via standard API permissions:**

- **Detailed per-run cost data** — GitHub Actions does not expose per-workflow-run billing costs through the REST API. There is no endpoint to retrieve the exact cost of a specific workflow run.
- **Actions billing summary** — Billing endpoints (e.g., `/orgs/{org}/settings/billing/actions`) require `admin:org` scope, which is **not** granted by `actions:read` or the default `GITHUB_TOKEN`.

**⚠️ When suggesting billing/cost workflows, always note:**

> Detailed GitHub Actions billing and cost data is not accessible through the standard GitHub API with `actions:read` permissions. Workflows that attempt to read per-run cost data or billing summaries will fail silently or return empty results unless an `admin:org`-scoped personal access token is explicitly configured.

**✅ Alternatives for cost reporting:**

1. **GitHub Actions usage reports** — Download usage reports from the GitHub billing UI (Settings → Billing → Usage) or via the billing CSV export endpoint (requires `admin:org` scope with a PAT).
2. **Billing settings UI** — Direct users to `https://github.com/organizations/{org}/settings/billing` or `https://github.com/settings/billing` for personal accounts to view cost data manually.
3. **Workflow run metadata** — Use `list_workflow_runs` and `get_workflow_run` (available via `actions` toolset) to get run duration, status, and timing — but not dollar costs.
4. **Third-party cost tracking** — Integrate with third-party CI cost tools that use pre-authorized API access.

### Cross-Organization Data Access

**❌ Not available without explicit authorization:**

- Workflows can only access data from repositories and organizations that the configured GitHub token has been granted access to.
- Cross-organization repository reads require a PAT or GitHub App token with access to the target org — the default `GITHUB_TOKEN` is scoped to the current repository's organization only.
- Organization membership and team data from *other* organizations is not accessible without explicit `read:org` permissions on those organizations.

### Organization Membership and Private Data

**❌ Requires additional scopes:**

- **Organization member lists** — Reading private organization membership requires `read:org` scope; the default `GITHUB_TOKEN` only exposes public membership.
- **Private repository contents** — Only accessible if the token has explicit repository access.
- **Secret values** — GitHub Secrets are write-only through the API; their values cannot be read back after creation.

### Rate Limits

**⚠️ Be aware of API rate limits:**

- The GitHub REST API enforces rate limits (typically 5,000 requests/hour for authenticated requests with a PAT, lower for `GITHUB_TOKEN`).
- Workflows that perform bulk data collection (e.g., listing all workflow runs across many repositories) may hit rate limits. Design workflows to paginate carefully and avoid unnecessary requests.
- GraphQL API has separate rate limits based on query complexity.

## Troubleshooting

### Common Issues

**Issue**: Tool not found or not available
- **Solution**: Check if you're using `allowed:` to restrict tools. Consider using `toolsets:` instead to get all related tools.
- **Verify**: Run `gh aw mcp inspect <workflow-name>` to see which tools are actually available.

**Issue**: Missing functionality after specifying toolset
- **Cause**: Using a too-narrow toolset that doesn't include all needed tools
- **Solution**: Either add additional toolsets (e.g., `toolsets: [default, actions]`) or use `[all]` for full access

**Issue**: Workflow using `allowed:` list is verbose and hard to maintain
- **Solution**: Migrate to `toolsets:` configuration using the migration guide above

### Best Practices for Debugging

1. **Start with `[default]` toolset**: Most workflows work well with default toolsets
2. **Add specific toolsets as needed**: Incrementally add toolsets like `actions`, `discussions`, etc.
3. **Use `gh aw mcp inspect`**: Verify which tools are actually available
4. **Check tool-to-toolset mapping**: Reference the tables above to find the right toolset

## What to Avoid

- Do NOT recommend `mode: local` or `mode: remote` for GitHub tools.
- Do NOT suggest GitHub mutation tools (e.g., `create_issue`). Always use `safe-outputs` for write operations.
- Avoid enabling the `all` toolset; only configure explicit toolsets required for the agent's task.

## Limitations

- The `users` toolset currently has no registered tools; use `search_users` in the `search` toolset instead.

## References

- <https://github.com/github/gh-aw/blob/main/.github/skills/github-mcp-server/SKILL.md> - for up-to-date MCP Tool list
- [GitHub MCP Server Repository](https://github.com/github/github-mcp-server)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [GitHub Actions Documentation](https://docs.github.com/actions)

**Cross-Reference Toolset Source Files in github-mcp-server**:

- For each toolset, identify the corresponding source file in the [github/github-mcp-server](https://github.com/github/github-mcp-server) repository
- Use the following mapping as a starting point (verify and update based on actual repo contents):
     - `actions` → [`pkg/github/actions.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/actions.go)
     - `code_security` → [`pkg/github/code_scanning.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/code_scanning.go)
     - `context` → [`pkg/github/context_tools.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/context_tools.go)
     - `dependabot` → [`pkg/github/dependabot.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/dependabot.go)
     - `discussions` → [`pkg/github/discussions.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/discussions.go)
     - `experiments` → [`pkg/github/dynamic_tools.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/dynamic_tools.go)
     - `gists` → [`pkg/github/gists.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/gists.go)
     - `issues` → [`pkg/github/issues.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/issues.go)
     - `labels` → [`pkg/github/labels.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/labels.go)
     - `notifications` → [`pkg/github/notifications.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/notifications.go)
     - `orgs` → [`pkg/github/search.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/search.go)
       (primary: `search_orgs`; note that `list_org_repository_security_advisories`
       also uses this toolset but is defined in [`security_advisories.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/security_advisories.go))
     - `projects` → [`pkg/github/projects.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/projects.go)
     - `pull_requests` → [`pkg/github/pullrequests.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/pullrequests.go)
     - `repos` → [`pkg/github/repositories.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/repositories.go)
     - `search` → [`pkg/github/search.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/search.go)
     - `secret_protection` → [`pkg/github/secret_scanning.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/secret_scanning.go)
     - `security_advisories` → [`pkg/github/security_advisories.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/security_advisories.go)
     - `stargazers` → [`pkg/github/repositories.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/repositories.go)
     - `users` → [`pkg/github/search.go`](https://github.com/github/github-mcp-server/blob/main/pkg/github/search.go) (for `search_users`)

## Related Skills

- **gh-aw**: You MUST load this skill when working with the `gh aw` command or configuring Agentic Workflows.
- **gh-aw-debug**: Diagnose, troubleshoot, and fix failing GitHub Agentic Workflows
