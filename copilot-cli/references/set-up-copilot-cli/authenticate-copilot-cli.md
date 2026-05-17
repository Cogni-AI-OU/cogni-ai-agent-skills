# Authenticate Copilot CLI

**Goal**: Establish an authenticated session with GitHub to enable Copilot CLI operations.

### Invariants
- Requires an active GitHub Copilot entitlement.
- Authentication can use visual device flows or direct Personal Access Tokens (PATs).
- Fine-grained PATs must have the **Copilot Requests** permission.

### Schema / Configuration
- Web workflow outputs a one-time code for device authentication.
- Automated environments must inject the PAT via the environment variable `GH_TOKEN` or `GITHUB_TOKEN`.

### Commands / Execution
```bash
# Interactive web authentication
gh copilot auth login

# Check authentication status
gh copilot auth status
```

## References
- [Authenticate Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli.md)