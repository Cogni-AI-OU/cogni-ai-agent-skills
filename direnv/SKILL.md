---
name: direnv
description: How to maintain credentials and authenticate using direnv without exposing secrets to the output.
license: MIT
---
# Skill: direnv

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Guidance for using `direnv` to securely maintain credentials and load environment variables without exposing them in agent outputs.

## Core Process

1. **Setup Environment**: Copy `.env.example` to `.env` if `.env` does not exist and needs configuration.
2. **Authorize Directory**: Run `direnv allow <path-to-env-dir>` to approve the environment variables.
3. **Export Variables**: Run `eval "$(direnv export bash)"` to inject the variables into the current session.

## Core Principles

- **Security Focus**: Never print, echo, or expose API keys and secrets in the terminal output.
- **Session Persistence**: Always follow `direnv allow` with `eval "$(direnv export bash)"` to ensure the agent's shell session properly loads the variables, as standard direnv shell hooks may not be active.

## When to Use

- When you need to automatically load environment variables upon entering a specific project directory.
- To safely manage API keys and secrets in local development without committing them to version control.
- When an agent needs to execute commands that depend on project-specific credentials stored in `.env`.

## When Not to Use

- In production CI/CD pipelines where secrets are securely injected by the runner environment (like GitHub Actions secrets).
- For managing global, system-wide environment variables (use `~/.bashrc` or `~/.profile` instead).
- When running commands in isolated, ephemeral Docker containers where environment variables are passed via `--env-file`.

## Common Pitfalls

- **Forgetting to Eval**: Running `direnv allow` but forgetting to run `eval "$(direnv export bash)"`, meaning the variables never actually load into the agent's current shell session.
- **Committing Secrets**: Adding sensitive keys to `.env` but failing to ensure `.env` is listed in the project's `.gitignore`.
- **Assuming Global State**: Expecting `direnv` variables to persist if the agent changes directories (`cd ..`), which naturally unloads them.

## Commands / Usage Patterns

To authenticate when API keys are missing (e.g., loading from `../../`):

```bash
direnv allow ../../
eval "$(direnv export bash)"
```

### Full Workflow Example

Example usage for maintaining credentials and running commands from a subdirectory:

```bash
cp ../../.env.example ../../.env
# Edit ../../.env and set real values using file editing tools
direnv allow ../../
eval "$(direnv export bash)"
```

## What to Avoid

- Do not manually `source` or `cat` `.env` files.
- Do not run `direnv allow` without immediately running `eval "$(direnv export bash)"` within the same execution context.
