---
name: dotfiles
description: 'Reference for repository dotfiles, including their purposes, standard configurations, and usage guidelines. You MUST load this skill when configuring, troubleshooting, or understanding repository dotfiles.'
license: MIT
---

# dotfiles

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Identifying the correct dotfile to modify for a specific configuration change (e.g., formatting, linting, git behavior).
- Troubleshooting CI/CD, linting, formatting, or environment configuration issues.
- Setting up a new repository with standard organizational configuration files.
- Understanding the purpose of existing hidden configuration files in the root directory.

## When Not to Use

- Modifying application-specific source code or core business logic.
- Configuring cloud infrastructure outside the repository itself (e.g., Terraform, AWS).
- Modifying standard documentation files (`README.md`, `CONTRIBUTING.md`) that are not hidden dotfiles.

## Step-by-Step Workflows

### Configuring a Dotfile

1. **Identify the Scope**: Determine what needs configuring (e.g., editor settings, git attributes, linting rules, dependency management).
2. **Locate the Dotfile**: Find the appropriate dotfile in the repository root or `.github/` directory.
3. **Analyze Existing Configuration**: Read the file to understand current rules, overrides, and syntax.
4. **Apply Changes**: Modify the configuration following the specific tool's exact documentation and syntax.
5. **Verify Changes**: Run the associated tool (linter, formatter, or git command) to ensure changes are valid and have the intended effect.

## Dotfile Reference

- **`.editorconfig`**: Defines consistent coding styles (indentation, line endings, character set) for multiple developers working on the same project across various IDEs.
- **`.gitignore`**: Specifies intentionally untracked files to ignore (e.g., build artifacts, temporary files, secrets) preventing them from being committed to the Git repository.
- **`.gitattributes`**: Defines Git attributes per path, controlling line ending normalization, merge strategies, text/binary classification, and diff output.
- **`.pre-commit-config.yaml`**: Configures pre-commit hooks to automatically format code, check for secrets, and run linters before a commit is finalized.
- **`.markdownlint.yaml` / `.markdownlint.json`**: Configures rules for Markdownlint to enforce structural and stylistic consistency across Markdown files.
- **`.markdownlintignore`**: Specifies files and directories to exclude from Markdown linting.
- **`.lycheeignore`**: Defines URL patterns and regular expressions to exclude from link checking with lychee.
- **`.markdown-link-check.json`**: Configures `markdown-link-check` behavior, including timeouts, ignore patterns, and status code handling.
- **`.yamllint` / `.yamllint.yaml`**: Defines rules for yamllint to ensure YAML files are syntactically valid and stylistically consistent.
- **`.yamlfix.toml`**: Configures `yamlfix` for automated YAML formatting and style enforcement.
- **`.nvmrc` / `.node-version`**: Specifies the required Node.js version for the project, automatically picked up by tools like nvm or n (Node Version Manager).
- **`.env.example` / `.env.sample`**: Provides a template of required environment variables without including actual secret values.
- **`.github/dependabot.yml`**: Configures GitHub Dependabot to automatically check for and create pull requests to update dependencies.
- **`.github/workflows/*.yml`**: GitHub Actions workflow files for CI/CD automation, testing, and deployment.
- **`.github/workflows/README.md`**: Documentation for GitHub Actions workflows, describing their purpose, inputs, and usage.
- **`.github/workflows/AGENTS.md`**: Agent instruction file specifically for managing and understanding GitHub workflows.
- **`.github/{actionlint,pre-commit}-matcher.json`**: GitHub Actions problem matchers that enable inline error reporting for linters in PRs.
- **`.github/prompts/*.{md,yml}`**: Prompt templates and instructions for GitHub Models, Copilot, and other AI agents.
- **`.github/copilot-instructions.md`**: Comprehensive coding standards and instructions for GitHub Copilot in the repository context.
- **`.github/mcp-config.json`**: Configuration for the Model Context Protocol (MCP) server, providing agents with access to GitHub tools.
- **`.github/CODEOWNERS`**: Defines individuals or teams responsible for specific code paths, automatically assigning them as PR reviewers.
- **`.github/ISSUE_TEMPLATE/*.yml`**: Structured templates for bug reports and feature requests to ensure consistent issue reporting.
- **`.devcontainer/devcontainer.json`**: Configures a containerized development environment with specific tools, extensions, and settings.
- **`.devcontainer/requirements*.txt`**: Defines Python dependencies required within the development container.
- **`.devcontainer/apt-packages.txt`**: Lists system-level packages (Debian/Ubuntu) to be installed in the development container.
- **`.tours/*.tour`**: VS Code CodeTour files providing step-by-step interactive walkthroughs of the codebase.
- **`AGENTS.md`**: The primary entry point and quick reference for AI agents, defining common tasks, commands, and context.
- **`.gemini/settings.json`**: Configuration for Google Gemini, typically pointing it to use `AGENTS.md` for context.

