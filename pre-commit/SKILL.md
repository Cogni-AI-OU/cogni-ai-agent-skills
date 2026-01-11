<!-- markdownlint-disable MD003 MD013 MD022 MD026 MD041 -->
---
name: pre-commit
description: Guide for using pre-commit hooks to validate code formatting, linting, and security checks before commits.
license: MIT
---

Expert guide for pre-commit framework usage, configuration, and custom hook development. Focus on autonomous validation, diagnostics, and fix workflows.

## Core Principles

- **Staged files only**: Pre-commit runs exclusively on staged (cached) files, not the entire working directory.
- **Fast feedback**: Catch issues before commit/push to reduce CI failures and review cycles.
- **Configuration-driven**: Hooks reference external config files (.yamllint, .markdownlint.yaml, etc.) for consistency.
- **Idempotent fixes**: Many hooks auto-fix issues (e.g., trailing-whitespace, end-of-file-fixer); re-stage and re-run to pass.
- **Skip only when necessary**: Use `--no-verify` or `SKIP=<hook-id>` sparingly; prefer fixing issues over bypassing validation.

## Testing Commands

**Run all hooks on all files** (recommended before committing):

```bash
pre-commit run --all-files
```

**Run all hooks on staged files only** (default behavior):

```bash
pre-commit run
```

**Run specific hook on all files**:

```bash
pre-commit run <hook-id> --all-files
```

**Run specific hook on staged files**:

```bash
pre-commit run <hook-id>
```

**Examples for individual linters**:

```bash
pre-commit run yamllint --all-files          # YAML linting
pre-commit run markdownlint --all-files      # Markdown linting
pre-commit run flake8 --all-files            # Python linting
pre-commit run black --all-files             # Python formatting
pre-commit run ansible-lint --all-files      # Ansible linting
pre-commit run actionlint --all-files        # GitHub Actions workflow linting
pre-commit run gitleaks --all-files          # Secret scanning
pre-commit run detect-secrets --all-files    # Alternative secret detection
pre-commit run trailing-whitespace -a        # Fix trailing spaces (auto-fix)
pre-commit run end-of-file-fixer -a          # Fix EOF newlines (auto-fix)
```

**Run hook on specific file**:

```bash
pre-commit run <hook-id> --files <file-path>
```

## Configuration Dependencies

Pre-commit hooks reference external dotfiles for linting rules. Key dependencies in this repository:

| Hook ID | Config File | Purpose | Notes |
| ------- | ----------- | ------- | ----- |
| `yamllint` | `.yamllint` | YAML linting rules | Max line length: 120, enforces consistent formatting |
| `markdownlint` | `.markdownlint.yaml` | Markdown style rules | Max line length: 120, allows consistent heading styles |
| `yamlfix` | `.yamlfix.toml` | YAML auto-formatting | Line length: 110, forces block-style sequences |
| `flake8` | CLI args in `.pre-commit-config.yaml` | Python linting | Max line length: 120 (via `--max-line-length=120`) |
| `black` | Defaults | Python code formatting | Uses Black's default line length (88) |
| `ansible-lint` | Embedded defaults | Ansible best practices | No custom config file in this repo |
| `actionlint` | Embedded defaults | GitHub Actions validation | No custom config file in this repo |
| `gitleaks` | Optional `.gitleaks.toml` | Secret scanning patterns | Can override default rules (see below) |
| `detect-secrets` | Optional `.secrets.baseline` | Secret detection baseline | Can store known false positives |
| All hooks | `.editorconfig` | Cross-editor consistency | Indent size: 2 for YAML/JSON, 4 for others; LF line endings |

**Why trailing-whitespace excludes YAML**: The `trailing-whitespace` hook in the repository's `.pre-commit-config.yaml` excludes `\.ya?ml$` (YAML files) because yamllint handles trailing spaces for YAML files with warning-level enforcement, avoiding duplicate checks.

## Optional Configuration Files

Some hooks support optional config files to customize behavior beyond defaults:

### gitleaks

**Default**: Uses embedded ruleset for secret detection (API keys, passwords, tokens).

**Custom config**: Create `.gitleaks.toml` in repository root to:

- Add custom secret patterns
- Exclude specific paths or files
- Allowlist known false positives

Example `.gitleaks.toml`:

```toml
[extend]
useDefault = true

[[rules]]
id = "custom-api-key"
description = "Custom API Key Pattern"
regex = '''MYAPI-[A-Z0-9]{32}'''

[allowlist]
paths = [
  '''.*test.*''',
  '''.*example.*'''
]
```

### detect-secrets

**Default**: Scans all files for high-entropy strings and common secret patterns.

**Baseline file**: Create `.secrets.baseline` to store known false positives:

```bash
detect-secrets scan > .secrets.baseline
```

