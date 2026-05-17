# Steer Agents

**Goal**: Mid-flight control of agent logic, constraints, and task scope during execution.

## Invariants

- Steering input can be sent while the agent is "Thinking".
- Messages are processed in order as part of the active task.
- Steering interrupts agents heading in the wrong direction or clarifies scope.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

- Steering is performed by entering prompts while the agent is in the "Thinking" state.
- No specific CLI flags; interactive input only.

## Usage Patterns

- **Interrupt**: Send new instructions to redirect the agent.
- **Feedback**: Provide inline feedback when rejecting tool permission requests.
- **Refine**: Narrow or expand task boundaries partway through.

## References

- [Steering agents in GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/steer-agents.md)
