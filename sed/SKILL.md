---
name: sed
description: 'Fast, non-interactive text stream editing and precise file segment extraction using sed.'
---

# Skill: sed

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Fast, non-interactive text stream editing and precise file segment extraction using `sed`.

## When to Use This Skill

- You need to extract specific line ranges from a large file without reading the whole file into memory.
- You need to perform non-interactive, programmatic find-and-replace across files.
- You are writing shell scripts or processing streams of data in pipelines.
- You want to extract snippets of log files or codebase for context extraction.

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

### 5. In-Place Edit (With Safety)

When modifying files directly, use `-i` (or `-i.bak` to create backups on some OS). Note: GNU `sed` supports `-i` directly, but macOS/BSD `sed` requires `-i ''`.

```bash
# GNU sed (Linux)
sed -i 's/old/new/g' <file>
```

## Core Principles

- **Prefer `sed -n`**: Always suppress default output when extracting segments to prevent flooding the terminal.
- **Quote Safely**: Use single quotes `'...'` for sed commands to avoid shell expansion issues, unless you intentionally need variable expansion (in which case use double quotes `"..."` carefully).
- **Non-Interactive First**: Never assume human intervention is possible.

## Gotchas

- **macOS/BSD vs. GNU `sed`**: macOS `sed -i` requires an extension argument (like `sed -i '' 's/old/new/g' file`), whereas Linux (GNU) `sed` allows `-i` without an extension. Since the agent primarily runs on Linux, `sed -i` is usually safe, but be cautious of cross-platform scripts.
- **Regex Dialects**: By default, `sed` uses Basic Regular Expressions (BRE). You must escape `+`, `?`, `|`, `(`, `)`, `{`, `}`. To use Extended Regular Expressions (ERE), pass the `-E` flag (e.g., `sed -E 's/(foo|bar)/baz/g'`).

## What to Avoid

- Avoid using `sed` to edit JSON, YAML, or XML files when structured tools like `jq` or `yq` are available.
- Do not use `sed` to edit source code AST when specialized formatting/refactoring tools exist.
