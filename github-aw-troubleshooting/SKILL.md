---
name: github-aw-troubleshooting
description: Debug and refine GitHub Agentic Workflows (gh-aw) by analyzing execution logs, auditing runs, and resolving missing tool errors or prompt inefficiencies. You MUST load this skill when asked to debug, audit, or analyze a failing GitHub Agentic Workflow.
license: MIT
---

# GitHub Agentic Workflow Troubleshooting

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Debug and refine agentic workflows using `gh-aw` CLI tools or the `agentic-workflows` tool to analyze logs, audit runs, and improve workflow performance.

## Core Process

1. **Identify Workflow**: Discover the workflow via `gh aw status` or user-provided run URL.
2. **Audit Run**: Execute `gh aw audit <run-id> --json` (or the `audit` tool) to download artifacts, check metrics, and identify missing tools.
3. **Analyze Logs**: Use `gh aw logs <workflow-name> --json` to download and evaluate past runs, identifying performance, token, or failure patterns.
4. **Fix Misconfigurations**: Correct `tools:`, `safe-outputs:`, or prompt syntax based on audit results.
5. **Compile & Validate**: Verify changes with `gh aw compile <workflow-name>`.

## Core Principles

- **Rely on Audit Artifacts**: Always inspect the `missing_tools` array and `safe_outputs.jsonl` to detect misconfigured or mistyped tool names.
- **Differentiate Token Logs**: Find per-API-request token details in the `firewall-audit-logs` artifact (`api-proxy-logs/token-usage.jsonl`), and aggregated totals in `agent_usage.json`.
- **Compile After Editing**: Ensure every configuration or prompt fix is strictly validated by running `gh aw compile <workflow-name>`.
- **Alternative Tools**: When `gh aw` is unauthenticated or unavailable, use the built-in `agentic-workflows` tools (e.g., `audit`, `logs`, `status`, `compile`).

## Commands / Usage Patterns

- **Audit a Run**: `gh aw audit <run-id> --json`
- **Diff Runs (Regression)**: `gh aw audit <base-run-id> <compare-run-id> --json`
- **Analyze Logs**: `gh aw logs <workflow-name> --json`
- **Trigger a Run**: `gh aw run <workflow-name>`
- **Check Workflow Status**: `gh aw status`
- **Validate Fixes**: `gh aw compile <workflow-name>`
- **Strict Validation**: `gh aw compile <workflow-name> --strict`
- **Check Run Annotations**: `gh run view <run-id>`
- **Inspect Specific Job Log**: `gh run view --job <job-id> --log`

## Diagnostics and Troubleshooting

- **Missing Tools**: The agent calls `safeoutputs-<name>` instead of `<name>` or tries to use tools not listed in `tools:` / `safe-outputs:`. Update the workflow prompt or frontmatter.
- **In-Progress Runs**: If `gh aw audit` returns `"status": "in_progress"`, poll every ~45 seconds until terminal status (`completed`, `failure`, `cancelled`).
- **Timeouts**: Workflows exceeding `timeout-minutes`. Increase timeout, optimize prompt, or add concurrency controls.
- **Network Issues**: Blocked domains in `network:` allowlist. Update `network:` configuration with required domains.
- **GitHub Action Cancellation**: If a maintainer cancels a run, artifacts may be missing. Check `gh run view <run-id>` and re-run instead of searching for non-existent files.
- **Workflow Setup**: Steps using `gh aw` within workflows require `actions: read` permissions and prior installation via `github/gh-aw/actions/setup-cli`.

### Required Secrets

The GitHub Copilot CLI engine requires the corresponding secrets to be configured.

Common causes if the secret appears to be configured:
- Organization secrets must have repository access granted
- Environment secrets require the job to specify that environment
- Secret names are case-sensitive - verify exact spelling

Refs: <https://github.github.com/gh-aw/reference/auth/>

## What to Avoid

- Looking for per-request token usage in `agent_usage.json` (it only contains aggregated totals).
- Modifying workflow files without running `gh aw compile` afterward.
- Spamming the API with rapid polling loops; use a sleep interval when waiting for runs to finish.

## Limitations

- `gh aw` commands may require `actions: read` permissions when used inside GitHub Actions workflows.
- Cannot debug local scripts unrelated to GitHub Agentic Workflows via `gh aw` tooling.

## Common Issues

Frequently encountered issues when working with GitHub Agentic Workflows and their solutions:

