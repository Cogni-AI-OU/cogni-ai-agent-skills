# Run CLI Programmatically

**Goal**: Execute Copilot CLI prompts via scripts and automation without interactive sessions.

## Invariants

- Use `-p` or `--prompt` for non-interactive execution.
- Piped input is supported: `echo "Prompt" | copilot`.
- Use `-s` (silent) to suppress metadata and capture clean text output.
- Use `--no-ask-user` to disable clarifying questions.
- Use `--model` for consistent behavior across environments.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# Capture output in variable
result=$(copilot -p 'Explain @src/app.js' -s)

# Conditional logic
if copilot -p 'Has errors? Reply YES/NO' -s | grep -qi "YES"; then exit 1; fi

# Share session to file
copilot -p "Audit deps" --share='./report.md'

# Share session to Gist
copilot -p "Summarize arch" --share-gist
```

## References

- [Running GitHub Copilot CLI programmatically](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/run-cli-programmatically.md)
