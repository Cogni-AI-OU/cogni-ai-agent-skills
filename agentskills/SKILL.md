---
name: agentskills
description: >-
  Guidance on the Agent Skills open standard for creating portable, non-interactive, and secure Copilot agent skills.
  You MUST load this skill when designing or manually creating agent skills.
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# Agent Skills (Standard)

The Agent Skills open standard provides a framework for structuring and specifying skills to ensure portability across different AI systems and agent hosts.

## Core Principles

- **Open Standard**: Rely on the open standard for structure and specifications to ensure portability across different AI systems.
- **Portability**: Keep scripts self-contained within the skill folder to allow sharing and avoid referencing external absolute paths.
- **Non-Interactive Execution**: Always design skills for non-interactive flow, using specific arguments or flags to avoid stalling the agent.
- **Pre-flight Inspection**: Always inspect third-party skills before installing to verify content safety and avoid malicious instructions or scripts.
- **Supply Chain Integrity**: Prefer pinning skills to specific tags or commit SHAs to ensure deterministic behavior.
- **Portable Provenance**: Skills should include tracking metadata (repository, ref, tree SHA) in the `SKILL.md` frontmatter to allow tracking even if files are moved.
- **Progressive Disclosure**: Structure skills so detail is loaded only as needed:
  1. **Metadata** (~100 tokens): `name` and `description` are loaded at startup.
  2. **Instructions** (< 5000 tokens): `SKILL.md` body is loaded when the skill is activated.
  3. **Resources** (as needed): Scripts, references, or assets are loaded only when required.

## Core Process (Manual Creation)

1. **Determine Scope**:
   - **Project-specific**: Stored in the shared standard `.agents/skills/`, or provider-specific locations like `.opencode/skills/`, `.github/skills/`, or `.claude/skills/`. Scope is limited to the repository.
   - **Personal**: Stored in the shared standard `~/.agents/skills/`, or provider-specific locations like `~/.config/opencode/skills/` or `~/.copilot/skills/`. Scope is global for the user's CLI environment.
2. **Scaffold Skill**:
   - Create a directory named after the skill (lowercase-hyphenated).
   - Create a `SKILL.md` file with the required YAML frontmatter (`name`, `description`).
   - Add any supporting scripts or resources within the same directory.
3. **Verify Structure**: Ensure the `SKILL.md` follows the standard sections and style (imperative, dense, expert-level).

## Directory Structure

A standard skill directory should be organized as follows:

```text
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code (Python, Bash, JS)
├── references/       # Optional: additional documentation
├── assets/           # Optional: templates, resources, images
└── ...               # Any additional files or directories
```

## Skill Structure & Formatting

### `SKILL.md` Frontmatter

| Field | Required | Constraints |
| :--- | :--- | :--- |
| `name` | Yes | 1-64 chars, lowercase alphanumeric and hyphens only. No start/end hyphens. |
| `description` | Yes | 1-1024 chars. Should describe what the skill does AND when to use it. |
| `license` | No | License name or reference to a bundled license file. |
| `compatibility` | No | Max 500 chars. System packages, network access needs, etc. |
| `metadata` | No | Arbitrary key-value mapping (e.g., author, version). |
| `allowed-tools` | No | (Experimental) Space-separated string of pre-approved tools. |

### Body Content

- Use imperative, dense, expert-level instructions.
- Keep `SKILL.md` under 500 lines to preserve context window.
- Recommended sections: step-by-step instructions, examples, edge cases.

## File References

- Use relative paths from the skill root (e.g., `[reference](references/REF.md)`).
- Keep file references one level deep from `SKILL.md` if possible.
- Avoid deeply nested reference chains.

## Directory Scopes

| Level | Location | Scope |
| :--- | :--- | :--- |
| Project (Shared) | `.agents/skills/` | Single repository, portable across agents |
| Project (Provider) | `.opencode/skills/`, `.github/skills/`, `.claude/skills/` | Single repository, provider-specific |
| Project (Runtime) | `.skills/` | Ephemeral workspace symlink (e.g., CI/CD) |
| Personal (Shared) | `~/.agents/skills/` | User-wide (CLI), portable across agents |
| Personal (Provider) | `~/.config/opencode/skills/`, `~/.copilot/skills/` | User-wide (CLI), provider-specific |
| System | `/usr/share/agents/skills/` | System-wide |

## Runtime and CI/CD Caveats

- **Discoverability**: In CI/CD environments (like GitHub Actions), agents may run with workspace-scoped tools. If skills are cloned outside the workspace (e.g., `${{ runner.temp }}/.skills`), they should be symlinked into the workspace (e.g., `.skills/`) to be discoverable by the agent.
- **Trust Boundaries**: When running agent workflows on `pull_request_target` or `issue_comment` triggers, the PR branch's `.github/skills/` and `.github/instructions/` might be checked out by platform tools. Ensure base branch skills are preserved to prevent malicious forks from injecting altered skills.

## Validation

Use the `skills-ref` reference library to validate skills locally:

```bash
skills-ref validate ./my-skill
```

## What to Avoid

- Placing project-specific skills in global directories.
- Referencing external absolute paths in scripts inside a skill folder.
- Hardcoding environment-specific values that break portability.
- Including interactive scripts that require user input.

## References

- [Agent Skills Open Standard](https://github.com/agentskills/agentskills)
- [OpenCode Skills](https://opencode.ai/docs/skills/) — OpenCode documentation for skills
- [Documentation](https://agentskills.io) — Guides and tutorials
- [Specification](https://agentskills.io/specification) — Format details
- [Example Skills](https://github.com/anthropics/skills) — See what's possible
- [skills-ref - Reference library for Agent Skills](https://github.com/agentskills/agentskills/tree/main/skills-ref)

## Related Skills

- **skill-writer**:
  You MUST load this skill when creating or updating specific Copilot coding agent skills.
- **gh-skill**:
  See this skill for using the GitHub CLI (`gh skill`) to manage and publish Agent Skills.
