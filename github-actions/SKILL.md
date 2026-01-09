<!-- markdownlint-disable MD003 MD013 MD022 MD026 MD041 -->
---
name: github-actions
description: Diagnose GitHub Actions workflow failures by retrieving run statuses and logs using MCP tools or gh CLI.
---

This skill enables autonomous diagnosis of GitHub Actions failures, preferring MCP tools for summaries and falling back to gh CLI.

When to Activate
----------------

- User reports a failing GitHub Actions workflow, CI failure, or red status check
- User provides a GitHub Actions URL (e.g., `https://github.com/owner/repo/actions/runs/RUN_ID/job/JOB_ID`)
- Pull request shows failed Actions checks
- Task requires identifying or fixing a workflow failure
- Error output references Actions job steps

Step-by-Step Process
--------------------

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

   - Run_in_terminal `gh run list --limit 20` (adds `--branch $(git rev-parse --abbrev-ref HEAD)` if needed).
   - Identify the most recent failed `run_id` from output.
   - Run_in_terminal `gh run view <run_id> --log-failed` to get only failed job logs (avoids full output).
   - If more context needed: `gh run view <run_id> --log | grep -EC 10 -i 'error|failed|exception|traceback|exit code [1-9][0-9]*'`.
   - If ripgrep available: `gh run view <run_id> --log-failed | rg -i -C 10 "failed|error|exception|exit"`.
   - Capture and analyze output for root cause.

5. With evidence from either path:

   - Trace error to specific step, dependency, environment, or configuration issue.
   - Correlate with common patterns (version mismatch, missing secret, cache failure, flaky test, timeout).
   - Propose precise code or workflow fixes.
   - If reproducible locally, recommend `act -j <job>` for validation.

6. Before committing fixes, verify logically against observed error. Stage changes and re-run verification if possible.

Finding Build Issues via `gh` Command
-------------------------------------

- Use `gh` command to interact with GitHub resources. For example:
  - `gh run list --limit 3` to list recent builds.
  - `gh run view <run_id> --log-failed` to view only failed job logs.
  - `gh run view <run_id> --log | rg -C3 -iw "failed|error|exit"` to search full logs for key terms.
- When reading long logs, use `sed` or `awk` to read content in smaller parts (e.g. `sed -n '100,200p'`).

Useful Diagnostic Commands
--------------------------

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
gh run list --limit 20                # List recent runs
gh run view <run_id> --log-failed     # Failed jobs only (recommended first)
gh run view <run_id> --log | grep -C 10 -i "error\|failed\|exit code"
```

What to Avoid
-------------

- Never fetch full raw logs first — always use summaries (`summarize_job_log_failures`) or `--log-failed`
- Do not guess causes without log evidence
- Avoid modifying workflow YAML unless failure clearly originates there
- Do not trigger re-runs or external commands unless explicitly safety-checked

Limitations
-----------

- MCP tools require server access and may not be available in all environments
- gh CLI requires installation, authentication, and repository access (limited on public repos without login)
- Private secrets are always redacted in logs
- Large log output may truncate in terminal — prioritize failed-only retrieval
- Cannot trigger new workflow runs autonomously

Repository Context in CI
-------------------------

When working with GitHub Actions build logs and investigating issues:

- **Shallow clones**: GitHub Actions often checks out repositories as shallow clones (limited history)
  - Detect: `git rev-parse --is-shallow-repository` or `test -f .git/shallow`
  - Fix: `git fetch --unshallow` to retrieve complete history
- **Commits from other PRs/branches**: If a commit isn't found, it may be from a different PR or branch
  - Search all branches: `git log --all --oneline | grep <commit-sha>`
  - Fetch specific PR: `git fetch origin pull/<pr-number>/head:pr-<pr-number>`
  - Check if commit exists: `git cat-file -e <commit-sha> 2>/dev/null`
- **Cross-reference with PR**: When user mentions a commit from a PR URL, use the PR number to fetch it first
