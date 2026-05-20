# GitHub Copilot Hooks Reference

Hooks are external commands executing at specific lifecycle points during a session, enabling custom automation, security controls, and integrations. Supported in GitHub Copilot CLI and Copilot Cloud Agent.

## Hooks Locations

- **Copilot CLI** (Local machine):
  1. Repository-level: `.github/hooks/*.json`
  2. User-level: `~/.copilot/hooks/*.json` (macOS/Linux), `%USERPROFILE%\.copilot\hooks\*.json` (Windows), or `$COPILOT_HOME/hooks/*.json`.
  3. Inline blocks: `hooks` field in `.github/copilot/settings.json`, `.github/copilot/settings.local.json`, `.claude/settings.json`, `.claude/settings.local.json`.
  4. User-level inline block: `hooks` field in `~/.copilot/settings.json`.
  5. Plugins: `hooks.json` or `hooks/hooks.json` inside plugin installation directory.

- **Copilot Cloud Agent** (Ephemeral Linux sandbox):
  - Configuration loaded *only* from `.github/hooks/*.json` in cloned repository.
  - OS: Linux (only `bash` or `command` fields honored).
  - Working directory: `/workspace` (with repository) or `/root`.
  - Filesystem: Ephemeral.
  - Network: Restricted to GitHub and Copilot hostnames unless allowlisted.
  - Environment variables available: `GITHUB_COPILOT_API_TOKEN`, `GITHUB_COPILOT_GIT_TOKEN`, `COPILOT_AGENT_PROMPT`, `HOME=/root`. (`GITHUB_TOKEN` is not set).
  - Interactivity: Fully non-interactive (no permission dialogs).

## Hook Configuration Format

JSON format with version `1`.

### Command Hooks

Run shell scripts. Cloud agent honors `bash` or `command` fallback.

```json
{
  "version": 1,
  "hooks": {
    "preToolUse": [
      {
        "type": "command",
        "bash": "your-bash-command",
        "powershell": "your-powershell-command",
        "cwd": "optional/working/directory",
        "env": { "VAR": "value" },
        "timeoutSec": 30
      }
    ]
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `bash` | string | 1 of 3 | Shell command for Unix. |
| `command` | string | 1 of 3 | Cross-platform fallback. |
| `cwd` | string | No | Working directory (relative to repository root or absolute). |
| `env` | object | No | Environment variables to set. |
| `powershell` | string | 1 of 3 | Shell command for Windows. |
| `timeoutSec` | number | No | Timeout in seconds. Default: `30`. |
| `type` | `"command"` | Yes | Must be `"command"`. |

### HTTP Hooks

Send input payload as JSON `POST`.

```json
{
  "version": 1,
  "hooks": {
    "postToolUse": [
      {
        "type": "http",
        "url": "https://hooks.example.com/copilot",
        "headers": { "X-Source": "copilot-cli" },
        "allowedEnvVars": ["GITHUB_TOKEN"],
        "timeoutSec": 30
      }
    ]
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `allowedEnvVars` | string[] | No | Env var names that may be expanded inside `headers` values. URL must use `https://`. |
| `headers` | object | No | Request headers. |
| `timeoutSec` | number | No | Timeout in seconds. Default: `30`. |
| `type` | `"http"` | Yes | Must be `"http"`. |
| `url` | string | Yes | Target URL. Must use `https://` for `preToolUse` and `permissionRequest`. |

### Prompt Hooks

Auto-submit text. (Supported only on `sessionStart`). Does not fire on resume, non-interactive mode, or Cloud Agent.

```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [
      {
        "type": "prompt",
        "prompt": "Your prompt text or /slash-command"
      }
    ]
  }
}
```

## Hook Events

| Event | Output Processed | Cloud Agent Behavior |
|-------|------------------|----------------------|
| `agentStop` | Block/force continuation | Fires. `decision: "block"` forces turn. |
| `errorOccurred` | No | Fires. |
| `notification` | Inject `additionalContext` | Does not fire. |
| `permissionRequest` | Allow/deny tool programmatically | Does not fire / No effect. Use `preToolUse`. |
| `postToolUse` | No | Fires. |
| `postToolUseFailure` | Inject `additionalContext` | Fires. |
| `preCompact` | No | Fires only with `trigger: "auto"`. |
| `preToolUse` | Allow, deny, modify | Fires. `"ask"` treated as `"deny"`. |
| `sessionEnd` | No | Fires. |
| `sessionStart` | Inject `additionalContext` | Fires as new session. |
| `subagentStart` | Prepended `additionalContext` | Fires. |
| `subagentStop` | Block/force continuation | Fires. |
| `userPromptSubmitted`| No | Fires at most once for job prompt. |

## Matcher Filtering

Optional `matcher` regex filters hook invocations. Pattern anchored as `^(?:matcher)$`.

| Event | `matcher` checks against |
|-------|--------------------------|
| `notification` | `notification_type` |
| `permissionRequest` | `toolName` |
| `preCompact` | `trigger` (`"manual"`/`"auto"`) |
| `preToolUse` | `toolName` |
| `subagentStart` | `agentName` |

## Decision Control

### `preToolUse` Control

Output JSON object to stdout.

| Field | Values | Description |
|-------|--------|-------------|
| `permissionDecision` | `"allow"`, `"deny"`, `"ask"` | Empty uses default. `"ask"` becomes `"deny"` in Cloud Agent. |
| `permissionDecisionReason` | string | Reason shown if `"deny"`. |
| `modifiedArgs` | object | Substitute arguments. |

### `agentStop` / `subagentStop` Control

Output JSON object to stdout.

| Field | Values | Description |
|-------|--------|-------------|
| `decision` | `"block"`, `"allow"` | `"block"` forces another turn. |
| `reason` | string | Prompt for next turn if `"block"`. |

### `permissionRequest` Control (CLI only)

Output JSON object to stdout.

| Field | Values | Description |
|-------|--------|-------------|
| `behavior` | `"allow"`, `"deny"` | Short-circuits permission flow. |
| `message` | string | Reason if `"deny"`. |
| `interrupt` | boolean | Stop agent entirely if `"deny"`. |

Exit code `2` from command hooks acts as deny (stdout merged).

## Disabling Hooks

Set `disableAllHooks: true` at top-level of configuration payload to ignore hooks.

## References

- [GitHub Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference)
