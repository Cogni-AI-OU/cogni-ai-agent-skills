# Steer a Session Remotely

**Goal**: Monitor, respond, and continue sessions from web browser or GitHub Mobile.

## Invariants

- Requires Git repository hosted on GitHub.
- User-specific: only the session owner can access their sessions.
- Remote control is **disabled by default**.
- Machine must remain online with session actively running.
- CWD must be a GitHub-hosted Git repository.

## Enabling Remote Control

```bash
# During interactive session
/remote on

# Start with remote enabled
copilot --remote

# Disable for current session (during session)
/remote off
```

### Persistent Configuration

```json
// ~/.copilot/settings.json
{ "remoteSessions": true }
```

Override per-session with `--no-remote`. CLI options always take precedence over settings file.

## Access Points

- **Web**: github.com → Menu → Copilot → "Recent agent sessions" or repository "Agents" tab.
- **Mobile**: GitHub Mobile → Copilot button → "Agent sessions".
- **Filter**: Use "Type" filter to show only CLI sessions.

## QR Code

```bash
# Toggle QR code display (input field must be empty)
Ctrl+E
```

Scan with phone to open session directly in GitHub Mobile.

## Keep-Alive

Prevents machine sleep during remote sessions:

```bash
/keep-alive on          # Prevent sleep while session active
/keep-alive off         # Allow normal sleep
/keep-alive busy        # Prevent sleep only while Copilot is working on a task
/keep-alive 30m         # Prevent sleep for N minutes
/keep-alive 8h          # Prevent sleep for N hours
/keep-alive 1d          # Prevent sleep for N days
/keep-alive             # Display current keep-alive status
```

- Bare number = minutes.
- Machine can sleep when Copilot is waiting for user input (except in `on` mode).

## Reviewing Past Sessions

Web/Mobile: Navigate to agent sessions list, click a session. Web shows the `copilot --resume` command for resumption.

## Resuming

Use `copilot --resume` on the machine where the session was originally run.

## Preventing Remote Control

- Per session: `copilot --no-remote`
- Permanently: Remove `"remoteSessions": true` from `~/.copilot/settings.json` or set to `false`.

## References

- [Steering a GitHub Copilot CLI session from another device - github/docs](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/steer-remotely.md)
