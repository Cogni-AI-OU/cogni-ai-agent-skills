# Invoke Custom Agents

**Goal**: Extend agent capabilities via specialized personas, skills, and MCP servers.

## Invariants

- Built-in agents: Explore, Task, General-purpose, Code-review.
- Additional built-in agents (auto-consulted): Research, Rubber duck.
- Custom agents defined via Markdown agent profiles (*.agent.md / CLAUDE.md / AGENTS.md).
- Resolution order: User (`~/.copilot/agents`) > Repository (`.github/agents`) > Organization/Enterprise (`.github-private/agents`).
- System-level overrides repository-level; repository-level overrides organization-level.

## Invocation Methods

```bash
# Interactive: list and select available agents
/agent

# Direct mention in prompt (auto-inferred)
Use the refactoring agent to refactor this code block

# CLI option
copilot --agent=refactor-agent --prompt "Refactor this code block"
```

## Skills

- Custom skills add specialized instructions, scripts, and resources.
- Managed via GitHub CLI (`gh skill`) or manual file placement.

## MCP Servers

- GitHub MCP server pre-configured (enables PR merging, issue management, etc.).
- Add additional MCP servers interactively:

```bash
/mcp add
```

- MCP config stored in `~/.copilot/mcp-config.json` (override via `COPILOT_HOME` env var).
- Fill in server details, use Tab to navigate fields, Ctrl+S to save.

## Agent Storage Locations

| Level | Path | Scope |
|-------|------|-------|
| User | `~/.copilot/agents/` | All projects |
| Repository | `.github/agents/` | Current project |
| Organization/Enterprise | `.github-private/agents/` | All projects under org/enterprise |

## References

- [Invoking custom agents - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents.md)
