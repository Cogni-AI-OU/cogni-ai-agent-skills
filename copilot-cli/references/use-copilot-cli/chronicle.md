# Chronicle

**Goal**: Track, query, and resume historical Copilot CLI execution sessions.

### Invariants
- Execution state must be persisted automatically for temporal navigation.
- Sensitive output must not be leaked when sharing session history.

### Schema / Configuration
- Sessions are tracked via unique temporal IDs.
- Enables contextual continuity across intermittent executions.

### Commands / Execution
```bash
# View session history
gh copilot history

# Resume a previous contextual session
gh copilot resume <SESSION_ID>
```

## References
- [Chronicle](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle.md)