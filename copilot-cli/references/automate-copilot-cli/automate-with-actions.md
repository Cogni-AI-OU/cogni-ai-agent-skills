# Automate with Actions

**Goal**: Integrate GitHub Copilot CLI into GitHub Actions workflows for AI-powered automation.

## Invariants

- Install via `npm install -g @github/copilot`.
- Requires `COPILOT_GITHUB_TOKEN` secret with "Copilot Requests" permission.
- Use `--no-ask-user` to prevent hanging on interactive prompts.
- Explicitly allow necessary tools (e.g., `--allow-tool='shell(git:*)'`, `--allow-tool=write`).

## Schema (if applicable)

```yaml
jobs:
  automate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm install -g @github/copilot
      - run: copilot -p "PROMPT" --no-ask-user --allow-tool='shell(git:*)' --allow-tool=write
        env:
          COPILOT_GITHUB_TOKEN: ${{ secrets.COPILOT_GITHUB_TOKEN }}
```

## Commands / Execution (if applicable)

- **Trigger**: `workflow_dispatch`, `schedule`, or repository events.
- **Output**: Redirect to files or `$GITHUB_STEP_SUMMARY`.

## References

- [Automating tasks with Copilot CLI and GitHub Actions](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/automate-with-actions.md)
