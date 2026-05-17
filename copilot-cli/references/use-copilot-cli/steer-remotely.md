# Steer a Session Remotely

**Goal**: Monitor, respond, and continue sessions from another device or GitHub Mobile.

## Invariants

- Requires Git repository hosted on GitHub.
- User-specific: Only you can access your own sessions.
- Remote control is disabled by default.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# Enable in session
/remote on

# Start with remote enabled
copilot --remote

# Prevent sleep
/keep-alive on (or 8h, 1d, etc.)
```

## Access Points

- **Web**: "Recent agent sessions" on GitHub.com homepage.
- **Mobile**: "Agent sessions" in GitHub Mobile app.
- **QR Code**: Toggle display in CLI via `Ctrl+E` (when prompt is empty).

## References

- [Steering a GitHub Copilot CLI session from another device](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/steer-remotely.md)
