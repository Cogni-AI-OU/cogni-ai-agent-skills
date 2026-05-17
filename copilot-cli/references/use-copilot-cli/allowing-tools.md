# Allowing Tools

**Goal**: Configure and enforce explicit execution boundaries for tool access within Copilot CLI.

### Invariants
- Principle of Least Privilege applies: explicitly enable required tools; deny all others.
- YOLO mode bypasses all restrictions and must only be used in completely trusted, disposable environments.

### Schema / Configuration
- `--allow-tool`: Whitelists specific tools (e.g., `shell(git,ls)`).
- `--deny-tool`: Blacklists restricted operations (e.g., `shell(rm,chmod)`).
- `--yolo`: Requires user opt-in, suppresses all tool execution confirmations.

### Commands / Execution
```bash
# Explicitly allow specific tools for a task
gh copilot --allow-tool="shell(git,ls)" --prompt "Check git status"

# Run in unrestricted YOLO mode
gh copilot --yolo --prompt "Automate full setup"
```

## References
- [Allowing Tools](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools.md)