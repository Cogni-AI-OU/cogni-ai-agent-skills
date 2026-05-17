---
name: copilot-cli
description: Guidance for installing GitHub Copilot CLI on Debian/Ubuntu and executing commands using custom agents. You MUST load this skill when interacting with or installing the copilot-cli command.
---

# Skill: copilot-cli

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Guidance for installing the GitHub Copilot CLI on Debian/Ubuntu and using it with custom agents via command-line options.

## Core Process

1. **Install CLI**: Use `snap install copilot-cli` on Debian/Ubuntu systems.
2. **Discover Usage**: Run `copilot --help` for standard command usage options.
3. **Agent Selection**: Use the `--agent` flag to target specialized `.agent.md` files (located in `.github/agents/` or `~/.copilot/agents/`).
4. **Command Execution**: Provide the explicit instruction string via the `--prompt` flag.

## Core Principles

- **Programmatic Execution**: Avoid interactive slash commands (like `/agent`) in scripts. Always use explicit programmatic flags (`--agent` and `--prompt`).
- **Context Management**: Utilize custom subagents to offload specific tasks, ensuring the main agent's context window remains uncluttered for higher-level planning.
- **Agent Resolution**: If custom agents share a name, the one in the user's home directory (`~/.copilot/agents/`) takes precedence over the project repository (`.github/agents/`).

## Commands / Usage Patterns

**Installation (Debian/Ubuntu)**
```bash
snap install copilot-cli
```

**Discover Usage options**
```bash
copilot --help
```

**Programmatic Custom Agent Execution**
Specify the custom agent file name (excluding the `.agent.md` extension) and the exact instruction prompt.
```bash
copilot --agent security-auditor --prompt "Check /src/app/validator.go"
```

## References

- [Create custom agents for CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)