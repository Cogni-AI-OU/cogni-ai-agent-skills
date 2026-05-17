# Troubleshoot Copilot CLI Auth

**Goal**: Diagnose and resolve authentication and connection failures within the Copilot CLI.

### Invariants
- Ensure network access to github.com and api.github.com is permitted.
- Proxies or VPNs must support standard certificate negotiation without intercepting the SSL/TLS session aggressively.

### Schema / Configuration
Common failure states:
- `401 Unauthorized`: Entitlement inactive or missing permissions.
- Timeout / DNS resolution: Proxy configuration blocks.

### Commands / Execution
```bash
# Refresh and force re-authentication
gh auth login --scopes "copilot"

# Verify connection and entitlement
gh copilot auth status
```

## References
- [Troubleshoot Copilot CLI Auth](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/troubleshoot-copilot-cli-auth.md)