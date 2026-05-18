---
name: gh-agent-task
description: GitHub CLI (`gh agent-task`) operations for creating, listing, and viewing preview agent tasks. You MUST load this skill when working with the `gh agent-task` command.
license: MIT
---
# Skill: gh-agent-task

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Provides usage patterns and expert guidance for the GitHub CLI `gh agent-task` extension, which manages preview agent tasks on repositories and pull requests.
The agent-task command set is only available in v2.80.0 or later of the GitHub CLI.
This command set is a public preview and is subject to change.

## Core Process

1. Determine if the goal is to create a new task, list existing tasks, view a specific task, or view tasks associated with a PR.
2. Select the correct subcommand (`create`, `list`, or `view`).
3. Apply filtering (`--jq`), formatting (`--json`, `--template`), or input options (`-F`) as required.

## Core Principles

- Keep descriptions clear when creating tasks; prefer using a file (`-F`) for multi-line instructions instead of inline strings.
- Always use non-interactive mode. For JSON extraction, rely on the built-in `--jq` and `--json` flags rather than external piping when possible.

## Commands / Usage Patterns

### Create an Agent Task

Create a task from a file (recommended for complex tasks):
`gh agent-task create -F task-desc.md`

Create a task using stdin:
`echo "description" | gh agent-task create -F -`

Create a task with a custom agent on a specific base branch:
`gh agent-task create "fix errors" --base main --custom-agent my-agent`

Create a task and follow logs:
`gh agent-task create "build me a new app" --follow`

### List Agent Tasks

List tasks and format output with JSON/JQ:
`gh agent-task list --limit 10 --json id,state,pullRequestNumber --jq '.[] | "\(.id): \(.state)"'`

### View Agent Tasks

View an agent task by session ID:
`gh agent-task view e2fa49d2-f164-4a56-ab99-498090b8fcdf`

View an agent task by PR number:
`gh agent-task view 12345`

View an agent task by PR reference:
`gh agent-task view OWNER/REPO#12345`

View task and output specific JSON fields:
`gh agent-task view 12345 --json id,state,pullRequestNumber`

Show agent session logs:
`gh agent-task view 12345 --log`

## Diagnostics and Troubleshooting

- If a task creation fails, verify repository permissions and ensure the GitHub CLI is authenticated (`gh auth status`).
- If using a custom agent, ensure the agent file exists in `.github/agents/`.

## Limitations

- The `gh agent-task` commands are currently in preview and subject to change.

## References

- [gh agent-task manual](https://cli.github.com/manual/gh_agent-task)
- [Starting GitHub Copilot sessions](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions)
- [Tracking GitHub Copilot's sessions](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/track-copilot-sessions)

## Related Skills

- **gh**: Use for general GitHub CLI operations.
- **gh-pr**: Use for pull request specific operations.
