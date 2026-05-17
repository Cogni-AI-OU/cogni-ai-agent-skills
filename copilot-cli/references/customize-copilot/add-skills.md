# Add Agent Skills

**Goal**: Extend agent capabilities via specialized instructions, scripts, and resources.

## Invariants

- Skills are folders containing a `SKILL.md` file.
- Location: `~/.copilot/skills/` (User) or `.github/skills/` (Project).
- Trigger: Mention skill name with `/` prefix in prompt (e.g., `/frontend-design`).
- Comparison: Skills are lighter than agents and don't require separate subagent processes.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# List available skills
/skills list

# Show skill info and location
/skills info SKILL-NAME

# Add a new skills directory
/skills add /path/to/dir

# Reload skills without restarting
/skills reload

# Remove a skill
/skills remove /path/to/skill-dir
```

## References

- [Adding agent skills for GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md)
