# Install Copilot CLI

**Goal**: Deploy the GitHub Copilot CLI securely onto the host environment.

## Invariants

- Requires Node.js 22+ for npm installation.
- Support for WinGet, Homebrew, npm, and direct install scripts.
- Fine-grained PATs require "Copilot Requests" permission.
- Authenticate via OAuth device flow or PAT.

## Schema (if applicable)

- Binary name: `copilot`.
- Home directory: `~/.copilot/` (configurable via `COPILOT_HOME`).
- Trusted directories stored in `~/.copilot/config.json`.

## Commands / Execution (if applicable)

```bash
# Install via npm (Recommended)
npm install -g @github/copilot

# Install via script (macOS/Linux)
curl -fsSL https://gh.io/copilot-install | bash

# Authenticate
copilot login
```

## References

- [Installing GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli.md)
