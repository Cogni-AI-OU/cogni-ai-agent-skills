# Authenticate Copilot CLI

**Goal**: Establish device flow or token authentication for GitHub Copilot CLI.

## Invariants

- OAuth device flow is the default for interactive use.
- Environment variables (`COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN`) are recommended for CI/CD and headless environments.
- Fine-grained PATs MUST have "Copilot Requests" permission.
- Classic PATs are NOT supported.
- Stored in system keychain (service: `copilot-cli`) or `~/.copilot/config.json` if keychain is unavailable.

## Schema (if applicable)

- Token types: OAuth (`gho_`), Fine-grained PAT (`github_pat_`), GitHub App (`ghu_`).
- Priority: `COPILOT_GITHUB_TOKEN` > `GH_TOKEN` > `GITHUB_TOKEN` > Keychain > `gh` fallback.

## Commands / Execution (if applicable)

```bash
# Start OAuth login flow
copilot login

# Check login status
/user

# Switch accounts
/user switch

# Logout
/logout
```

## References

- [Authenticating GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli.md)
