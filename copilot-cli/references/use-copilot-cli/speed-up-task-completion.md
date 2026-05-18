# Speed Up Task Completion

**Goal**: Parallelize multi-step implementations via `/fleet` slash command, assigning work to concurrent subagents.

## Invariants

- `/fleet` assigns separate parts of the work to subagents for parallel execution.
- Best used after establishing an implementation plan in plan mode.
- Subagents run as background tasks within the current session.

## Workflow

1. **Plan**: Enter plan mode (`Shift+Tab`) and define implementation plan collaboratively.
2. **Execute**:
   - **Accept plan and build on autopilot + /fleet**: Fully autonomous parallel implementation with subagents.
   - **Exit plan mode and I will prompt myself** then: `/fleet implement the plan`
3. Copilot starts working on the plan, using subagents to parallelize work where possible. May ask questions during execution.

## Commands

```bash
# Execute plan with subagents
/fleet implement the plan
```

## Monitoring

```bash
# View background tasks / subagent subtasks
/tasks
```

### Task List Controls

| Key | Action |
|-----|--------|
| `↓` / `↑` | Navigate through background tasks. |
| `Enter` | View subtask details (shows summary when complete). |
| `k` | Kill the subagent process. |
| `r` | Remove completed or killed subtasks from list. |
| `Esc` | Exit task list and return to main prompt. |

## References

- [Speeding up task completion with the /fleet command - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/speed-up-task-completion.md)
