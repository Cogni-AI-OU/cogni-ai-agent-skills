# GitHub Actions Workflows (Agent Catalog)

Authoritative, agent-facing catalog of workflows in this repository. Use this when loading or modifying
workflows and keep it in sync with the files in this directory.

For a human-readable overview, see [README.md](README.md).

## Workflow catalog

| Workflow | Purpose | Key triggers / notes |
| -------- | ------- | -------------------- |
| [check.yml](check.yml) | Linting and quality gates via actionlint and pre-commit | push, pull_request, schedule, workflow_run (after OpenCode); reusable via `workflow_call` |
| [opencode.yml](opencode.yml) | OpenCode agent invocation via comments or manual triggers | issue_comment keywords `/oc` or `/opencode`, workflow_dispatch, `workflow_call` |
| [opencode-review.yml](opencode-review.yml) | OpenCode PR review | pull_request (trusted authors), `/review` comment by OWNER/MEMBER, workflow_dispatch, `workflow_call` |
| [devcontainer-ci.yml](devcontainer-ci.yml) | Build/test devcontainer and required tools/packages | push/pull_request touching .devcontainer or workflow; schedule; `workflow_call` |

## Details

### check.yml

- Purpose: run actionlint and pre-commit to enforce workflow and repo standards.
- Triggers: `push`, `pull_request`, `schedule`, `workflow_call`, `workflow_dispatch`,
  `workflow_run` (after OpenCode/OpenCode Review workflows complete successfully).
- Bot-PR support: `workflow_run` trigger enables checks on PRs created by bots
  (e.g., `opencode-agent`), since normal `pull_request` events don't trigger for bot actors.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/check.yml@main`.
- Jobs: `actionlint`, `link-checker`, `pre-commit`.

### opencode.yml

- Purpose: invoke OpenCode agents via slash commands or manual triggers.
- Inputs: `agent` (default `cogni-ai`), `model` (workflow_call default via
  `vars.OPENCODE_MODEL_DEFAULT` with fallback `opencode/gemini-3.1-pro`; workflow_dispatch
  default `opencode/gemini-3.1-pro`), `prompt` (optional override).
- Triggers: `workflow_dispatch`, `workflow_call`, or issue comments with `/oc` or `/opencode` from trusted (non-bot) collaborators/members/owners.
- Concurrency: one run per branch/PR context via workflow-level `concurrency` group to avoid competing pushes.
- Guardrail: comment-triggered runs do not populate `inputs.*`; back shared OpenCode defaults
  with workflow-level `env` values instead of hardcoding agent/model literals in steps.
- Permissions: `contents: read`, `id-token: write`, `issues: write`, `pull-requests: write`.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/opencode.yml@main`.

### opencode-review.yml

- Purpose: OpenCode-driven PR review.
- Inputs: agent (reviewer), model (workflow_call default via
  `vars.OPENCODE_MODEL_DEFAULT` with fallback `opencode/gpt-5.3-codex`; workflow_dispatch
  default `opencode/gpt-5.3-codex`), additional_prompt, pr_number (req for call/dispatch),
  prompt (default pr-review).
- Triggers: pull_request (trusted authors), /review comment (COLLABORATOR/OWNER/MEMBER), workflow_call,
  workflow_dispatch.
- Concurrency: Only one run per issue/PR/branch at a time; new runs cancel pending ones.
- Guardrail: align review default behavior with OpenCode by using workflow-level
  `env` fallbacks for `agent` and `model` rather than hardcoded literals in steps.
- Permissions: `contents: read`, `id-token: write`, `issues: read`, `pull-requests: write`.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/opencode-review.yml@main`.

### devcontainer-ci.yml

- Purpose: build and validate the dev container; ensure required tools and Python packages exist.
- Inputs: `required_commands` (defaults to common CLI tools), `required_python_packages`
  (defaults to ansible, ansible-lint, docker, molecule, pre-commit, uv).
- Triggers: pull_request/push affecting `.devcontainer/` or this workflow; weekly schedule;
  `workflow_call`.
- Permissions: callers must grant `packages: write` when pushing images to GHCR.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/devcontainer-ci.yml@main`.

## Synchronized Configuration

The following configuration values **MUST** be kept in sync across multiple files:

### OPENCODE_PERMISSION

The `OPENCODE_PERMISSION` environment variable defines the bash command allowlist for OpenCode agents.
It must be identical in both workflow files:

| File | Location |
| ---- | -------- |
| [opencode.yml](opencode.yml) | Line ~130 (env section) |
| [opencode-review.yml](opencode-review.yml) | Line ~210 (env section) |

### Model options list

The `model` input options for `workflow_dispatch` must be identical in both workflow files:

| File | Location |
| ---- | -------- |
| [opencode.yml](opencode.yml) | Lines ~48-90 (workflow_dispatch inputs) |
| [opencode-review.yml](opencode-review.yml) | Lines ~67-107 (workflow_dispatch inputs) |

## Notes

- Follow [.github/instructions/github-workflows.instruction.md](../instructions/github-workflows.instruction.md)
  when editing workflow files (ordering, formatting, validation).
- Keep this catalog updated when workflows are added, removed, or renamed.
