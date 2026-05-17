# Connecting VS Code

**Goal**: Sync terminal CLI with IDE context for shared selection, trust settings, and visual diffing.

## Invariants

- Shares editor selection as context for CLI prompts.
- Displays proposed file edits as side-by-side diffs in VS Code.
- Surfaces live IDE diagnostics (errors/warnings) to the agent.
- Requires workspace to be open in trusted mode.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# View connection status / switch workspace
/ide

# Prompt with editor selection
"Debug this" (with code selected in IDE)

# Resume CLI session in VS Code terminal
[Right-click session in Sessions view] -> "Resume in Terminal"
```

## Configuration (if applicable)

- `Auto-connect to matching IDE workspace`: Toggle in `/ide` menu.
- `Open file edit diffs in IDE`: Toggle in `/ide` menu.

## References

- [Connecting GitHub Copilot CLI to Visual Studio Code](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code.md)
