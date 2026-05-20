---
name: npx-skills
description: 'Install, find, update, and manage agent skills using the npx skills CLI tool. You MUST load this skill when asked to use the npx skills command.'
license: MIT
---

# npx-skills

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- **Skill Discovery & Search**: Searching the skills ecosystem via `npx skills find`.
- **Skill Installation**: Installing open agent skills from repositories (e.g., `vercel-labs/agent-skills`) for various autonomous agents.
- **Skill Updates**: Updating previously installed skills via `npx skills update`.
- **Skill Scaffolding**: Initializing a new agent skill boilerplate via `npx skills init`.

## When Not to Use

- **Content Creation**: Do not use this skill to write the internal markdown content of `SKILL.md` files (use `agent-skill-md-writer` or `agentskills` instead).

## Core Process

### Install Skills

1. **Repository Installation**: Add skills from a GitHub repo shorthand or URL.
   ```bash
   npx skills add vercel-labs/agent-skills
   ```
2. **Target Specific Agents**: Use `-a` or `--agent` to install to specific agents (e.g., `claude-code`, `opencode`, `cursor`, `github-copilot`).
   ```bash
   npx skills add vercel-labs/agent-skills -a claude-code -a opencode
   ```
3. **Target Specific Skills**: Use `-s` or `--skill` to limit which skills to install from a repository.
   ```bash
   npx skills add vercel-labs/agent-skills --skill frontend-design
   ```
4. **Global Installation**: Use `-g` or `--global` to install the skill globally across all projects for the user.
   ```bash
   npx skills add vercel-labs/agent-skills -g
   ```

### Manage Skills

1. **List Installed Skills**:
   ```bash
   npx skills list
   npx skills ls -g
   ```
2. **Update Skills**: Update all installed skills or specific ones.
   ```bash
   npx skills update
   npx skills update frontend-design
   ```
3. **Remove Skills**:
   ```bash
   npx skills remove <skill-name>
   ```
4. **Search Skills**:
   ```bash
   npx skills find <query>
   ```

### Scaffold Skills

1. **Initialize New Skill**: Create a boilerplate `SKILL.md` in the current directory or a new subdirectory.
   ```bash
   npx skills init
   npx skills init <skill-name>
   ```

## Examples

```
# List skills in a repository
npx skills add vercel-labs/agent-skills --list

# Install specific skills
npx skills add vercel-labs/agent-skills --skill frontend-design --skill skill-creator

# Install a skill with spaces in the name (must be quoted)
npx skills add owner/repo --skill "Convex Best Practices"

# Install to specific agents
npx skills add vercel-labs/agent-skills -a claude-code -a opencode

# Non-interactive installation (CI/CD friendly)
npx skills add vercel-labs/agent-skills --skill frontend-design -g -a claude-code -y

# Install all skills from a repo to all agents
npx skills add vercel-labs/agent-skills --all

# Install all skills to specific agents
npx skills add vercel-labs/agent-skills --skill '*' -a claude-code

# Install specific skills to all agents
npx skills add vercel-labs/agent-skills --agent '*' --skill frontend-design
```

## Core Principles

- **Automatic Discovery**: The CLI detects installed agents automatically; manually specifying `-a` is only needed to override this.
- **Symlinking Strategy**: Interactive installations use symlinks by default (creating a canonical copy linked from agent directories). Use `--copy` to force copying.
- **Scope Awareness**: Project scope is default. It commits skills within `.agents/skills/` (or agent-specific paths). Global scope (`-g`) applies across all projects.
- **Non-Interactive Execution**: When executing via an autonomous agent, use the `-y` or `--yes` flag to bypass all confirmation prompts.

## Limitations

- Connecting to remote repositories or the `skills.sh` registry requires an active internet connection.
- Global installation might require correct filesystem permissions for the user's home directory.

## Common Pitfalls

- **Hangs on Interactive Prompts**: Forgetting to use the `-y` flag in automated agent workflows.
  *Prevention*: Always append `-y` or `--yes` for CI/CD or agent-driven non-interactive execution.
- **Unquoted Spaces or Wildcards**: The shell prematurely expanding `*` or mishandling spaces in skill names.
  *Prevention*: Always quote names with spaces (e.g., `"Convex Best Practices"`) and asterisks (e.g., `--skill '\*'`).

## Related Skills

- **agent-skill-md-writer**:
  You MUST load this skill when creating or updating `SKILL.md` files.
- **agentskills**:
  You MUST load this skill to understand the technical structure of an agent skill.

## References

- [The Open Agent Skills Ecosystem](https://www.skills.sh/)
- [Official skills from the companies and organizations](https://www.skills.sh/official)
- [CLI Reference](https://www.skills.sh/docs/cli)
- <https://github.com/vercel-labs/skills>
