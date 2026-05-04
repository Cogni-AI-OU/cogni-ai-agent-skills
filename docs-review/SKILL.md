---
name: docs-review
description: >-
  Check core architecture and documentation files for mutual consistency,
  identifying contradictions, outdated references, and structural mismatches.
  You must load this skill when asked to review or check consistency of documentation (such as *.md/*.mmd files).
license: MIT
---

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

# Docs Review

Guidance for reviewing core architecture, documentation, and constraint files for mutual consistency and accuracy. Use this skill when checking or updating repository documentation.

## When to Activate

- Checking core architecture files (`*.mmd`, `*.mzn`) for consistency.
- Reviewing documentation (`**/AGENTS.md`, `**/README.md`) for outdated references.

## Core Process

1. **Analyze Relationships**:
   Cross-reference the relationships, definitions, rules, and configurations defined across these files.
2. **Identify Inconsistencies**:
   Look for contradictions, outdated references, missing updates, or structural mismatches between files.
3. **Verify Up-to-Date Status**:
   Check if any of the documentation lags behind the current state of the repository.
4. **Conditional Edits**:
   **CRITICAL INSTRUCTION:** ONLY apply changes to these files if actual inconsistencies, contradictions,
   or outdated information are found. If all files are mutually consistent and up-to-date,
   do not make any edits—simply report back that the files are in order.
