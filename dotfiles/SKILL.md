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
- **`.yamllint` / `.yamllint.yaml`**: Defines rules for yamllint to ensure YAML files are syntactically valid and stylistically consistent.
- **`.nvmrc` / `.node-version`**: Specifies the required Node.js version for the project, automatically picked up by tools like nvm or n (Node Version Manager).
- **`.env.example` / `.env.sample`**: Provides a template of required environment variables without including actual secret values.
- **`.github/dependabot.yml`**: Configures GitHub Dependabot to automatically check for and create pull requests to update dependencies.
- **`.github/workflows/*.yml`**: GitHub Actions workflow files for CI/CD automation, testing, and deployment.
- **`.github/copilot-instructions.md`**: Custom instructions for GitHub Copilot in the repository context.

## Best Practices

- **Keep it Minimal**: Only add necessary rules; rely on community standard defaults where possible.
- **Document Non-Standard Rules**: If a configuration deviates from standard conventions, add an inline comment explaining why.
- **Test Hooks Locally**: Always test `.pre-commit-config.yaml` changes locally by running `pre-commit run --all-files` before pushing.
- **Use .env.example**: Never commit actual `.env` files. Maintain an up-to-date `.env.example` for developers to copy.

## Common Pitfalls

- **Overlapping Rules**: Configuring conflicting rules in `.editorconfig` and language-specific linters (e.g., Prettier/ESLint). Ensure linter configs take precedence or align exactly with `.editorconfig`.
- **Ignoring Generated Files**: Forgetting to add build output directories (like `node_modules/`, `dist/`, `.venv/`) to `.gitignore`, leading to massive, unwanted commits.
- **Incorrect Line Endings**: Not enforcing `* text=auto eol=lf` in `.gitattributes`, causing cross-platform line ending issues (CRLF vs LF) and noisy git diffs.
- **Hardcoding Secrets**: Accidentally committing secrets because `.env` wasn't added to `.gitignore` before creating the file.

## Related Skills

- **editorconfig**:
  You MUST load this skill when creating or updating an `.editorconfig` file.
- **gitattributes**:
  You MUST load this skill when configuring Git behaviors via `.gitattributes`.
- **pre-commit**:
  You MUST load this skill when managing pre-commit hooks.
- **yaml**:
  You MUST load this skill when updating YAML configuration dotfiles.
