---
name: gh-aw-debug
description: Diagnose and fix GitHub Agentic Workflows (gh-aw) failures by analyzing logs for missing tools, permissions, or MCP server configurations.
---

# gh-aw-debug

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Diagnose, troubleshoot, and fix failing GitHub Agentic Workflows by analyzing logs, verifying MCP configurations, and correcting frontmatter.

## Core Process

1. **Analyze Logs**: Use `gh aw logs --run-id <run-id>` to identify error patterns (e.g., "missing-tool" or HTTP 403).
2. **Identify Root Cause**: Determine if failure is due to missing `tools`, `permissions`, `mcp-scripts`, or `safe-outputs`.
3. **Verify Configuration**: Run `gh aw mcp inspect <workflow-name>` to check active MCP server settings.
4. **Apply Fix**: Update the workflow's YAML frontmatter.
5. **Recompile & Test**: Run `gh aw compile <workflow-name>.md` and trigger a run to verify.

## Core Principles & Safety

- **Frontmatter Focused**: Most failures originate in the YAML frontmatter. Always check `permissions:`, `tools:`, `mcp-scripts:`, and `safe-outputs:`.
- **Compile Mandatory**: Any change to `.md` workflow files MUST be recompiled using `gh aw compile`.
- **Least Privilege**: Only add the specific permissions required for the failing operation.
- **Inside Workflows**: To run `gh aw logs` within a workflow, add `actions: read` permission and install the extension via `setup-cli`.

## Commands / Usage Patterns

### Diagnostics

```bash
# Download logs for a specific run or workflow
gh aw logs --run-id <run-id> -o /tmp/logs
gh aw logs --workflow <workflow-name> --start-date -1d

# Audit a specific workflow run (detailed analysis with missing tools and errors)
gh aw audit <run-id> --json

# Diff two runs to detect regressions (firewall, MCP, metrics)
gh aw audit <base-run-id> <compare-run-id> --json

# Show status of all workflows
gh aw status

# Inspect MCP configuration
gh aw mcp inspect <workflow-name>
gh aw mcp list
```

### Verification

```bash
gh aw compile <workflow-name>.md
# Validate workflow with strict security checks
gh aw compile --strict <workflow-name>.md
gh workflow run <workflow-name>.lock.yml
gh run watch <run-id>
```

## Common Failure & Fix Patterns

### Missing Tools (e.g., "Tool 'github:read_issue' not found")

Add the missing MCP server to `tools:`:
```aw
tools:
  github:
    toolsets: [default]
```

### Permission Errors (e.g., HTTP 403 or "Resource not accessible")

Prefer `read` permissions combined with `safe-outputs` for mutations. Use `write` only if `safe-outputs` is not supported for the task:
```aw
permissions:
  issues: read

safe-outputs:
  jobs:
    create-issue:
      labels: ["bug"]
```

### MCP Scripts & Safe-Outputs

Fix "missing tool configuration for mcpscripts-gh" or resource creation failures:
```aw
mcp-scripts:
  issue:
    number: ${{ github.event.issue.number }}
    title: ${{ github.event.issue.title }}

safe-outputs:
  jobs:
    create-issue:
      labels: ["ai-generated"]
```

## Investigation Steps

1. **Verify Version**: Run `gh extension list | grep 'github/gh-aw'` to retrieve the installed `gh aw` version, then ensure it is not in the retired range `[0.68.4, 0.71.3]`. If it is, run `gh extension upgrade aw`.
2. **Check Logs**: Look for `Error: Tool '...' not found` or `Error: 403`. Use `gh aw audit <run-id> --json` for detailed insights.
3. **Inspect MCP**: Ensure `gh aw mcp inspect` shows the expected toolsets.
4. **Validate Triggers**: Ensure `mcp-scripts` maps the correct event payload fields.
5. **Check Recompilation**: Verify the `.lock.yml` timestamp matches your last edit.

## Case Study: Triage Workflow Fix

**Problem**: Workflow failed to label issues with "Tool not found".
**Diagnosis**: `gh aw logs` showed `github:add_labels` missing. `gh aw mcp inspect` showed no `github` tool.
**Fix**: Added `tools.github.toolsets: [default]`, set `permissions.issues: read`, and added a `safe-outputs.jobs` entry for labeling, then recompiled.

## What to Avoid

- Blindly adding `permissions: write-all` or `write` scopes when `safe-outputs` is supported.
- Forgetting to `gh aw compile` after frontmatter edits.
- Using `gh aw logs` inside a workflow without `actions: read` permission.

## References

- [gh-aw Runbook](https://github.com/github/gh-aw/blob/main/.github/aw/runbooks/workflow-health.md)
- [Official gh-aw Repo](https://github.com/github/gh-aw)
- <https://github.com/github/gh-aw/blob/main/debug.md>

## Related Skills

- **gh-aw**: Core CLI commands for repository automation.
- **github-ah**: Guidance on incremental workflow updates and prompt engineering.
