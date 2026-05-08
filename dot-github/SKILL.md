---
name: dot-github
description: >-
  Standardize `.github` directory structure, enforce agentic documentation patterns.
  Must load when creating or updating files in `.github/` dir.
---
# Skill: dot-github

<!-- markdownlint-disable MD013 MD023 MD031 MD032 MD033 -->

Standardize `.github` directory structure, enforce agentic documentation patterns.

## Core Principles

- **Configuration Validation**:
  Validate `.github/mcp-config.json` if the file exists.
- **Disabling Workflows**:
  To temporarily disable workflows, consider moving them to `.github/workflows-disabled/`.
- **Do Not Invent CODEOWNERS**:
  Never guess or invent teams in `CODEOWNERS` when they are unknown. Only use verified, existing teams.
- **Agentic Instructions (`AGENTS.md`)**:
  - Use `.github/AGENTS.md` to describe the structure of the `.github` directory and its contents (agents, instructions, prompts, skills).
  - Use `.github/workflows/AGENTS.md` to list workflows that can be triggered manually (crucial when the agent has actions write permissions).
  - Document available prompts in `.github/prompts/AGENTS.md` and specify when to load them.
  - Document instruction scopes in `.github/instructions/AGENTS.md`.
- **Upstream Organization Fallbacks**:
  If an org/owner-level `.github` repository exists,
  follow its upstream guides instead of creating local duplicates (e.g., `CONTRIBUTING.md`, `ISSUE_TEMPLATE/`).
- **Workflow Documentation**:
  Document the list of available workflows in `.github/workflows/README.md`.

## Firewall

To document encountered restrictive firewall during runtime, this can be documented in `.github/FIREWALL.md`, e.g.

````markdown
# Firewall Allowlist

If your agent runs behind a restrictive firewall, allow these hosts.
Always check the official guidance for updates.

```plaintext
agents.md
aka.ms
gh.io
ghcr.io
github.com
img.shields.io
pkg-containers.githubusercontent.com
raw.githubusercontent.com
support.github.com
tldrlegal.com
uploads.github.com
user-images.githubusercontent.com
yaml-multiline.info
web.archive.org
```

Note: Keep the list sorted alphabetically for easier maintenance.

Reference: <https://gh.io/copilot/firewall-config>
````

## Hardened NEVER List

- **NEVER create `.github/README.md`**:
  GitHub renders `.github/README.md` with the highest priority.
  Creating it will override the main `README.md` on the repository homepage and profile page.
- **Do not break your own workflow**:
  Refactoring, such as removing required triggers, can prevent the workflow from being triggered again.
  Always be careful and double-check your changes to ensure the continuity of your own runtime workflow.

## What to Avoid

- Creating undocumented workflows in `.github/workflows/`.
- Deleting workflows instead of moving them to `.github/workflows-disabled/`.
- Overwriting upstream organization defaults in `.github/` repo.

## Related Skills

- **agents-md-writer**: Must be loaded when creating or updating `AGENTS.md` files.
- **docs-writer**: Must be loaded when asked to write, document, or generate new documentation.
