# Plugins: Finding and Installing

**Goal**: Extend functionality via community or team-created plugins from marketplaces.

## Invariants

- Marketplaces are registered registries of plugins.
- Default marketplaces: `copilot-plugins`, `awesome-copilot`.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# List registered marketplaces
copilot plugin marketplace list

# Browse a marketplace
copilot plugin marketplace browse awesome-copilot

# Install a plugin
copilot plugin install PLUGIN-NAME@MARKETPLACE-NAME

# Manage plugins
copilot plugin list
copilot plugin update PLUGIN-NAME
copilot plugin uninstall PLUGIN-NAME

# Add a marketplace
copilot plugin marketplace add OWNER/REPO
```

## References

- [Finding and installing plugins for GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing.md)
