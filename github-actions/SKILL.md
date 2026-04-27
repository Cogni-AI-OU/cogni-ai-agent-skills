---
name: github-actions
description: >-
  Diagnose GitHub Actions workflow failures by retrieving run statuses and logs using MCP tools or gh CLI.

  Maintained at: <https://github.com/Cogni-AI-OU/cogni-ai-agent-skills>
license: MIT
---
<!-- markdownlint-disable MD003 MD013 MD022 MD023 MD026 MD031 MD032 MD041 -->
This skill enables autonomous diagnosis of GitHub Actions failures, preferring MCP tools for summaries and falling back to gh CLI.

## When to Activate

- Agent needs to identify or fix a workflow failure
- Error output references Actions job steps
- Pull request shows failed Actions checks
- User provides a GitHub Actions URL (e.g., `https://github.com/owner/repo/actions/runs/RUN_ID/job/JOB_ID`)
- User reports a failing GitHub Actions workflow, CI failure, or red status check

## Step-by-Step Process

1. Extract IDs from GitHub Actions URL if provided.

   If user provides a URL like `https://github.com/owner/repo/actions/runs/RUN_ID/job/JOB_ID`:
   - Extract `RUN_ID` (numeric) from the URL path
   - Extract `JOB_ID` (numeric) if present in the URL
   - Skip to step 2 with these IDs ready to use

2. Detect available tools for diagnosis.

   First, check for gh CLI: run_in_terminal `gh --version`.
   If successful, verify access: run_in_terminal `gh auth status`.
   Prioritize MCP tools (e.g., `list_workflow_runs`, `get_job_logs`) if present — they provide the most token-efficient access.
   If neither MCP nor authenticated gh is available, respond: 'Automated retrieval of workflow logs is not possible in this environment. Please share the workflow run URL, specific error messages, or screenshots for diagnosis.'

3. Preferred path: Use MCP tools (if available).

   **If you have RUN_ID and JOB_ID from URL:**
   - Use `github-mcp-server-actions_get` with method `get_workflow_job` and `resource_id=JOB_ID` to get job details
   - Use `github-mcp-server-get_job_logs` with `job_id=JOB_ID`, `return_content=true`, and `tail_lines=100` (or more) to retrieve logs
   - Parse logs for failing step, command, and error message

   **If you only have RUN_ID or need to find failures:**
   - Use `github-mcp-server-actions_get` with method `get_workflow_run` and `resource_id=RUN_ID` to get run details
   - Use `github-mcp-server-actions_list` with method `list_workflow_jobs` and `resource_id=RUN_ID` to list all jobs
   - Identify failed jobs (`conclusion: "failure"`) and note their `job_id`
   - Use `github-mcp-server-get_job_logs` for each failed job

   **If you need to find recent runs:**
   - Use `github-mcp-server-actions_list` with method `list_workflow_runs` and filters (current branch, PR number, or workflow name)
   - Identify failed runs (`conclusion: "failure"`). Note the latest `run_id`
   - Follow steps above to get job details and logs

4. Fallback path: Use gh CLI (if available and authenticated).

   - Run_in_terminal `gh run list --limit 20 --json databaseId,name,status,conclusion,url`.
   - Inspect run metadata first; do not assume pathological sessions conclude with `failure`.
   - Use `gh run view <run_id> --log-failed` only when the relevant run or job actually concluded with failure.
   - For job metadata, prefer `gh api repos/<owner>/<repo>/actions/jobs/<job_id>` over shell pipelines.
   - If `gh run view ... --log` returns empty output or `gh api .../logs` returns a signed-blob `403`, classify it as `LOG_ACCESS_UNSUPPORTED` and pivot instead of retrying the same command shape.
   - In restricted shells, prefer `gh --json/--jq/--template` over `grep` or `rg` pipelines.