- **Extension Installation Fails**: If `gh extension install github/gh-aw` fails, use the standalone installer: `curl -sL https://raw.githubusercontent.com/github/gh-aw/main/install-gh-aw.sh | bash`.
- **Custom Actions Not Allowed**: Enterprise policies may restrict `github/gh-aw/actions/setup-cli`. An admin must allow `github/gh-aw@*` in Organization Settings -> Actions -> Policies.
- **Frontmatter Silently Ignored**: The compiler does not warn about unknown field names. Check for typos: `agent:` (use `engine:`), `mcp-servers:` (use `tools:`), `timeout:` (use `timeout-minutes:`).
- **Write Operations Fail**: All writes (issues, comments, PRs) must be declared in `safe-outputs`. If `create-issue` is not working, check if `staged: true` is blocking it (set to `false` for immediate creation).

## Debugging GHE Cloud with Data Residency

Step-by-step guide for setting up and debugging agentic workflows on GitHub Enterprise Cloud with data residency (*.ghe.com):

1. **Configure Engine (Critical)**: Set `api-target` in frontmatter to point to your enterprise's Copilot API subdomain:
    ```yaml
    engine:
      id: "copilot"
      api-target: "copilot-api.yourorg.ghe.com"
    ```
2. **Authenticate CLI**: Use `GH_HOST=yourorg.ghe.com gh auth login` to target the correct instance.
3. **Compile with Host**: Always use `GH_HOST=yourorg.ghe.com gh aw compile <workflow>` to ensure the correct domains are auto-added to the firewall allow-list.
4. **Local Diagnostic**: Launch `GH_HOST=yourorg.ghe.com copilot` and use `/agent agentic-workflows` to test authentication and run audits from your machine.

## Debugging Workflows

How to run, debug, and investigate agentic workflow failures using the Copilot CLI, `gh aw audit`, and log analysis:

- **AI-Assisted Debugging (Recommended)**: Launch the Copilot CLI (`copilot`), load the `agentic-workflows` agent with `/agent`, and ask: `Debug this workflow run: <RUN_URL>`.
- **Comprehensive Audit**: Run `gh aw audit <run-id> --parse` to get a structured markdown report including failure analysis, tool usage, MCP status, and firewall denials.
- **Multi-Run Analysis**: Use `gh aw logs <workflow-name> --firewall --safe-output` to identify recurring network blocks or behavioral patterns across multiple runs.
- **Verbose Logging**: Set `DEBUG=*` for CLI commands to see internal processing logs. In GitHub Actions, set the repository secret `ACTIONS_STEP_DEBUG=true` for detailed step-level logs.
- **Inspect Artifacts**: Download run artifacts to find `prompt.txt` (the exact prompt sent to the AI), `agent-stdio.log` (raw interaction logs), and `firewall-logs/access.log`.

## Error Reference

Comprehensive reference of common error messages in GitHub Agentic Workflows:

- **`frontmatter not properly closed`**: Missing the closing `---` delimiter at the end of the YAML section.
- **`Authentication failed` / `403 unauthorized`**: The `COPILOT_GITHUB_TOKEN` is invalid or the account lacks a Copilot license seat.
- **`DENIED CONNECT <domain>:443`**: The firewall blocked a network request. Add the domain or ecosystem shorthand (e.g., `node`, `python`) to `network: allowed:`.
- **`cannot use 'command' with 'issues'`**: Conflicting triggers detected. The `command:` configuration handles issue/PR events automatically; remove the redundant `on: issues` block.
- **`strict mode: wildcard '*' is not allowed`**: Public repositories require strict mode, which forbids standalone wildcards in network configuration. Use specific domains or patterns (e.g., `*.github.com`).
- **`tool <name> missing required 'url' field`**: HTTP MCP server configuration is incomplete. Add the `url:` field.

## Troubleshooting Tips

- Use `--verbose` flag for detailed error information
- Validate YAML syntax and check file paths
- Consult the frontmatter reference.
- Run `gh aw compile` frequently to catch errors early
- Use `--strict` flag to catch security issues early
- Test incrementally: add one feature at a time

## References

- [Common Issues](https://github.com/github/gh-aw/blob/v0.74.3/docs/src/content/docs/troubleshooting/common-issues.md)
- [Debugging GHE Cloud with Data Residency](https://github.com/github/gh-aw/blob/v0.74.3/docs/src/content/docs/troubleshooting/debug-ghe.md)
- [Debugging Workflows](https://github.com/github/gh-aw/blob/v0.74.3/docs/src/content/docs/troubleshooting/debugging.md)
- [Error Reference](https://github.com/github/gh-aw/blob/v0.74.3/docs/src/content/docs/troubleshooting/errors.md)
- [Frontmatter reference](https://github.com/github/gh-aw/blob/v0.74.3/docs/src/content/docs/reference/frontmatter.md)
- [Troubleshooting](https://github.com/github/gh-aw/tree/v0.74.3/docs/src/content/docs/troubleshooting)

## Related Skills

- **github-aw**:
  You MUST load this skill when safely updating existing GitHub Agentic Workflows configuration.
- **github-actions**:
  You MUST load this skill when diagnosing or debugging GitHub Actions workflow failures.
