# Customization Overview

**Goal**: Summary of extension points for GitHub Copilot CLI.

## Invariants

- Customizations improve response quality by providing guidelines, context, and specialized tools.
- Requires directory trust for local customizations.

## Customization Vectors

- **Custom Instructions**: Persistent guidelines added to every prompt.
- **Hooks**: Shell commands triggered by session events (start, end, task complete, error).
- **Skills**: Instruction sets and resources for specialized domains.
- **Custom Agents**: Subagents with scoped expertise, context, and toolsets.
- **MCP Servers**: Model Context Protocol integration for external databases and services.
- **Plugins**: Bundled, distributable packages of customization components.

## References

- [Overview of customizing GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/overview.md)
