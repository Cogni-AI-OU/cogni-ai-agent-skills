# Manage Pull Requests

**Goal**: Automate the generation, summarization, and management of GitHub Pull Requests.

### Invariants
- Commands must infer context strictly from existing commits, branches, and diffs.
- Avoids manual data entry for PR body creation.

### Schema / Configuration
- Requires active branch divergence from `main` or `master`.
- Relies on Git and GitHub CLI native authentication.

### Commands / Execution
```bash
# Generate and summarize a Pull Request
gh copilot pr create
```

## References
- [Manage Pull Requests](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/manage-pull-requests.md)