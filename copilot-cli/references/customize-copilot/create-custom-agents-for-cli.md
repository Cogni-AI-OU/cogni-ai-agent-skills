# Create Custom Agents for CLI

**Goal**: Deploy specialized subagents with scoped context, tailored expertise, and restricted toolsets.

## Invariants

- Defined via `.agent.md` files.
- Location: `~/.copilot/agents/` (User) or `.github/agents/` (Project).
- Subagents run in a separate context to avoid main agent clutter.
- Resolution order: User > Repository > Organization.

## Schema (if applicable)

- Frontmatter defines metadata, description, and tools.

```markdown
---
name: security-expert
description: Reviews code for vulnerabilities.
tools: ["bash", "edit", "view"]
---
Instructions for the agent...
```

## Commands / Execution (if applicable)

```bash
# Create agent interactively
/agent -> "Create new agent"

# Invoke specifically
copilot --agent security-expert --prompt "Audit src/"

# Use via slash command
/agent -> [Select Agent]
```

## References

- [Creating and using custom agents for GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md)
