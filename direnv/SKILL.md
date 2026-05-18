---
name: direnv
description: 'How to maintain credentials and authenticate using direnv without exposing secrets to the output.'
license: MIT
---
# Skill: direnv

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- Loading environment variables and API keys from `.envrc` or `.env` files into the agent session
- Authenticating with cloud providers or GitHub by sourcing credentials via direnv
- Setting up project-specific environment configurations that change between directories
- Restoring environment variable state after checking out a new branch or switching projects

## When Not to Use
- Storing secrets permanently — use a dedicated secret manager (e.g., GitHub Secrets, Vault) for CI/CD and production
- Simple single-variable exports that don't warrant the direnv overhead — a regular `export` command suffices
- Cross-session environment persistence — direnv only loads per-shell; use shell init files for always-present variables

## Gotchas
- Running `direnv allow` without immediately following with `eval "$(direnv export bash)"` within the same execution context will NOT load the variables into the current agent shell session
- Never use `cat` or `source` on `.env` files — this exposes secrets in the terminal output and may persist in logs
- The `.envrc` file must be explicitly allowed with `direnv allow` before direnv will load it; a new `.envrc` silently does nothing until authorized

Guidance for using `direnv` to securely maintain credentials and load environment variables without exposing them in agent outputs.

## Core Process

1. **Setup Environment**: Copy `.env.example` to `.env` if `.env` does not exist and needs configuration.
2. **Authorize Directory**: Run `direnv allow <path-to-env-dir>` to approve the environment variables.
3. **Export Variables**: Run `eval "$(direnv export bash)"` to inject the variables into the current session.

## Core Principles

- **Security Focus**: Never print, echo, or expose API keys and secrets in the terminal output.
- **Session Persistence**: Always follow `direnv allow` with `eval "$(direnv export bash)"` to ensure the agent's shell session properly loads the variables, as standard direnv shell hooks may not be active.

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
