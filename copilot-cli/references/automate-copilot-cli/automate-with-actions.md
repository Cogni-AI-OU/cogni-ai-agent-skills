# Automate with Actions

**Goal**: Run GitHub Copilot CLI in GitHub Actions workflows for AI-powered CI/CD automation.

## Invariants

- Install via `npm install -g @github/copilot`.
- Requires PAT with "Copilot Requests" permission, stored as Actions secret.
- Authenticate via `COPILOT_GITHUB_TOKEN` env var (supports setting different permissions than `GITHUB_TOKEN`).
- Use `--no-ask-user` to prevent hanging on interactive prompts.
- Use `--allow-tool` to grant only necessary tool access (e.g., `--allow-tool='shell(git:*)'`, `--allow-tool=write`).

## Workflow Pattern

```
Trigger (schedule / workflow_dispatch / repo event)
  → Setup (checkout, Node.js)
  → Install (`npm install -g @github/copilot`)
  → Authenticate (COPILOT_GITHUB_TOKEN secret)
  → Run (`copilot -p "PROMPT" --allow-tool=... --no-ask-user`)
  → Handle output (file, $GITHUB_STEP_SUMMARY, PR)
```

## Example Workflow

Generates daily summary of changes in default branch and writes to workflow summary.

```yaml
name: Daily summary
on:
  workflow_dispatch:
  schedule:
    - cron: '30 17 * * *'
permissions:
  contents: read
jobs:
  daily-summary:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
      - run: npm install -g @github/copilot
      - name: Run Copilot CLI
        env:
          COPILOT_GITHUB_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
        run: |
          copilot -p "Review the git log for this repository and write a bullet point summary of all code changes that were made today, with links to the relevant commit on GitHub. Above the bullet list give a description (max 100 words) summarizing the changes made. Write the details to summary.md" --allow-tool='shell(git:*)' --allow-tool=write --no-ask-user
          cat summary.md >> "$GITHUB_STEP_SUMMARY"
```

## Key Options

| Option | Purpose |
|--------|---------|
| `--allow-tool='shell(git:*)'` | Allow git commands for repo analysis |
| `--allow-tool=write` | Allow writing output files |
| `--no-ask-user` | Suppress interactive prompts |
| `-p "PROMPT"` | Pass prompt non-interactively |

## Next Steps

- Change the prompt to target different automation tasks.
- Redirect output to PRs, emails, or changelogs instead of step summary.

## References

- [Automating tasks with Copilot CLI and GitHub Actions](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/automate-with-actions.md)
