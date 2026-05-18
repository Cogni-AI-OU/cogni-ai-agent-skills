---
name: yaml
description: >-
  Generic guidelines for YAML formatting, linting, and structural rules.
  You MUST load this skill when updating or creating YAML files.
license: MIT
---

# yaml

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generic guidelines for YAML formatting, linting, and structural rules.

## When to Use

- When creating or modifying YAML configuration files (e.g., `.yml`, `.yaml`).
- To ensure proper formatting, quoting, and indentation of YAML data structures.
- Before committing YAML files to ensure they pass project linting standards.

## When Not to Use

- When performing complex, programmatic queries, merges, or deep value extractions from YAML files (use the `yq` skill instead).
- For processing JSON files, unless converting them explicitly to YAML.
- When working in a repository that mandates a strictly different data serialization format (e.g., TOML, INI).

## Common Pitfalls

- **Tabs for Indentation**: Using tabs instead of spaces, which is strictly invalid in the YAML specification and will cause parsing errors.
- **Unquoted Boolean Strings**: Writing unquoted `yes`, `no`, `on`, or `off`, which older YAML 1.1 parsers evaluate as booleans rather than strings.
- **Relying on Text Tools**: Using `sed` or `awk` to modify YAML structures, leading to broken indentation and corrupted files.

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
