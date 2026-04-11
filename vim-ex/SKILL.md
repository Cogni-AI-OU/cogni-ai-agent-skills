---
name: vim-ex
description: 'How to use Ex mode in Vim for non-interactive file editing'
---

# File Editing with Ex Mode

`ex` is the line-editor mode of Vim, which is useful for non-interactive file editing in shell scripts
or agent executed terminal commands.

Unlike tools such as `sed` or `awk` which are *stream editors* designed to process data sequentially line-by-line—`ex`
is a true *file editor*. It loads the entire file into a buffer, allowing you to freely navigate forwards and backwards,
execute complex multi-line modifications, and utilize powerful normal-mode commands. Furthermore, while `sed -i` merely
mimics in-place editing by secretly using temporary files (which leads to notoriously frustrating syntax
incompatibilities between GNU/Linux and macOS), `ex` safely and natively edits the file directly in-place.

## Basic Usage

You can run `ex` using the `-c` flag for commands and `-s` for silent (batch) mode:

```bash
# Search and replace all occurrences
ex -s -c '%s/oldString/newString/g' -c 'wq' filename.txt

# Append text to the end of a file
ex -s -c '$put =\"New appended line\"' -c 'wq' filename.txt

# Delete a specific line (e.g., line 5)
ex -s -c '5d' -c 'wq' filename.txt

# Wrap all lines in a file to 120 characters
ex -s -c 'set tw=120' -c '%normal gqq' -c 'wq' filename.txt

# Wrap specific lines (e.g., lines 19 to 23) to 120 characters
ex -s -c 'set tw=120' -c '19,23normal gqq' -c 'wq' filename.txt
```

## Using Heredocs

For multiple commands, a heredoc is often cleaner:

```bash
ex -s filename.txt << 'VIMEOF'
%s/foo/bar/g
3,5d
wq
VIMEOF
```

## Using a Script File

When you have a complex or reusable set of commands, you can store them in a script file
and apply them to your target file using standard input redirection or the `source` command:

```bash
# Using standard input redirection
ex -s Makefile < Makefile-Fix1.vim

# Alternatively, using the source command
ex -s -c "source Makefile-Fix1.vim" Makefile
```

## Advanced Examples

You can also use Ex mode for more advanced manipulation like piping streams or executing normal mode commands:

```bash
# Print file contents to stdout after making a substitution
ex -s -c '%s/127/128/ge' -c '%p' -c 'q!' /etc/hosts

# Edit data piped via standard input
echo Example | ex -s -c '%p' -c 'q!' /dev/stdin

# Edit multiple files using find
find . -name "*.txt" -type f -exec ex -s -c '%s/old/new/ge' -c 'wq' {} \;

# Use normal mode commands (e.g. to extract or delete complex HTML tags or XML node)
ex -s -c '/<div.*id="the_div_id"/norm nvatd' -c '%p' -c 'q!' index.html

# String parsing examples
echo "This is example." | vim -es '+s/example/test/g' '+%print' '+q!' /dev/stdin
echo "This is example." | ex -s -c '%s/example/test/g' -c '%p' -c 'q!' /dev/stdin

# More examples for editing files in-place (non-interactive)
ex -s -c '%s/127/128/g' -c 'wq' file
ex -s -c '%s/olddomain\.com/newdomain.com/g' -c 'wq' file
printf '%s\n' '%s/olddomain\.com/newdomain.com/ge' w q | ex -s file
ex -s file <<< $'%s/old/new/ge\nw\nq'
ex -s -c 'argdo %s/old/new/ge|update' -c 'q' ./**
find . -type f -exec ex -s -c '%s/old/new/ge' -c 'wq' {} \;
ex -s -c '%p' -c 'q!' /etc/hosts
```

Running vim/ex commands from a file:

```bash
echo :%s/127/128/g > cmds.vim
echo :%print >> cmds.vim
echo :%quit! >> cmds.vim
ex -s /etc/hosts < cmds.vim # The same as: vim -s cmds.vim /etc/hosts
```

### Parse HTML/XML with Ex Mode

Examples:

```bash
# Extracting html tags
ex -s -c 'bufdo! /<div.*id=.the_div_id/norm nvatdggdG"2p' -c 'bufdo! %p' -c 'qa!' *.html

# Removing XML tags
ex -s -c '%s/<[^>].\{-}>//ge' -c '%p' -c 'q!' file.txt

# Removing style tag from the header and print the parsed output
curl -s http://example.com/ | ex -s -c '/<style.*/norm nvatd' -c '%p' -c 'q!' /dev/stdin

# Parse html with multiple complex rules
ex -s index.html << 'EOF'
  %s,'//,'http://,ge
  %s,"//,"http://,ge
  %s,[^,]\zs'/\ze[^>],'http://www.example.com/,ge
  %s,[^,]\zs"/\ze[^>],"http://www.example.com/,ge
  " Remove the margin on the left of the main block. "
  %s/id="doc_container"/id="doc_container" style="min-width:0px;margin-left : 0px;"/ge
  %s/<div class="outer_page/<div style="margin: 0px;" class="outer_page/ge
  " Remove useless html elements. "
  /<div.*id="global_header"/norm nvatd
  wq " Update changes and quit.
EOF

# Real live example from the RPM specification
ex -s Makefile << 'EOF'
   %s/CFLAGS = -g$/CFLAGS =-fPIC -DPIC -g/ge
   %s/CFLAGS =$/CFLAGS =-fPIC -DPIC/ge
   %s/ADAFLAGS =$/ADAFLAGS =-fPIC -DPIC/ge
   wq
EOF
```

Create a new HTML file by downloading html of Example site
and replacing its body by auto-generated 20x20 table with random numbers in it:

```bash
ex -s table.html << 'VIMEOF'
%!curl -s example.com
let @t='<table>'.repeat('<tr>'.repeat('<td>_</td>',20).'</tr>',20).'</table>'
/<body
norm! vitd"tP
%s/_/\=trim(system('echo $RANDOM'))/g
wq
VIMEOF
```

### Plugins

One-liner to convert source code file into HTML using one of the standard plugins
(redirecting standard output to `/dev/null` avoids unnecessary logging):

```bash
ex -s -c 'let g:html_no_progress=1' -c 'syntax on' -c 'set ft=c' -c 'runtime syntax/2html.vim' -c 'wqa' my_code.c > /dev/null
```

## Tips

- Always include `wq` at the end to write changes and quit.
- The `-s` flag suppresses prompts and feedback, making it ideal for automated file edits.
- Use `ex` when complex string replacements or regular expression-based modifications are required directly
  from the terminal without breaking the automated flow.
- When adding or updating examples in this file, ensure they work non-interactively and do not require user input.

## References

- [Does Ex mode have any practical use?](https://vi.stackexchange.com/a/2692/467)
- [How to edit files non-interactively (e.g. in pipeline)?](https://vi.stackexchange.com/a/789/467)
- [Vim Ex Mode Documentation](https://vimhelp.org/)
- [Vim Q&A](https://vi.stackexchange.com/)
- [Learning the vi Editor/Vim/Modes](https://en.wikibooks.org/wiki/Learning_the_vi_Editor/Vim/Modes#Ex-mode)
