# MCP Servers

**Goal**: Register and manage Model Context Protocol (MCP) servers locally.

### Invariants
- Protocols supported: `stdio`, `sse`.
- Configuration: `gh copilot mcp add` maps tools locally.

### Schema
```json
{
  "mcpServers": {
    "local-tools": {
      "command": "python",
      "args": ["-m", "my_mcp_server"]
    }
  }
}
```

### Commands
Execute:
- `/mcp add <SERVER-NAME> <COMMAND>`
- `/mcp list`
- `/mcp delete <SERVER-NAME>`

## References
- [Adding MCP servers for Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers.md)
