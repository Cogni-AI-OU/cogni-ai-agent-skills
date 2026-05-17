# Speed Up Task Completion

**Goal**: Accelerate multi-step implementations by parallelizing subtasks via the `/fleet` command.

## Invariants

- Assigns separate parts of the work to concurrent subagents.
- Best used after establishing an implementation plan in plan mode.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

1. **Plan**: Enter plan mode (`Shift+Tab`) and define implementation.
2. **Execute**:
    - **Interactive**: Select "Accept plan and build on autopilot + /fleet".
    - **Slash Command**: `/fleet implement the plan`.

## Monitoring

```bash
# View background subtasks
/tasks

# Within /tasks view:
# [Enter] - View details
# [k] - Kill process
# [r] - Remove task
```

## References

- [Speeding up task completion with the /fleet command](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/speed-up-task-completion.md)
