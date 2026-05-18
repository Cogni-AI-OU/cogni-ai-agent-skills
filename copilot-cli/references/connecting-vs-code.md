# Connecting VS Code

**Goal**: Sync terminal CLI with IDE context for shared selection, trust settings, and visual diffing.

## Invariants

- Auto-connects when CWD matches an open VS Code workspace in trusted mode.
- Connection works from both VS Code integrated terminal and external terminals.
- Cannot connect to multiple IDE instances simultaneously.
- Codespaces: CLI session running locally cannot connect to a remote codespace VS Code instance. CLI inside the codespace (built-in terminal or SSH) can connect.
- If same workspace open in multiple windows, CLI auto-connects to one. Switch via `/ide`.

## IDE Connection Features

- **Editor selection as context**: Selected code in VS Code is displayed under the prompt box (right-aligned) and referenced in CLI prompts without specifying file paths.
- **Diff review**: File edits appear as side-by-side diffs in VS Code editor tabs. Accept (✓) or reject (✗) to resolve pending file-edit permission.
- **Live diagnostics**: Copilot can access real-time errors/warnings from VS Code diagnostics.
- **Session transcripts**: View CLI session transcripts in VS Code Copilot Chat sidebar > Sessions icon. Unread sessions show dot icon in VS Code title bar.

## Commands

```bash
# View connection status / switch workspace / disconnect
/ide
```

### `/ide` Toggle Settings

- **Auto-connect to matching IDE workspace**: Controls automatic connection at startup.
- **Open file edit diffs in IDE**: Controls whether proposed file changes show as diffs in VS Code.

## Resume Sessions in Terminal

From VS Code Copilot Chat > Sessions view:
1. Right-click a session.
2. Choose **Resume in Terminal** to continue in VS Code integrated terminal with full context.

## Diff Behavior Notes

- If file write permissions are pre-allowed (`--allow-all`, `/allow-all`, `--yolo`), diffs are NOT shown; changes applied directly.
- Turn off diff view in `/ide` menu to see proposed changes in CLI instead.

## References

- [Connecting GitHub Copilot CLI to Visual Studio Code - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code.md)
