---
name: astro-cli
description: 'Expert-level guide for using the Astro CLI to manage Astronomer Airflow deployments, authenticate, run APIs, and develop dags locally. You MUST load this skill when asked to use the astro command.'
license: MIT
---

# Astro CLI Skill

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use This Skill

- When the user asks you to execute commands starting with `astro`.
- When interacting with Astronomer deployments using the Astro CLI.
- When calling the Astro API or Airflow REST API via the CLI.
- When you need context on Astro CLI commands, deployment updates, or triggering dags via CLI.

## When Not to Use

- When writing generic Apache Airflow DAGs not specific to Astronomer CLI operations.

## Prerequisites

- Astro CLI (`astro`) must be installed.

## Core Process

1. Use `astro login` to authenticate before attempting API or deployment commands.
2. For API requests, use `astro api` instead of `curl` for automatic authentication handling.

## Step-by-Step Workflows

### Executing Airflow REST API calls via Astro CLI

The `astro api airflow` command is a convenient wrapper around the Airflow REST API that automatically handles authentication for your currently active Astro workspace/deployment context.

Examples:
- **Get a DAG**: `astro api airflow get_dag -a <dag_id>`
- **Patch a DAG**: `astro api airflow patch_dag -a <dag_id> -d '{"is_paused": false}'`
- **Trigger a DAG Run**: `astro api airflow trigger_dag_run -a <dag_id> -d '{"conf": {"my_param": "value"}}'`

### Managing Local Environment

- **Start local Airflow**: `astro dev start`
- **Stop local Airflow**: `astro dev stop`
- **Restart local Airflow**: `astro dev restart`
- **Kill local Airflow**: `astro dev kill`
- **View logs**: `astro dev logs`
- **Access container shell**: `astro dev bash`
- **Run Airflow CLI command**: `astro dev run <command>`

## Common Pitfalls

- **Missing Authentication**: Forgetting to run `astro login` before `astro api` or `astro deployment` commands will result in auth errors.
- **Interactive Hangs**: Avoid running `astro login` or other interactive commands without appropriate non-interactive flags if you are running fully autonomously.

## References

- [Astro CLI llms.txt index](https://www.astronomer.io/docs/astro/cli/llms.txt)
- [Astronomer platform llms.txt](https://www.astronomer.io/llms.txt)
- [Managing Astro Local Environment](https://www.skills.sh/astronomer/agents/managing-astro-local-env)
