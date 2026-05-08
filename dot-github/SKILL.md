---
name: dot-github
description: Standardize `.github` directory structure, enforce agentic documentation patterns, and prevent creation of conflicting files like `.github/README.md`.
---
# Skill: dot-github

<!-- markdownlint-disable MD013 MD023 MD031 MD032 MD033 -->

Standardize `.github` directory structure, enforce agentic documentation patterns, and prevent creation of conflicting files like `.github/README.md`.

## Core Principles

- **Do Not Invent CODEOWNERS**: Never guess or invent teams in `CODEOWNERS` when they are unknown. Only use verified, existing teams.
- **Workflow Documentation**: Document the list of available workflows in `.github/workflows/README.md`.
- **Agentic Instructions (`AGENTS.md`)**:
  - Use `.github/AGENTS.md` to describe the structure of the `.github` directory and its contents (agents, instructions, prompts, skills).
  - Use `.github/workflows/AGENTS.md` to list workflows that can be triggered manually (crucial when the agent has actions write permissions).
  - Document available prompts in `.github/prompts/AGENTS.md` and specify when to load them.
  - Document instruction scopes in `.github/instructions/AGENTS.md`.
- **Configuration Validation**: Validate `.github/mcp-config.json` if the file exists.
- **Upstream Organization Fallbacks**: If an org/owner-level `.github` repository exists, follow its upstream guides instead of creating local duplicates (e.g., `CONTRIBUTING.md`, `ISSUE_TEMPLATE/`).
- **Disabling Workflows**: Instead of deleting or commenting out workflows, consider moving disabled workflows to `.github/workflows-disabled/`.

## Hardened NEVER List

- **NEVER create `.github/README.md`**: GitHub renders `.github/README.md` with the highest priority. Creating it will override the main `README.md` on the repository homepage and profile page. (See: https://github.com/Cogni-AI-OU/.github/blob/161f41dd87ff54d271677054a71be817669cea79/.github/AGENTS.md?plain=1#L27)

## What to Avoid

- Overwriting upstream organization defaults in `.github/` repo.
- Creating undocumented workflows in `.github/workflows/`.
- Deleting workflows instead of moving them to `.github/workflows-disabled/`.

## Related Skills

- **agents-md-writer**: Must be loaded when creating or updating `AGENTS.md` files.
- **docs-writer**: Must be loaded when asked to write, document, or generate new documentation.
