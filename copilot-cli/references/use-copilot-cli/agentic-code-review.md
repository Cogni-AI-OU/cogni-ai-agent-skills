# Agentic Code Review

**Goal**: Automate Pull Request and code reviews directly from the terminal.

## Invariants

- Analyzes code changes without leaving the CLI.
- Prioritizes actionable code changes over conversational feedback.
- Requires confirmation before running inspection commands (diff, verify).

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# Start code review
/review

# Narrow review scope
/review focus on security @src/auth/

# Run programmatically
copilot -p "/review changes compared to main" -s
```

## References

- [Requesting a code review with GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/agentic-code-review.md)
