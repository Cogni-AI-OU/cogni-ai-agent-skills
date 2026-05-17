# Run CLI Programmatically

**Goal**: Execute GitHub Copilot CLI programmatically from scripts or automation tools.

### Invariants
- Use structured output (JSON) for programmatic parsing.
- Always check exit codes for command success or failure.
- Execution must run in silent/non-interactive mode to prevent terminal hangs.

### Schema / Configuration
- Utilize the `--format json` or `-f json` flag to receive JSON responses.
- Utilize the `--silent` or `-sc` flag to suppress interactive elements and conversational filler.
- Check return codes: `0` (Success), non-zero (Error).

### Commands / Execution
```bash
# Get suggestion as JSON
gh copilot suggest "Commit changes" -t shell --format json

# Explain command as JSON
gh copilot explain "git log" --format json
```

## References
- [Run CLI Programmatically](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/run-cli-programmatically.md)