# Hooks Integration

**Goal**: Bind custom shell logic to pre/post execution lifecycle events in Copilot CLI.

### Invariants
- Supported events: `pre-prompt`, `post-prompt`, `pre-exec`, `post-exec`.
- Failures in `pre-*` hooks halt execution pipeline.
- Hooks located in standard `.copilot/hooks/` directory.

### Schema
Location: `.copilot/hooks/pre-exec.sh`
```bash
#!/usr/bin/env bash
# Validate command schema before shell invocation.
set -e
```

### Commands
Execute: Set execution permissions `chmod +x .copilot/hooks/*`

## References
- [Use hooks](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/use-hooks.md)
- [Hooks Reference](https://github.com/github/docs/blob/main/content/copilot/reference/hooks-reference.md)