Future runs compare against baseline; only new secrets trigger failures.

### j2lint

**Default**: Validates Jinja2 template syntax using embedded rules.

**Custom config**: Create `.j2lint.toml` or `.j2lint.yaml` for custom linting rules (rarely needed).

## Update Process

**Update all hooks to latest versions**:

```bash
pre-commit autoupdate
```

This updates `.pre-commit-config.yaml` with the newest `rev` for each repo. Always review diff and test after updating:

```bash
pre-commit run --all-files
```

**Update specific hook**:

```bash
pre-commit autoupdate --repo https://github.com/<owner>/<repo>
```

**Freeze at specific version**: Manually edit `.pre-commit-config.yaml` and pin `rev` to a specific tag/commit.

## Creating Custom Local Hooks

Pre-commit supports custom hooks via local repository scripts. Add to `.pre-commit-config.yaml`:

### Example: Local Shell Script Hook

1. Create script in repository:

```bash
#!/usr/bin/env bash
# File: .github/scripts/check-copyright.sh
set -euo pipefail

for file in "$@"; do
  if ! grep -q "Copyright $(date +%Y)" "$file"; then
    echo "Missing copyright header in $file" >&2
    exit 1
  fi
done
```

1. Make executable:

```bash
chmod +x .github/scripts/check-copyright.sh
```

1. Add to `.pre-commit-config.yaml`:

```yaml
- repo: local
  hooks:
    - id: check-copyright
      name: Verify copyright headers
      entry: .github/scripts/check-copyright.sh
      language: system
      types: [python]
```

### Example: Local Python Script Hook

1. Create script with uv shebang:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pyyaml",
# ]
# ///
import sys
import yaml

def validate_yaml_keys(filepath):
    with open(filepath) as f:
        data = yaml.safe_load(f)
        if 'required_key' not in data:
            print(f"Missing required_key in {filepath}", file=sys.stderr)
            return False
    return True

if __name__ == '__main__':
    all_valid = all(validate_yaml_keys(f) for f in sys.argv[1:])
    sys.exit(0 if all_valid else 1)
```

1. Make executable:

```bash
chmod +x .github/scripts/validate-yaml-keys.py
```

1. Add to `.pre-commit-config.yaml`:

```yaml
- repo: local
  hooks:
    - id: validate-yaml-keys
      name: Check YAML required keys
      entry: .github/scripts/validate-yaml-keys.py
      language: system
      types: [yaml]
```

### Local Hook Best Practices

- **Use `language: system`** for scripts that require executables in PATH (bash, python, etc.).
- **Pass filenames as args**: Pre-commit passes matching files as arguments to `entry` command.
- **Exit codes matter**: Exit 0 for success, non-zero for failure.
- **Keep scripts idempotent**: Hook may run multiple times; avoid side effects.
- **Document dependencies**: If script requires specific tools, document in script comments or repo README.

## Diagnostics and Troubleshooting

**Hook fails on specific file**:

```bash
pre-commit run <hook-id> --files <file-path> --verbose
```

**Skip hooks temporarily** (commit without validation):

```bash
git commit --no-verify -m "message"
```

**Skip specific hook** (run all except one):

```bash
SKIP=<hook-id> git commit -m "message"
```

**Check pre-commit installation and config**:

```bash
pre-commit --version
pre-commit validate-config
```

**Clean pre-commit cache** (fixes stale hook errors):

```bash
pre-commit clean
pre-commit install --install-hooks
```

**Debug hook execution**:

```bash
pre-commit run <hook-id> --verbose --all-files
```

## Common Failure Patterns

**Auto-fixable hooks modified files**: Re-stage and re-run:

```bash
git add -u
pre-commit run
```

**YAML formatting conflicts**: Run yamllint before yamlfix to catch syntax errors first:

```bash
pre-commit run yamllint --all-files
pre-commit run yamlfix --all-files
```

**Markdown line length violations**: Reflow paragraphs manually or use editor formatter (VS Code: "Format Document").

**Secret detection false positives**:

- For gitleaks: Add to `.gitleaks.toml` allowlist.
- For detect-secrets: Update `.secrets.baseline` with `detect-secrets scan --baseline .secrets.baseline`.

## What to Avoid

- Committing with `--no-verify` without documenting reason.
- Modifying `.pre-commit-config.yaml` without testing changes locally.
- Bypassing hooks to "save time" — fixing issues post-merge costs more.
- Running hooks on untracked files (pre-commit ignores them; stage first).

## Limitations

- Pre-commit only validates staged files; unstaged changes are ignored.
- Hooks run sequentially; large repos may experience slower commit times.
- Some hooks (e.g., yamlfix) may conflict with manual formatting preferences.
- Custom local hooks require executable scripts in repository; not portable across forks without dependencies.
