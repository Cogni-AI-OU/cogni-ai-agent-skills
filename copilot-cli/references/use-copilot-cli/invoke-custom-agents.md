# Invoke Custom Agents

**Goal**: Execute and interact with specialized, user-defined agent personas directly from the CLI.

### Invariants
- Agent selection uses strict resolution order: User (`~`) > Project (`.github`) > Org (`.github-private`).
- Must supply the precise agent slug excluding `.agent.md`.

### Schema / Configuration
- Resolution path targeting: `[target].agent.md`.

### Commands / Execution
```bash
# Invoke defined agent persona
gh copilot --agent security-auditor --prompt "Verify codebase boundaries"
```

## References
- [Invoke Custom Agents](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents.md)