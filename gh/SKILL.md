<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->
---
name: gh
description: >-
  Use when operating the GitHub CLI (`gh`) for issues, pull requests,
  workflow runs, or API queries, especially in restricted CI shells where
  pipelines and log endpoints can mislead or fail.
---
# gh Skill

Use `gh` as a structured client first, not as text to be post-processed by brittle shell pipelines.

## When to Activate

- User asks to use `gh`, GitHub CLI, or to query GitHub from shell.
- Task involves issues, PRs, reviews, workflow runs, jobs, or GitHub REST endpoints.
- Execution is inside CI, Codespaces, or another restricted shell.

## Core Process

1. Verify availability and auth first: `gh --version`, then `gh auth status`.
2. Prefer `gh` native structure over shell filtering:
   - use `--json`, `--jq`, or `--template` instead of `grep`/`rg`
   - use `gh api` for metadata, not ad hoc HTML scraping
3. Query the smallest object that answers the question:
   - issue/PR metadata before comments
   - run metadata before logs
   - job metadata before job logs
4. After each command, verify progress explicitly:
   - non-empty stdout
   - expected field present
   - no warning that changes command semantics
5. If the same normalized command shape fails twice with the same error or empty result, pivot strategy instead of retrying.

## Preferred Patterns

- Comment directly without touching workspace files:
  `gh issue comment <number> --body "..."`
- For long comments, use a HEREDOC body:
  `gh issue comment <number> --body "$(cat <<'EOF'
  ...
  EOF
  )"`
- Use JSON-capable commands first:
  `gh run list --limit 20 --json databaseId,workflowName,status,conclusion,url`
- Use `gh api repos/<owner>/<repo>/actions/jobs/<job_id>` for job metadata.

## Workflow Run Diagnostics

- `gh run view <run_id> --log-failed` is only reliable when the relevant job or run concluded with failure.
- Jobs can conclude `success` while still containing pathological agent
  behavior; inspect run/job metadata before assuming failed-only logs are
  sufficient.
- Do not pass both run ID and job ID to `gh run view`; the CLI warns and ignores the run ID.
- Treat `gh run view ... --log` as environment-sensitive. If it returns
  empty output, do not loop on it; switch to metadata, artifacts, or another
  supported log source.
- Treat `gh api .../logs` as a special case. The endpoint may redirect to a
  signed blob URL that does not behave like normal JSON API calls and can
  return `403` when replayed incorrectly.

## Restricted Shell Rules

- In allowlisted shells, do not assume `grep`, `rg`, or complex pipelines are
  permitted just because `gh` is permitted.
- Prefer `gh --json/--jq/--template` over external text filters.
- Probe one command shape first before parallel fan-out.
- If a shell policy blocks a `gh`-adjacent command shape, classify it as
  `POLICY_DENIED` and pivot immediately.

## Failure Signatures

- Warning like `both run and job IDs specified; ignoring run ID` means the
  command did not execute the way you intended; fix arguments before
  continuing.
- Empty stdout from a supposedly successful `gh` query is a signal, not a
  success. Check whether the subcommand supports the requested mode in this
  environment.
- Repeated `403` from `gh api` on log/archive endpoints usually indicates
  redirect or signed-URL handling issues, not missing repository access.

## What to Avoid

- Do not build `gh ... | grep ... | grep ...` chains as the default diagnostic path.
- Do not retry the same `gh` command shape after semantic warnings.
- Do not assume Actions log retrieval is uniform across public pages, API
  endpoints, and CLI subcommands.
- Do not create temp files for comments or analysis when direct `gh` subcommands are available.

## Maintenance

Update this skill when new `gh` failure signatures or reliable structured-query patterns are discovered.
