# Automate Copilot CLI Quickstart

**Goal**: Build a simple automation script leveraging GitHub Copilot CLI in minutes.

## Invariants

- Pass prompts directly using the `-p` flag.
- Leverage shell scripting to generate dynamic prompts and process results.
- Ensure the script is executable (`chmod +x`).

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
#!/bin/bash
# Example: Describe large files
while IFS= read -r -d '' file; do
    description=$(copilot -p "Describe briefly: $file" -s 2>/dev/null)
    echo "File: $file - $description"
done < <(find . -type f -size +10M -print0)
```

## References

- [Quickstart for automating with GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/quickstart.md)
