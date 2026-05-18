---
name: unicode
description: 'Reference for Unicode character hex ranges and regex blocks for searching, matching, or filtering text across international scripts and symbols.'
license: MIT
---

# Unicode Regex Ranges

<!-- markdownlint-disable MD013 MD023 MD031 MD032 MD033 -->

## When to Use This Skill

- You need to search, match, or filter text containing specific Unicode ranges (e.g., CJK, Cyrillic, Emoji).
- You are writing regex to validate or extract international characters, symbols, or specific scripts.
- You need a reference for exact hexadecimal ranges for various languages or symbols.

## Core Process

When tasked with matching specific languages or symbols:
1. Identify the target script, language, or symbol category.
2. Look up the precise hex range (`\x{XXXX}-\x{YYYY}`) in the reference tables below.
3. Insert the range into your tool's regex syntax (e.g., `[\x{0100}-\x{024F}]+` for PCRE-compliant engines like `rg` or `grep -P`).

## Core Principles

- **Engine Compatibility**: The ranges provided use `\x{XXXX}` syntax, which is standard in PCRE (e.g., ripgrep, PHP, Python via `regex` module). In other languages like JavaScript or standard Python, you may need `\uXXXX` or `\U000XXXXX` for surrogate pairs.
- **Combined Ranges**: Multiple ranges can be grouped in character classes: `[\x{0900}-\x{097F}\x{0A00}-\x{0A7F}]`.
- **Case Sensitivity**: For ranges containing cased letters, ensure your tool is set to case-insensitive mode if required, though ranges often cover both.

## Unicode Range Reference

For a comprehensive list of Unicode character hex ranges and regex blocks categorized by script, language, and symbol type, see the [Unicode Range Reference](references/unicode-ranges.md).

## Gotchas

- **Surrogate Pairs in JS/Python**: If using standard JavaScript or Python (`re` module, not `regex`), you cannot use `\x{10000}`. You must either use the `\uXXXX` equivalent, `\U00010000`, or the ES6 `\u{10000}` syntax with the `/u` flag in JS.
- **Combined Ranges**: Take care not to overlap or create invalid ranges when combining (e.g., `[\x{2500}-\x{257F}\x{2580}-\x{259F}]` can safely be written as `[\x{2500}-\x{259F}]`).
- **Missing Characters**: The ranges cover primary codepoints but might omit rarely used characters placed in Extended blocks unless the Extended blocks are explicitly included.
