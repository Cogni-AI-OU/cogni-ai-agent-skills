---
name: yaml
description: >-
  Generic guidelines for YAML formatting, linting, and structural rules.
  You must load this skill when updating or creating YAML files.
---

# yaml

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generic guidelines for YAML formatting, linting, and structural rules.

## Core Principles

- **Indentation**: Use 2 spaces for indentation. Never use tabs.
- **Structure**: Ensure valid YAML structure, with proper use of arrays (`- `) and objects.
- **Quoting**: Strings do not need to be quoted unless they contain special characters or might be evaluated as a different type (e.g., `true`, `false`, `yes`, `no`, numbers).
- **Comments**: Use `#` for comments. Be descriptive but concise.
- **yq Skill**: For programmatic parsing, editing, merging, and transforming of YAML files, load the **yq** skill instead.

## What to Avoid

- Using `sed`, `awk`, or `grep` to modify YAML structures, as these tools are not schema-aware and often break indentation.
- Mixing tabs and spaces.
