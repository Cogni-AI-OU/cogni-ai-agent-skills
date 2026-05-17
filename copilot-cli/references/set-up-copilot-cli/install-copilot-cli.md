# Install Copilot CLI

**Goal**: Deploy the GitHub Copilot CLI extension securely onto the host environment.

### Invariants
- Requires the baseline `gh` (GitHub CLI) to be installed beforehand.
- The Copilot CLI runs as an operational extension (`gh-copilot`) to the GitHub CLI.

### Schema / Configuration
- Once installed, the extension commands are scoped under `gh copilot`.

### Commands / Execution
```bash
# Install the extension via GitHub CLI
gh extension install github/gh-copilot

# Upgrade an existing installation
gh extension upgrade gh-copilot
```

## References
- [Install Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli.md)