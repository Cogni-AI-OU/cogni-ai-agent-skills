# CLI Best Practices

**Goal**: Optimize execution prompts, context handling, and strict permission models for Copilot CLI.

## Invariants

- Repository instructions ALWAYS take precedence over global instructions.
- Keep instructions concise and actionable to prevent dilution.
- Models achieve higher success rates when given a concrete plan to follow.
- Focused sessions (using `/clear` or `/new`) produce better results than long-running unrelated tasks.

## Schema (if applicable)

- **Custom Instructions Supported Locations**:
  - `~/.copilot/copilot-instructions.md` (Global)
  - `.github/copilot-instructions.md` (Repository)
  - `AGENTS.md` (Project Directives)
- **Valid Models**:
  - `auto` (Default)
  - `claude-opus-4-5`
  - `claude-sonnet-4-5`
  - `codex-5-2`

## Commands / Execution (if applicable)

```bash
# Preconfigure allowed tools via flags
copilot --allow-tool='shell(git:*)' --deny-tool='shell(git push)'

# Reset approvals
/reset-allowed-tools

# Visualize context usage
/context

# Switch model mid-session
/model
```

## References

- [Best practices for GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/cli-best-practices.md)
