# Configure Copilot CLI

**Source**: `github/docs` — Configuring GitHub Copilot CLI.

## Trusted Directories

- Config file: `~/.copilot/config.json` (or `$COPILOT_HOME/config.json`).
- Edit `trustedFolders` array to permanently trust directories.

```bash
# Disable path verification entirely (allow all paths)
copilot --allow-all-paths

# Disallow temp directory access
copilot --disallow-temp-dir
```

Default accessible paths: current working directory, subdirectories, and system temp dir.

## Tool Permissions

### Command-Line Flags

```bash
# Allow all tools (skip approval)
copilot --allow-all-tools

# Allow specific tool
copilot --allow-tool='shell'

# Deny specific tool
copilot --deny-tool='shell(rm)'
copilot --deny-tool='shell(git push)'

# Deny MCP server tool
copilot --deny-tool='My-MCP-Server(tool_name)'

# Deny all tools from an MCP server
copilot --deny-tool='My-MCP-Server'

# Allow write tools (file modification, non-shell)
copilot --allow-tool='write'

# Limit to specific toolset (others unavailable)
copilot --available-tools='shell,write'
```

Tool specification syntax:
- **Shell commands**: `shell(COMMAND)` — for `git`/`gh`, use first-level subcommand: `shell(git push)`.
- **Write tools**: `'write'` — non-shell file modification tools.
- **MCP tools**: `'MCP_SERVER_NAME'` or `'MCP_SERVER_NAME(tool_name)'`.

### Combination Examples

```bash
# Allow all tools except rm and git push
copilot --allow-all-tools --deny-tool='shell(rm)' --deny-tool='shell(git push)'

# Allow all MCP server tools except one specific tool
copilot --allow-tool='My-MCP-Server' --deny-tool='My-MCP-Server(tool_name)'
```

## URL Permissions

Default: all URLs require approval before access.

```bash
# Disable URL verification entirely
copilot --allow-all-urls

# Pre-approve specific domain
copilot --allow-url=github.com

# Deny specific domain
copilot --deny-url=github.com
```

Applies to: `web_fetch` tool + curated shell commands (`curl`, `wget`, `fetch`). HTTP != HTTPS — treated separately.

## All-in-One Flags

```bash
# Allow all tools + paths + URLs
copilot --allow-all
# or
copilot --yolo

# CLI session equivalent
/yolo
/allow-all
```

## Path Detection Limitations

- Paths embedded in complex shell constructs may not be detected.
- Only specific env vars expanded: `HOME`, `TMPDIR`, `PWD`, etc. Custom vars like `$MY_PROJECT_DIR` are not.
- Symlinks resolved for existing files but not for files being created.

## URL Detection Limitations

- URLs in file contents, config files, or env vars read by commands are not detected.
- Obfuscated URLs (split strings, escape sequences) may not be detected.

## References

- <https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli.md>
