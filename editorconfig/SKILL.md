---
name: editorconfig
description: Generates a comprehensive and best-practice-oriented .editorconfig file based on project analysis and user preferences.
---

# editorconfig

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generate a robust, comprehensive, and best-practice-oriented `.editorconfig` file to ensure consistent coding styles across different editors and IDEs.

## Core Process

1. **Analyze Context**: Scan the project structure and file types to infer the languages and technologies being used.
2. **Incorporate Preferences**: Adhere to explicit user constraints (e.g., indentation style/size). Note any conflicts with best practices in the final explanation.
3. **Apply Universal Best Practices**: Enforce baseline standards (character sets, LF line endings, trailing whitespace, and final newlines).
4. **Generate File**: Output a structured `.editorconfig` file covering all relevant file types found in the project via glob patterns (`*`, `**.js`, `**.py`, etc.).
5. **Provide Explanations**: Detail the rationale for every single rule generated in a clear Markdown "Rule-by-Rule Explanation" section below the code block.

## Core Principles

- **Precision Targeting**: Apply rules via universal and specific glob patterns without polluting unrelated scopes.
- **Universal Standards**: Use `lf` for line endings, `utf-8` charset, trim trailing whitespace, and insert final newlines globally unless context demands otherwise.
- **Exceptions Mapping**: Explicitly disable `trim_trailing_whitespace` for `[*.md]` files since trailing whitespace holds semantic meaning (hard line breaks).

## When to Use

- When requested to generate, update, or configure an `.editorconfig` file.
- When standardizing coding styles or formatting hooks for a workspace.

## Quick Start

```editorconfig
# Top-most EditorConfig file
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = false
```

## Diagnostics and Troubleshooting

- If settings are overridden by parent directories, verify that `root = true` is placed at the top of the file.
- If whitespace handling causes issues in Markdown or Makefiles, explicitly add overrides for `[*.md]` or `[Makefile]`.

## Best Practices

- Start with `root = true` to stop the EditorConfig search in the current directory.
- Combine the output into two parts: A single code block with the `.editorconfig` and a "Rule-by-Rule Explanation" section in Markdown.

## What to Avoid

- Outputting an `.editorconfig` without rule-by-rule explanations.
- Overwriting existing `.editorconfig` files blindly without reading and merging current project conventions.

## References

- <https://github.com/github/awesome-copilot/blob/main/skills/editorconfig/SKILL.md>
