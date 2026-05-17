# Chronicle

**Goal**: Leverage historical session data for insights, standup reports, and instruction optimization.

## Invariants

- Session data is stored locally.
- Provides personalized tips based on actual usage patterns.
- Identifies "friction signals" to improve custom instructions.
- Full-text search across session history for recalling past work.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# Generate standup report (last 24h)
/chronicle standup

# Get personalized usage tips
/chronicle tips

# Improve custom instructions based on friction
/chronicle improve

# Resume specific session
copilot --resume SESSION-ID

# Rename current session
/rename "New Session Name"

# Share session to Gist/File
/share gist
/share file [PATH]
```

## References

- [Using GitHub Copilot CLI session data](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle.md)
