# Allowing Tools

**Goal**: Control tool permissions to bound agent actions and prevent unintended system changes.

## Invariants

- Read-only operations (searching, reading files, read-only shell commands): **auto-allowed**.
- Destructive operations (shell commands, file writes, URL access): **require explicit approval**.
- Deny rules ALWAYS take precedence over allow rules, even with `--allow-all`.
- `/reset-allowed-tools` revokes all session permissions back to startup defaults.
- Two layers of tool control:
  1. Restrict AI model's awareness of tools (`--available-tools`, `--excluded-tools`).
  2. Allow/deny permission for specific tools (`--allow-tool`, `--deny-tool`).

## Tool Availability Controls

| Option | Effect |
|--------|--------|
| `--available-tools` | Disable all tools except those specified (allowlist). |
| `--excluded-tools` | Disable only the specified tools (denylist). |
| Both together | Allowlist takes precedence; denylist ignored. |

If a tool is not in the available set, the AI model cannot use it at all—even if also specified with `--allow-tool`.

### Example

```bash
# Prevent AI from attempting web search
copilot --excluded-tools='web_fetch, web_search'
```

## Permission Controls

| Option | Effect |
|--------|--------|
| `--allow-tool=shell` | Allow all shell commands without prompting. |
| `--allow-tool='shell(git commit)'` | Allow specific command. |
| `--allow-tool='shell(git:*)' --deny-tool='shell(git push)'` | Allow all git except push. |
| `--deny-tool=write` | Forbid all file mutations. |
| `--allow-tool='read, write(.github/copilot-instructions.md)'` | Allow read + write to specific file. |
| `--allow-tool='MyMCP(create_issue), MyMCP(delete_issue)'` | Allow MCP server tools by name. |
| `--available-tools='bash,edit,view,grep,glob' --allow-tool='shell(git:*)' --deny-tool='shell(git push)'` | Combined: explore, edit, commit; no internet, no push, no subagents. |

## Permissive Options

| Option | Effect |
|--------|--------|
| `--allow-all-tools` | Full access to available tools. |
| `--allow-all` / `--yolo` | Allow all tools + paths + URLs (equivalent to all `--allow-*` options combined). |
| `/allow-all` / `/yolo` (interactive) | Same as above, within a running session. |

Only use permissive options in isolated environments. Never alias to default.

## Resetting Permissions

```
/reset-allowed-tools
```

Revokes all session-granted permissions. Resets to the state defined at session start (CLI options).

## References

- [Allowing and denying tool use - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools.md)
