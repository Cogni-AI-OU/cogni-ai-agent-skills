# Instructions Catalog for Agents

Authoritative list of repository instruction files. Use these when editing matching files so changes
stay compliant with linting and CI.

For a human-readable overview, see [README.md](README.md).

## Instruction files

| Instruction | Scope | Purpose |
| ----------- | ----- | ------- |
| [README.md](README.md) | All instructions | Overview of instruction purpose and validation tooling |
| [ansible.instructions.md](ansible.instructions.md) | Ansible roles and playbooks | Conventions, idempotency, and linting for Ansible content |
| [github-workflows.instruction.md](github-workflows.instruction.md) | .github/workflows and workflow-templates | Ordering, formatting, validation for GitHub Actions workflows |
| [json.instructions.md](json.instructions.md) | **/*.json | Formatting rules for JSON and JSONC |
| [markdown.instructions.md](markdown.instructions.md) | **/*.md | Markdown structure and linting expectations |
| [readme.instructions.md](readme.instructions.md) | Repository README.md | Layout, badges, and content guidance for the main README |
| [yaml.instructions.md](yaml.instructions.md) | **/*.{yaml,yml} | YAML formatting and linting rules |

## Usage

- Before editing a file, check this table and read the relevant instruction file.
- Follow the `applyTo` patterns in each instruction file to know when it applies.
- Keep this catalog updated when adding, renaming, or removing instruction files.
