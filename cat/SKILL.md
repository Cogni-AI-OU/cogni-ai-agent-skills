---
name: cat
description: >-
  Guidelines for safely using `cat` and avoiding shell hangs with heredocs.
  You MUST load this skill before running the `cat` command (especially with `EOF`).
license: MIT
---

# cat Skill

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Reading the content of small text files during automated or agentic workflow execution.
- Concatenating multiple short files for combined inspection or display output.
- Displaying short file contents in CI/CD log output for quick debugging.

## When Not to Use

- Creating files with long or programmatically generated content — use the Write tool or `--body-file` flags instead to avoid heredoc truncation hangs.
- Reading or processing binary files — `cat` can corrupt binary output in terminal. Use `xxd`, `od`, or dedicated binary tools.
- Operating on files larger than a few hundred lines — use `grep`, the Read tool, or `head` for targeted extraction.

## Common Pitfalls

- **Heredoc Truncation Hangs**: If output is truncated before the `EOF` delimiter is printed, `cat` hangs forever waiting for input. This is the #1 cause of shell hangs in agentic workflows. Never use heredocs for long or generated content.
- **Timeout Enforcement**: When you must execute `cat` reading from stdin or a heredoc, always wrap it in `timeout 10s cat <<'EOF'...EOF` so a hang fails fast instead of locking the workflow.
- **Cleanup Required**: Temporary files created via `mktemp` or heredoc redirection must be explicitly removed after use (`rm "$FILE"`) to avoid leaking files across workflow steps.
- **Shell Injection via Unquoted EOF**: If the heredoc body contains unescaped shell variables or command substitutions (`$var`, `` `cmd` ``), they will be expanded. Use `'EOF'` (single-quoted delimiter) to prevent expansion.

Use caution when running `cat` or heredocs (`<<EOF`) in automated environments or agentic runtimes, as missing or
truncated EOF delimiters can cause persistent shell hangs.

## Avoid Heredocs for Long Strings

Never use heredocs (`cat <<EOF > file.md` or `command --body "$(cat <<EOF)"`) for long strings or generated code. If the
output gets truncated before the `EOF` delimiter is printed, the `cat` command will hang forever waiting for input,
which forces the runtime to cancel the job.

### Bad Pattern (Hangs easily)

```bash
# DO NOT DO THIS
gh issue comment 123 --body "$(cat <<'EOF'
Very long text...
EOF
)"

# DO NOT DO THIS
cat <<'EOF' > /tmp/file.md
Very long text...
EOF
```

### Good Pattern (Safe alternatives)

#### Alternative 1: Use native file flags

Use your agentic file-writing tools (like the Write or Edit tool) to create a temporary file first, and then pass that
file using commands' native file flags (like `--body-file`).

```bash
# First, use your Write tool to save content to /tmp/comment.md
gh issue comment 123 --body-file /tmp/comment.md
```

#### Alternative 2: mktemp and quoted writes

```bash
COMMENT_FILE=$(mktemp)
# Use your Write tool to write to $COMMENT_FILE, or use safe quoted echoing if short
echo "Short text" > "$COMMENT_FILE"
gh issue comment 123 --body-file "$COMMENT_FILE"
rm "$COMMENT_FILE" # Always clean up temporary files after use
```

## Always Use Timeouts with Stdin and Heredocs

When you absolutely must execute `cat` reading from `stdin` or a heredoc in a shell command, enforce a timeout so that
if it hangs, it will fail fast instead of locking up the workflow. Note that simple file reads like `cat somefile.txt`
do not typically require a timeout.

```bash
timeout 10s cat <<'EOF'
Long text...
EOF
```

## Related Skills

- **robust-commands**:
  You MUST load this skill when executing commands requiring resilient error recovery or fallbacks.
