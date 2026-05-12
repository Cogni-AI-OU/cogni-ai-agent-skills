---
name: python
description: >-
  Execute Python inline scripts via heredocs for complex log processing, summarization, or JSON parsing.
  You MUST load this skill when processing large logs.
---

# Skill: python

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Use Python via `python3 - <<'PY'` heredocs when processing large log files, complex text summarization, or parsing structured data (like JSON) where standard bash utilities (awk/sed/grep) become unwieldy or fragile. If `python3` is unavailable, you may fall back to `python`.

## Core Principles

- **Avoid Fragile Bash Pipelines**: Transition to Python for multi-file processing, stateful parsing, or complex data transformations.
- **Self-Contained Execution**: Use heredoc (`<<'PY'`) to execute inline Python without writing temporary `.py` scripts.
- **Quote the delimiter**: Always quote the heredoc delimiter (`<<'PY'`) to prevent variable expansion by bash.
- **Robust Parsing**: Utilize built-in `json`, `pathlib`, and `re` modules for robust text parsing.

## Usage Patterns

### Generic Log Processing and Filtering

Process multiple files, parse JSON structures, and filter for specific keywords or conditions dynamically.

```bash
python3 - <<'PY'
import json
import pathlib

# Define input sources mapping logical names to file paths
files = {
    'system-A': '/tmp/log-A.json',
    'system-B': '/tmp/log-B.json'
}

keywords = ['failed', 'fatal', 'error']

for name, path in files.items():
    print(f'===== {name} =====')
    try:
        # Use streaming approach for large files to minimize memory footprint
        with open(path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                lower_line = line.lower()
                if any(k in lower_line for k in keywords):
                    # strip() removes trailing newline for cleaner output
                    print(f'{i+1}: {line.strip()}')
    except Exception as e:
        print(f"Failed to process {name} (path: {path}): {e}")
    print()
PY
```
