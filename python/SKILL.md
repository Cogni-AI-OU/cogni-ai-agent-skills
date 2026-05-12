---
name: python
description: >-
  Execute Python inline scripts via heredocs for complex log processing, summarization, or JSON parsing.
  You MUST load this skill when processing large logs.
---

# Skill: python

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Use Python via `python - <<'PY'` heredocs when processing large log files, complex text summarization, or parsing structured data (like JSON) where standard bash utilities (awk/sed/grep) become unwieldy or fragile.

## Core Principles

- **Avoid Fragile Bash Pipelines**: Transition to Python for multi-file processing, stateful parsing, or complex data transformations.
- **Self-Contained Execution**: Use heredoc (`<<'PY'`) to execute inline Python without writing temporary `.py` scripts.
- **Quote the delimiter**: Always quote the heredoc delimiter (`<<'PY'`) to prevent variable expansion by bash.
- **Robust Parsing**: Utilize built-in `json`, `pathlib`, and `re` modules for robust text parsing.

## Usage Patterns

### Generic Log Processing and Filtering

Process multiple files, parse JSON structures, and filter for specific keywords or conditions dynamically.

```bash
python - <<'PY'
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
        # Load JSON and extract lines (adjust parsing to match actual format)
        content = json.loads(pathlib.Path(path).read_text())['logs_content']
        lines = content.splitlines()

        for i, line in enumerate(lines):
            if any(k in line.lower() for k in keywords):
                print(f'{i+1}: {line}')
    except Exception as e:
        print(f"Failed to process {name}: {e}")
    print()
PY
```
