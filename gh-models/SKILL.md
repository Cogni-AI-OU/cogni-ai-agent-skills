# gh-models

Guidance for using the GitHub CLI models extension (`gh models`) to run and evaluate models on issues, PRs, or repo events.

## Best Practices

- `gh models` is excellent for CLI-centric workflows (`run`, `eval`, `generate`).
- When running models on repo content (like issues, PRs, or repo events), the typical pattern is:
  `gh models run --file <prompt-file>`
  - Example: `cat issue_body.txt | gh models run --file summarize.prompt.yml > summary.txt`
- Use `gh models eval` to run evaluations.
  - Example: `gh models eval <prompt-file>`
  - If you need to parse results in a workflow to enforce pass/fail logic, use the JSON output format: `gh models eval my_prompt.prompt.yml --json`
