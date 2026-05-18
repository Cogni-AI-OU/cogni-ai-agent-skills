---
name: yaml
license: MIT
description: >-
  Generic guidelines for YAML formatting, linting, and structural rules.
  You MUST load this skill when updating or creating YAML files.
---

# yaml

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Creating or editing YAML configuration files (e.g., CI/CD pipelines, Docker Compose, Kubernetes manifests, Ansible playbooks).
- Formatting and linting YAML files to ensure consistency across a project.
- Writing portable YAML that must parse correctly across different parsers and language implementations.
- Reviewing pull requests for YAML structural validity, indentation consistency, and syntax correctness.

## When Not to Use

- Programmatic YAML manipulation (reading, editing, merging values) where the `yq` skill provides proper schema-aware tooling.
- Writing complex data pipelines or transformations better suited to JSON (where more tooling exists) or a proper programming language.
- When the data volume or depth makes YAML cumbersome—consider alternatives like TOML for config or JSON for data interchange.

## Common Pitfalls

- YAML's implicit typing can silently convert unquoted values: `yes`/`no` becomes boolean, `0123` becomes octal (in some parsers), and large numbers lose precision.
- Indentation must be consistent across the entire file—mixing spaces with tabs or using inconsistent indent depth causes parse errors that are hard to debug.
- Multi-line strings have multiple syntaxes (`|`, `>`, `|-`, `>-`, double-quoted, single-quoted) with subtle behavioral differences in trailing newline handling.
- Not all YAML parsers handle all YAML 1.2 features—some older parsers (e.g., Python `PyYAML` defaults) target 1.1, causing issues with boolean representation and other edge cases.

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
