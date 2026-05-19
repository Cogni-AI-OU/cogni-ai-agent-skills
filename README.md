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

- **[agent-log-analysis](agent-log-analysis/SKILL.md)**: Procedures and templates for analyzing agent session
  logs, extracting telemetry, and generating standardized visual audit reports
- **[agents-md-writer](agents-md-writer/SKILL.md)**: Autonomous documentation editor responsible for creating,
  updating, and maintaining AGENTS.md files strictly adhering to the organizational baseline structure
- **[agentskills](agentskills/SKILL.md)**: Guidance on the Agent Skills open standard for creating
  portable, non-interactive, and secure agent skills.
  You MUST load this skill when designing or manually creating agent skills.
- **[ansible](ansible/SKILL.md)**: How to run and manage Ansible operations safely and prevent hangs.
- **[brainstorm](brainstorm/SKILL.md)**: Activate brainstorming protocol to explore options, research, deconstruct
  complexities, and summarize available data into simple diagrams and MiniZinc constraints.
- **[brainstorm-agent-runs](brainstorm-agent-runs/SKILL.md)**: Activate agent-run brainstorming protocol to identify and
  analyze agent runs via GitHub API for a given Pull Request.
- **[brainstorm-github-pr](brainstorm-github-pr/SKILL.md)**: Activate PR brainstorming protocol to analyze and visualize
  commit history, review threads, and CI pipeline checks using Mermaid diagrams.
- **[cat](cat/SKILL.md)**: Guidelines for safely using `cat` and avoiding shell hangs with heredocs.
- **[code-review](code-review/SKILL.md)**: Execute expert-level code reviews, dissecting codebases and Pull Requests (PRs)
  with surgical precision to identify logical flaws, hygiene issues, and architectural drift.
- **[code-tour](code-tour/SKILL.md)**: Create, update, and maintain VSCode CodeTour (.tour) JSON walkthrough files
  with full schema compliance and interactive step configuration.
- **[context-aware-ops](context-aware-ops/SKILL.md)**: Intelligent resource management with size checking and filtering
- **[critical-thinking](critical-thinking/SKILL.md)**: Engage deep analytical reasoning, deconstruct assumptions,
  apply Socratic questioning, and perform adversarial red-teaming to solve complex problems and validate architectural plans.
- **[datadog-agent](datadog-agent/SKILL.md)**: Expert-level guidance for installing, configuring, and
  extending the Datadog Agent.
- **[datadog-mcp](datadog-mcp/SKILL.md)**: Query observability data via Datadog MCP,
  selecting minimal toolsets
- **[datadog-pulumi](datadog-pulumi/SKILL.md)**: Use when creating or debugging Datadog monitors in Pulumi YAML,
  especially for schema mismatches, monitor validation errors, and provider-specific field mapping.
- **[dockerfile](dockerfile/SKILL.md)**: Write, review, and optimize Dockerfiles applying multi-stage
  builds, non-root constraints, layer caching, and strict image pinning
- **[docs-review](docs-review/SKILL.md)**: Enforce documentation quality, completeness, and mutual consistency
  across architecture, ADRs, runbooks, and code
- **[docs-writer](docs-writer/SKILL.md)**: Create, update, and maintain documentation including Architectural Decision
  Records (ADRs), runbooks, READMEs, and code-level documentation
- **[editorconfig](editorconfig/SKILL.md)**: Generates a comprehensive and best-practice-oriented .editorconfig file
  based on project analysis and user preferences
- **[fact-writer](fact-writer/SKILL.md)**: Guidance for writing, structuring, and maintaining verifiable project
  fact files without contradictions
- **[gdpr-compliant](gdpr-compliant/SKILL.md)**: Apply GDPR-compliant engineering practices across your codebase
- **[gh](gh/SKILL.md)**: GitHub CLI (`gh`) operations for issues, pull requests, workflow runs, reviews, and API
- **[gh-api](gh-api/SKILL.md)**: Advanced GitHub CLI (`gh api`) queries and mutations via REST or GraphQL
- **[gh-aw](gh-aw/SKILL.md)**: GitHub Agentic Workflows (`gh aw`) operations for repository automation,
  creating workflows, running coding agents, and auditing workflow runs
