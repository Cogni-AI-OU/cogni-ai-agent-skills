# Getting Started with Copilot CLI

**Goal**: Quickly deploy and begin using GitHub Copilot CLI in the terminal.

## Invariants

- Requires active GitHub Copilot subscription.
- Requires directory trust confirmation.
- Copilot won't make changes without explicit approval.

## Installation

```bash
# Cross-platform (npm)
npm install -g @github/copilot

# Windows (WinGet)
winget install GitHub.Copilot

# macOS/Linux (Homebrew)
brew install copilot-cli
```

## Execution

```bash
# Start interactive session
copilot

# Authenticate (first time)
/login

# Programmatic prompt
copilot -p "PROMPT"

# Silent programmatic prompt (output only)
copilot -sp "PROMPT"
```

## Shortcuts

| Shortcut | Action |
| -------- | ------ |
| `Esc` | Cancel operation |
| `Ctrl+C` | Cancel thinking/Clear input/Exit |
| `Ctrl+L` | Clear screen |
| `@` | Mention files for context |
| `/` | Show slash commands |
| `?` | Show tabbed help |

## References

- [Getting started with GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/cli-getting-started.md)
