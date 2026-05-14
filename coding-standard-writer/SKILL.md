---
name: coding-standard-writer
description: Write a coding standards document for a project using the coding styles inferred from provided file(s) or folder(s).
---

# Skill Name: coding-standard-writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Dynamically generate a coding standards document based on the existing syntax, formatting, and conventions found in provided file(s) or folder(s).

## Core Process

1. **Ingest Targets**: Read the contents of the target `<file-path>` or `<folder-path>`.
2. **Analyze Syntax**: Parse indentation, variable naming (`camelCase`, `snake_case`), commenting styles, block nesting, and string quotation formats.
3. **Identify Majority Rules**: Tally occurrences of different styles; establish the majority as the standard.
4. **Handle Inconsistencies**: Automatically fix minority inconsistencies to match the established standard or report them to the user.
5. **Format Document**: Use a "minimal" or "verbose" template structure to compose the guidelines.
6. **Output Generation**: Write the result to a new file (e.g., `CONTRIBUTING.md`, `STYLE.md`) or inject it into the `README.md`.

## Core Principles

- **Empirical Inference**: Standards must be derived strictly from existing code, not assumed.
- **Template Adaptation**: Use "verbose" for comprehensive style guides and "minimal" for concise rule summaries.
- **Contextual Insertion**: When appending to `README.md`, locate the most logical insertion point (e.g., at the end or under a "Contributing" heading).

## When to Use

- When tasked with creating coding guidelines from existing code.
- To detect and fix formatting inconsistencies across multiple files.
- When generating `CONTRIBUTING.md`, `STYLE.md`, or `CODE_OF_CONDUCT.md`.

## Quick Start

1. Identify the reference file or folder.
2. Read the source contents to infer formatting patterns.
3. Generate the coding standard using a minimal or verbose markdown template.
4. Write to the designated output location.

## Diagnostics and Troubleshooting

- If file styles are extremely chaotic, prompt the user to choose a baseline reference file before generating the standard.

## Best Practices

- Fetch external style guides as reference if standard language conventions (e.g., PEP 8 for Python, standard for JavaScript) are requested or heavily implied.
- If requested, generate a companion test file to enforce the newly defined standards.

## What to Avoid

- Overwriting existing documented standards without confirmation.
- Injecting subjective preferences that contradict the codebase's existing majority style.

## Related Skills

- **docs-writer**: You MUST load this skill when writing or updating READMEs and Architectural Decision Records.
