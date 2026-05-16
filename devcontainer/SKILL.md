---
name: devcontainer
description: Create, update, and maintain robust devcontainer.json configurations and lifecycle scripts for reproducible development environments.
---
# Devcontainer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Create, update, and maintain robust `devcontainer.json` configurations and associated lifecycle scripts (e.g., `onCreateCommand`, `updateContentCommand`, `postCreateCommand`) to ensure reproducible, feature-rich, and secure development environments.

## Core Process

1. **Locate or Create Configuration**: Target `.devcontainer/devcontainer.json` or `.devcontainer/<name>/devcontainer.json`.
2. **Define Base Metadata**: Assign a descriptive `name` and define the base `image` (e.g., `mcr.microsoft.com/devcontainers/base:jammy`).
3. **Configure Features**: Leverage Dev Container Features (`ghcr.io/devcontainers/features/*`) for modular tool installation instead of complex Dockerfiles.
4. **Define Lifecycle Scripts**: Use `onCreateCommand`, `updateContentCommand`, and `postCreateCommand` strategically based on execution timing.
5. **Customize IDE**: Populate `customizations.vscode.extensions` and `customizations.vscode.settings` for a ready-to-use editor experience.

## Core Principles

- **Features over Dockerfiles**: Prefer standardized Dev Container features (e.g., `ghcr.io/devcontainers/features/python:1`) instead of custom `RUN apt-get...` in Dockerfiles for better caching and modularity.
- **Lifecycle Script Separation**:
  - `onCreateCommand`: Background OS-level updates, `apt-get`, or `pipx` installations (runs once when container is created).
  - `updateContentCommand`: Installing project-level dependencies like `npm install` or `pip install -r requirements.txt` (runs when workspace content is available).
  - `postCreateCommand`: Foreground commands like `pre-commit install` or starting background services.
- **Root vs RemoteUser**: Execute system installs as `root` (e.g., using `sudo` if `remoteUser` is `vscode`) and user installs (e.g., Python packages) as the `remoteUser`.
- **Reproducibility**: Pin feature versions and base image tags (e.g., `:jammy` instead of `:latest`).

## Example: Enhanced devcontainer.json

```jsonc
{
  "name": "Project Dev Container",
  "image": "mcr.microsoft.com/devcontainers/base:jammy",
  "remoteUser": "vscode",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/python:1": {
      "version": "latest"
    },
    "ghcr.io/devcontainers-contrib/features/actionlint:1": {},
    "ghcr.io/devcontainers-extra/features/pipx-package:1": {},
    "ghcr.io/prulloac/devcontainer-features/pre-commit:1": {}
  },
  "customizations": {
    "vscode": {
      "settings": {
        "editor.formatOnSave": true,
        "python.defaultInterpreterPath": "/usr/local/bin/python"
      },
      "extensions": [
        "GitHub.copilot",
        "GitHub.copilot-chat",
        "DavidAnson.vscode-markdownlint",
        "xaver.clang-format",
        "vsls-contrib.codetour",
        "bierner.markdown-mermaid"
      ]
    }
  },
  "onCreateCommand": "sudo apt-get update && sudo apt-get install -y --no-install-recommends jq curl && pipx install --include-deps ansible",
  "updateContentCommand": "pip install -r .devcontainer/requirements.txt",
  "postCreateCommand": "pre-commit install"
}
```

## What to Avoid

- **Monolithic Dockerfiles**: Avoid massive custom Dockerfiles unless doing complex system setups unsupported by standard features.
- **Using `latest` Tags**: Avoid `ubuntu:latest` or base images without explicit versions. Prefer stable tags like `jammy`.
- **Long Synchronous Post-Create Commands**: Move long-running OS package installs to `onCreateCommand` or `updateContentCommand` to improve perceived startup time.
- **Hardcoding Workspace Paths**: Avoid hardcoding `/workspaces/...`. Use the `${localWorkspaceFolder}` or `${containerWorkspaceFolder}` variables if needed.

## Limitations

- Agents cannot natively build or attach to the devcontainer to test the environment interactively. Rely on schema validation, JSON linting, and best practices.

## Related Skills

- **json**: You MUST load this skill when formatting or linting `devcontainer.json` files.
- **docker**: You MUST load this skill when creating or modifying custom `Dockerfile` or `docker-compose.yml` configurations for the devcontainer.