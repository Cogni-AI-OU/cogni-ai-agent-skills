# Custom Instructions

**Goal**: Configure persistent persona and constraints for Copilot CLI agents.

### Invariants
- Location: `.copilot/instructions.md` (local) or user config directory.
- Execution: Automatically prepended to system prompts.
- Validation: Evaluate token budget limits.

### Schema
```markdown
# Role
System-level expert.

# Constraints
- Strict YAML output.
- No markdown wrappers.
```

### Commands
Execute: `gh copilot set-instruction "Always use absolute paths."`

## References
- [Adding custom instructions](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md)
- [Support for custom instructions](https://github.com/github/docs/blob/main/content/copilot/reference/custom-instructions-support.md)
- [Concepts](https://github.com/github/docs/blob/main/content/copilot/concepts/prompting/response-customization.md)
- [Custom agents configuration](https://github.com/github/docs/blob/main/content/copilot/reference/custom-agents-configuration.md)
- [Cloud agent secrets](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/configure-secrets-and-variables.md)
