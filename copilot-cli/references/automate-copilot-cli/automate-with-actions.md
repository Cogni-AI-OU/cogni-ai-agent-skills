# Automate with Actions

**Goal**: Automate operations using the GitHub Copilot CLI inside GitHub Actions workflows.

### Invariants
- Requires a GitHub App token or a Personal Access Token (PAT) with `copilot` access.
- Standard `GITHUB_TOKEN` does not grant Copilot access.
- CLI must be explicitly installed via the `gh extension install` command in the runner.

### Schema / Configuration
Workflow Authentication Schema:
```yaml
env:
  GH_TOKEN: ${{ secrets.COPILOT_PAT }}
```

### Commands / Execution
```yaml
steps:
  - name: Install Copilot CLI
    run: gh extension install github/gh-copilot
    
  - name: Run Copilot CLI
    run: gh copilot explain "echo 'Hello World'"
```

## References
- [Automate with Actions](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/automate-with-actions.md)