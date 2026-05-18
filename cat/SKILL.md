---
name: cat
description: >-
  Guidelines for safely using `cat` and avoiding shell hangs with heredocs.
  You MUST load this skill before running the `cat` command (especially with `EOF`).
license: MIT
---

# cat Skill

Use caution when running `cat` or heredocs (`<<EOF`) in automated environments or agentic runtimes, as missing or
truncated EOF delimiters can cause persistent shell hangs.

## When to Use

- Using `cat` to write files.
- Using heredoc (`<<EOF`) to pass multiline strings.
- Reading or streaming file contents.

## When Not to Use

- For modifying or appending to files when specific, robust file-writing tools (like the Edit or Write tools) are available.
- When printing massive, multi-gigabyte log files to standard out, which will completely crash the terminal or context window.
- In automated scripts that write complex YAML or JSON where a missing quote or delimiter can silently break the entire file structure.

## Common Pitfalls

- **Heredoc Hangs**: Using `cat <<EOF` inside a script without quoting the EOF delimiter or failing to print the delimiter exactly, causing the shell to hang indefinitely waiting for input.
- **Overwriting Files**: Accidentally using `>` instead of `>>` and instantly destroying the contents of a critical configuration file.
- **Binary Garbling**: Running `cat` on a compiled binary or PDF, dumping control characters into the terminal that corrupt the session's display state.

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
