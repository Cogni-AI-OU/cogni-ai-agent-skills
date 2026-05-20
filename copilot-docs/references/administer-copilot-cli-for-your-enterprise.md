# Administering Copilot CLI for Enterprise

**Goal**: Configure and control Copilot CLI usage across an enterprise.

## Invariants

- Users must have an assigned Copilot seat.
- Enterprise policies override organization settings.
- Model availability follows enterprise-level configuration.
- Audit logging records policy updates.

## Policies Managed

- **Enablement**: Enable/disable at enterprise or organization level.
- **Model Selection**: Restrict available AI models (visible via `/model`).
- **Custom Agents**: Enable access to enterprise-configured agents.
- **MCP Servers**: Enforce registry URLs and allowlist policies.
- **Cloud Agent**: Requires both CLI and Cloud Agent policies for `/delegate`.

## Non-applicable Controls

- IDE-specific policies.
- Content exclusions (file path-based).
- User-configured model providers (BYOK).

## References

- [Administering Copilot CLI for your enterprise](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise.md)
