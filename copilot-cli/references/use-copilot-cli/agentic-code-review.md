# Agentic Code Review

**Goal**: AI-powered code review directly from the terminal using `/review` slash command.

## Invariants

- Analyzes code changes without leaving the CLI.
- Requires confirmation before running inspection commands (diff, verify).
- Prioritizes actionable code changes over conversational feedback.
- Optionally specify path, file pattern, or prompt to narrow review scope.

## Commands / Execution

```bash
# Start code review (interactive)
/review

# Narrow review scope
/review focus on security @src/auth/

# Programmatic: use with --prompt flag
copilot -p "/review changes compared to main"
```

## Interaction Flow

1. Enter `/review [optional scope]` and press Enter.
2. If Copilot proposes running a command (e.g., git diff, file verify):
   - Select **Yes** to run command.
   - Select **No** to skip and redirect Copilot.
3. Read feedback and apply suggested improvements in code editor.

## References

- [Requesting a code review with GitHub Copilot CLI - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/agentic-code-review.md)
