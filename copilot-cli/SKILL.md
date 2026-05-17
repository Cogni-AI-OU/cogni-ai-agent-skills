---
name: copilot-cli
description: Guidance for installing GitHub Copilot CLI on Debian/Ubuntu and executing commands using custom agents. You MUST load this skill when interacting with or installing the copilot-cli command.
---

# Skill: copilot-cli

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Guidance for installing the GitHub Copilot CLI on Debian/Ubuntu and using it with custom agents via command-line options.

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

- [Adding custom instructions for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/add-custom-instructions)
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
