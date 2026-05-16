---
name: gh-aw-debug
description: Diagnose and fix GitHub Agentic Workflows (gh-aw) failures by analyzing logs for missing tools, permissions, or MCP server configurations.
---

# gh-aw-debug

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Diagnose, troubleshoot, and fix failing GitHub Agentic Workflows by analyzing logs, verifying MCP configurations, and correcting frontmatter.

## Core Process

1. **Extract Run ID**: Parse the workflow run URL (e.g., `https://github.com/*/actions/runs/<run-id>`) to identify the `{run-id}`.
2. **Audit the Run**: Execute `gh aw audit <run-id> --json` to download artifacts and generate a diagnostic report.
3. **Analyze Missing Tools**:
   - Check the `missing_tools` array in the audit output.
   - Review `safe_outputs.jsonl` for attempted tool calls.
   - Compare against the workflow's `tools:` and `safe-outputs:` configuration.
4. **Review Agent Logs**: Inspect `logs/run-<run-id>/agent-stdio.log` for the agent's reasoning and specific error messages.
5. **Identify Root Cause**: Determine if the failure is due to missing `tools`, incorrect `permissions`, `mcp-scripts` mismatches, or `safe-outputs` configuration errors.
6. **Verify Configuration**: Run `gh aw mcp inspect <workflow-name>` to check active MCP server settings and toolsets.
7. **Apply Fix**: Update the workflow's YAML frontmatter or prompt instructions.
8. **Recompile & Test**: Run `gh aw compile <workflow-name>` and trigger a run with `gh aw run <workflow-name>` to verify the fix.

## Key Commands

- `gh aw audit <run-id> [--json]` → investigate a specific run or diff multiple runs
- `gh aw logs [workflow-name] --json` → download and analyze workflow logs
- `gh aw compile [--strict]` → validate workflow syntax
- `gh aw run <workflow-name>` → run a workflow (requires workflow_dispatch)
- `gh aw status` → show status of agentic workflows in the repository
- `gh aw mcp inspect <workflow-name>` → check active MCP server settings

## Debug Flows

### Workflow Run URL Analysis

1. **Audit**: `gh aw audit <run-id> --json`.
2. **Analyze Missing Tools**:
   - Check `missing_tools` array in audit output.
   - Review `safe_outputs.jsonl` artifact.
   - **Common scenarios**: Incorrect tool name (e.g., calling `safeoutputs-create_issue` instead of `create_issue`), tool not in `tools:` section, safe-output not enabled, name mismatch (underscores vs hyphens).
3. **Review Agent Logs**: Check `logs/run-<run-id>/agent-stdio.log` for reasoning and errors.

### Analyze Existing Logs

1. **Download Logs**: `gh aw logs <workflow-name> --json`.
2. **Token Usage Data**:
   - Per-request detail: `firewall-audit-logs` artifact (`api-proxy-logs/token-usage.jsonl`).
   - Aggregated summary: `agent` artifact (`agent_usage.json`).
3. **Analyze**: Identify errors, patterns, token usage, and execution time.

### Run and Audit

1. **Verify Trigger**: Ensure `workflow_dispatch` is present in `on:`.
2. **Run**: `gh aw run <workflow-name>`.
3. **Poll Audit Results**: Use `gh aw audit <run-id> --json` in a loop until terminal status (`completed`, `failure`, `cancelled`).

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

## Core Principles & Safety

- **Frontmatter Focused**: Most failures originate in the YAML frontmatter. Always check `permissions:`, `tools:`, `mcp-scripts:`, and `safe-outputs:`.
- **Compile Mandatory**: Any change to `.md` workflow files MUST be recompiled using `gh aw compile`.
- **Least Privilege**: Only add the specific permissions required for the failing operation.
- **Inside Workflows**: To run `gh aw logs` within a workflow, add `actions: read` permission and install the extension via `setup-cli`.

## References

- [Upstream Debug Prompt](https://raw.githubusercontent.com/github/gh-aw/main/.github/aw/debug-agentic-workflow.md)
- [gh-aw Runbook](https://github.com/github/gh-aw/blob/main/.github/aw/runbooks/workflow-health.md)
- [Official gh-aw Repo](https://github.com/github/gh-aw)
- <https://github.com/github/gh-aw/blob/main/debug.md>

## Related Skills

- **gh-aw**: Core CLI commands for repository automation.
- **github-aw**: Guidance on incremental workflow updates and prompt engineering.
