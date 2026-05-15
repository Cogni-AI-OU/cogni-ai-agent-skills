---
name: yaml
description: >-
  Generic guidelines for YAML formatting, linting, and structural rules.
  You MUST load this skill when updating or creating YAML files.
---

# yaml

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generic guidelines for YAML formatting, linting, and structural rules.

## Core Principles

- **Indentation**: Use 2 spaces for indentation. Never use tabs.
- **Structure**: Ensure valid YAML structure, with proper use of dash-space list items (`-`) and objects.
- **Quoting**: Strings do not need to be quoted unless they contain special characters or might be evaluated as a different type (e.g., `true`, `false`, `yes`, `no`, numbers).
- **Comments**: Use `#` for comments. Be descriptive but concise.
- **yq Skill**: For programmatic parsing, editing, merging, and transforming of YAML files, load the **yq** skill instead.

## Linting and Formatting

- **yamllint**: Use `yamllint` to check for syntax and style issues according to the project's `.yamllint` configuration. Run it via pre-commit: `pre-commit run yamllint -a`.
- **yamlfix**: Use `yamlfix` for automated formatting based on `.yamlfix.toml` settings. Run it via pre-commit: `pre-commit run yamlfix -a`.
- **Pre-commit**: It is best practice to run all validation hooks before pushing changes: `pre-commit run -a`.

## What to Avoid

- Using `sed`, `awk`, or `grep` to modify YAML structures, as these tools are not schema-aware and often break indentation.
- Mixing tabs and spaces.
