# Connecting VS Code

**Goal**: Seamlessly bind the terminal-based Copilot CLI execution environment with the VS Code editor context.

### Invariants
- Context synchronization must be established between the headless CLI and the IDE.
- Extends the agent's visibility into unsaved editor buffers and active selections.

### Schema / Configuration
- Operates via IDE extension handshakes and local RPC/sockets.

### Commands / Execution
```bash
# Explicitly sync or connect with active VS Code instance
gh copilot connect vscode
```

## References
- [Connecting VS Code](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code.md)