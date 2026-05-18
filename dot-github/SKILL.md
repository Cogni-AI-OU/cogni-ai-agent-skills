---
name: dot-github
description: 'Standardize `.github` directory structure, enforce agentic documentation patterns. You MUST load this skill when creating or updating files in `.github/` dir.'
license: MIT
---
# Skill: dot-github

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Creating or updating the `.github` directory structure for a new or existing repository.
- Adding or modifying AGENTS.md files within `.github/` subdirectories (workflows, prompts, instructions).
- Configuring CODEOWNERS, workflow files, issue templates, or other `.github` governance files.
- Setting up firewall documentation in `.github/FIREWALL.md` for agentic workflows.
- Standardizing agentic documentation patterns across a repository or organization.

## When Not to Use

- Editing the main repository README or project-level documentation outside `.github/` — use `docs-writer` instead.
- Modifying CI/CD workflow logic — use `github-actions` or `gh-aw` skills for workflow content changes.
- Writing agent skill files (`SKILL.md`) or instructions (`*.instructions.md`) — those belong in the repo root, not `.github/`.
- Creating `.github/README.md` — this overrides the main repository README on the GitHub homepage.

## Gotchas

- Creating `.github/README.md` is a hard NEVER — GitHub renders it with the highest priority, completely overriding the main project README.md on the repository homepage.
- Refactoring workflow triggers (e.g., removing required pull_request events) can silently break your own runtime workflow — always double-check that your CI/CD pipeline remains triggerable.
- Never guess or invent team names in CODEOWNERS — only reference verified existing teams to avoid broken ownership rules.
- Moving workflows to `.github/workflows-disabled/` is preferred over deleting them, as it preserves history and allows easy re-enablement.

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

- **agents-md-writer**: You MUST load this skill when creating or updating `AGENTS.md` files.
- **docs-writer**: You MUST load this skill when asked to write, document, or generate new documentation.
