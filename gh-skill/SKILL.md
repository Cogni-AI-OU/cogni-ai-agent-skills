---
name: gh-skill
description: >-
  Expert-level guidance on GitHub CLI (`gh skill`) operations for searching, previewing, installing, updating, and publishing agent skills.
  You MUST load this skill when managing agent skills via the GitHub CLI.
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# Agent Skills CLI (gh-skill)

Manage agent skills directly via the `gh skill` CLI command. This tool automates the installation, discovery, and management of skills adhering to the Agent Skills open standard.

## Core Principles

- **Non-Interactive Execution**: Always use specific arguments or non-interactive flags (`--all`, `--dry-run`) when running `gh skill` commands to avoid stalling the agent with interactive prompts.
- **Pre-flight Inspection**: Always inspect third-party skills using `gh skill preview` before installing to verify content safety.
- **Supply Chain Integrity**: Prefer pinning skills to specific tags or commit SHAs via the `--pin` flag to ensure deterministic behavior.
- **Automated Metadata**: `gh skill` automatically writes tracking metadata (repository, ref, tree SHA) into the `SKILL.md` frontmatter during installation.

## Core Process

1. **Discovery & Inspection**: Use `gh skill search` to find skills and `gh skill preview` to review their content and requirements BEFORE installation.
2. **Installation**: Use `gh skill install` to add skills from external repositories.
3. **Management**: Use `gh skill update` to keep skills current and `gh skill publish` to share your own skills.

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
- **Install for Specific Agent/Scope**:
  `gh skill install <owner>/<repository> <skill-name> --agent claude-code --scope user`
- **Update Skills**:
  `gh skill update <skill-name>`
  `gh skill update --all` (Non-interactive)
- **Publish/Validate Skills**:
  `gh skill publish` (Validates against spec and checks security settings)
  `gh skill publish --fix` (Auto-fixes metadata issues)

## Awesome Copilot Skills

To search for curated Awesome Copilot skills, run `gh skill install github/awesome-copilot` for an interactive browsing and installation flow,
or view the directory at <https://awesome-copilot.github.com/skills/>.
To install a specific skill directly, use `gh skill install github/awesome-copilot <skill-name>`.

## Supported Agent Hosts

| Host | Agent Flag (`--agent`) |
| :--- | :--- |
| GitHub Copilot | `copilot` (default) |
| Claude Code | `claude-code` |
| Cursor | `cursor` |
| Codex | `codex` |
| Gemini CLI | `gemini` |
| Antigravity | `antigravity` |

## Diagnostics and Troubleshooting

- If a skill isn't loading, verify the install path using `gh skill list`.
- Verify that `gh skill` is authenticated and up to date (version 2.90.0+) if commands fail.
- Check `gh skill status` (if available) to see the health of installed skills.

## What to Avoid

- Running `gh skill install` or `gh skill update` without arguments (launches interactive prompts).
- Using `@VERSION` and `--pin` simultaneously (they are mutually exclusive).
- Installing unverified third-party skills that request broad permissions without review.

## Limitations

- The `gh skill` command requires GitHub CLI version 2.90.0 or later.
- Third-party skills are not verified by GitHub and may contain malicious content; always preview.

## References

- [Manage agent skills with GitHub CLI](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/)
- [Add skills to Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Awesome Copilot Skills Directory](https://awesome-copilot.github.com/skills/)
- [`gh skill` manual](https://cli.github.com/manual/gh_skill)

## Related Skills

- **agentskills**:
  You MUST load this skill for deep understanding of the Agent Skills open standard and manual skill creation.
- **skill-writer**:
  You MUST load this skill when developing new skills to be published via `gh skill`.
