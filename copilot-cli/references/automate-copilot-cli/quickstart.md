# Automate Copilot CLI Quickstart

**Goal**: Build a simple automation script using GitHub Copilot CLI programmatic mode.

## Invariants

- Use `-p` flag to pass prompts non-interactively: `copilot -p "prompt"`.
- Any interactive prompt works with `-p`.
- Scripts can generate dynamic prompts, capture output, and chain logic.

## Commands

### Direct prompt from command line

```bash
copilot -p "Summarize what this file does: ./README.md"
```

### Script: find large files and describe them

```bash
#!/bin/bash
# Find files over 10 MB, use Copilot CLI to describe them, and email a summary

EMAIL_TO="user@example.com"
SUBJECT="Large file found"
BODY=""

while IFS= read -r -d '' file; do
    size=$(du -h "$file" | cut -f1)
    description=$(copilot -p "Describe this file briefly: $file" -s 2>/dev/null)
    BODY+="File: $file"$'\n'"Size: $size"$'\n'"Description: $description"$'\n\n'
done < <(find . -type f -size +10M -print0)

if [ -z "$BODY" ]; then
    echo "No files over 10MB found."
    exit 0
fi

echo -e "To: $EMAIL_TO\nSubject: $SUBJECT\n\n$BODY" | sendmail "$EMAIL_TO"
echo "Email sent to $EMAIL_TO with large file details."
```

### Execute

```bash
chmod +x find_large_files.sh
./find_large_files.sh
```

## Automation Triggers

- Cron jobs or CI/CD pipelines for scheduled execution.
- File system watchers for event-driven execution.

## References

- [Quickstart for automating with GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/quickstart.md)