- **[gh-aw-troubleshooting](gh-aw-troubleshooting/SKILL.md)**: Diagnose and fix GitHub Agentic Workflows (`gh-aw`) failures
  by analyzing logs for missing tools, permissions, or MCP configurations
- **[gh-issue](gh-issue/SKILL.md)**: GitHub CLI (`gh issue`) operations for managing, viewing, and editing issues
- **[gh-models](gh-models/SKILL.md)**: GitHub CLI models (`gh models`) operations for running and evaluating AI models
- **[gh-pr](gh-pr/SKILL.md)**: GitHub CLI (`gh pr`) operations for pull requests, reviews, PR checks, and PR branches
- **[gh-run](gh-run/SKILL.md)**: GitHub CLI (`gh run` and `gh workflow`) operations for workflow runs, jobs, logs, and attempts
- **[gh-search](gh-search/SKILL.md)**: GitHub CLI (`gh search`) operations for searching code, commits, issues,
  pull requests, and repositories with structured JSON output
- **[gh-skill](gh-skill/SKILL.md)**: Expert-level guidance on GitHub CLI (`gh skill`) operations for
  searching, previewing, installing, updating, and publishing agent skills.
  You MUST load this skill when managing agent skills via the GitHub CLI.
- **[git](git/SKILL.md)**: Guide for using git with non-interactive, safe operations
- **[git-expert](git-expert/SKILL.md)**: Advanced Git operations including reflog recovery,
  bisecting, complex conflict resolution, and history manipulation
- **[git-filter-branch](git-filter-branch/SKILL.md)**: Extract a specific subdirectory with history using git filter-branch
- **[git-merge](git-merge/SKILL.md)**: Guide and safety rules for performing git merges,
  ensuring no conflict markers and no duplicate lines are present.
- **[git-rebase](git-rebase/SKILL.md)**: Advanced Git rebase operations including
  interactive history cleanup and non-interactive scripted rewrites
- **[github](github/SKILL.md)**: GitHub-specific features and collaborative practices
- **[github-actions](github-actions/SKILL.md)**: Diagnosing and debugging failing GitHub Actions workflows
- **[github-aw](github-aw/SKILL.md)**: Safely update existing GitHub Agentic Workflows (gh-aw), distinguishing between
  frontmatter configuration that requires recompilation and markdown body prompt edits that do not
- **[github-aw-troubleshooting](github-aw-troubleshooting/SKILL.md)**: Debug and refine GitHub Agentic Workflows
  (gh-aw) by analyzing execution logs, auditing runs, and resolving missing tool errors or prompt inefficiencies
- **[github-aw-memory](github-aw-memory/SKILL.md)**: Guide for persistent memory strategies in agentic workflows
- **[github-issue](github-issue/SKILL.md)**: Guidance for issue context routing, response routing, and workspace invariants
- **[github-mcp-server](github-mcp-server/SKILL.md)**: Guide for configuring and using the GitHub MCP server within
  Agentic Workflows
- **[github-pr](github-pr/SKILL.md)**: Guidance for PR context routing, branch sync policies,
  and workspace invariants
- **[github-pr-review](github-pr-review/SKILL.md)**: Comprehensive PR review workflow for verifying code quality,
  metadata accuracy, and merge readiness
- **[github-script](github-script/SKILL.md)**: Advanced use cases and examples for using actions/github-script
- **[github-topics](github-topics/SKILL.md)**: Search GitHub repositories by topics and keywords
- **[mermaid](mermaid/SKILL.md)**: Guide for creating and maintaining stable Mermaid.js diagrams
- **[mermaid-beta](mermaid-beta/SKILL.md)**: Guide for creating and maintaining experimental Mermaid.js beta diagrams
- **[minizinc](minizinc/SKILL.md)**: Expert MiniZinc modeling for constraint satisfaction and combinatorial problems
- **[molecule](molecule/SKILL.md)**: Molecule testing workflows for Ansible roles
- **[mot](mot/SKILL.md)**: Evaluate and classify machine learning models based on the Model Openness Framework (MOF)
- **[opencode](opencode/SKILL.md)**: Manage OpenCode configuration, credentials, and access the OpenCode Zen API
- **[pdf](pdf/SKILL.md)**: PDF file inspection, object-level editing, and lossless size reduction
- **[pipenv](pipenv/SKILL.md)**: Manage Python project dependencies, virtual environments, and security using the
  pipenv CLI
