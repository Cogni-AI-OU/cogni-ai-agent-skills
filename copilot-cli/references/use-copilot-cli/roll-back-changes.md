# Roll Back Changes

**Goal**: Revert codebase mutations or faulty command executions executed by Copilot CLI agents.

### Invariants
- Copilot CLI agents execute state mutations; rollback paths must be clearly identifiable.
- Uses native Git mechanics to ensure absolute consistency.

### Schema / Configuration
- State reversions target explicit temporal session hashes or standard Git tracking.

### Commands / Execution
```bash
# Check repository diffs after an agentic execution
git diff

# Rollback uncommitted changes
git checkout -- .
```

## References
- [Roll Back Changes](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/roll-back-changes.md)