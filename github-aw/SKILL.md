---
name: github-aw
description: 'Safely update existing GitHub Agentic Workflows (gh-aw), distinguishing between frontmatter configuration that requires recompilation and markdown body prompt edits that do not.'
license: MIT
---
# Skill github-aw

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- A user asks to update, modify, or refine an existing GitHub Agentic Workflow (`.md` file in `.github/workflows/`).
- You need to change the agent prompt (markdown body) — a quick edit with no recompilation required.
- You need to modify the YAML frontmatter configuration (tools, network, triggers) and recompile the workflow.
- Optimizing token usage of an existing workflow through prompt minimization, DataOps, or batching strategies.
- Auditing token consumption between workflow variants using `gh aw audit` for A/B experiment comparison.
- The user explicitly requests help with the `gh aw` CLI command or its subcommands (`compile`, `audit`, `logs`, etc.).

## When Not to Use
- Creating a new agentic workflow from scratch (use `gh aw new` or the appropriate creation flow instead).
- Debugging a workflow execution failure (load `github-aw-troubleshooting` instead for root-cause analysis).
- Designing workflow architecture patterns (load `github-aw-patterns` for BatchOps, ChatOps, DailyOps guidance).
- Diagnosing issues with the AWF firewall or network blocks (load `gh-aw-firewall-debug` instead).

## Gotchas
- Editing the YAML frontmatter REQUIRES running `gh aw compile <workflow-id>` afterward — forgetting this leaves the workflow in a broken state with a stale `.lock.yml`.
- Never use `mode: remote` or `mode: local` for GitHub tools in agentic workflows; always prefer `mode: gh-proxy` to skip Docker overhead and use `gh` CLI directly.
- Write permissions (`issues: write`, `pull-requests: write`) in the main job will cause compilation errors — all writes must go through `safe-outputs`.
- `post-steps:` run OUTSIDE the firewall sandbox and must never be used for agentic compute or untrusted AI execution — they are for cleanup and artifact uploads only.

Update existing agentic workflows using the GitHub Agentic Workflows (gh-aw) CLI extension. Guide users on making incremental modifications, refining prompts, and recompiling when configuration changes.

## Core Process

1. **Identify the Workflow**: Target a specific workflow file at `.github/workflows/<workflow-id>.md`.
2. **Determine Edit Scope**:
   - **Agent Behavior/Instructions**: Edit the markdown body (after `---`). *No recompilation needed.*
   - **Configuration**: Edit the YAML frontmatter (between `---`). *Recompilation required.*
3. **Make Targeted Changes**: Perform small, incremental edits preserving existing structures and sensible defaults.
4. **Compile if Needed**: If the YAML frontmatter was modified, run `gh aw compile <workflow-id>` to update the `.lock.yml` file.
5. **Verify**: Ensure all syntax errors are resolved and the updated behavior matches the intent.

## Core Principles

- **Single-Job Execution**: Workflows execute as a single job. They cannot manage cross-job state, wait for external events, or perform multi-stage orchestration. Suggest traditional GitHub Actions for these.
- **Incremental Frontmatter Edits**: Do not rewrite entire frontmatter sections. Only append or modify specific fields required. Avoid specifying default fields (like `engine: copilot`).
- **Security First**: Default to `permissions: read-all`. Use `safe-outputs` (e.g., `safe-outputs.jobs`) instead of write permissions or `post-steps` for external writes. Limit network access domains.
- **Strict Mode Validation**: Prefer `gh aw compile --strict` for production workflows to enforce secure configurations.

## Token Optimization (Cost Reduction)

When updating workflows, proactively suggest and implement token optimization techniques:

1. **DataOps (Move Compute to Steps)**: Replace agentic data fetching with bash `steps:` (e.g., using `gh` and `jq` to fetch and aggregate data into `/tmp/gh-aw/data/stats.json`). This prevents the agent from spending tokens reading large raw API responses. The prompt should direct the agent to read the compact JSON instead.
2. **gh-proxy and cli-proxy**: Use `tools.github.mode: gh-proxy` instead of MCP servers (`mode: local`) to skip Docker initialization overhead. Use `cli-proxy: true` to mount MCPs as CLI tools, allowing the agent to filter outputs via `jq` before they enter its context.
3. **Inline Sub-Agents**: For repetitive per-item tasks (e.g., classifying 50 issues), define a `sub-agents:` block using `model: small`. Let cheap sub-agents do the extraction, and the main agent synthesize their results.
4. **Prompt Minimization & Caching**:
   - Apply the "Caveman Technique": Strip redundant prose, hedging, and unnecessary examples.
   - Place stable instructions (rules, schemas) *before* dynamic content (issue bodies, logs) to maximize prompt cache hits.
   - Inject only required fields (e.g., `${{ github.event.issue.number }}`) rather than full event payloads.
5. **Experiments**: Use the `experiments:` frontmatter field and `metric: "effective_tokens"` to A/B test prompt variations. Validate savings with `gh aw audit <base-run-id> <optimized-run-id>`.
6. **Batching**: Convert reactive triggers to scheduled batches (`schedule:`) if near-real-time feedback is not strictly required.

## Commands / Usage Patterns

- **View a Workflow**:
  `view .github/workflows/<workflow-id>.md`

- **Edit Prompt (No Recompile)**: Modify the markdown instructions only.
  `edit .github/workflows/<workflow-id>.md`

- **Compile a Specific Workflow**:
  `gh aw compile <workflow-id>`

- **Compile with Strict Validation**:
  `gh aw compile --strict <workflow-id>`

- **Audit Token Usage**:
  `gh aw audit <run-id> --json` (measure baseline)
  `gh aw audit <base-run-id> <optimized-run-id> --json` (compare improvements)

## Diagnostics and Troubleshooting

- **Compilation Errors**: Never leave a workflow in a broken state. Fix all syntax errors and re-run `gh aw compile`.
- **Security Warnings**: If strict mode compilation fails, fix the workflow to meet security requirements rather than disabling strict mode. Proceed with relaxed security only upon explicit user confirmation.

## What to Avoid

- Do not use `gh-aw` for creating new workflows from scratch (use the appropriate creation flow instead).
- Do not recommend `mode: remote` or `mode: local` for GitHub tools. Prefer `mode: gh-proxy` and `toolsets: [default]`.
- Do not suggest GitHub mutation tools (e.g., `create_issue`). Always use `safe-outputs` for write operations.
- Do not use `post-steps:` for custom write operations triggered by the agent; use `safe-outputs.jobs:`.

## Limitations

- Cannot orchestrate pipelines with conditional progression, human-in-the-loop pauses, or auto-retry across external systems.
- Cannot manage cross-workflow coordination or state passing.

## Related Skills

- **gh-aw**: You MUST load this skill when working with the general `gh aw` command for repository automation.
- **github-aw-syntax**: Reference for GitHub Agentic Workflows frontmatter schema and syntax.
