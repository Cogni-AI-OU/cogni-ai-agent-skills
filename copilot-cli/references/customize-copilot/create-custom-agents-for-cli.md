# Custom Agents

**Goal**: Define specialized runtimes with bounded domains and customized system prompts.

### Schema
File: `agent.yaml`
```yaml
name: "SecAudit"
model: "gpt-4o"
system_instruction: "Perform strict security code audit."
tools:
  - "github-mcp"
```

### Invariants
- Requires `github.copilot` authentication.
- Scoped to `gh copilot` runtime or `@agent` invocation in VS Code.

## References
- [Create custom agents for CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md)
- [Custom agents configuration](https://github.com/github/docs/blob/main/content/copilot/reference/custom-agents-configuration.md)
