---
name: pulumi-cli
description: 'Execute Pulumi CLI commands for stack management, infrastructure deployments, schemas, and API interactions. You MUST load this skill when working with the pulumi command.'
license: MIT
---

# Pulumi CLI

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Executing core Pulumi commands like `pulumi up`, `pulumi preview`, or `pulumi destroy`.
- Managing Pulumi stacks with `pulumi stack` and configuration with `pulumi config`.
- Retrieving provider schemas using `pulumi package get-schema`.
- Interacting directly with the Pulumi Cloud REST API using `pulumi api`.
- Fetching documentation or schemas programmatically (e.g., parsing `https://www.pulumi.com/llms.txt`).

## When Not to Use

- Writing or refactoring Pulumi infrastructure code (use language-specific skills like `python` or `typescript`).

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
3. **Query Registry API**:
   `pulumi api /api/registry/packages/<source>/<publisher>/<name>/versions/latest/readme`

### Retrieving Provider Schemas

1. **Get Schema for Package**:
   `pulumi package get-schema <name>[@version]` (e.g., `pulumi package get-schema aws@6.0.0`)

### Accessing Markdown Documentation

1. **Fetch Documentation as Markdown**:
   Use `webfetch` with `Accept: text/markdown` or append `.md` to the URL.
   `curl -H "Accept: text/markdown" https://www.pulumi.com/docs/iac/concepts/resources/`
   `curl https://www.pulumi.com/docs/iac/concepts/resources.md`

## Common Pitfalls

- **Interactive Hangs**: Running `pulumi up` or `pulumi destroy` without `--non-interactive` and `--yes` will cause the agent session to hang waiting for user confirmation.
- **Missing Auth Token**: The Cloud registry API for private packages requires `Authorization: token $PULUMI_ACCESS_TOKEN`. Ensure environment variables are populated when making direct HTTP calls instead of using `pulumi api`.
- **Incomplete Endpoints**: When using `pulumi api`, remember that type tokens for `docs/{typeToken}` must be URL-encoded (e.g. `random:index/RandomPassword` becomes `random%3Aindex%2FRandomPassword`).

## What to Avoid

- Avoid modifying Pulumi state directly unless absolutely necessary. Rely on standard deployments where possible.
- Do not use interactive commands in agent scripts. Always supply all required flags and use `--non-interactive`.
