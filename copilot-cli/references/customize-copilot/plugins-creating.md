# Creating Plugins

**Goal**: Build extensions via npm/Node.js to add sub-commands and custom workflow logic to Copilot CLI.

### Invariants
- Package manager: npm.
- Language: JavaScript/TypeScript.
- Entrypoint: Defined in `package.json` under `bin` or Copilot spec.

### Commands
Execute: `gh copilot extension create` (or package equivalent).

## References
- [Creating Plugins](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md)
