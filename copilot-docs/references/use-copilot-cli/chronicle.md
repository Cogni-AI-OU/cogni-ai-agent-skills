# Chronicle

**Goal**: Leverage historical session data for insights, standup reports, and instruction optimization.

## Invariants

- Session data stored **locally** on the machine.
- Full-text search across session history for recalling past work.
- `/chronicle` commands provide structured insights based on usage patterns.
- `copilot --continue` resumes most recent local session.
- `copilot --resume` opens session picker; `copilot --resume SESSION-ID` resumes directly.
- `/session` displays current session ID.

## Session Management

```bash
# Resume most recent session
copilot --continue

# Select from session list
copilot --resume

# Resume specific session by ID
copilot --resume SESSION-ID

# Rename current session (appears in resume list)
/rename Improve test coverage

# Display current session ID
/session
```

## Sharing Sessions

```bash
# Share as private GitHub gist
/share gist

# Export as Markdown file (default: copilot-session-SESSIONID.md in CWD)
/share file [PATH-TO-FILE]
```

## Chronicle Subcommands

| Subcommand | Description |
|------------|-------------|
| `/chronicle` | Opens picker to choose subcommand. |
| `/chronicle standup` | Generate standup report (default: last 24h). Groups output by completion status, labels by branch, checks linked PR statuses. |
| `/chronicle tips` | 3-5 personalized recommendations based on actual usage patterns, cross-referenced with CLI features and installed custom agents/skills. |
| `/chronicle improve` | Analyze session history for friction signals; suggest improvements to `.github/copilot-instructions.md`. Applies selected recommendations interactively. |
| `/chronicle reindex` | Rebuild session store index from history. |

### Standup Customization

```bash
# Custom time range
/chronicle standup for the last 3 days
```

### Tips Customization

```bash
# Focus tips on specific area
/chronicle tips for better prompting
```

### Improve Scope

The `improve` subcommand scope is limited to the current repository/working directory only. It detects:
- Repeated test failures or build errors requiring multiple attempts.
- User messages that corrected or redirected the agent.
- Patterns that recur across sessions.

## Free-form Session Queries

Copilot auto-detects questions about session history. Examples:

```bash
# Analyze completion patterns
Using what you know about my sessions, what type of tasks give me one-shot successes
and which do I have to iterate on most?

# Reduce premium request usage
Based on my previous CLI sessions, how could I prompt you in a way that would cost less?

# Find productive times
Look at data for previous sessions. What time of day am I most and least effective
at getting good results from Copilot?

# Recall past work
Have I worked on anything related to authentication in the last month?
```

By default, queries span all recorded sessions regardless of repository/branch.

## References

- [Using GitHub Copilot CLI session data - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/chronicle.md)
