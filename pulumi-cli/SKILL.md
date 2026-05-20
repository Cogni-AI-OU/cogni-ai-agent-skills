---
name: pulumi-cli
description: >-
  Execute Pulumi CLI commands for stack management, infrastructure deployments, and API interactions.
  You MUST load this skill when working with the pulumi command.
license: MIT
---

# Pulumi CLI

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Executing core Pulumi commands like `pulumi up`, `pulumi preview`, or `pulumi destroy`.
- Managing Pulumi stacks with `pulumi stack` and configuration with `pulumi config`.
- Interacting directly with the Pulumi Cloud REST API using `pulumi api`.

## When Not to Use

- Writing or refactoring Pulumi infrastructure code (use language-specific skills like `python` or `typescript`).
- Fetching documentation or schemas (use `pulumi-docs` instead).

## Core Principles

- **Non-Interactive Execution**: Autonomous agents MUST always use the `--non-interactive` flag to prevent the CLI from hanging while waiting for human input.
- **JSON Output**: Use `--output=json` where supported (especially with `pulumi api`) for stable and parsable outputs that agents can easily consume.
- **Stable Exit Codes**: Rely on Pulumi CLI's exit codes for stable error handling in automation scripts.

## Step-by-Step Workflows

### Deploying Infrastructure

1. **Preview Changes**: Always run a preview before deploying to understand the impact.
   `pulumi preview --non-interactive`
2. **Deploy Changes**: Deploy the infrastructure changes automatically.
   `pulumi up --non-interactive --yes`
3. **Destroy Infrastructure**: Tear down the stack entirely when instructed.
   `pulumi destroy --non-interactive --yes`

### Managing Stacks

1. **List Stacks**:
   `pulumi stack ls`
2. **Select Stack**:
   `pulumi stack select <stack-name>`
3. **Show Fully Qualified Stack Names**:
   `pulumi stack ls -Q`

### Interacting with Pulumi API (Agent Workflow)

1. **List API Endpoints**:
   `pulumi api list --output=json`
2. **Call API Endpoint**:
   `pulumi api /api/user`

## Common Pitfalls

- **Interactive Hangs**: Running `pulumi up` or `pulumi destroy` without `--non-interactive` and `--yes` will cause the agent session to hang waiting for user confirmation.

## What to Avoid

- Avoid modifying Pulumi state directly unless absolutely necessary. Rely on standard deployments where possible.
- Do not use interactive commands in agent scripts. Always supply all required flags and use `--non-interactive`.

## Related Skills

- **pulumi-docs**: You MUST load this skill when retrieving Pulumi documentation or schemas.
