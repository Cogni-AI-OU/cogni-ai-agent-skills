# Steer Agents

**Goal**: Control the execution logic, constraints, and decision loops of autonomous CLI agents.

### Invariants
- Feedback loops must be explicitly manageable mid-flight.
- Context injection via instructions overrides default agent drift.

### Schema / Configuration
- Implements prompt injection directives or mid-execution interruption.

### Commands / Execution
```bash
# Inject explicit constraint boundary
gh copilot --prompt "Refactor this file, but DO NOT modify imports"
```

## References
- [Steer Agents](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/steer-agents.md)