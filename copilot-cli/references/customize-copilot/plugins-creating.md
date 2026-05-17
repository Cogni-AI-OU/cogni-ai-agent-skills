# Plugins: Creating

**Goal**: Bundle agents, skills, hooks, and MCP servers into distributable units.

## Invariants

- Requires `plugin.json` manifest at root.
- Caching: Installed plugins are cached; reinstall to apply local changes.

## Schema (if applicable)

```text
my-plugin/
|-- plugin.json
|-- agents/ (Optional: *.agent.md)
|-- skills/ (Optional: NAME/SKILL.md)
|-- hooks.json (Optional)
`-- .mcp.json (Optional)
```

## Commands / Execution (if applicable)

```bash
# Install local plugin for testing
copilot plugin install ./my-plugin

# List installed plugins
copilot plugin list

# Uninstall plugin
copilot plugin uninstall PLUGIN-NAME
```

## References

- [Creating a plugin for GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md)
