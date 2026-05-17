# Manage Pull Requests

**Goal**: Orchestrate the full Pull Request lifecycle (view, create, fix) from the terminal.

## Invariants

- Requires Git repository hosted on GitHub.
- Subcommands relate to the current branch.
- Automated fix loops handle feedback, conflicts, and CI failures.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# Open PR in browser
/pr view web

# Set default merge strategy in settings.json
{ "mergeStrategy": "rebase" }
```

## Subcommands

| Command | Action | May Commit/Push |
| ------- | ------ | --------------- |
| `/pr` | Show current PR status. | No |
| `/pr create` | Create or update PR. | Yes |
| `/pr fix feedback` | Address review comments. | Yes |
| `/pr fix conflicts` | Sync branch and resolve conflicts. | Yes |
| `/pr fix ci` | Diagnose and fix CI failures. | Yes |
| `/pr auto` | Automated loop: Create -> Fix All -> Green. | Yes |

## References

- [Managing pull requests with the /pr command](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/manage-pull-requests.md)
