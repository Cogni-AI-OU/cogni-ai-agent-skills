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
- **Explicit Versioning**: Pin skills to specific versions (`@vX.Y.Z` or `--pin`) in production or shared environments to maintain deterministic behavior and prevent unexpected updates.

## Commands / Usage Patterns

- **Search Skills**:
  `gh skill search <topic>`
- **Preview a Skill**:
  `gh skill preview <owner>/<repository> <skill-name>`
- **Install a Skill**:
  `gh skill install <owner>/<repository> <skill-name>`
- **Install a Specific Version**:
  `gh skill install <owner>/<repository> <skill-name>@<version>`
- **Install and Pin a Skill**:
  `gh skill install <owner>/<repository> <skill-name> --pin <version>`
- **Install for Specific Agent/Scope**:
  `gh skill install <owner>/<repository> <skill-name> --agent <agent-name> --scope <scope-name>`
- **Update a Specific Skill**:
  `gh skill update <skill-name>`
- **Update All Skills (Non-Interactive)**:
  `gh skill update --all`
- **Validate Skill for Publishing (Dry Run)**:
  `gh skill publish --dry-run`
- **Auto-Fix Skill Metadata**:
  `gh skill publish --fix`

## What to Avoid

- Running `gh skill install` or `gh skill update` without arguments, as this launches interactive prompts.
- Using `@VERSION` and `--pin` simultaneously (they are mutually exclusive).
- Installing unverified third-party skills that request `shell` or `bash` in `allowed-tools` without rigorous manual review.

## Limitations

- The `gh skill` command requires GitHub CLI version 2.90.0 or later.
- Third-party skills are not verified by GitHub and may contain prompt injections or malicious scripts; inspect before installation.

## Related Skills

- **gh**:
  You MUST load this skill when working with the `gh` command and its subcommands.
