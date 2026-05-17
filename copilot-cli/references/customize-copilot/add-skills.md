# Agent Skills

**Goal**: Extend Copilot CLI capability with predefined structural tools or domain knowledge via SKILL.md.

### Invariants
- Path: `skills/` or `.github/skills/`.
- File: Must contain `SKILL.md` or `.prompt.md`.
- Inclusion: Dynamic load using context injection.

### Commands
Execute: Use `@workspace` to target `.github/skills/`.

## References
- [Adding agent skills for Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md)
- [Creating and adding a skill](https://github.com/github/docs/blob/main/data/reusables/copilot/creating-adding-skills.md)
