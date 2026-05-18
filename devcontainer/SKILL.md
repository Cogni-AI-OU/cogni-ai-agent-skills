---
name: devcontainer
description: Create, update, and maintain robust devcontainer.json configurations and lifecycle scripts for reproducible development environments.
license: MIT
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
  - `updateContentCommand`: Background OS-level or build-time setups that run after the workspace is mounted.
  - `postCreateCommand`: Installing project-level dependencies like `npm install` or `pip install -r requirements.txt` and foreground commands like `pre-commit install` (ensures full workspace availability; `updateContentCommand` can sometimes execute too early).
- **Root vs RemoteUser**: Execute system installs as `root` (e.g., using `sudo` if `remoteUser` is `vscode`) and user installs (e.g., Python packages) as the `remoteUser`.
- **Reproducibility**: Pin feature versions and base image tags (e.g., `:jammy` instead of `:latest`).

## Example: devcontainer.json

```jsonc
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/ubuntu
{
  "name": "Dev Container (Python & Ansible)",
  // "build": {
  //   "dockerfile": "Dockerfile",
  //   // Update 'VARIANT' to pick an Ubuntu version: jammy / ubuntu-22.04, focal / ubuntu-20.04, bionic / ubuntu-18.04
  //   // Use ubuntu-22.04 or ubuntu-18.04 on local arm64/Apple Silicon.
  //   // "args": { "VARIANT": "ubuntu-22.04" }
  // },

  // Configure tool-specific properties.
  // Note: Keep the list in alphabetical order.
  "customizations": {
    "vscode": {
      "extensions": [
        "bierner.markdown-mermaid",
        "DavidAnson.vscode-markdownlint",
        "GitHub.copilot",
        "GitHub.copilot-chat",
        "GitHub.vscode-github-actions",
        "ms-vscode.vscode-chat-customizations-evaluations",
        "vscodevim.vim",
        "vsls-contrib.codetour",
        "xaver.clang-format"
      ],
      "settings": {
        "editor.formatOnSave": true,
        "python.defaultInterpreterPath": "/usr/local/bin/python"
      }
    }
  },
  // Features to add to the dev container. More info: https://containers.dev/features.
  "features": {
    "ghcr.io/devcontainers-contrib/features/actionlint:1": {},
    "ghcr.io/devcontainers-contrib/features/node-asdf:0": {},
    "ghcr.io/devcontainers-extra/features/pipx-package:1": {},
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/python:1": {},
    "ghcr.io/guiyomh/features/vim:0": {},
    "ghcr.io/jungaretti/features/make:1": {},
    "ghcr.io/jungaretti/features/ripgrep:1": {},
    "ghcr.io/sliekens/devcontainer-features/opencode:1": {}
  },

  // Pre-create opencode directories on host before container starts (required for bind mounts)
  "initializeCommand": "mkdir -p \"$HOME/.local/share/opencode\" \"$HOME/.config/opencode\"",

  // Use 'forwardPorts' to make a list of ports inside the container available locally.
  // Note: Keep examples generic and repository-agnostic; add repo-specific setup only when those files and tools are guaranteed to exist.
  // "forwardPorts": [],

  // Use 'postCreateCommand' to run commands after the container is created.
  // "postCreateCommand": "uname -a",

  // Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
  "image": "mcr.microsoft.com/devcontainers/base:jammy",

  "postCreateCommand": "pip install -r requirements.txt || npm install || true",

  // Comment out to connect as root instead. More info: https://aka.ms/vscode-remote/containers/non-root.
  "remoteUser": "vscode",
  // Note: Python dependencies can be added in the `requirements.txt` file.
  "onCreateCommand": "sudo apt-get update && if [ -f .devcontainer/apt-packages.txt ]; then xargs -a .devcontainer/apt-packages.txt sudo apt-get install -y; fi"
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

- **yaml**: You MUST load this skill when formatting or linting YAML configurations related to devcontainers.
- **pre-commit**: You MUST load this skill when configuring pre-commit hooks in the devcontainer.
