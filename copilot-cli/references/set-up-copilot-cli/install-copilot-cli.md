# Install Copilot CLI

**Source**: `github/docs` — Installing GitHub Copilot CLI.

## Prerequisites

- Active Copilot subscription.
- (Windows) PowerShell v6+.
- Org/enterprise policy must not disable Copilot CLI.

## Install Methods

### npm (all platforms)

Prerequisite: Node.js version per `@github/copilot` package requirements.

```bash
npm install -g @github/copilot

# Prerelease version
npm install -g @github/copilot@prerelease
```

Note: If `~/.npmrc` has `ignore-scripts=true`, use:

```bash
npm_config_ignore_scripts=false npm install -g @github/copilot
```

### WinGet (Windows)

```powershell
winget install GitHub.Copilot

# Prerelease
winget install GitHub.Copilot.Prerelease
```

### Homebrew (macOS, Linux)

```bash
brew install copilot-cli

# Prerelease
brew install copilot-cli@prerelease
```

### Install Script (macOS, Linux)

```bash
curl -fsSL https://gh.io/copilot-install | bash
# or
wget -qO- https://gh.io/copilot-install | bash

# Install to /usr/local/bin (root)
curl -fsSL https://gh.io/copilot-install | sudo bash

# Custom directory + specific version
curl -fsSL https://gh.io/copilot-install | VERSION="v0.0.369" PREFIX="$HOME/custom" bash
```

Environment variables for install script:
- `PREFIX`: install prefix (default: `/usr/local` as root, `$HOME/.local` as non-root).
- `VERSION`: specific version to install (default: latest).

### Direct Download

Releases: <https://github.com/github/copilot-cli/releases/>

## Post-Install

On first launch, authenticate:

```bash
copilot login
```

Or set env var with fine-grained PAT (requires **Copilot Requests** permission):

```bash
export COPILOT_GITHUB_TOKEN="github_pat_..."
```

## References

- <https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli.md>
