---
applyTo:
  - '.github/workflows/*.{yaml,yml}'
  - '.github/workflow-templates/*.{yaml,yml}'
description: When editing, reviewing, or creating any file matching .github/workflows/*.yml
---

# GitHub Actions Workflow Instructions

Apply these rules autonomously whenever a GitHub Actions workflow file (`.github/workflows/*.yml`) is created or modified.

## Core Conventions

### Lexicographical Order

Sort all mapping keys and environment variables alphabetically (case-sensitive ASCII order).
This reduces diff noise and improves readability.

### Formatting

Format files with `yamlfix` according to the repository's `.yamlfix.toml`.
Do not deviate from its rules (preserve quotes, line width, indentation, etc.).

### Validation

- Ensure files pass `actionlint` for GitHub Actions-specific rules.
- Ensure files pass `yamllint` using the repository's `.yamllint` configuration.

### Documentation Links

Include links to the docs of the tools or services the workflow installs or integrates
(e.g., an action's README, a CLI tool site, or a reusable workflow reference).
Place the link next to the relevant job/step or in a short comment so maintainers can verify usage details quickly.

## Repository Tooling

- **Local Development**

  `actionlint`, `yamllint`, and `yamlfix` are run automatically via pre-commit hooks. Install with:

  ```bash
  pre-commit install
  ```

- **CI Integration**

  PRs are checked by `reviewdog/action-actionlint` which reports actionlint findings as review comments.

## What to Avoid

- Formatting that conflicts with `.yamlfix.toml`
- Missing or outdated documentation link
- Use of `@latest` or unversioned actions without justification

## Limitations

The agent cannot execute workflows directly.
Always propose changes as precise diffs and recommend the user run the local commands above or rely on CI feedback.
