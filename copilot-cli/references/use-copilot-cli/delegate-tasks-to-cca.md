# Delegate Tasks to CCA

**Goal**: Hand off tasks to GitHub Copilot Cloud Agent (CCA) for remote, background execution.

## Invariants

- Runs remotely on GitHub's servers.
- Automatically creates a branch and opens a draft Pull Request.
- Works in the background even if local machine is shut down.
- Requires GitHub authentication (BYOK-only mode does not support `/delegate`).

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# Delegate via slash command
/delegate "complete the API integration tests"

# Delegate via shorthand prefix
& "fix failing edge cases"
```

## Local Alternative: Autopilot

- Runs locally in the current CLI session.
- Requires full permissions.
- Enabled via `Shift+Tab` (Interactive) or `--autopilot` (Programmatic).

## References

- [Delegating tasks to GitHub Copilot](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/delegate-tasks-to-cca.md)
