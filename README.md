# Cogni AI Agent Skills

[![PR Reviews][pr-reviews-image]][pr-reviews-link]
[![License][license-image]][license-link]

The primary purpose of this project/repository is to maintain technical skills commonly
used by AI agents to learn technical IT skills. These skills can be loaded into any
other repository by placing them into the `.github/skills/` directory, ideally
integrating this repository as a Git submodule.

This repository mirrors the structure and conventions of the
[Cogni-AI-OU/.github](https://github.com/Cogni-AI-OU/.github) organization repository.

## Installation

To set up the required agents, instructions, and skills in your repository:

```bash
# Clone agents, instructions and skills.
git clone --depth=1 https://github.com/Cogni-AI-OU/cogni-ai-agents .github/agents
git clone --depth=1 https://github.com/Cogni-AI-OU/cogni-ai-agent-instructions .github/instructions
git clone --depth=1 https://github.com/Cogni-AI-OU/cogni-ai-agent-skills .github/skills

# Symlink individual agents from their subdirectories to the discovery directory.
for d in .github/agents/*/ ; do ln -fsv "$(basename "$d")/$(basename "$d").agent.md" .github/agents/ ; done
```

After cloning the repositories, your project will have access to the full suite of
Cogni AI capabilities loaded into the `.github/` directory.

## Skills

- **[ansible](ansible/SKILL.md)**: How to run and manage Ansible operations safely and prevent hangs
- **[context-aware-ops](context-aware-ops/SKILL.md)**: Intelligent resource management with size checking and filtering
- **[git](git/SKILL.md)**: Guide for using git with non-interactive, safe operations
- **[git-expert](git-expert/SKILL.md)**: Advanced Git operations including interactive rebasing, reflog recovery,
  bisecting, complex conflict resolution, and history manipulation
- **[github](github/SKILL.md)**: GitHub specific features and collaborative practices
- **[github-actions](github-actions/SKILL.md)**: Diagnosing and debugging failing GitHub Actions workflows
- **[github-script](github-script/SKILL.md)**: Advanced use cases and examples for using actions/github-script
- **[mermaid](mermaid/SKILL.md)**: Guide for creating and maintaining stable Mermaid.js diagrams
- **[mermaid-beta](mermaid-beta/SKILL.md)**: Guide for creating and maintaining experimental Mermaid.js beta diagrams
- **[minizinc](minizinc/SKILL.md)**: Expert MiniZinc modeling for constraint satisfaction and combinatorial problems
- **[molecule](molecule/SKILL.md)**: Molecule testing workflows for Ansible roles
- **[pdf](pdf/SKILL.md)**: PDF file inspection, object-level editing, and lossless size reduction
- **[pre-commit](pre-commit/SKILL.md)**: Using pre-commit to validate code formatting, linting, and security checks
- **[robust-commands](robust-commands/SKILL.md)**: Resilient command execution with automatic fallbacks and error recovery
- **[shell](shell/SKILL.md)**: Efficient shell command execution with timing, timeouts, and best practices
- **[skill-writer](skill-writer/SKILL.md)**: Generate or update SKILL.md files for GitHub Copilot coding agents
- **[vim-ex](vim-ex/SKILL.md)**: Non-interactive file editing with Vim Ex mode (in favor of sed, shell or Python editing)

## What This Repository Provides

This repository includes the standard operations infrastructure and AI agent skills for
Cogni-AI-OU projects:

### Key Features

- **[GitHub Actions Workflows](GitHub Actions Workflows)**: CI/CD and automation (OpenCode, pre-commit, etc.)
- **AI Agent Configurations**: AGENTS.md and the skill directories in the repository root
- **Coding Guidance**: Follow `.github/copilot-instructions.md` and the instructions stored within each skill directory
- **Pre-commit Hooks**: Linting and validation tooling
- **Code Tours**: Guided walkthroughs for repository onboarding

## Getting Started

1. Install the local validation tooling:

   ```bash
   pip install pre-commit
   pip install -r .devcontainer/requirements.txt
   ```

2. Run the repository checks:

   ```bash
   pre-commit run -a
   ```

3. Review the core guidance:
   - This README for repository scope and the local workflow
   - [.tours/getting-started.tour](.tours/getting-started.tour) for a guided walkthrough
   - [AGENTS.md](AGENTS.md) for repository-specific agent guidance

## Development

### Setup

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Install Python dependencies (for devcontainer)
pip install -r .devcontainer/requirements.txt
```

### Testing and Validation

```bash
# Run all pre-commit checks
pre-commit run -a

# Run specific checks
pre-commit run markdownlint -a
pre-commit run yamllint -a
pre-commit run black -a
pre-commit run flake8 -a
```

## Project Layout

- `.github/`: default templates, workflows, and agent configuration
- `.tours/`: guided walkthroughs for repository onboarding
- `AGENTS.md`: repository-specific guidance for automation agents
- `README.md`: repository overview and local development workflow

## AI Agents

This repository provides AI agent configurations for automated development.

### Agent Configuration Files

| File/Directory | Audience | Purpose |
| -------------- | -------- | ------- |
| [AGENTS.md](AGENTS.md) | All agents | Repository-specific guidance and workflows |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Copilot | Coding standards and project context |

See also:

- [`AGENTS.md` file format specification](https://agents.md/)
- [Best practices for using GitHub Copilot](https://gh.io/copilot-coding-agent-tips).

### Agent Skills

Agent Skills are folders of instructions, scripts, and resources that GitHub
Copilot can load when relevant to improve its performance in specialized tasks.

Agent Skills work with:

- [Copilot coding agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent)
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- Agent mode in Visual Studio Code

For more information, see
[About Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).

#### Skills catalog

The full, machine-readable list of skills lives in [AGENTS.md](AGENTS.md). Use it when you need the
authoritative catalog for agent loading. This README stays human-focused.

#### Creating skills

Each skill lives in its own subdirectory and must contain a `SKILL.md` file with
YAML frontmatter:

```markdown
---
name: my-skill-name
description: Brief description of when Copilot should use this skill
license: MIT
---

Instructions for Copilot to follow when this skill is activated.
```

##### SKILL.md frontmatter

| Field | Required | Description |
| ----- | -------- | ----------- |
| `name` | Yes | Unique identifier (lowercase, hyphens for spaces) |
| `description` | Yes | What the skill does and when to use it |
| `license` | No | License that applies to this skill |

#### Skill locations

Skills can be stored at different levels:

| Level | Location | Scope |
| ----- | -------- | ----- |
| Project | Root directory (`/`) | Single repository |
| Personal | `~/.copilot/skills/` or `~/.claude/skills/` | All projects (CLI only) |

#### How Copilot uses skills

Copilot decides when to use skills based on your prompt and the skill's
description. When activated, the `SKILL.md` file is injected into the agent's
context, providing access to your instructions and any scripts or examples in
the skill's directory.

#### Skills vs custom instructions

- **Custom instructions** (`copilot-instructions.md`): Simple guidance relevant
  to almost every task (coding standards, repository conventions)
- **Skills**: Detailed instructions that Copilot accesses only when relevant to
  a specific task

#### Community resources

Find and share skills with the community:

- [anthropics/skills](https://github.com/anthropics/skills) - Reference skills
  repository
- [github/awesome-copilot](https://github.com/github/awesome-copilot) - Community
  collection of Copilot resources

## Customizing development environment

See: [Customizing the development environment for GitHub Copilot coding agent][customize-env].

## Firewall

See: [Customizing or disabling the firewall for GitHub Copilot coding agent][firewall-config].

### Firewall allowlist

See [.github/FIREWALL.md](.github/FIREWALL.md) for recommended hosts to allow and the official guidance link.

## Troubleshooting

### Claude Not Responding to Comments

If Claude isn't responding to your comments, verify:

1. **Permissions**: You must have one of these roles:
   - Repository OWNER, MEMBER, COLLABORATOR, or CONTRIBUTOR
   - PR/issue author (on your own content only)

2. **Trigger conditions** for PR review comments:
   - Your comment contains `@claude`, OR
   - You're replying to a comment from `github-actions[bot]` (Claude's responses), OR
   - You're replying to a comment that contains `@claude`

The workflow uses a two-stage filter to prevent abuse while allowing natural
conversation flow. Check the Actions tab in your repository for workflow run details
if Claude doesn't respond as expected.

## GitHub Actions

For documentation on GitHub Actions workflows, problem matchers, and CI/CD
configuration, see [.github/workflows/README.md](.github/workflows/README.md).

## Organization Profile

For information about Cogni AI OÜ, our mission, and how to collaborate, see our
[organization profile](https://github.com/Cogni-AI-OU/.github/blob/main/profile/README.md).

## Contributing

See [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) for organization-wide
contribution guidelines and expectations for issues, pull requests, and CI.

## References

- [How to Use the .github Repository](https://www.freecodecamp.org/news/how-to-use-the-dot-github-repository/)
- [Creating a Default Community Health File](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

## License

This repository is licensed under MIT. See [LICENSE](LICENSE) for the full text.

<!-- Named links -->

[pr-reviews-image]: https://img.shields.io/github/issues-pr/Cogni-AI-OU/cogni-ai-agent-skills?label=PR+Reviews&logo=github
[pr-reviews-link]: https://github.com/Cogni-AI-OU/cogni-ai-agent-skills/pulls
[license-image]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: https://tldrlegal.com/license/mit-license
[customize-env]: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment
[firewall-config]: https://gh.io/copilot/firewall-config
