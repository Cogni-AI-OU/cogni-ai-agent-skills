# Configure Copilot CLI

**Goal**: Manage trusted directories, tool access, path permissions, and URL boundaries.

## Invariants

- Default access: current working directory, subdirectories, and system temp directory.
- Trusted directories prevent unauthorized file access.
- Tool permissions can be session-based or permanent.
- URL boundary checks apply to `web_fetch` and common shell commands (`curl`, `wget`).

## Schema (if applicable)

- Config File: `~/.copilot/config.json` (configurable via `COPILOT_HOME`).
- `trustedFolders`: Array of directory paths in `config.json`.

## Commands / Execution (if applicable)

```bash
# Allow all tools, paths, and URLs (YOLO mode)
copilot --yolo --prompt "Perform task"

# Allow specific tool
copilot --allow-tool='shell(git push)'

# Deny specific tool
copilot --deny-tool='shell(rm)'

# Allow/Deny specific domains
copilot --allow-url=github.com --deny-url=google.com

# Disallow temp directory
copilot --disallow-temp-dir
```

## References

- [Configuring GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli.md)
