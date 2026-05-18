# Manage Pull Requests

**Goal**: Full PR lifecycle (view, create, fix) from the terminal via `/pr` slash command.

## Invariants

- Requires Git repository hosted on GitHub.
- All `/pr` subcommands relate to the **current branch**.
- Subcommands that commit/push will prompt for permission unless pre-allowed.
- PR template respected if present in repository.

## Subcommands Reference

| Command | Action | Requires PR | May Commit/Push |
|---------|--------|:-----------:|:---------------:|
| `/pr` or `/pr view` | Show current PR status. | Yes | No |
| `/pr view web` | Open PR in default browser. | Yes | No |
| `/pr create` | Create or update PR. Pushes commits to remote. | No | Yes |
| `/pr fix feedback` | Address review comments. | Yes | Yes |
| `/pr fix conflicts` | Sync branch with base, resolve conflicts. | Yes | Yes |
| `/pr fix ci` | Diagnose and fix CI failures. Loops until green or blocked. | Yes | Yes |
| `/pr fix` or `/pr fix all` | Run all three fix phases: feedback, conflicts, CI. | Yes | Yes |
| `/pr auto` | Create PR if needed + loop fix phases until all checks pass. | No | Yes |

## Command Details

### View PR

```bash
# Show current PR status in terminal
/pr

# Open PR in browser
/pr view web
```

### Create PR

```bash
/pr create
# With custom instructions:
/pr create prefix the PR title 'Project X: '
```

If PR already exists for the branch, `/pr create` updates it instead of creating new.

### Fix Review Feedback

```bash
/pr fix feedback
```

Fetches all review comment threads, determines requested changes, applies fixes, commits and pushes. Prioritizes actionable code changes over conversational comments.

### Resolve Merge Conflicts

```bash
/pr fix conflicts
```

Fetches latest base branch, syncs branch, resolves conflicts, pushes result.

#### Merge Strategy Configuration

Set default to avoid prompt each time:

```json
// ~/.copilot/settings.json or .github/copilot/settings.json
{ "mergeStrategy": "rebase" }   // or "merge"
```

### Fix CI Failures

```bash
/pr fix ci

# With focus scope
/pr fix ci focus on test failures
```

Identifies failing CI jobs, analyzes logs for root cause, applies targeted fixes, pushes. Re-checks CI and repeats until green or blocked. Notes failures unrelated to branch changes.

### Fix All

```bash
# All three fix phases in order
/pr fix
```

Order: (1) Review feedback → (2) Conflicts → (3) CI failures.

### Auto (Full Lifecycle)

```bash
/pr auto

# With custom instructions
/pr auto include migration notes in the description
```

Creates PR if none exists, then loops through fix phases until all checks pass.

## References

- [Managing pull requests with the /pr command - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/manage-pull-requests.md)
