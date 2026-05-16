---
name: agentskills
description: Expert-level guidance on the Agent Skills open standard for creating portable, non-interactive, and secure Copilot agent skills.
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# Agent Skills (Standard)

The Agent Skills open standard (`github.com/agentskills/agentskills`) provides a framework for structuring and specifying skills to ensure portability across different AI systems and agent hosts.

## Core Principles

- **Open Standard**: Rely on the open standard for structure and specifications to ensure portability across different AI systems.
- **Portability**: Keep scripts self-contained within the skill folder to allow sharing and avoid referencing external absolute paths.
- **Non-Interactive Execution**: Always design skills for non-interactive flow, using specific arguments or flags to avoid stalling the agent.
- **Pre-flight Inspection**: Always inspect third-party skills before installing to verify content safety and avoid malicious instructions or scripts.
- **Supply Chain Integrity**: Prefer pinning skills to specific tags or commit SHAs to ensure deterministic behavior.
- **Portable Provenance**: Skills should include tracking metadata (repository, ref, tree SHA) in the `SKILL.md` frontmatter to allow tracking even if files are moved.

## Core Process (Manual Creation)

1. **Determine Scope**:
   - **Project-specific**: Stored in `.github/skills/`, `.claude/skills/`, or `.agents/skills/`. Scope is limited to the repository.
   - **Personal**: Stored in `~/.copilot/skills/` or `~/.agents/skills/`. Scope is global for the user's CLI environment.
2. **Scaffold Skill**:
   - Create a directory named after the skill (lowercase-hyphenated).
   - Create a `SKILL.md` file with the required YAML frontmatter (`name`, `description`).
   - Add any supporting scripts or resources within the same directory.
3. **Verify Structure**: Ensure the `SKILL.md` follows the standard sections and style (imperative, dense, expert-level).

## Skill Structure & Formatting

Each skill must contain a `SKILL.md` file with:
- **YAML frontmatter**: Containing `name` and `description`.
- **Imperative Instructions**: Dense, expert-level guidance for the agent.
- **Section Discipline**: Use standard headers like `## Core Process`, `## Core Principles`, `## What to Avoid`.

## Directory Scopes

| Level | Location | Scope |
| :--- | :--- | :--- |
| Project | `.github/skills/` | Single repository |
| Personal | `~/.copilot/skills/` | User-wide (CLI) |
| System | `/usr/share/agents/skills/` | System-wide |

## What to Avoid

- Placing project-specific skills in global directories.
- Referencing external absolute paths in scripts inside a skill folder.
- Hardcoding environment-specific values that break portability.
- Including interactive scripts that require user input.

## References

- [Agent Skills Open Standard](https://github.com/agentskills/agentskills)
- [Documentation](https://agentskills.io) — Guides and tutorials
- [Specification](https://agentskills.io/specification) — Format details
- [Example Skills](https://github.com/anthropics/skills) — See what's possible
- [SKILL.md Specification](https://agents.md/)

## Related Skills

- **skill-writer**:
  You MUST load this skill when creating or updating specific Copilot coding agent skills.
- **gh-skill**:
  You MUST load this skill when using the GitHub CLI to manage Agent Skills.
