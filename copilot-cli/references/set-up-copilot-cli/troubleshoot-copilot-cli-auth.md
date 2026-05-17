# Troubleshoot Copilot CLI Auth

**Goal**: Diagnose and resolve authentication failures and permission blocks.

## Invariants

- `ghp_` (Classic PATs) are NOT supported.
- Fine-grained PATs MUST have "Copilot Requests" permission.
- OAuth app "GitHub CLI" must be authorized.
- Organization policies can block CLI usage.

## Schema (if applicable)

- N/A

## Commands / Execution (if applicable)

```bash
# Check GitHub CLI status
gh auth status

# Verify environment variable
echo $COPILOT_GITHUB_TOKEN

# macOS: Find stored password
security find-generic-password -s copilot-cli

# Linux: Search keyring
secret-tool search copilot-cli
```

## Error Resolutions

- **401 Unauthorized**: Token revoked or missing permissions. Re-authenticate with `copilot login`.
- **403 Forbidden**: Subscription missing or org policy restriction. Check license status.
- **Keychain Unavailable**: Install `libsecret` (Linux) or accept plaintext storage in `~/.copilot/config.json`.

## References

- [Troubleshooting GitHub Copilot CLI authentication](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/troubleshoot-copilot-cli-auth.md)
