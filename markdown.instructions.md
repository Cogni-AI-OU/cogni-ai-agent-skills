---
description: 'Documentation and content creation standards'
applyTo:
  - '**/*.md'
---

# Markdown Instructions

## Markdown Content Rules

The following markdown content rules are enforced in the validators:

1. **Headings**: Use H1 (`#`), H2 (`##`), and H3 (`###`) heading levels to structure content.
   Avoid H4 (`####`) and deeper levels, as they suggest content needs better organization or
   should be split into separate documents.
2. **Lists**: Use bullet points or numbered lists for lists. Ensure proper indentation and spacing.
3. **Code Blocks**: Use fenced code blocks for code snippets. Always specify the language for syntax
   highlighting (required for linting compliance).
4. **Links**: Use proper Markdown syntax for links. Ensure that links are valid and accessible.
5. **Images**: Use proper Markdown syntax for images. Include alt text for accessibility.
6. **Tables**: Use Markdown tables for tabular data. Ensure proper formatting and alignment.
7. **Line Length**: Limit line length to 120 characters to align with project linting.
8. **Whitespace**: Use appropriate whitespace to separate sections and improve readability.

## Formatting and Structure

Follow these guidelines for formatting and structuring your markdown content:

- **Lists**: Use `-` for bullet points and `1.` for numbered lists. Indent nested lists with two spaces.
- **Code Blocks**: Use triple backticks (```) to create fenced code blocks. Always specify the
  language after the opening backticks for syntax highlighting (e.g., `csharp`). This is required
  for linting compliance.
- **Links**: Use `[link text](URL)` for links. Ensure that the link text is descriptive and the URL is valid.
  - If a URL is long or reused, prefer reference-style links placed at the end of the file
    after `<!-- Named links -->`.
- **Images**: Use `![alt text](image URL)` for images. Include a brief description of the image in the alt text.
- **Tables**: Use `|` to create tables. Ensure that columns are properly aligned and headers are included.
- **Line Length**: Break lines at 120 characters to match `.markdownlint.yaml`. Use soft line breaks for long paragraphs.
- **Whitespace**: Use blank lines to separate sections and improve readability. Avoid excessive whitespace.

## Validation Requirements

Ensure compliance with the following validation requirements:

- **Content Rules**: Ensure that the content follows the markdown content rules specified above.
- **Formatting**: Ensure that the content is properly formatted and structured according to the guidelines.
- **Validation**: Run the validation tools to check for compliance with the rules and guidelines.

After making changes, run appropriate validation tools to verify compliance with the markdownlint rules.

## Project Markdown Lint Rules

The project enforces the following markdownlint rules:

- Keep line length <=120 characters.
- Surround headings and lists with blank lines; fence code blocks with blank lines.
- Avoid trailing spaces; ensure a single trailing newline.
- Table column style (MD060): follow the style defined in `.markdownlint.yaml`.
  The default style is `compact`, which requires spaces around pipes in both header separators and data rows.
  Example: `| ----- | ----------- |` not `|-------|-------------|`.
  Reflow columns with a markdown table formatter (for example, VS Code "Format Table"
  or `npx markdown-table`) to keep pipes consistent.
- Avoid hard tabs (MD010/no-hard-tabs).
- Headings must have blank lines around them (MD022/blanks-around-headings).
- Lists must be surrounded by blank lines (MD032/blanks-around-lists).
- Fenced code blocks need surrounding blank lines (MD031/blanks-around-fences) and a language.
- Files end with a single newline (MD047/single-trailing-newline).

## Validation

- Repository rules come from `.markdownlint.yaml`.
- Run `pre-commit run markdownlint -a` to verify locally.
