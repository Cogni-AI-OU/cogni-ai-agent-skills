---
name: gh-skill
description: GitHub CLI (`gh skill`) operations for searching, previewing, installing, updating, and publishing Copilot agent skills. You MUST load this skill when working with the `gh skill` command.
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# gh-skill

Manage GitHub Copilot agent skills directly via the `gh skill` CLI command.

## Core Principles

- **Non-Interactive Execution**: Always use specific arguments or non-interactive flags (`--all`, `--dry-run`) when running `gh skill` commands to avoid stalling the agent with interactive prompts.
- **Pre-flight Inspection**: Always inspect third-party skills using `gh skill preview` before installing to verify content safety and avoid malicious instructions or scripts.
- **Supply Chain Integrity**: Prefer pinning skills to specific tags or commit SHAs to ensure deterministic behavior. `gh skill` uses content-addressed change detection (git tree SHAs) to detect real content changes during updates.
- **Portable Provenance**: When installing, `gh skill` writes tracking metadata (repository, ref, tree SHA) directly into the `SKILL.md` frontmatter, allowing agents and users to track changes even if files are moved.

## Commands / Usage Patterns

- **Search Skills**:
  `gh skill search <topic>`
- **Browse Repository Skills**:
  `gh skill install <owner>/<repository>`
- **Preview a Skill**:
  `gh skill preview <owner>/<repository> <skill-name>`
- **Install a Skill**:
  `gh skill install <owner>/<repository> <skill-name>`
- **Install Specific Version/SHA**:
  `gh skill install <owner>/<repository> <skill-name>@v1.2.0`
  `gh skill install <owner>/<repository> <skill-name>@abc123def`
- **Install and Pin**:
  `gh skill install <owner>/<repository> <skill-name> --pin v1.2.0`
  `gh skill install <owner>/<repository> <skill-name> --pin abc123def`
- **Install for Specific Agent/Scope**:
  `gh skill install <owner>/<repository> <skill-name> --agent claude-code --scope user`
- **Update Skills**:
  `gh skill update <skill-name>`
  `gh skill update --all` (Non-interactive)
- **Publish/Validate Skills**:
  `gh skill publish` (Validates against spec, checks security settings, and offers to enable immutable releases)
  `gh skill publish --fix` (Auto-fixes metadata issues)
- **Usage**:
  Run `gh skill --help` to see all available commands.

## Supported Agent Hosts

| Host | Agent Flag (`--agent`) |
| :--- | :--- |
| GitHub Copilot | `copilot` (default) |
| Claude Code | `claude-code` |
| Cursor | `cursor` |
| Codex | `codex` |
| Gemini CLI | `gemini` |
| Antigravity | `antigravity` |

## What to Avoid

- Running `gh skill install` or `gh skill update` without arguments, as this launches interactive prompts.
- Using `@VERSION` and `--pin` simultaneously (they are mutually exclusive).
- Installing unverified third-party skills that request `shell` or `bash` in `allowed-tools` without rigorous manual review.

## Limitations

- The `gh skill` command requires GitHub CLI version 2.90.0 or later.
- Third-party skills are not verified by GitHub and may contain prompt injections or malicious scripts; inspect before installation.

## References

- [`gh_skill` documentation](https://cli.github.com/manual/gh_skill)
- [Manage agent skills with GitHub CLI](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/)

## Related Skills

- **agentskills**
  You MUST load this skill when working with specification and documentation for Agent Skills.
