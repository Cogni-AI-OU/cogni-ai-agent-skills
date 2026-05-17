# Roll Back Changes

**Goal**: Undo session mutations and restore repository state via automated snapshots.

## Invariants

- Requires Git repository with at least one commit.
- Snapshots created automatically at each prompt.
- Rewinding is PERMANENT; subsequent history is removed.
- Cannot undo changes made before the current session started.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

- **Trigger**: Press `Esc` twice in quick succession or use `/undo` / `/rewind`.
- **Review**: The rewind picker shows the 10 most recent snapshots.

```bash
# Verify state after rollback
! git status
! git log --oneline -1
```

## References

- [Rolling back changes made during a GitHub Copilot CLI session](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/roll-back-changes.md)
