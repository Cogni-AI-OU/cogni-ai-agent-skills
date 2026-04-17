# GitHub Actions Workflows (Agent Catalog)

Authoritative, agent-facing catalog of workflows in this repository. Use this when loading or modifying
workflows and keep it in sync with the files in this directory.

For a human-readable overview, see [README.md](README.md).

## Workflow catalog

| Workflow | Purpose | Key triggers / notes |
| -------- | ------- | -------------------- |
| [check.yml](check.yml) | Linting and quality gates via actionlint and pre-commit | push, pull_request, schedule, workflow_run (after OpenCode); reusable via `workflow_call` |
| [opencode.yml](opencode.yml) | OpenCode agent invocation via comments or manual triggers | issue_comment keywords `/oc` or `/opencode`, workflow_dispatch, `workflow_call` |
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

### devcontainer-ci.yml

- Purpose: build and validate the dev container; ensure required tools and Python packages exist.
- Inputs: `required_commands` (defaults to common CLI tools), `required_python_packages`
  (defaults to ansible, ansible-lint, docker, molecule, pre-commit, uv).
- Triggers: pull_request/push affecting `.devcontainer/` or this workflow; weekly schedule;
  `workflow_call`.
- Permissions: callers must grant `packages: write` when pushing images to GHCR.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/devcontainer-ci.yml@main`.

## Notes

- Follow [.github/instructions/github-workflows.instruction.md](../instructions/github-workflows.instruction.md)
  when editing workflow files (ordering, formatting, validation).
- Keep this catalog updated when workflows are added, removed, or renamed.
