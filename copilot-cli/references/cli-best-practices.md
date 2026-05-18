# CLI Best Practices

**Goal**: Optimize execution prompts, context handling, and strict permission models for Copilot CLI.

## Invariants

- Repository instructions ALWAYS take precedence over global instructions.
- Keep instructions concise and actionable.
- Models achieve higher success rates when given a concrete plan to follow.
- Focused sessions (using `/clear` or `/new`) produce better results than long-running unrelated tasks.
- Infinite sessions automatically manage context through intelligent compaction.
- Images can be used for UI work (drag & drop or `@file`).

## Recommendations

- **Plan Mode**: Use `Shift+Tab` or `/plan` for complex, multi-file changes or refactoring.
- **Model Selection**:
  - `Auto`: Default. Reduced rate limiting and lower latency.
  - `Claude Opus 4.5`: Best for complex architecture and nuanced debugging.
  - `Claude Sonnet 4.5`: Ideal for day-to-day coding and routine tasks.
  - `GPT-5.2 Codex`: Excellent for code generation and review.
- **Context Management**: Use `@` to mention specific files.
- **Delegation**: Use `/delegate` to offload work to cloud agents.
- **Multi-repo**: Run from parent directory or use `/add-dir` to expand access.

## Schema

- **Custom Instructions Locations**:
  - `~/.copilot/copilot-instructions.md` (Global)
  - `.github/copilot-instructions.md` (Repository)
  - `.github/instructions/**/*.instructions.md` (Modular)
  - `AGENTS.md` (Git root or cwd)
- **Valid Models**: `auto`, `claude-opus-4-5`, `claude-sonnet-4-5`, `codex-5-2`.
- **Permission Patterns**: `shell(git:*)`, `shell(npm run:*)`, `write`.

## Commands

```bash
# Preconfigure allowed tools via flags
copilot --allow-tool='shell(git:*)' --deny-tool='shell(git push)'

# Within CLI
/model                 # Switch model
/reset-allowed-tools    # Reset approvals
/session               # View session info
/session checkpoints   # View checkpoints
/context               # Visualize context usage
/clear or /new         # Start fresh session
/compact               # Manual compaction
/add-dir [PATH]        # Add directory context
/delegate [PROMPT]     # Offload to cloud
/fleet [PROMPT]        # Parallel subtasks
/help [TOPIC]          # Help on topic (config, commands, environment, logging, permissions)
```

## References

- [Best practices for GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/cli-best-practices.md)
