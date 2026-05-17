# Configure Copilot CLI

**Goal**: Manage persistent telemetry, alias, and operational settings for the Copilot CLI.

### Invariants
- Configuration is stored locally in `$XDG_CONFIG_HOME/github-copilot/` or `~/.config/github-copilot/`.
- Enables or disables telemetry tracking.
- Binds shortcut aliases for CLI tool integration.

### Schema / Configuration
Valid settings:
- `telemetry` (enabled/disabled)
- `aliases` (custom shell aliases)

### Commands / Execution
```bash
# Set telemetry preference
gh copilot config telemetry disable

# Display current configuration
gh copilot config list
```

## References
- [Configure Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli.md)