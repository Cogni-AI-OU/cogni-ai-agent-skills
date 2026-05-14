---
name: github-ah-syntax
description: Complete reference for GitHub Agentic Workflows (gh-aw) frontmatter schema, engine configuration, network access, tools, and imports syntax. You MUST load this skill when writing or debugging Agentic Workflow files.
---

# github-ah-syntax

<!-- markdownlint-disable MD013 MD023 MD031 MD032 MD033 MD041 -->

Reference for GitHub Agentic Workflows frontmatter schema, engines, networking, tools, and safe-outputs.

## Core Principles

- **No Write Permissions in Main Job**: Never use `issues: write`, `pull-requests: write`, or `contents: write`. Write operations must use `safe-outputs`.
- **Prefer `gh-proxy`**: For GitHub API tool access, use `mode: "gh-proxy"` to leverage `gh` CLI directly for reads.
- **Narrow Bash Allowlist**: For PR-triggered workflows, restrict `bash` tools to safe commands (e.g., `[find, cat, grep, jq]`). Use `["*"]` only for trusted internal schedules.
- **Explicit Ecosystems**: Always specify target language ecosystems (e.g., `node`, `python`, `go`) in `network.allowed` alongside `defaults` to prevent package manager blocks.

## Core GitHub Actions Fields

- `on:` Workflow triggers. Includes `slash_command:`, `forks:`, `stop-after:`, `reaction:`, `status-comment:`, `manual-approval:`, `skip-roles:`, `skip-bots:`, `labels:`, `skip-if-match:`, `skip-if-no-match:`, `skip-if-check-failing:`, `github-token:`, `github-app:`, `stale-check:`.
- `permissions:` Only `read` or `none` allowed. `id-token: write` permitted for OIDC.
- `runs-on:` Agent job runner. `runs-on-slim:` for framework/generated jobs.
- `timeout-minutes:`, `concurrency:` (`job-discriminator` prevents fan-out cancellation).
- `pre-steps:`, `steps:`, `pre-agent-steps:`, `post-steps:` Custom steps. `steps` run outside firewall sandbox; do not use for agentic compute.

## Agentic Workflow Specific Fields

- `strict:` Enable enhanced validation (`true` by default).
- `max-runs:`, `user-rate-limit:` (w/ `max-runs-per-window`, `window`, `events`, `ignored-roles`).
- `check-for-updates:` Version checking.
- `features:` Flags like `copilot-requests`, `disable-xpia-prompt`, `action-tag`, `action-mode`, `difc-proxy`, `cli-proxy`, `integrity-reactions`.
- `experiments:` A/B testing configs.
- `imports:`, `inlined-imports:`, `import-schema:` for typed inputs.
- `mcp-servers:` custom MCP servers, `mcp-scripts:` lightweight JS/Shell/Python/Go tools.
- `private:`, `redirect:`, `resources:`, `tracker-id:`, `secret-masking:`, `observability:`.
- `runtimes:` Override/define runtimes (`version`, `action-repo`, `action-version`, `if`).
- `checkout:` Override checkout, supports array for multiple repos, `fetch-depth`, `sparse-checkout`.

## Engine Configuration

Configure the AI processor via `engine:` field:
- `id:` `copilot` (default), `claude`, `codex`, `gemini`, `opencode`.
- `version:`, `model:`, `max-turns:`, `max-continuations:` (copilot).
- `api-target:`, `bare:`, `token-weights:`.

## Network Permissions

Control AI engine network access via `network:` field (top-level):
- `defaults`: Basic infrastructure only.
- `allowed: [defaults, python, node, "api.custom.com"]` Allows specific ecosystems and domains.
- `blocked: ["*.untrusted.com", ruby]` Denies access.
- `firewall: true` Enables AWF (Copilot only).

## Tool Configuration

Configure tools under `tools:` field:
- `github:` Mode: `"gh-proxy"` (preferred) or `"local"`. Configs: `min-integrity`, `blocked-users`, `trusted-users`, `toolsets: [default]`.
- `agentic-workflows:` MCP server for workflow introspection (`status`, `compile`, `logs`, `audit`, `checks`).
- `edit:`, `web-fetch:`, `web-search:`.
- `bash:` Restrict array of allowed commands.
- `playwright:` `mode: cli` (recommended), `version:`.

## Imports Configuration

Import shared components under `imports:` array:
- String format: `shared/common.md`
- Object format: `path:`/`uses:`, `with:` (inputs), `env:`, `checkout:`.
- Note: `copilot-setup-steps.yml` steps are extracted and injected at the start of the agent job.

## Safe Outputs

Use `safe-outputs:` for all write operations (e.g., `create-issue`, `add-comment`, `create-pull-request`).
- Global fields: `github-token:`, `github-app:`, `staged:`, `footer:`, `threat-detection:`, `runs-on:`, `max-patch-size:`.