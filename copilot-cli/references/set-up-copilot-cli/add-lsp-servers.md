# Add LSP Servers

**Source**: `github/docs` — Adding LSP servers for Copilot CLI.

## Invariants

- Two-step process: (1) install LSP server software locally; (2) configure in a JSON file.
- ONLY install LSP servers from trusted sources.
- Config file locations: `~/.copilot/lsp-config.json` (user-global) or `.github/lsp.json` (per-project).
- After config change, run `/lsp reload` in CLI session.
- Server names must be alphanumeric (underscores and hyphens allowed), unique per config.

## Configuration Schema

`~/.copilot/lsp-config.json` or `.github/lsp.json`:

```json
{
  "lspServers": {
    "SERVER-NAME": {
      "command": "COMMAND",
      "args": ["ARG1", "ARG2"],
      "fileExtensions": {
        ".ext": "LANGUAGE-ID"
      }
    }
  }
}
```

### Fields

| Field | Required | Description |
|---|---|---|
| `command` | Yes | Command to start the LSP server. |
| `args` | No | Arguments to pass to command. |
| `fileExtensions` | Yes | JSON map: file extension → language ID (e.g. `{ ".rs": "rust" }`). |
| `env` | No | Env vars for server process. Supports `${VAR}` and `${VAR:-default}` expansion. |
| `rootUri` | No | Root directory relative to Git root. Default `"."`. Useful for monorepos. |
| `initializationOptions` | No | Custom options sent to server at startup. |
| `requestTimeoutMs` | No | Server request timeout in ms (default: 90000). |

## Install Commands (example LSP servers)

```bash
# TypeScript/JavaScript
npm install -g typescript typescript-language-server

# Ruby
gem install ruby-lsp
# or
gem install solargraph

# Python (via npm)
npm install -g pyright
# or (via pip)
pip install python-lsp-server
```

## Example Configurations

### TypeScript/JavaScript

```json
{
  "lspServers": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "fileExtensions": {
        ".ts": "typescript",
        ".tsx": "typescriptreact",
        ".js": "javascript",
        ".jsx": "javascriptreact",
        ".mjs": "javascript",
        ".cjs": "javascript",
        ".mts": "typescript",
        ".cts": "typescript"
      }
    }
  }
}
```

### Ruby

```json
{
  "lspServers": {
    "ruby": {
      "command": "ruby-lsp",
      "args": [],
      "fileExtensions": {
        ".rb": "ruby",
        ".rbw": "ruby",
        ".rake": "ruby",
        ".gemspec": "ruby"
      }
    }
  }
}
```

### Python (pyright)

```json
{
  "lspServers": {
    "python": {
      "command": "pyright-langserver",
      "args": ["--stdio"],
      "fileExtensions": {
        ".py": "python",
        ".pyw": "python",
        ".pyi": "python"
      }
    }
  }
}
```

## `/lsp` Slash Commands (CLI session)

| Command | Description |
|---|---|
| `/lsp` or `/lsp show` | Show status of all configured LSP servers. |
| `/lsp test SERVER-NAME` | Test server starts correctly (spawns temporary instance, reports result, kills it). |
| `/lsp reload` | Reload LSP configurations from disk. |
| `/lsp help` | Show `/lsp` command info. |

## References

- <https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/add-lsp-servers.md>
