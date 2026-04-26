<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->
---
name: gh
description: >-
  Use when planning or executing GitHub CLI (`gh`) commands for issues, pull
  requests, workflow runs, reviews, or API queries, especially in restricted
  shells where structured output and fallback choice matter.
---
# gh Skill

Use `gh` as a structured client first. Prefer native fields, explicit routing,
and bounded fallbacks over brittle shell post-processing.

## When to Activate

- User asks to use `gh`, GitHub CLI, or to query GitHub from shell.
- Task involves issues, PRs, reviews, workflow runs, jobs, or GitHub REST endpoints.
- Execution is inside CI, Codespaces, or another restricted shell.

## Core Process

1. Verify availability and auth first: `gh --version`, then `gh auth status`.
2. Choose the narrowest native `gh` surface before reaching for `gh api`:
   - `gh issue view/comment` for issues
   - `gh pr view/comment/review` for pull requests and reviews
   - `gh run list/view` for workflow runs
   - `gh api` only when native subcommands do not expose the needed field
3. Prefer structured output over shell filtering:
   - use `--json`, `--jq`, or `--template` instead of `grep`/`rg`
   - use `gh api` for metadata, not ad hoc HTML scraping
4. Query the smallest object that answers the question:
   - issue or PR metadata before comments
   - run metadata before logs
   - job metadata before job logs
5. After each command, verify progress explicitly:
   - non-empty stdout or expected JSON field
   - no warning that changes command semantics
   - result actually answers the current question
6. If the same normalized command shape fails twice with the same warning,
   error, or empty result, pivot strategy instead of retrying.

## Structured Query Patterns

- Prefer native JSON first:
  - `gh issue view <number> --json comments,number,title,state,author,url`
  - `gh pr view <number> --json number,title,state,reviewDecision,url`
  - `gh run list --limit 20 --json databaseId,workflowName,status,conclusion,url`
- Use `gh api` for objects that native subcommands do not expose cleanly:
  - `gh api repos/<owner>/<repo>/actions/jobs/<job_id>`
  - `gh api repos/<owner>/<repo>/issues/<number>/comments`
- Use `--jq` or `--template` before external filters.

## Preferred Patterns

- Comment directly without touching workspace files:
  `gh issue comment <number> --body "..."`
- Reply through the originating GitHub surface:
  - issue thread -> `gh issue comment`
  - PR thread -> `gh pr comment` or `gh pr review`
  - inline review thread -> `gh api .../replies`
- For long comments, use a HEREDOC body:
  `gh issue comment <number> --body "$(cat <<'EOF'
  ...
  EOF
  )"`
- For non-code-change tasks, verify workspace cleanliness after posting.

## Workflow Run Diagnostics

- `gh run view <run_id> --log-failed` is only reliable when the relevant job
  or run concluded with failure.
- `gh run view <run_id> --log | rg -iw "failed|error|exit"` can be used to find
  errors in runs that might have partially succeeded or where `--log-failed` is
  insufficient.
- Jobs can conclude `success` while still containing pathological agent
  behavior; inspect run/job metadata before assuming failed-only logs are
  sufficient.
- Do not pass both run ID and job ID to `gh run view`; the CLI warns and
  ignores the run ID.
- Treat `gh run view ... --log` as environment-sensitive. If it returns
  empty output, do not loop on it; switch to metadata, artifacts, or another
  supported log source.
- Treat `gh api .../logs` as a special case. The endpoint may redirect to a
  signed blob URL that does not behave like normal JSON API calls and can
  return `403` when replayed incorrectly.
- Probe one run or one job first before launching parallel diagnostics.

## GitHub Actions Runtime

When executing autonomously within a GitHub Actions environment, adhere strictly to these interaction constraints:

### OpenCode PR Context & Response Routing

**Context & Targeting Invariants**:

- **Extract Context**: Parse the `## Pull Request Context` block containing `**Base Branch:**` dynamically.
- **Dynamic PR Targeting**: ALWAYS target this explicitly provided **Base Branch** when creating/updating PRs.

**Response Detection & Routing**: Check `github.event_name` and payload to identify trigger source:

- **General PR comment** (`issue_comment`):
  - Condition: `if: ${{ github.event.issue.pull_request }}`
  - Reply Method: `gh pr comment`
- **Issue comment** (`issue_comment`):
  - Condition: `if: ${{ !github.event.issue.pull_request }}`
  - Reply Method: `gh issue comment`
- **Inline code review** (`pull_request_review_comment`):
  - Reply Method: `gh api repos/{owner}/{repo}/pulls/{pr}/comments/{comment_id}/replies -f body="..."`

**Routing Invariants**:

- **Symmetric Routing**: ALWAYS reply via the exact originating channel. NEVER cross threads.
- Parse `github.event.comment.id` and `in_reply_to_id` to maintain thread continuity.

### Branch Sync Policy (No Rebase During Runtime)

When the prompt asks to "pull" or "sync with base" in GitHub Actions runtime, the agent MUST integrate remote changes with a merge commit workflow.

- **MUST NOT** run any rebase-based update command during runtime.
- **FORBIDDEN**: `gh pr update-branch --rebase`, `git pull --rebase`, `git rebase`, or any history rewrite that changes commit SHAs.
- **MUST** use pull-with-merge semantics: `git pull --no-rebase`.
- **MUST** preserve remote branch compatibility for post-run auto PR/push logic.

**Execution Steps (strict order)**:

1. Determine PR base/head from context (`## Pull Request Context`, `gh pr view`).
2. Ensure work is on the PR head branch (not detached HEAD).
3. Sync head branch from remote with merge semantics: `git pull --no-rebase origin <head-branch>`.
4. If base changes must be integrated into head, merge base explicitly: `git fetch origin <base-branch> && git merge --no-ff origin/<base-branch>`.
5. Resolve conflicts, commit merge if required, then push normally (no force).

**Verification Gate (required before push)**:

- Confirm no rebase command was executed in this run.
- Confirm `git log --oneline --graph -n 10` shows merge topology (no rewritten linearized history from rebase).
- Proceed with normal `git push` only after these checks pass.

### GitHub Runtime Decision Policy

- **Default to Best Practice:** Implement the most recommended path autonomously when multiple options exist.
- **Document Trade-offs:** Capture unresolved decisions, explicit options, and impacts in the PR description.
- **Never Stall:** Proceed immediately with safe defaults. Request preference feedback in the PR instead of waiting.
- **Report Defensively:** Present recommended option first; list alternatives only if they alter scope or risk.

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

- Do not build `gh ... | grep ... | grep ...` chains as the default diagnostic
  path.
- Do not retry the same `gh` command shape after semantic warnings.
- Do not assume Actions log retrieval is uniform across public pages, API
  endpoints, and CLI subcommands.
- Do not create temp files for comments or analysis when direct `gh`
  subcommands are available.

## Maintenance

Update this skill when new `gh` failure signatures, routing patterns, or
reliable structured-query workflows are discovered.
