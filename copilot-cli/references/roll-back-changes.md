# Roll Back Changes

**Goal**: Undo session mutations and restore repository state via automated snapshots.

## Invariants

- Requires Git repository with at least one commit.
- Snapshot created **automatically** at the start of each prompt interaction.
- Rewinding is **PERMANENT**: all snapshots and session history after the rollback point are removed.
- Cannot roll back changes made before the first prompt in a session.
- Cannot roll back to states where snapshot creation was skipped.

## Rollback Triggers

| Method | Trigger |
|--------|---------|
| Double Esc | Press `Esc` twice in quick succession when input area is empty and Copilot is idle. |
| `/undo` | Alternative way to open rewind picker. |
| `/rewind` | Alias for `/undo`. |

## Rewind Picker

- Displays up to **10 most recent snapshots**, with the most recent first.
- Arrow key (`↓`) to scroll to earlier snapshots beyond 10.
- Each snapshot shows the beginning of the associated prompt and relative age.
- Rolling back restores repository to state **immediately before** Copilot started working on that prompt.
- The selected prompt is pre-filled in the input area for editing and resubmission.

## Verification Commands

```bash
# Check modified/staged/untracked files
! git status

# Show current commit SHA and message
! git log --oneline -1

# Review unstaged changes
! git diff
```

## References

- [Rolling back changes made during a GitHub Copilot CLI session - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/roll-back-changes.md)
