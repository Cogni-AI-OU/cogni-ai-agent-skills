---
name: copilot-cli
description: Guidance for installing GitHub Copilot CLI on Debian/Ubuntu and executing commands using custom agents. You MUST load this skill when interacting with or installing the copilot-cli command.
license: MIT
---

# Skill: copilot-cli

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Guidance for installing the GitHub Copilot CLI on Debian/Ubuntu and using it with custom agents via command-line options.

## When to Use

- When executing programmatic requests against GitHub Copilot via the terminal.
- To orchestrate specialized subagents using the `--agent` flag.
- When installing or authenticating the Copilot CLI in a CI/CD or local environment.

## When Not to Use

- When trying to use standard `gh` commands for repo management (Copilot CLI is an extension specifically for AI assistance).
- Inside highly restricted environments without internet access or where external API calls to `api.github.com` are blocked.
- For generating extremely large, multi-file architectural scaffolds where a dedicated repository generation tool is more appropriate.

## Common Pitfalls

- **Interactive Prompts in Scripts**: Using the raw `copilot` command in a CI script without the `-s` (silent) or programmatic flags, causing the pipeline to hang waiting for user input.
- **Agent Name Clashes**: Creating a custom agent that shares a name with a built-in alias, leading to the wrong prompt instructions being loaded.
- **Untrusted Directories**: Failing to pre-approve or trust the working directory, causing Copilot CLI to block execution and demand a manual terminal confirmation.

## Core Process

1. **Install CLI**: Use `npm install -g @github/copilot` (recommended), `curl -fsSL https://gh.io/copilot-install | bash` (install script), or `snap install copilot-cli` on Debian/Ubuntu.
2. **Authentication**: Use `copilot login` or set `COPILOT_GITHUB_TOKEN`. Fine-grained PATs require the **Copilot Requests** permission.
3. **Discover Usage**: Run `copilot --help` for standard command usage options. Alternatively, load the **copilot-docs** skill for detailed overview.
4. **Agent Selection**: Use the `--agent` flag to target specialized `.agent.md` files. For details, load the **copilot-docs** skill.
5. **Command Execution**: Provide the explicit instruction string via the `--prompt` or `-p` flag. Use `-s` (silent) in scripts to capture output. Manage tools via tool flags.
6. **Task Steering**: Control outputs dynamically or remotely via workflow configuration. For detailed guides on steering, load the **copilot-docs** skill.
7. **Session Management**: Validate and trace logic using session commands. For comprehensive session management, load the **copilot-docs** skill.
8. **Pull Requests**: For collaborative tasks, leverage PR-focused commands described in the **copilot-docs** skill.

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

## Related Skills

- **copilot-docs**: Detailed references on automating, customizing, and advanced usage patterns for Copilot CLI.
- **gh-agent-task**: Use for managing preview agent tasks on repositories and pull requests.
