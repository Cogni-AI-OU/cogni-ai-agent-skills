---
name: dot-claude
description: 'Configure and manage Claude Code (.claude) workspace settings, permissions, and tool hooks.'
license: MIT
---

# dot-claude

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Configuring allowed tools and bash permissions for Claude Code.
- Defining PreToolUse or PostToolUse hooks for specific commands or file edits.
- Setting up environment variables or enabling LSP plugins for Claude Code.
- Analyzing or updating the `.claude/settings.json` workspace configuration.

## When Not to Use

- When working with the Anthropic Claude API or Claude documentation.
- When configuring generic coding standard rules instead of Claude-specific behavior.

## Core Process

1. **Locate or Create Configuration**: Ensure the `.claude` directory exists at the root of the project.
2. **Define Permissions**: Use `.claude/settings.json` to explicitly allow specific Bash commands to prevent Claude Code from blocking them.
3. **Configure Hooks**: Set up `PreToolUse` or `PostToolUse` hooks in `settings.json` to enforce safety checks, trigger auto-formatting, or log activity.
4. **Set Environment & Plugins**: Enable required tools like language servers (`pyright-lsp`) or specify environment variables.

## Best Practices

- **Explicit Permissions**: Instead of granting broad permissions, use precise glob patterns (e.g., `Bash(uv tool *)`).
- **Hook Activity Logging**: Redirect output from hooks into a specific log file like `.claude/hook-activity.log` to trace tool side effects.
- **Fail-Safe Hooks**: Ensure `PreToolUse` hooks return appropriate exit codes (e.g., `exit 2`) to block destructive commands.

## Common Pitfalls

- **JSON Syntax Errors**: `settings.json` must be strictly valid JSON, without trailing commas or comments.
- **Overly Broad Matchers**: Be precise with `matcher` regex in hooks to avoid triggering scripts unnecessarily (e.g., `Edit|Write` vs just `Bash`).

## References

- [Example settings.json](references/vojay-dev/settings.json)
