---
name: copilot-docs
description: Reference and documentation for GitHub Copilot CLI customization, automation, and advanced usage. You MUST load this skill when asked to read Copilot CLI documentation.
license: MIT
---

# Skill: copilot-docs

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Reference and documentation for GitHub Copilot CLI customization, automation, advanced usage, and setup.

## Customization

Optimize Copilot CLI by providing project-specific guidelines, automation hooks, and specialized skills. See [Customize Copilot](references/customize-copilot.md).

## Automate Copilot CLI

Automate operations and orchestrate GitHub Copilot CLI in pipelines or custom scripts. See [Automate Copilot CLI](references/automate-copilot-cli.md).

### Quickstart

- **Usage**: General introduction to automation paths.
- **Reference**: See [quickstart.md](references/automate-copilot-cli/quickstart.md)

### Run CLI Programmatically

- **Usage**: Call the CLI from scripts, capturing structured JSON output silently.
- **Reference**: See [run-cli-programmatically.md](references/automate-copilot-cli/run-cli-programmatically.md)

### Automate with Actions

- **Usage**: Inject Copilot CLI capabilities natively into GitHub Actions workflows.
- **Reference**: See [automate-with-actions.md](references/automate-copilot-cli/automate-with-actions.md)

### Custom Instructions

Inject project-wide standards and context into every prompt.
- **Usage**: Define guidelines in `AGENTS.md` or `.prompts/` to enforce coding standards automatically.
- **Reference**: See [add-custom-instructions.md](references/customize-copilot/add-custom-instructions.md) for detailed configuration patterns.

### Hooks

Automate shell commands at specific lifecycle events (session start, post-task, errors).
- **Trigger**: Run tests, refresh environment variables, or trigger CI updates based on agent actions.
- **Reference**: See [use-hooks.md](references/customize-copilot/use-hooks.md) for trigger definitions and [hooks-reference.md](references/reference/hooks-reference.md) for configuration schemas and events.

### Skills

Load instruction sets and scripts to extend agent capabilities for specialized domains.
- **Impact**: Enhances reasoning for complex workflows like cloud deployments or security reviews.
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

## Use Copilot CLI

Harness the core capabilities of the Copilot CLI for code review, task delegation, and execution management. See [Use Copilot CLI](references/use-copilot-cli.md).

- **Overview**: Core capabilities and usage. See [overview.md](references/use-copilot-cli/overview.md).
- **Agentic Code Review**: Automate PR and code reviews. See [agentic-code-review.md](references/use-copilot-cli/agentic-code-review.md).
- **Allowing Tools**: Enforce tool execution boundaries. See [allowing-tools.md](references/use-copilot-cli/allowing-tools.md).
- **Chronicle**: Track and resume historical sessions. See [chronicle.md](references/use-copilot-cli/chronicle.md).
- **Connecting VS Code**: Sync terminal CLI with IDE context. See [connecting-vs-code.md](references/use-copilot-cli/connecting-vs-code.md).
- **Delegate Tasks to CCA**: Route specific workloads to Custom Copilot Agents. See [delegate-tasks-to-cca.md](references/use-copilot-cli/delegate-tasks-to-cca.md).
- **Invoke Custom Agents**: Run specialized agent personas directly. See [invoke-custom-agents.md](references/use-copilot-cli/invoke-custom-agents.md).
- **Manage Pull Requests**: Generate and summarize PRs. See [manage-pull-requests.md](references/use-copilot-cli/manage-pull-requests.md).
- **Roll Back Changes**: Revert codebase mutations cleanly. See [roll-back-changes.md](references/use-copilot-cli/roll-back-changes.md).
- **Speed Up Task Completion**: Optimize workflows and reduce latency. See [speed-up-task-completion.md](references/use-copilot-cli/speed-up-task-completion.md).
- **Steer Agents**: Mid-flight control of constraints and logic. See [steer-agents.md](references/use-copilot-cli/steer-agents.md).
- **Steer Remotely**: Orchestrate workflows across remote boundaries. See [steer-remotely.md](references/use-copilot-cli/steer-remotely.md).

## Set Up Copilot CLI

Establish the foundation for the GitHub Copilot CLI and securely connect it to your environments. See [Set Up Copilot CLI](references/set-up-copilot-cli.md).

- **Install Copilot CLI**: Deploy the extension natively via GitHub CLI. See [install-copilot-cli.md](references/set-up-copilot-cli/install-copilot-cli.md).
- **Authenticate Copilot CLI**: Establish device flow or token authentication. See [authenticate-copilot-cli.md](references/set-up-copilot-cli/authenticate-copilot-cli.md).
- **Configure Copilot CLI**: Manage internal setup, aliases, and telemetry. See [configure-copilot-cli.md](references/set-up-copilot-cli/configure-copilot-cli.md).
- **Add LSP Servers**: Connect language intelligence for robust command context. See [add-lsp-servers.md](references/set-up-copilot-cli/add-lsp-servers.md).
- **Troubleshoot Auth**: Diagnose and repair underlying connectivity failures. See [troubleshoot-copilot-cli-auth.md](references/set-up-copilot-cli/troubleshoot-copilot-cli-auth.md).

## Best Practices

Adopt strict standards and guidelines to maximize Copilot CLI efficacy and security.

- **CLI Best Practices**: Optimize execution prompts, context handling, and strict permission models bounding. See [cli-best-practices.md](references/cli-best-practices.md).

## References

- [GitHub Docs](https://docs.github.com/llms.txt)
- [Customize Copilot](references/customize-copilot.md)
- [Automate Copilot CLI](references/automate-copilot-cli.md)
- [Use Copilot CLI](references/use-copilot-cli.md)
- [Set Up Copilot CLI](references/set-up-copilot-cli.md)
- [AI Engines (Coding Agents)](references/reference/engines.md)
- [Hooks Reference](references/reference/hooks-reference.md)
- [copilot-cli docs repository](https://github.com/github/docs/tree/main/content/copilot/how-tos/copilot-cli)
- [Custom agents configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [GitHub Copilot CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)
