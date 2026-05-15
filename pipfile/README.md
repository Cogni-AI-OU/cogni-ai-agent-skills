# Pipfile Skill

This skill enables agents to adeptly manage `Pipfile` and `Pipfile.lock` files within Python projects utilizing `pipenv`.

## Overview

Pipenv uses two files to manage project dependencies:
- **`Pipfile`**: A human-readable, TOML-formatted file that declares top-level project dependencies and constraints.
- **`Pipfile.lock`**: An automatically generated JSON file that records exact versions and hashes of all resolved dependencies.

## How to use it

When an agent detects a task relating to Python dependency management, particularly creating, updating, or reviewing a `Pipfile` or `Pipfile.lock`, they should load this skill:

1. **Load Skill**: 
   The agent automatically loads this skill based on the keywords `Pipfile`, `Pipfile.lock`, or `pipenv`.
   
2. **Apply Standards**: 
   The agent will enforce separation between `[packages]` and `[dev-packages]`, rely on the command-line interface (`pipenv install`, `pipenv lock`) for safer modifications, and forbid manual edits to the `Pipfile.lock`.
   
3. **Execute Commands**:
   - `pipenv install <package>` to add a standard dependency.
   - `pipenv install --dev <package>` for dev dependencies.
   - `pipenv lock` to update the `.lock` file.
   - `pipenv sync` or `pipenv install --deploy` to establish the exact environment in CI/CD.

## Repository Setup

This skill is part of the `cogni-ai-agent-skills` repository and should be located in the `pipfile` directory alongside its `SKILL.md` counterpart.