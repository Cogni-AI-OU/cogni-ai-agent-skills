# Steer Remotely

**Goal**: Orchestrate Copilot CLI autonomous workflows across remote boundary environments (Codespaces, SSH servers).

### Invariants
- Authentication states must persist or forward across SSH/Codespace boundaries safely.
- Remote workspaces command standard tool access without local host violations.

### Schema / Configuration
- Primarily impacts Codespace integrations and remote GitHub automation.
- Relies on headless Auth mechanisms `GH_TOKEN`.

### Commands / Execution
```bash
# Invoke CLI on remote target headless execution
gh copilot --prompt "Audit environment"
```

## References
- [Steer Remotely](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/steer-remotely.md)