- **[pipfile](pipfile/SKILL.md)**: Create, update, and manage Python project dependencies via Pipfile and Pipfile.lock
- **[pre-commit](pre-commit/SKILL.md)**: Using pre-commit to validate code formatting, linting, and security checks
- **[python](python/SKILL.md)**: Expert Python language skill for writing, refactoring, and testing idiomatic Python 3 code
- **[python-cli](python-cli/SKILL.md)**: Execute Python inline scripts via heredocs for complex log processing,
  data transformation, or CLI utilities like URL encoding/decoding
- **[robust-commands](robust-commands/SKILL.md)**: Resilient command execution with automatic
  fallbacks and error recovery
- **[sbom](sbom/SKILL.md)**: Guidelines and commands for generating a Software Bill of Materials (SBOM) using syft
- **[security-audit](security-audit/SKILL.md)**: Commands, step-by-step procedures, and mechanical execution for
  performing deep security audits, vulnerability assessments, and report generation
- **[security-review](security-review/SKILL.md)**: Lightweight security review focused on Pull Requests and
  incremental changes
- **[shell](shell/SKILL.md)**: Efficient shell command execution with timing, timeouts, and best practices
- **[agent-skill-md-writer](agent-skill-md-writer/SKILL.md)**: Generate or update SKILL.md files for coding agents
- **[subagent-task](subagent-task/SKILL.md)**: Guidance and protocols for spawning sub-agents via the task tool.
- **[tdd](tdd/SKILL.md)**: Commands, step-by-step procedures, and mechanical execution for test engineering,
  testability audits, and the TDD lifecycle.
- **[tester](tester/SKILL.md)**: Elite autonomous test engineering kernel focused on proving software correctness,
  preventing regressions, and designing refactor-resilient behavioral tests.
- **[vim-ex](vim-ex/SKILL.md)**: Non-interactive file editing with Vim Ex mode (in favor of sed, shell
  or Python editing)
- **[yaml](yaml/SKILL.md)**: Generic guidelines for YAML formatting, linting, and structural rules
- **[yq](yq/SKILL.md)**: Safely parse, edit, merge, and transform YAML files using yq, providing robust
  command-line examples for extraction and in-place modifications

## What This Repository Provides

This repository includes the standard operations infrastructure and AI agent skills for
Cogni-AI-OU projects:

### Key Features

- **[GitHub Actions Workflows](.github/workflows/)**: CI/CD and automation (OpenCode, pre-commit, etc.)
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
```

### Specific Checks

```bash
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
| [AGENTS-RUNTIME.md](AGENTS-RUNTIME.md) | GitHub Runtime agents | Skill loading instructions and catalog |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Copilot | Coding standards and project context |

See also:

- [`AGENTS.md` file format specification](https://agents.md/)
- [Best practices for using GitHub Copilot](https://gh.io/copilot-coding-agent-tips).

### Agent Skills

Agent Skills are folders of instructions, scripts, and resources that autonomous
agents can load when relevant to improve their performance in specialized tasks.

Agent Skills work with:

- [Copilot coding agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent)
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- Agent mode in Visual Studio Code

For more information, see
[About Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).

#### Skills catalog

The full, machine-readable list of skills lives in [AGENTS-RUNTIME.md](AGENTS-RUNTIME.md). Use it when you need the
authoritative catalog for agent loading. [AGENTS.md](AGENTS.md) provides repository-specific guidance.
This README stays human-focused.

#### Creating skills

Each skill lives in its own subdirectory and must contain a `SKILL.md` file with
YAML frontmatter:

```markdown
---
name: my-skill-name
description: Brief description of when the agent should use this skill
license: MIT
---

Instructions for the agent to follow when this skill is activated.
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
