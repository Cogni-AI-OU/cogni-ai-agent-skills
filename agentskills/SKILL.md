---
name: agentskills
description: >-
  Reference for the Agent Skills open standard. Defines the schema, directory structure, formatting, and portability requirements for agent skills.
  You MUST load this skill to understand the technical structure of an agent skill.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# Agent Skills (Standard)

The Agent Skills open standard provides a framework for structuring and specifying skills to ensure portability across different AI systems and agent hosts. Agent Skills work with GitHub Copilot (Cloud, CLI, and VS Code), Claude Code, OpenCode, and other compliant agents. Agent Skills are self-contained folders with instructions and bundled resources that teach AI agents specialized capabilities, unlike custom instructions which only define coding standards.

## Core Principles

- **Open Standard**: Rely on the open standard for structure and specifications to ensure portability across different AI systems.
- **Portability**: Keep scripts self-contained within the skill folder to allow sharing and avoid referencing external absolute paths.
- **Non-Interactive Execution**: Always design skills for non-interactive flow, using specific arguments or flags to avoid stalling the agent.
- **Pre-flight Inspection**: Always inspect third-party skills before installing to verify content safety and avoid malicious instructions or scripts.
- **Supply Chain Integrity**: Prefer pinning skills to specific tags or commit SHAs to ensure deterministic behavior.
- **Portable Provenance**: Skills should include tracking metadata (repository, ref, tree SHA) in the `SKILL.md` frontmatter to allow tracking even if files are moved.
- **Progressive Loading Architecture**: Structure skills so detail is loaded only as needed:
  1. **Discovery** (~100 tokens): `name` and `description` are loaded at startup.
  2. **Instructions** (< 5000 tokens): `SKILL.md` body is loaded when the request matches the description.
  3. **Resources** (as needed): Scripts, examples, and docs are loaded only when explicitly referenced.

## When to Use

- When designing, architecting, or manually creating a new agent skill folder from scratch.
- To understand the progressive loading architecture, directory structure, and metadata requirements of the open standard.
- When reviewing a third-party skill for compliance with the Agent Skills specification.

## When Not to Use

- When generating the markdown content for a skill automatically (use `agent-skill-md-writer` instead).
- For configuring the top-level behavior or personality of the agent itself (use `agent-md-writer`).
- When writing project-specific coding conventions that do not require actionable agent instructions.

## Common Pitfalls

- **Vague Descriptions**: Writing a skill `description` that is too generic, meaning the agent will never trigger it when needed.
- **Absolute Paths**: Hardcoding absolute file paths inside skill scripts, breaking portability when the skill is installed on a different machine.
- **Interactive Prompts**: Bundling shell scripts that wait for human input, causing autonomous agents to hang indefinitely.

## Core Process (Manual Creation)

