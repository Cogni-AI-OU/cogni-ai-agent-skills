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

### Git Repository & Workspace Dotfiles

- **`.astro/config.yaml`**: Configuration file for the Astro web framework, defining build options, integrations, and project settings.
- **`.claude/`**: Directory containing workspace-specific Claude configuration, such as `settings.json` for hooks, tool permissions, and model or other workspace settings.
- **`.devcontainer/`**: Directory for containerized development environments, containing `devcontainer.json` (configuration), `requirements.txt` (Python dependencies), and `apt-packages.txt` (system packages).
- **`.editorconfig`**: Defines consistent coding styles (indentation, line endings, character set) for multiple developers working on the same project across various IDEs.
- **`.env.example` / `.env.sample` / `.env.dist`**: Provides a template of required environment variables without including actual secret values.
- **`.fdignore`**: Specifies files and directories to ignore for the `fd` search tool, often mirroring `.gitignore` but used for faster file finding.
- **`.gemini/`**: Directory containing configuration for Google Gemini, such as `settings.json` which typically points it to use `AGENTS.md` for context.
- **`.github/CODEOWNERS`**: Defines individuals or teams responsible for specific code paths, automatically assigning them as PR reviewers.
- **`.github/ISSUE_TEMPLATE/*.yml`**: Structured templates for bug reports and feature requests to ensure consistent issue reporting.
- **`.github/actionlint.yml`**: Configuration file for `actionlint` to define custom linting rules or ignore specific errors in GitHub Actions workflows.
- **`.github/copilot-instructions.md`**: Comprehensive coding standards and instructions for GitHub Copilot in the repository context.
- **`.github/dependabot.yml`**: Configures GitHub Dependabot to automatically check for and create pull requests to update dependencies.
- **`.github/mcp-config.json`**: Configuration for the Model Context Protocol (MCP) server, providing agents with access to GitHub tools.
- **`.github/prompts/*.{md,yml}`**: Prompt templates and instructions for GitHub Models, Copilot, and other AI agents.
- **`.github/workflows/AGENTS.md`**: Agent instruction file specifically for managing and understanding GitHub workflows.
- **`.github/workflows/README.md`**: Documentation for GitHub Actions workflows, describing their purpose, inputs, and usage.
- **`.github/workflows/*.yml`**: GitHub Actions workflow files for CI/CD automation, testing, and deployment.
- **`.github/{actionlint,pre-commit}-matcher.json`**: GitHub Actions problem matchers that enable inline error reporting for linters in PRs.
- **`.gitattributes`**: Defines Git attributes per path, controlling line ending normalization, merge strategies, text/binary classification, and diff output.
- **`.gitignore`**: Specifies intentionally untracked files to ignore (e.g., build artifacts, temporary files, secrets) preventing them from being committed to the Git repository.
- **`.gitmodules`**: Configures Git submodules, mapping their paths to the remote repository URLs.
- **`.htaccess`**: Distributed configuration file for Apache web server, allowing for decentralized management of web server configuration.
- **`.lycheeignore`**: Defines URL patterns and regular expressions to exclude from link checking with lychee.
- **`.markdown-link-check.json`**: Configures `markdown-link-check` behavior, including timeouts, ignore patterns, and status code handling.
- **`.markdownlint.yaml` / `.markdownlint.json`**: Configures rules for Markdownlint to enforce structural and stylistic consistency across Markdown files.
- **`.markdownlintignore`**: Specifies files and directories to exclude from Markdown linting.
- **`.mdlrc`**: Configuration file for the `mdl` (Markdown lint) tool, written in Ruby.
- **`.my.cnf`**: Local configuration file for MySQL/MariaDB clients, often used to store project-specific database credentials or settings.
- **`.npmrc`**: Project-specific npm configuration, such as registry URLs or dependency resolution strategies.
- **`.nvmrc` / `.node-version`**: Specifies the required Node.js version for the project, automatically picked up by tools like nvm or n (Node Version Manager).
- **`.pre-commit-config.yaml`**: Configures pre-commit hooks to automatically format code, check for secrets, and run linters before a commit is finalized.
- **`.ripgreprc`**: Project-specific configuration for `ripgrep` (`rg`), defining default flags and ignore patterns.
- **`.tours/`**: Directory for VS Code CodeTour files, including `*.tour` (walkthroughs) and `README.md` (documentation).
- **`.vscode/`**: Directory for VS Code-specific configurations, including `settings.json` (workspace settings), `extensions.json` (recommended extensions), `launch.json` (debug configurations), and `tasks.json` (task runners).
- **`.yamlfix.toml`**: Configures `yamlfix` for automated YAML formatting and style enforcement.
- **`.yamllint` / `.yamllint.yaml`**: Defines rules for yamllint to ensure YAML files are syntactically valid and stylistically consistent.
- **`AGENTS.md`**: The primary entry point and quick reference for AI agents, defining common tasks, commands, and context.

