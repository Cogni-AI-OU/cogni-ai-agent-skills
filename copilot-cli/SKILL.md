---
name: copilot-cli
description: Guidance for installing GitHub Copilot CLI on Debian/Ubuntu and executing commands using custom agents. You MUST load this skill when interacting with or installing the copilot-cli command.
---

# Skill: copilot-cli

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Guidance for installing the GitHub Copilot CLI on Debian/Ubuntu and using it with custom agents via command-line options.

## Customization

Optimize Copilot CLI by providing project-specific guidelines, automation hooks, and specialized skills.

### Custom Instructions

Inject project-wide standards and context into every prompt.
- **Usage**: Define guidelines in `AGENTS.md` or `.prompts/` to enforce coding standards automatically.
- **Reference**: See [add-custom-instructions.md](references/customize-copilot/add-custom-instructions.md) for detailed configuration patterns.

### Hooks

Automate shell commands at specific lifecycle events (session start, post-task, errors).
- **Trigger**: Run tests, refresh environment variables, or trigger CI updates based on agent actions.
- **Reference**: See [use-hooks.md](references/customize-copilot/use-hooks.md) for trigger definitions and context variables.

### Skills

Load instruction sets and scripts to extend agent capabilities for specialized domains.
- **Impact**: Enhances reasoning for complex workflows like cloud deployments or security audits.
- **Reference**: See [add-skills.md](references/customize-copilot/add-skills.md) for skill structuring and discovery paths.

### Custom Agents

Deploy specialized subagents with scoped context and toolsets.
- **Architecture**: Offloads specific tasks (e.g., code review, documentation) to agents with restricted permissions.
- **Reference**: See [create-custom-agents-for-cli.md](references/customize-copilot/create-custom-agents-for-cli.md) for custom agent subagent properties and configuration.

### MCP Servers

Integrate external data and tools via Model Context Protocol.
- **Capabilities**: Query databases, access issue trackers (Jira/GitHub), and interact with calendars.
- **Reference**: See [add-mcp-servers.md](references/customize-copilot/add-mcp-servers.md) for configuration schemas and tool filtering.

### Plugins

Bundle components (skills, agents, hooks) into distributable units.
- **Distribution**: Install via marketplace or direct repository link (`owner/repo:path`).
- **Find & Install**: See [plugins-finding-installing.md](references/customize-copilot/plugins-finding-installing.md) for installation commands and marketplace management.
- **Creation**: See [plugins-creating.md](references/customize-copilot/plugins-creating.md) for generating and structuring Copilot CLI plugins.
- **Marketplace**: See [plugins-marketplace.md](references/customize-copilot/plugins-marketplace.md) for creating and managing custom plugin registries.

### BYOK Models

Configure custom AI model providers via Bring Your Own Key (BYOK).
- **Usage**: Integrate external model providers (Anthropic, Google, generic OpenAI-compatible) using local API keys.
- **Reference**: See [use-byok-models.md](references/customize-copilot/use-byok-models.md) for environment variables and model selection flags.

## Core Process

1. **Install CLI**: Use `npm install -g @github/copilot` (recommended), `curl -fsSL https://gh.io/copilot-install | bash` (install script), or `snap install copilot-cli` on Debian/Ubuntu.
2. **Authentication**: Use `copilot login` or set `COPILOT_GITHUB_TOKEN`. Fine-grained PATs require the **Copilot Requests** permission.
3. **Discover Usage**: Run `copilot --help` for standard command usage options.
4. **Agent Selection**: Use the `--agent` flag to target specialized `.agent.md` files (located in `.github/agents/`, `~/.copilot/agents/`, or organization-level `.github-private/agents/`).
5. **Command Execution**: Provide the explicit instruction string via the `--prompt` or `-p` flag. Use `-s` (silent) in scripts to capture output.

## Core Principles

- **Programmatic Execution**: Avoid interactive slash commands (like `/agent`) in scripts. Always use explicit programmatic flags (`--agent` and `--prompt`).
- **Context Management**: Utilize custom subagents to offload specific tasks, ensuring the main agent's context window remains uncluttered. In scripts, keep prompts narrowly scoped, pass context explicitly with `--prompt`, and start a new `copilot` invocation when you need a fresh or reduced context window.
- **Agent Resolution**: If custom agents share a name, the resolution order is: User (`~/.copilot/agents/`) > Project (`.github/agents/`) > Organization (`.github-private/agents/`).
- **Trusted Directories**: Copilot CLI requires confirmation to trust the working directory. Permanent trust is stored in `~/.copilot/config.json`.

## Commands / Usage Patterns

### Installation & Authentication

```bash
# Recommended (requires Node.js 22+)
npm install -g @github/copilot

# Install script (macOS/Linux)
curl -fsSL https://gh.io/copilot-install | bash

# Authenticate
copilot login
```

### Security & Permissions

```bash
# Preferred: grant only the specific permissions needed for the task
copilot --allow-tool='shell(git)' --deny-tool='shell(rm)' --prompt "Clean repo"

# Only use YOLO mode after the user has explicitly confirmed unrestricted access
copilot --yolo --prompt "Perform complex task"
```

**Programmatic Custom Agent Execution**
Specify the custom agent file name (excluding the `.agent.md` extension) and the exact instruction prompt.
```bash
copilot --agent security-auditor --prompt "Check <target-file>"
```

## References

- [Custom Instructions Reference](references/customize-copilot/add-custom-instructions.md)
- [Hooks Reference](references/customize-copilot/use-hooks.md)
- [Adding LSP servers for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/add-lsp-servers)
- [Authenticating GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli)
- [Configuring GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli)
- [copilot-cli docs repository](https://github.com/github/docs/tree/main/content/copilot/how-tos/copilot-cli)
- [Create custom agents for CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
- [Custom agents configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [GitHub Copilot CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)
- [Install Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli)
- [Overview of customizing GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview)
- [Quickstart for automating with GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/automate-copilot-cli/quickstart)
- [Setting up GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli)
- [Troubleshooting GitHub Copilot CLI authentication](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/troubleshoot-copilot-cli-auth)
- [Using GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview)

## Related Skills

- **gh-agent-task**: Use for managing preview agent tasks on repositories and pull requests.
