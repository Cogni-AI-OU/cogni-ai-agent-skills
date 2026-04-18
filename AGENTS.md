# AGENTS.md

Persistent single-source truth for autonomous agent behavior.

For general project invariants see [README.md](README.md).

## Directory-Specific Agent files

Read and merge these when operating inside corresponding sub-directories (order = precedence):

- [`.github/AGENTS.md`](.github/AGENTS.md)
- Any `AGENTS.md` or `SKILL.md` in ancestor, then current directory tree

## Required References

- Project overview & install: [README.md](README.md)
- Agent configuration & conventions: [.github/copilot-instructions.md](.github/copilot-instructions.md)
- Workflow navigation: [.tours/getting-started.tour](.tours/getting-started.tour)
- Latest org baseline: <https://github.com/Cogni-AI-OU/.github/blob/main/AGENTS.md>

## Skills

You must load the skills relevant to the user prompt, inferred intent,
and planned work into the current context:

- **[ansible](ansible/SKILL.md)**: How to run and manage Ansible operations safely and prevent hangs
- **[context-aware-ops](context-aware-ops/SKILL.md)**: Intelligent resource management with size checking and filtering
- **[git](git/SKILL.md)**: Guide for using git with non-interactive, safe operations
- **[git-expert](git-expert/SKILL.md)**: Advanced Git operations including interactive rebasing, reflog recovery,
  bisecting, complex conflict resolution, and history manipulation
- **[github](github/SKILL.md)**: GitHub specific features and collaborative practices
- **[github-actions](github-actions/SKILL.md)**: Diagnosing and debugging failing GitHub Actions workflows
- **[molecule](molecule/SKILL.md)**: Molecule testing workflows for Ansible roles
- **[pre-commit](pre-commit/SKILL.md)**: Using pre-commit to validate code formatting, linting, and security checks
- **[robust-commands](robust-commands/SKILL.md)**: Resilient command execution with automatic fallbacks and error recovery
- **[shell](shell/SKILL.md)**: Efficient shell command execution with timing, timeouts, and best practices
- **[skill-writer](skill-writer/SKILL.md)**: Generate or update SKILL.md files for GitHub Copilot coding agents
- **[vim-ex](vim-ex/SKILL.md)**: Non-interactive file editing with Vim Ex mode (in favor of sed, shell or Python editing)

### Structural Invariant

- **Skills Location**: Skills are located directly in the root directory of this repository.
- **Do Not Add To Subdirectories**: Do not create or add new skills inside `.github/skills/` or other subdirectories.

### Final Assurance Gates

- Keep this file entropy-pruned and up-to-date.
- Inject full content into every sub-agent context.
- For latest standard see: <https://agents.md/>

## Common Tasks

### Linting and Validation

```bash
# Run all pre-commit checks
pre-commit run -a

# Run specific checks
pre-commit run markdownlint -a
pre-commit run yamllint -a
```

### Testing

```bash
# Run Molecule tests
molecule test

# Syntax check
molecule syntax
```

### Updating Coding Standards

- Language-specific conventions reside in individual skill directories alongside their `SKILL.md`
- Update `.markdownlint.yaml`, `.yamllint`, or `.editorconfig` for linting rules
- Run `pre-commit run -a` to verify changes pass all checks

## References

- Main documentation: [README.md](README.md)

## Troubleshooting

### GitHub Build issues

- Use `gh` command to interact with GitHub resources. For example:

  - `gh run list --limit 3` to list recent builds.
  - `gh run view {ID} --log | rg -iw "failed|error|exit"` to look for build errors.

### Firewall issues

If you encounter firewall issues when using the GitHub Copilot Agent:

- Refer to <https://gh.io/copilot/firewall-config> for configuration details.
- Do not workaround blocked URLs by adding markdown-link-check ignore/whitelist patterns for real links.
- Keep markdown-link-check validating real links, and request firewall allowlisting instead.
- If you need to allowlist additional hosts, update your firewall configuration accordingly
  by following `.github/agents/FIREWALL.md` and keep that file up to date.

### Linting issues

If Copilot or automated checks behave unexpectedly:

- Re-run `pre-commit run -a` locally to surface formatting or linting issues.
- Verify `.markdownlint.yaml` and `.yamllint` have not been modified incorrectly.
- If problems persist, open an issue with details of the command run and any error output.
