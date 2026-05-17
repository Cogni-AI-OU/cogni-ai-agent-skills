# Add LSP Servers

**Goal**: Integrate language intelligence for precise code navigation and symbol renaming.

## Invariants

- Install the LSP server software locally first.
- Configure servers via JSON mapping.
- Reload via `/lsp reload` or restart session.
- Only install LSP servers from trusted sources.

## Schema (if applicable)

- **Global Config**: `~/.copilot/lsp-config.json`.
- **Project Config**: `.github/lsp.json`.

```json
{
  "lspServers": {
    "SERVER-NAME": {
      "command": "COMMAND",
      "args": ["--stdio"],
      "fileExtensions": {
        ".ext": "LANGUAGE-ID"
      }
    }
  }
}
```

## Commands / Execution (if applicable)

```bash
# Automate setup for popular languages
/p setup lsp

# Check server status
/lsp show

# Test specific server
/lsp test SERVER-NAME

# Reload configurations
/lsp reload
```

## References

- [Adding LSP servers for GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/add-lsp-servers.md)
