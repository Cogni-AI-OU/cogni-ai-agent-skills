---
name: gh-aw-debug
description: Diagnose and fix GitHub Agentic Workflows (gh-aw) failures by analyzing logs for missing tools, permissions, or MCP server configurations.
---

# gh-aw-debug

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Diagnose, troubleshoot, and fix failing GitHub Agentic Workflows by analyzing logs, verifying MCP configurations, and correcting frontmatter configurations.

## Core Process

1. **Analyze Logs**: Use `gh aw logs` to identify error patterns (e.g., "missing-tool", "Tool not found", or HTTP 403 errors).
2. **Identify Root Cause**: Determine if the failure is due to missing MCP toolsets, missing permissions, or missing `mcp-scripts`/`safe-outputs` configuration.
3. **Verify Configuration**: Use `gh aw mcp inspect <workflow-name>` to check the current MCP server configuration.
4. **Apply Fix**: Update the workflow's YAML frontmatter to include missing `tools:`, `permissions:`, `mcp-scripts:`, or `safe-outputs:`.
5. **Recompile and Test**: Compile the updated workflow and trigger a manual run to verify the fix.

## Core Principles

- **Frontmatter Focused**: Most workflow failures originate from missing configurations in the YAML frontmatter. Check `permissions:`, `tools:`, `mcp-scripts:`, and `safe-outputs:`.
- **Compile After Changes**: Any changes to `.md` workflow files MUST be recompiled using `gh aw compile <workflow-name>.md` to generate the updated `.lock.yml`.
- **Agent Logs**: Local investigation requires `actions: read` permission and the `setup-cli` action if running from within a generated workflow.

## Commands / Usage Patterns

### Log Analysis

```bash
gh aw logs --start-date -1d -o /tmp/workflow-logs
gh aw logs --run-id <run-id> -o /tmp/workflow-logs
gh aw logs --workflow <workflow-name> --start-date -7d
```

### MCP Inspection

```bash
gh aw mcp inspect <workflow-name>
gh aw mcp list
```

### Testing Fixes

```bash
gh aw compile <workflow-name>.md
gh workflow run <workflow-name>.lock.yml
gh run list --workflow=<workflow-name>.lock.yml --limit 1
gh run watch <run-id>
```

## Common Fix Patterns

**Missing GitHub MCP Server** (fixes "missing-tool" or "Tool not found"):
```aw
tools:
  github:
    toolsets: [default]
```

**Missing Permissions** (fixes HTTP 403 or "Resource not accessible"):
```aw
permissions:
  contents: read
  issues: write
  pull-requests: write
  actions: read
```

**Missing MCP Scripts** (fixes "missing tool configuration for mcpscripts-gh"):
```aw
mcp-scripts:
  issue:
    title: ${{ github.event.issue.title }}
    body: ${{ github.event.issue.body }}
```

**Missing Safe Outputs** (fixes failures when agent tries to create resources):
```aw
safe-outputs:
  create-issue:
    labels: ["ai-generated"]
```

## What to Avoid

- Running `gh aw logs` inside a generated workflow without ensuring the agent has `actions: read` permission.
- Trying to fix missing tool errors without recompiling the workflow file.
- Blindly adding all permissions; only add scopes required for the specific operations failing.

## Limitations

- Fixing workflow logic inside the agent prompt won't resolve frontmatter-level missing tool or permission errors.

## Related Skills

- **gh-aw**:
  You MUST load this skill when working with the `gh aw` command for general repository automation.
- **github-ah**:
  You MUST load this skill when distinguishing between frontmatter configuration that requires recompilation and markdown body prompt edits.
