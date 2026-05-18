---
name: gitattributes
description: Define and modify .gitattributes to standardize line endings, merge drivers, diff generation, and GitHub linguist overrides.
license: MIT
---
# Skill gitattributes

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Define attributes per path to enforce line-ending conversions, custom merge drivers, textual diff strategies, and language statistics overrides across repositories.

## Core Principles

- **Global Consistency**: Ensure line endings (`text`, `eol`) and text normalization are explicitly controlled.
- **Merge Conflict Mitigation**: Use built-in or custom merge drivers (e.g., `merge=ours`) for auto-generated files (like lockfiles) to prevent spurious conflicts.
- **Diff Management**: Exclude binary files from diff generation (`-diff`) or enable binary diffs in patches (`diff`) for small assets using custom macros.
- **Linguist Overrides**: Control language statistics and diff suppression on GitHub using `linguist-generated=true` or `linguist-language=<lang>`.
- **Precedence**: In-tree `.gitattributes` overrides are evaluated top-down; `$GIT_DIR/info/attributes` has the highest precedence for local uncommitted overrides.

## Commands / Usage Patterns

- **Text Normalization (Line Endings)**
  `* text=auto`
  `*.sh text eol=lf`
  `*.vcproj text eol=crlf`

- **Handling Binary Files**
  `*.png binary`
  `*.jpg -text -diff`

- **GitHub Linguist Control & Merge Strategy**
  `.github/workflows/*.lock.yml linguist-generated=true merge=ours`

- **Macro Attributes**
  Define custom macros at top-level `.gitattributes`:
  `[attr]custom_text text eol=lf whitespace=blank-at-eol`
  `*.ext custom_text`

- **Verify Applied Attributes**
  `git check-attr -a -- <file>`
  `git check-attr --cached <attr> -- <file>`

- **Renormalize Line Endings**
  `git add --renormalize .`

## Diagnostics and Troubleshooting

- **Ignored Patterns**: Ensure you are not using trailing slashes for directories (use `path/**` instead of `path/`).
- **Overlapping Rules**: Later lines in the same file override earlier lines. Closest `.gitattributes` directory takes precedence.
- **Reversible Conversions**: If `core.safecrlf` is `true`, Git rejects irreversible end-of-line conversions.

## Example

```gitattributes
# git normalization file
# @docs https://www.kernel.org/pub/software/scm/git/docs/gitattributes.html

# Shorthand for text files.
# - Treat them as text.
# - Ensure no CRLF line-endings, neither on checkout nor on check-in.
# - Detect whitespace errors.
#   - Exposed by default in `git diff --color` on the CLI.
#   - Validate with `git diff --check`.
#   - Deny applying with `git apply --whitespace=error-all`.
#   - Fix automatically with `git apply --whitespace=fix`.
[attr]code    text eol=lf whitespace=blank-at-eol,-blank-at-eof,-space-before-tab,tab-in-indent,tabwidth=2

# Custom shorthand for binary files with diff enabled.
# - Do not treat them as text.
# - Include binary diff in patches instead of "binary files differ."
[attr]binpatch  -text diff

# Define file attributes.
*.bat     eol=crlf
*.cmd     eol=crlf
*.ex?     binpatch
*.h       code diff=c
CHANGELOG merge=union
```

Another example which can be used in `.github/aw/imports/.gitattributes`:

```gitattributes
# Mark all cached import files as generated
* linguist-generated=true

# Use 'ours' merge strategy to keep local cached versions
* merge=ours
```

## What to Avoid

- **Negative Patterns**: Never use negative patterns (e.g., `!pattern`); they are explicitly forbidden in `.gitattributes`.
- **Directory Syntax**: Do not use the trailing-slash syntax (`dir/`) as it does not recursively match paths.

## Limitations

- `gitattributes` do not follow symbolic links.
- Macro attributes can only be defined in top-level `.gitattributes` or `$GIT_DIR/info/attributes`.
