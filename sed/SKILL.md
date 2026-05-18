---
name: sed
description: 'Fast, non-interactive text stream editing and precise file segment extraction using sed.'
license: MIT
---

# Skill: sed

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Fast, non-interactive text stream editing and precise file segment extraction using `sed`.

## When to Use This Skill

- You need to extract specific line ranges from a large file without reading the whole file into memory.
- You need to perform non-interactive, programmatic find-and-replace across files.
- You are writing shell scripts or processing streams of data in pipelines.
- You want to extract snippets of log files or codebase for context extraction.

## When Not to Use

- Parsing or modifying complex structured data formats (JSON, YAML, XML) where context-aware tools (`jq`, `yq`) are significantly safer.
- Making multi-line replacements with complex indentation rules where `ex` (Vim) or Python scripting is more robust.
- Interactive text editing.

## Core Process

1. **Identify the Target Range or Pattern**: Determine the start and end line numbers or regex boundaries.
2. **Construct the One-Liner**: Use standard `sed` syntax. Do not use interactive tools.
3. **Validate Locally**: Run without `-i` (in-place) first if modifying files, or strictly use read-only modes like `-n`.

## Essential One-Liners

### 1. Extract a Specific Line Range

Use this to extract a precise segment of a file (e.g., lines 80 to 95) without dumping the whole file.

```bash
sed -n '80,95p' <file>
```

### 2. Extract Lines Between Two Regex Patterns

Extract text between two known boundary strings (inclusive).

```bash
sed -n '/START_PATTERN/,/END_PATTERN/p' <file>
```

### 3. Replace a String (First Occurrence Per Line)

```bash
sed 's/old/new/' <file>
```

### 4. Replace a String (All Occurrences Per Line)

```bash
sed 's/old/new/g' <file>
```

### 5. Text Cleaning (Trim Spaces)

Remove leading and trailing whitespace from each line. Note: `\t` for tabs is a GNU extension; use literal tabs or `[[:blank:]]` for portability.

```bash
# Trim leading spaces and tabs (GNU)
sed -e 's/^[ \t]*//g' <file>

# Trim trailing spaces and tabs (GNU)
sed -e 's/[ \t]*$//g' <file>

# Combined trim (Portable/POSIX)
sed -e 's/^[[:blank:]]*//' -e 's/[[:blank:]]*$//' <file>
```

### 6. Case Conversion

Note: `\u` and `\U` are GNU `sed` extensions and are not portable (e.g., on macOS/BSD).

```bash
# Capitalize first character of each line (GNU)
sed 's/./\u&/' <file>

# Capitalize first character of every word (GNU)
sed -E 's/\b[a-z]/\U&/g' <file>
```

### 7. Structure and Reordering

```bash
# Swap first and last characters of each line (Extended Regex)
# Handles 2+ characters; 1-character lines remain unchanged.
sed -E 's/(.)(.*)(.)/\3\2\1/' <file>
```

### 8. Content Extraction and Conversion

```bash
# Remove all XML/HTML tags
sed -e 's/<[^>]*>//g' <file>

# Convert XML/HTML tags to newlines (GNU: \n)
# Portable sed requires a literal escaped newline in the replacement.
sed -e 's/<[^>]*>/\n/g' <file>

# WIF to SHA (part of a pipeline)
base58 -d | xxd -p -c200 | sed s/^80// | rg -oz "[A-Fa-f0-9]{64}"
```

### 9. System and Database Fixes

```bash
# Recursive directory tree visualization (simplified)
ls -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'

# List 40 largest files (recursive) - more precise than ls -R
find . -type f -exec du -h {} + | sort -hr | head -n40

# MySQL Collation Fix (Use with caution: may downgrade utf8mb4 to utf8)
# Only use if the target database does not support utf8mb4.
sed "s/utf8mb4_0900_ai_ci\|utf8mb4_unicode_ci/utf8_general_ci/g;s/\butf8mb[34]/utf8/g" <dump.sql>
```

### 10. In-Place Edit (With Safety)

When modifying files directly, use `-i` (or `-i.bak` to create backups on some OS). Note: GNU `sed` supports `-i` directly, but macOS/BSD `sed` requires `-i ''`.

```bash
# GNU sed (Linux)
sed -i 's/old/new/g' <file>
```

## Core Principles

- **Prefer `sed -n`**: Always suppress default output when extracting segments to prevent flooding the terminal.
- **Quote Safely**: Use single quotes `'...'` for sed commands to avoid shell expansion issues, unless you intentionally need variable expansion (in which case use double quotes `"..."` carefully).
- **Non-Interactive First**: Never assume human intervention is possible.

## Common Pitfalls

- **macOS/BSD vs. GNU `sed`**: macOS `sed -i` requires an extension argument (like `sed -i '' 's/old/new/g' file`), whereas Linux (GNU) `sed` allows `-i` without an extension. Since the agent primarily runs on Linux, `sed -i` is usually safe, but be cautious of cross-platform scripts.
- **Regex Dialects**: By default, `sed` uses Basic Regular Expressions (BRE). You must escape `+`, `?`, `|`, `(`, `)`, `{`, `}`. To use Extended Regular Expressions (ERE), pass the `-E` flag (e.g., `sed -E 's/(foo|bar)/baz/g'`).

## What to Avoid

- Avoid using `sed` to edit JSON, YAML, or XML files when structured tools like `jq` or `yq` are available.
- Do not use `sed` to edit source code AST when specialized formatting/refactoring tools exist.
