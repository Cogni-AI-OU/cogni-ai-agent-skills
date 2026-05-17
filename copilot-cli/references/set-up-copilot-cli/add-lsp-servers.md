# Add LSP Servers

**Goal**: Configure Language Server Protocol (LSP) servers to provide real-time code intelligence context to the Copilot CLI.

### Invariants
- LSP servers must be installed and accessible in the system `PATH`.
- Enhances command context with go-to-definition, find-references, and hover provider data.

### Schema / Configuration
- Supported out-of-the-box servers vary by language.
- Standard mappings can be managed via the CLI configuration.

### Commands / Execution
```bash
# Add a new LSP server
gh copilot config --add-lsp-server <server_command>

# Verify configured LSP servers
gh copilot config --list-lsp-servers
```

## References
- [Add LSP Servers](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/add-lsp-servers.md)