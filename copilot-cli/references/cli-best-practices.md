# CLI Best Practices

**Goal**: Maximize effectiveness, precision, and security when operating the GitHub Copilot CLI.

### Invariants
- Custom instruction files (`.github/copilot-instructions.md`, `AGENTS.md`) always override global scopes.
- Allowed tools must follow the Principle of Least Privilege.
- Models must be selected based on task complexity (`Auto`, `Claude Opus 4.5`, `Claude Sonnet 4.5`, `GPT-5.2 Codex`).
- Planning mode must precede complex multi-file architectural changes.

### Schema / Configuration
- **Allowed Tools Check**: `copilot --allow-tool='shell(git:*)' --deny-tool='shell(git push)'`
- **Reset Tools State**: `/reset-allowed-tools` mid-session.
- **Set Planning Mode**: Use `/plan <PROMPT>` or `Shift+Tab`.
- **Custom Models (BYOK)**: Require streaming and tool-calling capabilities (>= 128k context recommended).

### Commands / Execution
```bash
# Set explicit boundaries before execution
copilot --allow-tool='shell(npm run test:*)' --prompt "Execute integration tests safely"

# Enforce planning mode before code execution
copilot --prompt "/plan Create authentication schemas"
```

## References
- [Copilot CLI Best Practices](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/cli-best-practices.md)