1. **Determine Scope**:
   - **Project skills**: Stored in `.github/skills/`, `.claude/skills/`, or `.agents/skills/` depending on the tool. Scope is limited to the repository.
   - **Personal skills**: Stored in `~/.copilot/skills/`, `~/.claude/skills/`, or `~/.agents/skills/` depending on the tool. Scope is global for the user's CLI environment.
   - **Installable skills**: Use `gh skill install OWNER/REPOSITORY` to browse skills interactively, `gh skill install OWNER/REPOSITORY SKILL-NAME` for a non-interactive install, or `npx skills add https://docs-url` (Vercel's skills CLI) to install external skills.
2. **Scaffold Skill**:
   - Create a directory named after the skill (lowercase-hyphenated).
   - Create a `SKILL.md` file with the required YAML frontmatter (`name`, `description`).
   - Add any supporting scripts or resources within the same directory.
3. **Verify Structure**: Ensure the `SKILL.md` follows the standard sections and style (imperative, dense, expert-level).

## Directory Structure

A standard skill directory should be organized as follows:

```text
skill-name/
├── SKILL.md          # MANDATORY: must be named SKILL.md (metadata + instructions)
├── LICENSE.txt       # Recommended: License terms (Apache 2.0 typical)
├── scripts/          # Optional: executable code (Python, Bash, JS). Loaded when executed.
├── references/       # Optional: additional documentation. Loaded when referenced.
├── assets/           # Optional: static files used AS-IS in output (not modified by agent).
└── templates/        # Optional: starter code/scaffolds that the AI agent MODIFIES.
```

**Assets vs Templates**: If the AI agent reads and builds upon the file content, place it in `templates/`. If the file is used as-is in output (e.g., logo.png, report format), place it in `assets/`.

## Skill Structure & Formatting

### Agent profile format (Frontmatter)

The `name` and `description` fields in `SKILL.md` frontmatter are critical. The agent decides whether to load a skill based on the description alone. A vague description means the skill never activates. Write descriptions that specify both when the skill applies and when it does not.

**CRITICAL**: Keep descriptions concise and keyword-dense to respect the context budget. Describe **WHAT** the skill does, **WHEN** to use it, and include relevant **KEYWORDS**.

| Field | Required | Constraints |
| :--- | :--- | :--- |
| `name` | Yes | 1-64 chars, lowercase alphanumeric and hyphens only. No start/end hyphens. |
| `description` | Yes | 10-1024 chars. Should describe capabilities AND use cases. Wrapped in single quotes. |
| `license` | No | License name or reference to a bundled license file (e.g., `Complete terms in LICENSE.txt`). |
| `compatibility` | No | Max 500 chars. System packages, network access needs, etc. |
| `metadata` | No | Arbitrary key-value mapping (e.g., author, version). |
| `allowed-tools` | No | Space-separated string of pre-approved tools (e.g., `shell`, `bash`). |

**Security Warning**: Only pre-approve `shell` or `bash` if you fully trust the skill source. Pre-approving these tools removes the confirmation step and can allow execution of arbitrary commands.

### Body Content

- Use imperative mood ("Run", "Create", "Configure"), dense, expert-level instructions.
- Keep `SKILL.md` under 500 lines to preserve context window. Split into `references/` if it exceeds ~200 lines.
- **Focus on What Copilot Doesn't Know**: Exclude standard language syntax or well-documented API behavior. Focus on internal conventions, non-obvious defaults, version-specific quirks, and domain-specific workflows.

Recommended sections:
- `# Title`: Brief overview of what this skill enables.
- `## When to Use This Skill`: List of scenarios reinforcing description triggers.
- `## Prerequisites`: Required tools or dependencies.
- `## Step-by-Step Workflows`: Numbered steps for repeatable procedures (build, deploy, setup). Use flexible guidelines instead of rigid steps for open-ended tasks.
- `## Gotchas`: Proactive warnings about non-obvious behavior. **This is the highest-signal content**. Bold the key constraint and explain why.
- `## Troubleshooting`: Reactive fixes for known issues (symptom → solution pairs).
- `## References`: Links to bundled docs (`references/`) or external resources.

## File References

- Use relative paths from the skill root (e.g., `[reference](./references/REF.md)`).
- Keep file references up to two levels deep from `SKILL.md` if necessary for organization (e.g., `references/subdir/file.md`).
- Avoid excessively deep nesting (beyond 2 levels) to maintain portability.

## Directory Scopes

| Level | Location | Scope |
| :--- | :--- | :--- |
| Project (Shared) | `.agents/skills/` | Single repository, portable across agents |
| Project (Provider) | `.github/skills/`, `.claude/skills/`, `.opencode/skills/` | Single repository, provider-specific |
| Project (Runtime) | `.skills/` | Ephemeral workspace symlink (e.g., CI/CD) |
| Personal (Shared) | `~/.agents/skills/` | User-wide (CLI), portable across agents |
| Personal (Provider) | `~/.copilot/skills/`, `~/.claude/skills/`, `~/.config/opencode/skills/` | User-wide (CLI), provider-specific |
| Installable | `gh skill install OWNER/REPOSITORY`, `npx skills add https://docs-url` | Install external skills via CLI |
| System | `/usr/share/agents/skills/` | System-wide |

## Managing Skills with GitHub CLI

The `gh skill` command in GitHub CLI (v2.90.0+) allows discovering, installing, and managing skills:

- **Search**: `gh skill search <topic>`
- **Preview**: `gh skill preview <owner>/<repository> <skill-name>`
- **Install**: `gh skill install <owner>/<repository> <skill-name>`
- **Update**: `gh skill update --all`
- **Publish**: `gh skill publish`

## Runtime and CI/CD Caveats

- **Discoverability**: In CI/CD environments (like GitHub Actions), agents may run with workspace-scoped tools. If skills are cloned outside the workspace (e.g., `${{ runner.temp }}/.skills`), they should be symlinked into the workspace (e.g., `.skills/`) to be discoverable by the agent.
- **Trust Boundaries**: When running agent workflows on `pull_request_target` or `issue_comment` triggers, the PR branch's `.github/skills/` and `.github/instructions/` might be checked out by platform tools. Ensure base branch skills are preserved to prevent malicious forks from injecting altered skills.

## Validation Checklist

Before publishing a skill, verify:
- [ ] `SKILL.md` has valid frontmatter with `name` and `description`
- [ ] `name` is lowercase with hyphens, ≤64 characters
- [ ] `description` clearly states **WHAT** it does, **WHEN** to use it, and relevant **KEYWORDS**
- [ ] Body focuses on information Copilot wouldn't know from training data
- [ ] `## Gotchas` section present if skill involves non-obvious behavior, API quirks, or common traps
- [ ] SKILL.md body under 500 lines (consider splitting into `references/` at ~200 lines)
- [ ] Large workflows (>5 steps) split into `references/` folder with clear links
- [ ] Scripts include help documentation and error handling
- [ ] Relative paths used for all resource references

Locally validate skills using the `skills-ref` reference library:
```bash
skills-ref validate ./my-skill
```

## What to Avoid

- Placing project-specific skills in global directories.
- Referencing external absolute paths in scripts inside a skill folder.
- Hardcoding environment-specific values that break portability.
- Including interactive scripts that require user input.
- Including information the agent already knows from its training data.

## References

- [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Adding agent skills for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Agent Skills Open Standard](https://github.com/agentskills/agentskills)
- [VS Code Agent Skills Documentation](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [OpenCode Skills](https://opencode.ai/docs/skills/) — OpenCode documentation for skills
- [Documentation](https://agentskills.io) — Guides and tutorials
- [Specification](https://agentskills.io/specification) — Format details
- [Example Skills](https://github.com/anthropics/skills) — See what's possible
- [Awesome Copilot Skills](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md)
- [skills-ref - Reference library for Agent Skills](https://github.com/agentskills/agentskills/tree/main/skills-ref)

## Related Skills

- **agent-skill-md-writer**:
  You MUST load this skill when creating or updating specific coding agent skills.
- **gh-skill**:
  See this skill for using the GitHub CLI (`gh skill`) to manage and publish Agent Skills.
