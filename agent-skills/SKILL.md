---
name: agent-skills
description: Provide expert-level guidance on creating, locating, and installing Agent Skills in project-specific or personal directories, and using the `gh skill` CLI for management.
---

# Agent Skills

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Provide guidance on creating, installing, and managing Copilot Agent Skills to improve its performance in specialized tasks. The Agent Skills specification is an open standard used by various AI systems.

## Core Process

1. **Determine Scope**: Decide if the skill should be project-specific (`.github/skills`, `.claude/skills`, `.agents/skills`) or personal (`~/.copilot/skills`, `~/.agents/skills`).
2. **Scaffold Skill**: Create a new folder for the skill containing instructions, scripts, and necessary resources.
3. **Install from GitHub**: Use `gh skill` to discover and install skills from external repositories (e.g., `github/awesome-copilot` or `anthropics/skills`).
4. **Load & Test**: Ensure the AI system is configured to load the path correctly.

## Core Principles

- **Open Standard**: Rely on the open standard (`github.com/agentskills/agentskills`) for structure and specifications.
- **Portability**: Keep scripts self-contained within the skill folder to allow sharing.
- **Reusability**: Use personal folders for cross-project utility and project folders for context-specific tasks.

## Commands / Usage Patterns

- **Install Skill via CLI**: `gh skill install <repository>`
- **List Installed Skills**: `gh skill list`
- **Search for Skills**: `gh skill search <keyword>`

## Diagnostics and Troubleshooting

- If a skill isn't loading, check if the folder path is correct (e.g., `.github/skills/`).
- Verify that `gh skill` is authenticated and up to date if installation commands fail.
- Ensure the skill structure adheres to the open standard specifications.

## What to Avoid

- Do not place project-specific skills in global directories.
- Avoid referencing external absolute paths in scripts inside a skill folder, keeping them portable.
- Avoid using undocumented directory locations not supported by the agent mode.

## Limitations

- Organization-level and enterprise-level skills are currently not supported natively but may be in the future.
- Real-time reloading of skills during an active session might require a session restart depending on the client.

## Related Skills

- **skill-writer**:
  You MUST load this skill when creating or updating specific Copilot coding agent skills.
- **gh**:
  You MUST load this skill when interacting with the GitHub CLI to run `gh skill` operations.