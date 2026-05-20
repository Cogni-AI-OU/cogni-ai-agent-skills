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

1. **Diverse Source Formats**: Add skills from GitHub, GitLab, Bitbucket, or local paths.
   ```bash
   # GitHub shorthand
   npx skills add vercel-labs/agent-skills
   # Full GitHub URL
   npx skills add https://github.com/vercel-labs/agent-skills
   # Direct path to a skill in a repo
   npx skills add https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines
   # GitLab URL
   npx skills add https://gitlab.com/org/repo
   # Local path
   npx skills add ./my-local-skills
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
5. **Force Copying**: Use `--copy` to copy files instead of symlinking (default).
   ```bash
   npx skills add vercel-labs/agent-skills --copy
   ```

### Manage Skills

1. **List Installed Skills**:
   ```bash
   # List all installed skills (project and global)
   npx skills list
   # List only global skills
   npx skills ls -g
   # Filter by specific agents
   npx skills ls -a claude-code -a cursor
   ```
2. **Update Skills**: Update all installed skills or specific ones.
   ```bash
   # Update all skills (interactive scope prompt)
   npx skills update
   # Update specific skill(s)
   npx skills update frontend-design web-design-guidelines
   # Update only global or project skills
   npx skills update -g
   npx skills update -p
   # Non-interactive update
   npx skills update -y
   ```
3. **Remove Skills**:
   ```bash
   # Remove interactively
   npx skills remove
   # Remove specific skill(s)
   npx skills remove web-design-guidelines
   # Remove from global scope
   npx skills remove --global web-design-guidelines
   # Remove from specific agents only
   npx skills remove --agent claude-code my-skill
   # Remove all installed skills without confirmation
   npx skills remove --all
   ```
4. **Search Skills**:
   ```bash
   # Interactive fzf-style search
   npx skills find
   # Search by keyword
   npx skills find typescript
   ```

### Scaffold Skills

1. **Initialize New Skill**: Create a boilerplate `SKILL.md` in the current directory or a new subdirectory.
   ```bash
   npx skills init
   npx skills init <skill-name>
   ```

## Examples

```bash
# List skills in a repository without installing
npx skills add vercel-labs/agent-skills --list

# Install specific skills from a repository
npx skills add vercel-labs/agent-skills --skill frontend-design --skill skill-creator

# Install a skill with spaces in the name (must be quoted)
npx skills add owner/repo --skill "Convex Best Practices"

# Install to specific agents
npx skills add vercel-labs/agent-skills -a claude-code -a opencode

# Non-interactive installation (CI/CD friendly)
npx skills add vercel-labs/agent-skills --skill frontend-design -g -a claude-code -y

# Install all skills from a repo to all agents
npx skills add vercel-labs/agent-skills --all

# Update only global skills non-interactively
npx skills update -g -y

# Remove all installed skills from a specific agent
npx skills remove --skill '*' -a cursor

# Remove a specific skill from all agents (global and project)
npx skills remove my-skill --agent '*' --yes

# Remove multiple skills at once
npx skills remove frontend-design web-design-guidelines

# Use 'rm' alias to remove a skill
npx skills rm my-skill
```

## Environment Variables

| Variable | Description |
| -------- | ----------- |
| `INSTALL_INTERNAL_SKILLS` | Set to `1` or `true` to show and install skills marked as `internal: true`. |
| `DISABLE_TELEMETRY` | Set to `1` to disable anonymous usage telemetry. |

Example:
```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add vercel-labs/agent-skills --list
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
  *Prevention*: Always quote names with spaces (e.g., `"Convex Best Practices"`) and asterisks (e.g., `--skill '*'`).

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