## Best Practices

- **Keep it Minimal**: Only add necessary rules; rely on community standard defaults where possible.
- **Document Non-Standard Rules**: If a configuration deviates from standard conventions, add an inline comment explaining why.
- **Merge, Don't Replace**: When updating existing configuration files, merge organizational standards into the existing content rather than replacing the file entirely. Preserve project-specific customizations.
- **Lexicographical Order**: Maintain hooks in `.pre-commit-config.yaml` and other list-based configurations in alphabetical order.
- **Standard Formatting**: Use 4-space indentation for most files, but 2-space for YAML and JSON in `.editorconfig`.
- **Test Hooks Locally**: Always test `.pre-commit-config.yaml` changes locally by running `pre-commit run --all-files` before pushing.
- **Use .env.example**: Never commit actual `.env` files. Maintain an up-to-date `.env.example` for developers to copy.

## Common Snippets

### .editorconfig (Organizational Standard)

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 4

[*.{yml,yaml,json,md}]
indent_size = 2
```

### .gitattributes (Normalization)

```gitattributes
* text=auto eol=lf
*.{png,jpg,jpeg,gif} binary
*.lock linguist-generated
```

### .github/workflows/check.yml (Reusable Reference)

```yaml
---
name: Check
on:
  pull_request:
  push:
    branches: [main]
jobs:
  check:
    uses: Cogni-AI-OU/.github/.github/workflows/check.yml@main
```

## Common Pitfalls

- **Overlapping Rules**: Configuring conflicting rules in `.editorconfig` and language-specific linters (e.g., Prettier/ESLint). Ensure linter configs take precedence or align exactly with `.editorconfig`.
- **Ignoring Generated Files**: Forgetting to add build output directories (like `node_modules/`, `dist/`, `.venv/`) to `.gitignore`, leading to massive, unwanted commits.
- **Incorrect Line Endings**: Not enforcing `* text=auto eol=lf` in `.gitattributes`, causing cross-platform line ending issues (CRLF vs LF) and noisy git diffs.
- **Hardcoding Secrets**: Accidentally committing secrets because `.env` wasn't added to `.gitignore` before creating the file.

## Related Skills

- **agent-md**:
  You MUST load this skill when working with `AGENTS.md` or other agent-specific configuration files.
- **code-tour**:
  You MUST load this skill when creating or updating `.tours/` files.
- **devcontainer**:
  You MUST load this skill when managing `.devcontainer/` configurations.
- **dot-github**:
  You MUST load this skill when standardizing or updating the `.github/` directory structure.
- **editorconfig**:
  You MUST load this skill when creating or updating an `.editorconfig` file.
- **gitattributes**:
  You MUST load this skill when configuring Git behaviors via `.gitattributes`.
- **github-actions**:
  You MUST load this skill when troubleshooting or configuring GitHub Actions workflows.
- **pre-commit**:
  You MUST load this skill when managing pre-commit hooks.
- **yaml**:
  You MUST load this skill when updating YAML configuration dotfiles.
