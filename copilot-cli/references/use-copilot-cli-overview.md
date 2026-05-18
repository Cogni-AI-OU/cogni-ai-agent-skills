# Overview

**Goal**: Foundational usage, interactions, and core capabilities of GitHub Copilot CLI.

## Invariants

- Requires active GitHub Copilot subscription.
- Requires directory trust confirmation before operation: `Yes, proceed` | `Yes, and remember` | `No, exit`.
- Directory trust scope: reading, modifying, and executing files in and below the trusted directory.
- Trust can be granted per-session or persisted via `Yes, and remember this folder for future sessions`.
- Untrusted directories require per-file approval for modifications outside the working directory.
- Authentication via `/login` slash command.

## Commands / Execution

```bash
# Start interactive session
copilot

# Run specific prompt programmatically
copilot --prompt "Fix the bug in @src/app.js"

# Resume most recent local session
copilot --continue

# Resume specific session
copilot --resume SESSION-ID

# Show help
copilot help

# Show config help
copilot help config

# Show environment variables
copilot help environment

# Show logging levels
copilot help logging

# Show permissions
copilot help permissions
```

## Key Interactive Features

- **File Context**: `@path/to/file` in prompts includes file contents. Tab-completion for paths.
- **Direct Shell**: `!` prefix executes shell commands directly without model invocation.
- **Plan Mode**: `Shift+Tab` toggles plan mode for collaborative implementation planning before code writing.
- **Autopilot**: `Shift+Tab` cycles to autopilot mode for autonomous local execution.
- **Autopilot Programmatic**: `copilot --prompt "<prompt>" --autopilot --allow-all --autopilot-max-continuations 10`
- **Stop Execution**: Press `Esc` while "Thinking" to abort current operation.
- **Reasoning Visibility**: `Ctrl+T` toggles model reasoning display (persists across sessions).
- **Add Trusted Directory**: `/add-dir /path/to/directory`
- **Change Working Directory**: `/cwd /path/to/directory` or `/cd /path/to/directory`
- **Resume Session**: `/resume` (opens picker) or `/resume SESSION-ID`

## Context Management

| Command | Effect |
|---------|--------|
| `/usage` | View session statistics: premium requests, duration, lines edited, token usage breakdown |
| `/context` | Visual overview of current token usage |
| `/compact` | Manually compress conversation history to free context space |
| Auto-compression | Triggers at ~95% token limit; runs in background without interrupting workflow |

## Tool Permission Model

- Read-only operations (searching, reading files, read-only shell commands): **allowed automatically**.
- Destructive operations (shell commands, file edits, URL access): **require explicit approval**.
- Approval options: One-time, Session-wide (`Yes, and approve TOOL for the rest of the session`), or Reject with inline feedback.
- `--allow-all` / `--yolo`: Enable all permissions at once (isolated environments only).

## Custom Instructions & Agent Files

- Repository-wide instructions: `.github/copilot-instructions.md`
- Path-specific instructions: `.github/instructions/**/*.instructions.md`
- Agent profiles: `AGENTS.md` files
- Resolution order: User (`~/.copilot/agents`) > Repository (`.github/agents`) > Organization (`.github-private/agents`)

## MCP Servers

- GitHub MCP server pre-configured for PR merging and resource interaction.
- Add additional MCP servers via `/mcp add` interactive dialog.
- MCP config stored in `~/.copilot/mcp-config.json` (override via `COPILOT_HOME` env var).

## Skills

- Skills extend Copilot with specialized instructions, scripts, and resources.
- Defined per the Agent Skills open standard.

## Built-in Custom Agents

| Agent | Purpose |
|-------|---------|
| Explore | Quick codebase analysis without main context impact |
| Task | Execute commands (tests, builds); summary on success, full output on failure |
| General-purpose | Complex multi-step tasks in separate context |
| Code review | Surface genuine issues with minimal noise |
| Research | Deep research across codebase, repos, and web; detailed report with citations |
| Rubber duck | Constructive critic; consulted automatically by CLI |

## References

- [Using GitHub Copilot CLI - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/overview.md)
