# Use Hooks

**Goal**: Execute custom shell commands at specific agent lifecycle events.

## Invariants

- Repository-level hooks: `.github/hooks/*.json`.
- User-level hooks: `~/.copilot/hooks/*.json`.
- Windows requires PowerShell 7.0+.
- Timeout defaults apply to command execution.

## Schema (if applicable)

```json
{
  "version": 1,
  "hooks": {
    "agentStop": [
      {
        "type": "command",
        "bash": "afplay /path/to/sound.aiff",
        "timeoutSec": 5
      }
    ],
    "sessionEnd": [ ... ]
  }
}
```

## Commands / Execution (if applicable)

- **Supported Events**: `agentStart`, `agentStop`, `taskStart`, `taskStop`, `sessionStart`, `sessionEnd`.
- Hooks are triggered automatically by the CLI based on configuration.

## References

- [Using hooks with GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/use-hooks.md)