### Linux-specific & User Home ($HOME) Dotfiles

- **`.bash_history`**: Stores the command history for the Bash shell.
- **`.bash_profile` / `.profile`**: Initialization scripts for login shells; `.bash_profile` is Bash-specific, while `.profile` is a more general fallback.
- **`.bashrc`**: The primary initialization script for non-login Bash shells, used for aliases, environment variables, and prompt settings.
- **`.cache/`**: Directory for user-specific non-essential data (XDG_CACHE_HOME), such as downloaded files or temporary application state.
- **`.config/`**: Directory for user-specific configuration files (XDG_CONFIG_HOME), following the XDG Base Directory Specification.
- **`.ctags`**: Configuration for Ctags, used to define how source code symbols are indexed for navigation.
- **`.curlrc`**: Default configuration for the `curl` command-line tool, used to specify common flags or proxy settings.
- **`.drush/`**: Configuration directory for Drush (Drupal Shell), containing aliases and command-specific settings.
- **`.gdbinit`**: Initialization script for the GDB debugger, used to define custom commands or UI settings.
- **`.gitconfig`**: The global Git configuration file (typically in `$HOME`), containing user identity, global aliases, and default behaviors.
- **`.gnupg/`**: Directory for GnuPG (GNU Privacy Guard) configuration, keys, and trust database.
- **`.hyper.js`**: Configuration file for the Hyper terminal emulator.
- **`.inputrc`**: Configuration for the Readline library, used by shells (Bash) and other CLI tools for line editing and history.
- **`.lesshst`**: Stores the search and command history for the `less` pager.
- **`.lldbinit`**: Initialization script for the LLDB debugger, similar to `.gdbinit`.
- **`.netrc`**: Stores credentials for automatic login to FTP servers, HTTP sites, and other services used by tools like `curl` and `git`. **CRITICAL**: Should be kept secure with `600` permissions.
- **`.npmrc`**: User-level npm configuration, often containing authentication tokens for registries.
- **`.p10k.zsh`**: Configuration file for the Powerlevel10k Zsh theme, defining the visual appearance of the terminal prompt.
- **`.ripgreprc`**: Global configuration for `ripgrep` (`rg`), ensuring consistent search behavior across all projects.
- **`.screenrc`**: Configuration file for GNU Screen, a terminal multiplexer similar to Tmux.
- **`.sqliterc`**: Configuration for the SQLite3 command-line interface, used for setting output formats and history.
- **`.ssh/`**: Directory containing SSH configuration, known hosts, and private/public keys. **CRITICAL**: Private keys MUST have `600` permissions and NEVER be committed.
- **`.terraformrc`**: Global configuration for Terraform, used to set provider mirrors or CLI behavior.
- **`.tmux.conf`**: Configuration for the Tmux terminal multiplexer, enabling custom key bindings and status bar layouts.
- **`.vimrc`**: Configuration file for the Vim text editor, defining key mappings, plugin settings, and UI preferences.
- **`.wgetrc`**: Configuration for the `wget` tool, defining default download behaviors and network settings.
- **`.wine/`**: The default prefix directory for Wine, containing the virtual Windows filesystem and registry.
- **`.zprofile`**: The login shell initialization script for Zsh.
- **`.zshrc`**: The initialization script for Zsh shells, similar to `.bashrc`.
- **`my.cnf`**: Configuration for MySQL and MariaDB clients and servers, defining connection parameters and system variables.

## Best Practices

- **Keep it Minimal**: Only add necessary rules; rely on community standard defaults where possible.
- **Document Non-Standard Rules**: If a configuration deviates from standard conventions, add an inline comment explaining why.
- **Merge, Don't Replace**: When updating existing configuration files, merge organizational standards into the existing content rather than replacing the file entirely. Preserve project-specific customizations.
- **Lexicographical Order**: Maintain hooks in `.pre-commit-config.yaml` and other list-based configurations in alphabetical order.
- **Standard Formatting**: Use 4-space indentation for most files, but 2-space for YAML and JSON in `.editorconfig`.
- **Test Hooks Locally**: Always test `.pre-commit-config.yaml` changes locally by running `pre-commit run --all-files` before pushing.
- **Use .env.example**: Never commit actual `.env` files. Maintain an up-to-date `.env.example` for developers to copy.

## Common Snippets

### Search for dotfiles repositories

```bash
gh search repos "dotfiles" --limit 20
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
- **gh-search**:
  You MUST load this skill when searching for repositories or code examples using the GitHub CLI.
- **github-actions**:
  You MUST load this skill when troubleshooting or configuring GitHub Actions workflows.
- **pre-commit**:
  You MUST load this skill when managing pre-commit hooks.
- **yaml**:
  You MUST load this skill when updating YAML configuration dotfiles.
