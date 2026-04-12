# Copilot Instructions

## Project Overview

This is the organization-wide `.github` repository. It provides
default community health files, GitHub Actions workflows, issue/PR templates,
and coding standards that apply across all repositories in the organization.

Key contents:

- **Community health files**: CODE_OF_CONDUCT.md, issue templates, PR templates
- **Reusable workflows**: CI/CD, linting, automated reviews
- **Organization profile**: Public-facing info in `profile/README.md`
- **Agent configurations**: `AGENTS.md` for AI coding assistants

### Getting started

- Refer to the `README.md` in the project root for setup and installation instructions.
- Check also `.tours/getting-started.tour` which provides a guided walkthrough of key project features and structure.

## Coding Standards

### Python

- Use **Python 3.11+**.
- Use `uv` script headers for dependency management:

  ```python
  #!/usr/bin/env -S uv run --script
  # /// script
  # requires-python = ">=3.11"
  # dependencies = [
  #     "xero-python",
  #     "PyYAML",
  # ]
  # ///
  ```

- Follow **PEP 8** style guidelines.
- Use `argparse` for CLI argument parsing.
- Handle `BrokenPipeError` for CLI tools that might be piped to `head` or `grep`.

## Formatting Guidelines

### JSON

Follow the JSON rules in `.github/instructions/json.instructions.md`, which mirror the repository `.editorconfig` configuration.

To test locally, use `jq` for validation or use the VS Code JSON formatter.

### Markdown

Follow the Markdown rules in `.github/instructions/markdown.instructions.md`, which mirror the repository markdownlint configuration.

To test locally, run via `pre-commit run markdownlint -a` or use the VS Code Markdownlint extension.

### YAML

Follow the YAML rules in `./.github/instructions/yaml.instructions.md`, which mirror the repository `.yamllint` configuration.

Notes:

- Project utilizes Codespaces with config at `.devcontainer/devcontainer.json` and requirements at `.devcontainer/requirements.txt`.
- GitHub Actions run pre-commit checks (`.pre-commit-config.yaml`).
- To verify locally, run `pre-commit run yamllint -a` from the repo root.

### Devcontainer Guidance

Project utilizes Codespaces with config at `.devcontainer/devcontainer.json`
and requirements at `.devcontainer/requirements.txt`.
These rules apply only when the agent is running inside GitHub Codespaces
or the repository's VS Code devcontainer.
In that environment, the container should be treated as the controller
runtime and as the source of required controller-side dependencies.

- Treat the repository devcontainer as the default controller environment
  for local development and testing.
- Keep controller dependency installation in the devcontainer
  configuration so Molecule scenarios can assume those tools are already
  available.
- Do not install controller-side Python dependencies during Molecule runs
  when the agent is already operating inside Codespaces or the repo
  devcontainer.
- Do not create additional Python virtual environments such as `.venv`
  or `venv`; use the existing container Python environment, which should
  already provide the required dependencies.
- If dependencies are missing in a Codespace or devcontainer, update
  `.devcontainer/requirements.txt` or `.devcontainer/devcontainer.json`
  instead of introducing a per-run Molecule install step or a separate
  virtual environment.
- Use `CODESPACES=true` as the primary quick check for GitHub Codespaces.
- Outside Codespaces, use the presence of `/.dockerenv` together with
  the repository `.devcontainer/devcontainer.json` as a practical check
  for the containerized dev environment.

## Project Structure

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/      # Issue templates (bug reports, feature requests)
│   ├── agents/              # AI agent configurations
│   ├── instructions/        # Language-specific coding standards
│   ├── skills/              # Agent skills definitions
│   ├── workflows/           # GitHub Actions workflows
│   ├── copilot-instructions.md
│   └── pull_request_template.md
├── .tours/                   # VS Code guided tours
├── profile/
│   └── README.md             # Organization profile (shown on GitHub org page)
├── AGENTS.md                 # AI agent guidance
├── CODE_OF_CONDUCT.md        # Community standards
└── README.md                 # Repository documentation
```

### Tours

- Keep the `.tours` folder up-to-date (especially `.tours/getting-started.tour`)
  when making significant changes to the codebase.
  Update existing tours or create new ones to reflect changes in project structure,
  workflows, or key files.

## Troubleshooting

### Finding Build Errors

To identify and diagnose the latest build errors:

1. **Reproduce errors locally:**
   - For pre-commit errors: Run `pre-commit run -a` to check all files
   - For specific hooks: Run `pre-commit run <hook-name> -a` (e.g., `markdownlint`, `yamllint`)
   - For actionlint errors: Install actionlint and run it on workflow files

2. **Common error patterns:**
   - **Ansible missing Python modules:** If a module such as `requests` or
     `docker` is installed for the main container Python but Ansible still
     cannot import it, check `ansible --version` to identify the interpreter in
     use. In Codespaces/devcontainers, Ansible may run from a pipx-managed
     environment, so install controller-side libraries there as well, for
     example with `pipx inject ansible -r .devcontainer/requirements-ansible.txt`.
   - **Markdown linting errors:** Check `.markdownlint.yaml` for rules; errors show line numbers
   - **YAML linting errors:** Check `.yamllint` for rules; verify indentation and structure
   - **JSON formatting errors:** Use `jq . <file>` to validate JSON syntax
