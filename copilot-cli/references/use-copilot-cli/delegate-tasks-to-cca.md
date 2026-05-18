# Delegate Tasks to CCA

**Goal**: Hand off tasks to GitHub Copilot Cloud Agent (CCA) for remote, background execution.

## Invariants

- **Autopilot mode**: Runs locally in CLI session with full permissions. Uses local machine resources.
- **`/delegate` command**: Pushes tasks to CCA on GitHub servers. Creates branch, opens draft PR, works in background.
- `/delegate` requires GitHub authentication (BYOK-only mode does not support it).
- Delegate sessions persist even if local machine shuts down.

## Autopilot (Local Autonomous Execution)

```bash
# Interactive: Press Shift+Tab until "autopilot" shown in status bar
# Programmatic:
copilot --prompt "complete the API integration tests" --autopilot --allow-all --autopilot-max-continuations 10
```

- Full permissions required.
- Progress visible in real time in the terminal.

## Delegate to CCA (Remote Execution)

```bash
# Slash command
/delegate complete the API integration tests and fix any failing edge cases

# Shorthand prefix
& complete the API integration tests and fix any failing edge cases
```

### Delegate Workflow

1. Copilot asks to commit unstaged changes as checkpoint in a new branch.
2. CCA opens a draft PR on GitHub.
3. CCA works in background making changes.
4. CCA requests review from you once complete.
5. Copilot provides link to the PR and agent session on GitHub.

## References

- [Delegating tasks to GitHub Copilot - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/delegate-tasks-to-cca.md)
