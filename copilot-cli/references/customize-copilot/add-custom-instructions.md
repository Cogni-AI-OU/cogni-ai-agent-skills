# Add Custom Instructions

**Goal**: Configure persistent project-specific context and constraints for AI agents.

## Invariants

- Repository-wide instructions: `.github/copilot-instructions.md`.
- Path-specific instructions: `.github/instructions/NAME.instructions.md`.
- Agent directives: `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`.
- Local instructions: `$HOME/.copilot/copilot-instructions.md`.
- `COPILOT_CUSTOM_INSTRUCTIONS_DIRS` environment variable extends discovery paths.

## Schema (if applicable)

- Repository-wide: `.github/copilot-instructions.md`
- Path-specific: `.github/instructions/*.instructions.md`
- Agentic: `AGENTS.md` (root, CWD, or custom dirs)

## Commands / Execution (if applicable)

- Changes are picked up automatically on the next prompt.
- Use `/skills reload` if instructions are bundled within skills.

## References

- [Adding custom instructions](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md)
