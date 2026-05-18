# Use BYOK Models

**Goal**: Configure external LLM providers (OpenAI, Anthropic, Azure) via Bring Your Own Key (BYOK).

## Invariants

- Models MUST support **tool calling** and **streaming**.
- Context window of at least 128k tokens is recommended.
- GitHub authentication is NOT required if using ONLY BYOK.
- Features like `/delegate` and GitHub MCP still require GitHub authentication.

## Schema (if applicable)

- `COPILOT_PROVIDER_BASE_URL`: API endpoint URL.
- `COPILOT_PROVIDER_TYPE`: `openai` (default), `azure`, or `anthropic`.
- `COPILOT_PROVIDER_API_KEY`: Provider API key.
- `COPILOT_MODEL`: Model identifier.
- `COPILOT_OFFLINE`: Set to `true` for air-gapped/isolated use.

## Commands / Execution (if applicable)

```bash
# Example: Local Ollama
export COPILOT_PROVIDER_BASE_URL=http://localhost:11434
export COPILOT_MODEL=llama3.2
copilot

# Example: Anthropic
export COPILOT_PROVIDER_TYPE=anthropic
export COPILOT_PROVIDER_BASE_URL=https://api.anthropic.com
export COPILOT_PROVIDER_API_KEY=sk-...
export COPILOT_MODEL=claude-3-5-sonnet
copilot
```

## References

- [Using your own LLM models in GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models.md)
