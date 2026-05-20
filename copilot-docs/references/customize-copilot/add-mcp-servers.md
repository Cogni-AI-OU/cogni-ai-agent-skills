# Add MCP Servers

**Goal**: Connect Model Context Protocol (MCP) servers to provide additional tools and context.

## Invariants

- GitHub MCP server is built-in and enabled by default.
- Remote (HTTP/SSE) or Local (STDIO) transport types supported.
- Tool filtering via allowlist or wildcard (`*`).

## Schema (if applicable)

- Config File: `~/.copilot/mcp-config.json` (configurable via `COPILOT_HOME`).

```json
{
  "mcpServers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["@org/mcp-server@latest"],
      "env": { "API_KEY": "..." },
      "tools": ["*"]
    }
  }
}
```

## Commands / Execution (if applicable)

```bash
# Add server interactively
/mcp add

# List servers and status
/mcp show

# Show tools for specific server
/mcp show SERVER-NAME

# Edit/Disable/Enable
/mcp edit SERVER-NAME
/mcp disable SERVER-NAME
/mcp enable SERVER-NAME
```

## References

- [Adding MCP servers for GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers.md)
