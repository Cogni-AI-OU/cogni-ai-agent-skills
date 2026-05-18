# Plugins: Marketplace

**Goal**: Create and share plugin registries for easy discovery and installation.

## Invariants

- Requires `marketplace.json` in `.github/plugin/` directory.
- `marketplace.json` is the only mandatory component.

## Schema (if applicable)

```json
{
  "name": "My Marketplace",
  "plugins": [
    {
      "name": "frontend-design",
      "source": "./plugins/frontend-design"
    }
  ]
}
```

## Commands / Execution (if applicable)

```bash
# Register a marketplace from GitHub
copilot plugin marketplace add octo-org/octo-repo

# Register from local filesystem
copilot plugin marketplace add /path/to/dir
```

## References

- [Creating a plugin marketplace for GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace.md)
