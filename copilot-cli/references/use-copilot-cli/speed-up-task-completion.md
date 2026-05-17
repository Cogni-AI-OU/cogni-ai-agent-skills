# Speed Up Task Completion

**Goal**: Optimize Copilot CLI workflows and reduce latency during complex logical generations.

### Invariants
- Prevent redundant context loading.
- Enable parallelized data parsing and stream-based generation where applicable.

### Schema / Configuration
- Maximize the usage of explicit scoped agents to reduce LLM bloat and latency.
- Pass explicit, narrow file scopes instead of scanning whole directories.

### Commands / Execution
```bash
# Fast, stateless query without broad context mapping
gh copilot suggest -t shell "Restart Nginx"
```

## References
- [Speed Up Task Completion](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/speed-up-task-completion.md)