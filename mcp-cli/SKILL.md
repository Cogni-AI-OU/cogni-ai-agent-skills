---
name: mcp-cli
description: Interface for MCP (Model Context Protocol) servers via CLI. Use when you need to interact with external tools, APIs, or data sources through MCP servers, list available MCP servers/tools, or call MCP tools from command line.
license: MIT
---

# mcp-cli

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Access MCP servers through the command line. MCP enables interaction with external systems like GitHub, filesystems, databases, and APIs.

## When to Use

- To interactively call an MCP (Model Context Protocol) server's tool from the command line.
- When debugging or inspecting the JSON schema of an available MCP tool.
- To execute specific filesystem, database, or API queries provided by a configured MCP server without writing a wrapper script.

## When Not to Use

- Inside automated scripts where direct API calls (e.g., `curl` or language-specific SDKs) are faster and more reliable than shelling out to an MCP server wrapper.
- For managing GitHub resources natively supported by `gh` (e.g., `gh issue list`).
- If the required MCP server is not installed or configured in the environment.

## Common Pitfalls

- **JSON Escaping Errors**: Passing complex, nested JSON payloads directly in the command line argument without proper escaping, causing parse errors. (Use stdin or heredocs instead).
- **Ignoring Descriptions**: Running a tool blindly without first checking its schema and description via `mcp-cli <server>/<tool>`, leading to incorrect parameter types.
- **Assuming Tool Availability**: Hardcoding an MCP tool call in a script without verifying that the specific server is actually running and accessible in that environment.

## Core Process

1. **Discover**: `mcp-cli` → see available servers and tools
2. **Explore**: `mcp-cli <server>` → see tools with parameters
3. **Inspect**: `mcp-cli <server>/<tool>` → get full JSON input schema
4. **Execute**: `mcp-cli <server>/<tool> '<json>'` → run with arguments

## Core Principles

- **Direct Execution**: Favor using `mcp-cli` commands directly from the shell rather than writing intermediate script wrappers.

## Commands / Usage Patterns

| Command                            | Output                          |
| ---------------------------------- | ------------------------------- |
| `mcp-cli`                          | List all servers and tool names |
| `mcp-cli <server>`                 | Show tools with parameters      |
| `mcp-cli <server>/<tool>`          | Get tool JSON schema            |
| `mcp-cli <server>/<tool> '<json>'` | Call tool with arguments        |
| `mcp-cli grep "<glob>"`            | Search tools by name            |

**Add `-d` to include descriptions** (e.g., `mcp-cli filesystem -d`)

## Quick Start

```bash
# List all servers and tool names
mcp-cli

# See all tools with parameters
mcp-cli filesystem

# With descriptions (more verbose)
mcp-cli filesystem -d

# Get JSON schema for specific tool
mcp-cli filesystem/read_file

# Call the tool
mcp-cli filesystem/read_file '{"path": "./README.md"}'

# Search for tools
mcp-cli grep "*file*"

# JSON output for parsing
mcp-cli filesystem/read_file '{"path": "./README.md"}' --json

# Complex JSON with quotes (use heredoc or stdin)
mcp-cli server/tool <<EOF
{"content": "Text with 'quotes' inside"}
EOF

# Or pipe from a file/command
cat args.json | mcp-cli server/tool

# Find all TypeScript files and read the first one
mcp-cli filesystem/search_files '{"path": "src/", "pattern": "*.ts"}' --json | jq -r '.content[0].text' | head -1 | xargs -I {} sh -c 'mcp-cli filesystem/read_file "{\"path\": \"{}\"}"'
```

## Options

| Flag         | Purpose                   |
| ------------ | ------------------------- |
| `-j, --json` | JSON output for scripting |
| `-r, --raw`  | Raw text content          |
| `-d`         | Include descriptions      |

## Diagnostics and Troubleshooting

Exit Codes:

- `0`: Success
- `1`: Client error (bad args, missing config)
- `2`: Server error (tool failed)
- `3`: Network error

## Limitations

- Server interactions are isolated to standard streams or network responses depending on the MCP server.

## References

- <https://github.com/github/awesome-copilot/blob/main/skills/mcp-cli/SKILL.md>

## Related Skills

- **robust-commands**:
  You MUST load this skill when executing commands requiring resilient error recovery or fallbacks.
