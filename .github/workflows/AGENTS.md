# GitHub Actions Workflows (Agent Catalog)

Authoritative, agent-facing catalog of workflows in this repository. Use this when loading or modifying
workflows and keep it in sync with the files in this directory.

For a human-readable overview, see [README.md](README.md).

## Workflow catalog

- **[check.yml](check.yml)**: Linting and quality gates via actionlint and pre-commit.
- **[cogni-ai-agent.yml](cogni-ai-agent.yml)**: Logic for the Cogni AI Agent.
- **[copilot-setup-steps.yml](copilot-setup-steps.yml)**: Environment setup utility.
- **[devcontainer-ci.yml](devcontainer-ci.yml)**: Build/test devcontainer and required tools/packages.
- **[opencode-agent.yml](opencode-agent.yml)**: OpenCode agent invocation via comments or manual triggers.

## Details

### check.yml

- Purpose: run actionlint and pre-commit to enforce workflow and repo standards.
- Triggers: `push`, `pull_request`, `schedule`, `workflow_call`, `workflow_dispatch`,
  `workflow_run` (after bot workflow completions).
- Bot-PR support: `workflow_run` trigger enables checks on PRs created by bots,
  since normal `pull_request` events don't trigger for bot actors.
- Reusable: `uses: Cogni-AI-OU/cogni-ai-agent-skills/.github/workflows/check.yml@main`.
- Jobs: `actionlint`, `link-checker`, `pre-commit`.

### cogni-ai-agent.yml

- Purpose: provides the underlying logic to run the Cogni AI Agent.
- Triggers: `issue_comment`, `pull_request_review_comment`, `workflow_dispatch`.
- Details: Installs Python dependencies from `.devcontainer/requirements.txt` and calls the
  `Cogni-AI-OU/cogni-ai-agent-action` to process instructions.
- Permissions: `contents: write`, `id-token: write`, `issues: write`, `pull-requests: write`.

### copilot-setup-steps.yml

- Purpose: utility workflow for setting up the environment.
- Triggers: `push` and `pull_request` on `copilot-setup-steps.yml` or `.devcontainer/requirements.txt`.
- Details: Checks out repo, sets up Python 3.12, restores cache, and installs dependencies.
- Permissions: `contents: read`.

### devcontainer-ci.yml

- Purpose: build and validate the dev container; ensure required tools and Python packages exist.
- Inputs: `required_commands` (defaults to common CLI tools), `required_python_packages`
  (defaults to ansible, ansible-lint, docker, molecule, pre-commit, uv).
- Triggers: pull_request/push affecting `.devcontainer/` or this workflow; weekly schedule;
  `workflow_call`.
- Permissions: callers must grant `packages: write` when pushing images to GHCR.
- Reusable: `uses: Cogni-AI-OU/cogni-ai-agent-skills/.github/workflows/devcontainer-ci.yml@main`.

### opencode-agent.yml

- Purpose: invoke OpenCode agents via slash commands or manual triggers.
- Uses: `Cogni-AI-OU/cogni-ai-agent-action/opencode@main` composite action.
- Inputs: `agent` (default `cogni-ai`), `model` (workflow_call default via
  `vars.OPENCODE_MODEL_DEFAULT` with fallback `opencode/gemini-3-flash`; workflow_dispatch
  default `opencode/gemini-3-flash`), `prompt` (optional override).
- Triggers: `workflow_dispatch`, `workflow_call`, or issue comments and PR review comments with `/oc` or `/opencode` from trusted (non-bot) collaborators/members/owners.
- Concurrency: one run per branch/PR context via workflow-level `concurrency` group to avoid competing pushes.
- Permissions: `contents: write`, `id-token: write`, `issues: write`, `pull-requests: write`.
- Reusable: `uses: Cogni-AI-OU/cogni-ai-agent-skills/.github/workflows/opencode-agent.yml@main`.

## Synchronized Configuration

The following configuration values **MUST** be kept in sync across multiple files:

### OPENCODE_PERMISSION

The `OPENCODE_PERMISSION` environment variable defines the bash command allowlist for OpenCode agents.
It must be identical in the workflow file:

| File | Location |
| ---- | -------- |
| [opencode-agent.yml](opencode-agent.yml) | env section |

### Model options list

The `model` input options for `workflow_dispatch` must be identical in the corresponding workflow files:

| File | Location |
| ---- | -------- |
| [cogni-ai-agent.yml](cogni-ai-agent.yml) | `workflow_dispatch` inputs |
| [opencode-agent.yml](opencode-agent.yml) | `workflow_dispatch` inputs |

## Notes

- Keep this catalog updated when workflows are added, removed, or renamed.
