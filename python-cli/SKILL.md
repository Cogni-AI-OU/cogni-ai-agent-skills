---
name: python-cli
description: >-
  Execute Python inline scripts via heredocs for complex log processing, data transformation,
  or CLI utilities like URL encoding/decoding.
  You MUST load this skill when processing large logs or performing one-liner data operations.
license: MIT
---

# Skill: python-cli

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Use Python via `python3 - <<'PY'` heredocs or one-liners when processing large log files,
performing data transformations (like URL encoding/decoding), or parsing structured data (like JSON)
where standard bash utilities (awk/sed/grep) become unwieldy or fragile. If `python3` is
unavailable, you may fall back to `python`.

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

### Read Specific Line Range

Use this pattern when you need to extract and print a specific slice of lines from a file.

```bash
python3 -c "import sys; print(''.join(open('<file-path>').readlines()[140:160]))"
```

### URL Encoding and Decoding

Perform quick URL encoding or decoding using Python's `urllib.parse`.

**URL Encode:**

```bash
echo "text to encode" | python3 -c "import urllib.parse; print(urllib.parse.quote(input()))"
```

**URL Decode:**

```bash
echo "text%20to%20decode" | python3 -c "import urllib.parse; print(urllib.parse.unquote(input()))"
```
