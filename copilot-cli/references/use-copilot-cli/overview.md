# Overview

**Goal**: Establish foundational usage, interactions, and core capabilities of the GitHub Copilot CLI.

## Invariants

- Requires active GitHub Copilot subscription.
- Requires directory trust confirmation before operation.
- Interactive mode supports slash commands (e.g., `/login`, `/skills`, `/mcp`).
- Plan mode enabled via `Shift+Tab`.
- Reasoning visibility toggled via `Ctrl+T`.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# Start interactive session
copilot

# Run specific prompt programmatically
copilot --prompt "Fix the bug in @src/app.js"

# Resume most recent local session
copilot --continue

# Show help
copilot help
```

## Key Interactive Features

- **File Context**: Use `@path/to/file` in prompts to include file contents.
- **Direct Shell**: Use `!` prefix to execute shell commands directly.
- **Autopilot**: Toggle local autonomous execution via `Shift+Tab`.
- **Delegation**: Use `/delegate` or `&` prefix to offload tasks to GitHub.

## References

- [Using GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/overview.md)
