# Steer Agents

**Goal**: Mid-flight control of agent logic, constraints, and task scope during execution.

## Invariants

- Steering input can be sent while the agent is in "Thinking" state.
- Messages are processed in order as part of the active task (no separate instruction queue).
- Interrupts agents heading in the wrong direction, provides inline feedback, or refines scope.
- No specific CLI flags for steering; purely interactive input.

## Steering Patterns

- **Interrupt**: Send new instructions when agent is "Thinking" to redirect task execution.
- **Inline feedback**: When rejecting a tool permission request (Esc), provide feedback so the agent adapts without stopping entirely.
- **Refine**: Narrow or expand task boundaries partway through execution.

## References

- [Steering agents in GitHub Copilot CLI - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/steer-agents.md)
