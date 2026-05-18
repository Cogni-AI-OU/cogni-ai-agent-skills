---
name: opencode
description: >-
  Manage OpenCode configuration, credentials, and OpenCode Zen API access to list available models and navigate XDG-compliant directory structures.
  You MUST load this skill when working with OpenCode configuration or listing models.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# opencode Skill

OpenCode uses XDG base directories for configuration and data. Access the OpenCode Zen API to list available models.

## OpenCode Zen API

List available models via the OpenCode Zen API:
`https://opencode.ai/zen/v1/models`

## Directory Structure

OpenCode uses XDG base directories instead of a single `~/.opencode` directory:

| Directory                 | Purpose                                                |
| ------------------------- | ------------------------------------------------------ |
| `~/.local/share/opencode` | Data **and** auth credentials (`auth.json` lives here) |
| `~/.config/opencode`      | User configuration (`opencode.json`/`opencode.jsonc`)  |
| `~/.cache/opencode`       | Ephemeral binary cache - not worth persisting          |
| `~/.local/state/opencode` | Runtime state - not worth persisting                   |

## Core Principles

- **XDG Compliance**: Always respect XDG base directory environment variables (`XDG_CONFIG_HOME`, `XDG_DATA_HOME`, etc.) when locating OpenCode files.
- **API First**: Use the OpenCode Zen API for the most up-to-date model information.

## Commands / Usage Patterns

### Listing Models

To list models using `curl` (if available):
```bash
curl https://opencode.ai/zen/v1/models
```

## Related Skills

- **gh**: OpenCode integrates with GitHub CLI for many operations.
