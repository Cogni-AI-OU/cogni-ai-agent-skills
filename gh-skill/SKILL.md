---
name: gh-skill
description: Expert-level guidance on the Agent Skills open standard and GitHub CLI (`gh skill`) operations for searching, previewing, installing, updating, and publishing Copilot agent skills.
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# Agent Skills (gh-skill)

Manage GitHub Copilot agent skills directly via the `gh skill` CLI command, or by manually following the Agent Skills open standard.

## Core Principles

- **Open Standard**: Rely on the open standard (`github.com/agentskills/agentskills`) for structure and specifications to ensure portability across different AI systems.
- **Portability**: Keep scripts self-contained within the skill folder to allow sharing and avoid referencing external absolute paths.
- **Non-Interactive Execution**: Always use specific arguments or non-interactive flags (`--all`, `--dry-run`) when running `gh skill` commands to avoid stalling the agent with interactive prompts.
- **Pre-flight Inspection**: Always inspect third-party skills using `gh skill preview` before installing to verify content safety and avoid malicious instructions or scripts.
- **Supply Chain Integrity**: Prefer pinning skills to specific tags or commit SHAs to ensure deterministic behavior. `gh skill` uses content-addressed change detection (git tree SHAs) to detect real content changes during updates.
- **Portable Provenance**: When installing, `gh skill` writes tracking metadata (repository, ref, tree SHA) directly into the `SKILL.md` frontmatter, allowing agents and users to track changes even if files are moved.

## Core Process (Manual & CLI)

1. **Determine Scope**: Decide if the skill should be project-specific (`.github/skills`, `.claude/skills`, `.agents/skills`) or personal (`~/.copilot/skills`, `~/.agents/skills`).
2. **Scaffold Skill**: Create a new folder for the skill containing instructions (`SKILL.md`), scripts, and necessary resources.
3. **Install/Discover**: Use `gh skill search` to find skills or `gh skill install` to discover and install skills from external repositories.
4. **Load & Test**: Ensure the AI system is configured to load the path correctly. Real-time reloading might require a session restart depending on the client.

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
- Do not place project-specific skills in global directories.
- Using `@VERSION` and `--pin` simultaneously (they are mutually exclusive).
- Avoid referencing external absolute paths in scripts inside a skill folder, keeping them portable.
- Installing unverified third-party skills that request `shell` or `bash` in `allowed-tools` without rigorous manual review.
- Avoid using undocumented directory locations not supported by the agent mode.

## Diagnostics and Troubleshooting

- If a skill isn't loading, check if the folder path is correct (e.g., `.github/skills/`, `~/.agents/skills/`).
- Verify that `gh skill` is authenticated and up to date (version 2.90.0+) if installation commands fail.
- Ensure the skill structure adheres to the open standard specifications (check `SKILL.md` frontmatter).

## Limitations

- The `gh skill` command requires GitHub CLI version 2.90.0 or later.
- Organization-level and enterprise-level skills are currently not supported natively but may be in the future.
- Third-party skills are not verified by GitHub and may contain prompt injections or malicious scripts; inspect before installation.
- Real-time reloading of skills during an active session might require a session restart depending on the client.

## References

- [`gh_skill` documentation](https://cli.github.com/manual/gh_skill)
- [Manage agent skills with GitHub CLI](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/)
- [Agent Skills Open Standard](https://github.com/agentskills/agentskills)

## Related Skills

- **skill-writer**:
  You MUST load this skill when creating or updating specific Copilot coding agent skills.
- **gh**:
  You MUST load this skill when interacting with the GitHub CLI to run `gh skill` operations.
