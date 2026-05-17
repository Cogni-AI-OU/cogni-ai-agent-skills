# Invoke Custom Agents

**Goal**: Extend agent capabilities via specialized personas, instructions, and toolsets.

## Invariants

- Built-in agents: Explore, Task, General-purpose, Code-review, Research, Rubber duck.
- Custom agents defined via Markdown agent profiles.
- Resolution order: User (`~/.copilot/agents`) > Repository (`.github/agents`) > Organization (`.github-private/agents`).
- System-level agents override repository-level agents.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# List available agents interactively
/agent

# Invoke specific agent programmatically
copilot --agent=refactor-agent --prompt "Refactor this code block"

# Direct mention in prompt
"Use the refactoring agent to refactor this code block"
```

## References

- [Invoking custom agents](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents.md)
