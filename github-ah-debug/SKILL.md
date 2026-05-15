---
name: github-ah-debug
description: Debug and refine GitHub Agentic Workflows (gh-aw) by analyzing execution logs, auditing runs, and resolving missing tool errors or prompt inefficiencies. You MUST load this skill when asked to debug, audit, or analyze a failing GitHub Agentic Workflow.
---

# GitHub Agentic Workflow Debugging

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

## References

- <https://github.github.com/gh-aw/troubleshooting/common-issues/>
- <https://github.github.com/gh-aw/troubleshooting/debug-ghe/>
- <https://github.github.com/gh-aw/troubleshooting/debugging/>
- <https://github.github.com/gh-aw/troubleshooting/errors/>

## Related Skills

- **github-ah**:
  You MUST load this skill when safely updating existing GitHub Agentic Workflows configuration.
- **github-actions**:
  You MUST load this skill when diagnosing or debugging GitHub Actions workflow failures.