5. With evidence from either path:

   - Trace error to specific step, dependency, environment, or configuration issue.
   - Correlate with common patterns (version mismatch, missing secret, cache failure, flaky test, timeout).
   - Propose precise code or workflow fixes.
   - If reproducible locally, recommend `act -j <job>` for validation.

6. Before committing fixes, verify logically against observed error. Stage changes and re-run verification if possible.

## Finding Build Issues via `gh` Command

- Use `gh run list --limit 3` to list recent builds.
- Use `gh run view <run_id>` to inspect run status and conclusion before choosing a log path.
- Use `gh run view <run_id> --log-failed` only when the run or job actually failed.
- Use `gh api repos/<owner>/<repo>/actions/jobs/<job_id>` to inspect job metadata when logs are unavailable or the session concluded `success`.
- When reading long logs, use `sed` or `awk` to read content in smaller parts (e.g. `sed -n '100,200p'`).

## Useful Diagnostic Commands

**MCP tools (preferred):**

```python
# When you have a GitHub Actions URL like:
# https://github.com/{org}/{repo}/actions/runs/{rid}/job/{jid}

# Extract IDs: RUN_ID={rid}, JOB_ID={jid}

# Get workflow run details
github-mcp-server-actions_get(method="get_workflow_run", owner="{org}", repo="{repo}", resource_id="{rid}")

# Get job details
github-mcp-server-actions_get(method="get_workflow_job", owner="{org}", repo="{repo}", resource_id="{jid}")

# Get job logs (most useful for diagnosis)
github-mcp-server-get_job_logs(job_id={jid}, owner="{org}", repo="{repo}", return_content=true, tail_lines=100)

# List all jobs in a workflow run
github-mcp-server-actions_list(method="list_workflow_jobs", owner="{org}", repo="{repo}", resource_id="{rid}")

# List recent workflow runs
github-mcp-server-actions_list(method="list_workflow_runs", owner="{org}", repo="{repo}")
```

**gh CLI (fallback):**

```bash
gh --version                          # Check availability
gh auth status                        # Verify login and repo access
gh run list --limit 20 --json databaseId,name,status,conclusion,url
gh run view <run_id>                  # Inspect status before choosing log access
gh run view <run_id> --log-failed     # Failed jobs only, when failure is confirmed
gh api repos/<owner>/<repo>/actions/jobs/<job_id>
```

## What to Avoid

- Never fetch full raw logs first — always use summaries (`summarize_job_log_failures`) or `--log-failed`
- Do not assume `gh run view --log` or `gh api .../logs` will work in every environment; empty output and signed-blob `403` should trigger a pivot, not retries.
- Do not guess causes without log evidence
- Do not default to `grep` or `rg` pipelines in restricted or allowlisted shells
- Avoid modifying workflow YAML unless failure clearly originates there
- Do not trigger re-runs or external commands unless explicitly safety-checked

## Limitations

- MCP tools require server access and may not be available in all environments
- gh CLI requires installation, authentication, and repository access (limited on public repos without login)
- Private secrets are always redacted in logs
- Large log output may truncate in terminal — prioritize failed-only retrieval
- Cannot trigger new workflow runs autonomously

## Repository Context in CI

When working with GitHub Actions build logs and investigating issues:

- **Shallow clones**: GitHub Actions often checks out repositories as shallow clones (limited history)
  - Detect: `git rev-parse --is-shallow-repository` or `test -f .git/shallow`
  - Fix: `git fetch --unshallow` to retrieve complete history
- **Commits from other PRs/branches**: If a commit isn't found, it may be from a different PR or branch
  - Search all branches: `git log --all --oneline | grep <commit-sha>`
  - Fetch specific PR: `git fetch origin pull/<pr-number>/head:pr-<pr-number>`
  - Check if commit exists: `git cat-file -e <commit-sha> 2>/dev/null`
- **Cross-reference with PR**: When user mentions a commit from a PR URL, use the PR number to fetch it first

## Maintenance

This file should be updated if it becomes outdated or if the steps/examples no longer work.
