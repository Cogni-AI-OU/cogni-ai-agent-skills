# BYOK Models (Bring Your Own Key)

**Goal**: Override default foundation models by injecting external API configurations.

### Invariants
- Requires compatible OpenAI-shaped inference endpoints.
- Models must bypass internal default filters.

### Schema
Environment Execution:
```bash
export COPILOT_API_KEY="sk-..."
export COPILOT_API_URL="https://custom.endpoint/v1"
export COPILOT_MODEL="gpt-4"
```

### Commands
Execute: `gh copilot --model <MODEL_ID>`

## References
- [Use BYOK Models](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models.md)
