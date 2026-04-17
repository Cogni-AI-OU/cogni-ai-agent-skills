---
description: 'JSON formatting standards'
applyTo:
  - '**/*.json'
---

# JSON Instructions

## JSON Content Rules

- Use spaces for indentation (2 spaces per level per .editorconfig); avoid tabs.
- End files with a newline (per .editorconfig).
- Use double quotes for all strings and property names (JSON standard).
- Ensure proper comma usage: include commas between elements, but not after the last element in an object or array.
- Use consistent indentation for nested structures.
- Keep the JSON structure valid and parseable.

## JSON Structure and Formatting

- **Objects**: Place opening braces on the same line as the property name or at the start of the file.
  Close braces on their own line at the same indentation level as the opening line.
- **Arrays**: For short arrays (single line), place all elements on one line. For longer arrays,
  place each element on its own line with proper indentation.
- **Property Order**: When practical, keep properties in a logical or alphabetical order to improve
  readability and maintainability.
- **Comments**: JSON does not officially support comments. However, some JSON files in this repository
  (like `.vscode/settings.json` and `.devcontainer/devcontainer.json`) use JSONC format with `//` style
  comments, which is supported by VS Code. Use comments sparingly and only in files where the tool
  explicitly supports them.
- **Whitespace**: Use consistent spacing around colons (no space before, one space after).

## Validation

Use the following tools and checks to validate JSON files and ensure they conform to these guidelines:

- Use `jq` for validation and formatting: `jq . file.json` to validate standard JSON files.
  Note that `jq` does not support JSONC (JSON with comments).
- Many editors provide built-in JSON formatting (e.g., VS Code's "Format Document" command).
- The repository's pre-commit hooks include `end-of-file-fixer` which applies to JSON files.
