# Delegate Tasks to CCA

**Goal**: Route specific high-complexity workloads to dedicated Custom Copilot Agents (CCA).

### Invariants
- Prevents context bloat by compartmentalizing capability sets.
- Subagents must operate tightly within their predefined `AGENTS.md` context.

### Schema / Configuration
- Delegation logic involves recognizing task boundaries and executing the specified internal agent.

### Commands / Execution
```bash
# Explicitly delegate specialized operations
gh copilot --agent <custom-agent-id> --prompt "Execute delegated workload"
```

## References
- [Delegate tasks to CCA](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/delegate-tasks-to-cca.md)