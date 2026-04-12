# Agent Skills Catalog

Authoritative list of skills for agent loading. Each entry points to a `SKILL.md` with activation
criteria and instructions.

For a human-readable overview, see [README.md](README.md).

## Skills

- **[context-aware-ops](context-aware-ops/SKILL.md)**: Intelligent resource management with size checking and filtering
- **[git](git/SKILL.md)**: Guide for using git with non-interactive, safe operations
- **[git-expert](git-expert/SKILL.md)**: Advanced Git operations including interactive rebasing, reflog recovery,
  bisecting, complex conflict resolution, and history manipulation
- **[github-actions](github-actions/SKILL.md)**: Diagnosing and debugging failing GitHub Actions workflows
- **[molecule](molecule/SKILL.md)**: Molecule testing workflows for Ansible roles
- **[pre-commit](pre-commit/SKILL.md)**: Using pre-commit to validate code formatting, linting, and security checks
- **[robust-commands](robust-commands/SKILL.md)**: Resilient command execution with automatic fallbacks and error recovery
- **[shell](shell/SKILL.md)**: Efficient shell command execution with timing, timeouts, and best practices
- **[skill-writer](skill-writer/SKILL.md)**: Generate or update SKILL.md files for GitHub Copilot coding agents
- **[vim-ex](vim-ex/SKILL.md)**: Non-interactive file editing with Vim Ex mode (in favor of sed, shell or Python editing)

## Usage

- Load skills from this catalog when the agent needs specialized guidance.
- Follow the instructions in each `SKILL.md`; do not duplicate content here.
- Keep this table in sync when adding or removing skills.

## Troubleshooting

### SKILL.md MarkdownLint Errors

When updating `SKILL.md` frontmatter, be aware of these common linting culprits:

- **MD023 (Heading start left)**: If you use a YAML block scalar (`>-`) for the `description` without padding,
  `markdownlint` may parse the frontmatter closure `---` as a Setext heading element.
  **Fix:** Always ensure there is at least one blank line before the closing `---` in the frontmatter.
- **MD034 (No bare URLs)**: URLs placed naked inside block strings will trigger this error.
  **Fix:** Wrap all URLs in `<>` (e.g., `<https://github.com/...>`) within the description field.
