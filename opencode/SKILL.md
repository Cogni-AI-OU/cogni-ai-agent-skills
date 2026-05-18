---
name: opencode
license: MIT
description: >-
  Manage OpenCode configuration, credentials, and OpenCode Zen API access to list available models and navigate XDG-compliant directory structures.
  You MUST load this skill when working with OpenCode configuration or listing models.
---
# opencode Skill

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- When configuring or troubleshooting OpenCode settings, including XDG base directory locations.
- When listing available AI models through the OpenCode Zen API (`/zen/v1/models`).
- When managing OpenCode authentication credentials stored in `~/.local/share/opencode/auth.json`.
- When editing OpenCode configuration files (`opencode.json` or `opencode.jsonc`) in `~/.config/opencode/`.
- When verifying OpenCode's directory structure for cache, data, config, and state locations.
- When debugging OpenCode XDG path resolution issues caused by custom `XDG_*` environment variables.

## When Not to Use
- When working with OpenCode's agent definitions, subagents, skills, plugins, or MCP server configurations — use the **customize-opencode** skill instead.
- When the user is not specifically asking about OpenCode tooling — this skill is narrowly scoped to OpenCode configuration and API access.
- When managing general GitHub CLI operations — use the **gh** skill for that.
- When the user is writing their own application code that merely uses OpenCode as a dependency.

## Common Pitfalls
- OpenCode uses XDG base directories exclusively — do NOT look for `~/.opencode/` as it does not exist in modern installations.
- Auth credentials (`auth.json`) live in `~/.local/share/opencode/`, NOT in `~/.config/opencode/` — confusing data and config directories is the most common mistake.
- The Zen API endpoint (`https://opencode.ai/zen/v1/models`) may require network access that is blocked in sandboxed or firewalled environments.
- Environment variables like `XDG_CONFIG_HOME`, `XDG_DATA_HOME`, etc. override default paths — always check their values before assuming standard locations.

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
