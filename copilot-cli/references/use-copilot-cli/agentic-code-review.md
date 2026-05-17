# Agentic Code Review

**Goal**: Automate comprehensive code and pull request reviews using Copilot CLI agents.

### Invariants
- Reviews must strictly evaluate code against documented repository standards and constraints.
- Output must highlight specific line-level issues, security vulnerabilities, and logic flaws.

### Schema / Configuration
- Operates primarily on active diffs, uncommitted changes, or specific pull requests.

### Commands / Execution
```bash
# Review uncommitted changes
gh copilot code-review

# Review a specific pull request
gh copilot pr-review <PR_NUMBER>
```

## References
- [Agentic Code Review](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/agentic-code-review.md)