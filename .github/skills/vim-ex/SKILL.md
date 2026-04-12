---
name: vim-ex
description: >-
  How to use Ex mode in Vim for non-interactive file editing (e.g., complex text substitution, deleting lines, file parsing, wrapping text, sorting lines).

  Maintained at: <https://github.com/Cogni-AI-OU/.github/blob/main/.github/skills/vim-ex/SKILL.md>

---

# File Editing with Ex Mode

`ex` is the line-editor mode of Vim, which is useful for non-interactive file editing in shell scripts
or when you need to perform batch operations on multiple files. It allows you to make file changes,
execute complex multi-line modifications, and utilize powerful normal-mode commands for large-scale operations.

Unlike `sed` (which mimics in-place editing by secretly using temporary files—which leads to notoriously frustrating syntax
incompatibilities between GNU/Linux and macOS), `ex` safely and natively edits the file directly in-place.

## When to Activate

You should prefer using `ex` over standard shell utilities (`sed`, `awk`, `grep`) in the following scenarios:

1. **Complex, multi-line substitutions** that would be error-prone or unreadable with `sed`.
2. **Batch operations across multiple files** where you need consistent, atomic changes.
3. **Preserving exact file formatting and encoding** without side effects from temp-file indirection.
4. **Executing normal-mode Vim commands non-interactively** (e.g., `norm! ...`, macros).
5. **Cross-platform consistency** (avoiding GNU vs. BSD `sed` incompatibilities).

## Core Commands

```bash
# Basic structure
ex -s input.txt << 'EOF'
<commands>
wq
EOF

# Using -c for single commands
ex -s -c '%s/old/new/g' -c 'wq' input.txt

# Multiple files with argdo
ex -s file1.txt file2.txt << 'EOF'
set hidden
argdo %s/old/new/g | update
qa!
EOF
```

## Common Patterns

### Simple substitution

```bash
ex -s file.txt << 'EOF'
%s/foo/bar/g
wq
EOF
```

### Delete lines matching pattern

```bash
ex -s file.txt << 'EOF'
g/pattern/d
wq
EOF
```

### Append text to end of file

```bash
ex -s file.txt << 'EOF'
$a
New line at end
.
wq
EOF
```

### Insert text at beginning

```bash
ex -s file.txt << 'EOF'
1i
First line
.
wq
EOF
```

### Replace entire file content

```bash
ex -s file.txt << 'EOF'
1,$d
a
New content
.
wq
EOF
```

## Tips

- **Appending Text in Heredocs:** When appending lines within an `ex` heredoc script, use `a` followed by a newline,
  the text to insert, and a single `.` on a new line to terminate the block. Do not use the `a\` syntax
  (which is only suitable for inline `-c` commands).
- **Custom Delimiters:** Use alternative delimiters in substitutions (e.g., `%s!pattern!replacement!g` or
  `%s,pattern,replacement,g`) when manipulating HTML tags (like `</body>`), paths, or URLs to bypass
  repetitive backslash escaping.
- **Inserting Newlines in Substitutions:** When using the substitution command (`s/.../.../`),
  you cannot insert literal newlines or `\n`. You must use `\r` in the replacement string to generate a newline (e.g., `%s/old/new\rnewLine/g`).
- **Non-interactive Execution:** When adding or updating examples in this file, ensure they work
  non-interactively and do not require user input.
- **Preserve Examples:** Do not change existing examples unless they are not working; keep proven examples unchanged.
- **Debugging Ex Commands:** When diagnosing issues,
  temporarily replace the `-s` (silent) flag with `-V1` (verbose level 1) to print the command execution steps
  and exact error messages to the terminal.
- **Hanging Commands:** When testing new commands, use `timeout` to prevent hanging risks on read-only files.
- **Hanging Processes (Control-Z or infinite wait)**: If you accidentally find yourself stuck in an
  interactive `ex` command-line prompt (often indicated by messages like `The terminal is
  awaiting input` or `Type "visual" to go to Normal mode`), **do not kill the terminal** and
  **never type `visual`** (this launches the full interactive UI and completely breaks headless
  agents). This usually happens if you forget the `-s` (silent) flag. Simply type `qa!` and press
  Enter to safely abort. In batch mode using `argdo`, a missing `update` or standard `q` command
  may leave `ex` waiting for interactively unsaved buffers. Run `qa!` unconditionally at the end
  of heredocs to cleanly abort everything if any step stalled.
- **Heredoc Conflicts / Infinite Hangs:** Avoid piping data (`command | ex -s /dev/stdin`) when you are also
  providing commands via a heredoc (`<< EOF`). This causes `ex` to confuse its input streams and hang indefinitely.
  Use process substitution instead: `ex -s <(command) << EOF`.

- **Newline appending via string (`$put=""/a\`)**: In headless automated CI or agent scripts,
  using `$put="string"` or `a\` across multiple files via `argdo` can fail explicitly or
  invisibly swallow newlines depending on shell escaping. Use Vimscript's explicit `call
  append('$', 'your string')` to safely bypass multiline shell escaping issues completely.

- **Range Errors (e.g. Exit code 1 with no output):** Complex address ranges like `/<pattern>/+1,+3command` often fail
  because `ex` evaluates the second relative address before the cursor moves to the pattern. Splitting them solves this by
  explicitly moving the cursor first.
- **Prefer explicit substitution (`:%s/old/new/g`) over text-object edits:** Avoid relying on
  normal mode actions (e.g., `norm! vitd`) when editing unstructured data like raw HTML, which might break
  text-object selections and fail implicitly if tags are unexpectedly unclosed.

## Appending to multiple files

Example of safely appending text across multiple files via `argdo` and `call append()` instead of multi-line shell escaping:

```bash
ex -s .github/skills/*/SKILL.md << 'VIMEOF'
set hidden
let m = 'Note that this file should be updated if outdated or steps/examples are not working.'
argdo call append('$', ['', '## Maintenance', '', m]) | update
qa!
VIMEOF
```

## References

- [Does Ex mode have any practical use?](https://vi.stackexchange.com/a/2692/467)
- [Why does Ex-mode exist?](https://vi.stackexchange.com/q/457/467)
- [Vim Ex Mode Documentation](https://vimhelp.org/)
- [Vim Q&A](https://vi.stackexchange.com/)
- [Learning the vi Editor/Vim/Modes](https://en.wikibooks.org/wiki/Learning_the_vi_Editor/Vim/Modes#Ex-mode)

## Maintenance

Note that this file should be updated if outdated or steps/examples are not working.
