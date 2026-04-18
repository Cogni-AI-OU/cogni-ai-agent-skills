# .github Directory Catalog (Agent View)

Catalog of folders within the `.github` directory of this repository.
Use this as the entry point for agent work, and follow linked catalogs where present.

## Folder catalog

| Folder | Purpose | Agent catalog |
| ------ | ------- | ------------- |
| [.github/agents/](agents/) | Agent configuration files (e.g., specialized agent definitions) | — |
| [.github/workflows/](workflows/) | Reusable GitHub Actions workflows | [.github/workflows/AGENTS.md](workflows/AGENTS.md) |

Archived catalogs for prompts and instructions have been removed; rely on the skill directories in the
repository root or `.github/copilot-instructions.md` for active guidance.

## Additional key files

- [.github/copilot-instructions.md](copilot-instructions.md): main coding standards for agents.
- [.github/actionlint-matcher.json](actionlint-matcher.json): problem matchers used in workflows.
- [.github/pre-commit-matcher.json](pre-commit-matcher.json): problem matchers used in workflows.

Keep this catalog updated when adding, removing, or renaming folders or agent catalogs.
