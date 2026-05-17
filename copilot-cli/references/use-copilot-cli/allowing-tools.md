# Allowing Tools

**Goal**: Manage tool execution boundaries and permissions to prevent unintended system changes.

## Invariants

- Read-only operations (searching, reading files) are allowed automatically.
- Destructive operations (writing files, destructive shell commands, URL access) require explicit approval.
- Deny rules ALWAYS take precedence over allow rules.
- Permission levels: One-time approval, Session-wide approval, or Permanent (via config).

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

- `--available-tools`: Restricted set of tools the model is aware of.
- `--excluded-tools`: Specifically disable tools.
- `--allow-tool`: Pre-approve specific tools for the session.
- `--deny-tool`: Explicitly forbid specific tools.
- `--allow-all` / `--yolo`: Full access to all tools, paths, and URLs.

| Option | Effect |
| ------ | ------ |
| `--allow-tool=shell` | Allow all shell commands. |
| `--allow-tool='shell(git commit)'` | Allow specific command. |
| `--deny-tool=write` | Forbid all file mutations. |
| `--allow-all` | Skip approval for all available tools. |

## References

- [Allowing and denying tool use](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools.md)
