# Agent Skills

Agent Skills are folders of instructions, scripts, and resources that GitHub
Copilot can load when relevant to improve its performance in specialized tasks.

Agent Skills work with:

- [Copilot coding agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent)
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- Agent mode in Visual Studio Code

For more information, see
[About Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).

## Skills catalog

The full, machine-readable list of skills lives in [AGENTS.md](AGENTS.md). Use it when you need the
authoritative catalog for agent loading. This README stays human-focused.

## Creating skills

Each skill lives in its own subdirectory and must contain a `SKILL.md` file with
YAML frontmatter:

```markdown
---
name: my-skill-name
description: Brief description of when Copilot should use this skill
license: MIT
---

Instructions for Copilot to follow when this skill is activated.
```

### SKILL.md frontmatter

| Field | Required | Description |
| ----- | -------- | ----------- |
| `name` | Yes | Unique identifier (lowercase, hyphens for spaces) |
| `description` | Yes | What the skill does and when to use it |
| `license` | No | License that applies to this skill |

### Skill locations

Skills can be stored at different levels:

| Level | Location | Scope |
| ----- | -------- | ----- |
| Project | `.github/skills/` or `.claude/skills/` | Single repository |
| Personal | `~/.copilot/skills/` or `~/.claude/skills/` | All projects (CLI only) |

## How Copilot uses skills

Copilot decides when to use skills based on your prompt and the skill's
description. When activated, the `SKILL.md` file is injected into the agent's
context, providing access to your instructions and any scripts or examples in
the skill's directory.

## Skills vs custom instructions

- **Custom instructions** (`copilot-instructions.md`): Simple guidance relevant
  to almost every task (coding standards, repository conventions)
- **Skills**: Detailed instructions that Copilot accesses only when relevant to
  a specific task

## Community resources

Find and share skills with the community:

- [anthropics/skills](https://github.com/anthropics/skills) - Reference skills
  repository
- [github/awesome-copilot](https://github.com/github/awesome-copilot) - Community
  collection of Copilot resources
