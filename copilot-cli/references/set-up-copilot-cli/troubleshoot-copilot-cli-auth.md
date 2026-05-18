# Troubleshoot Copilot CLI Auth

**Source**: `github/docs` — Troubleshooting GitHub Copilot CLI authentication.

## Error Reference

| Error | Cause | Fix |
|---|---|---|
| No authentication information found | No credentials stored | Run `copilot login` |
| 401 Unauthorized | Token revoked or insufficient permissions | Generate token with Copilot Requests permission |
| Classic PAT (`ghp_`) rejected | Classic PATs not supported | Use fine-grained PAT (`github_pat_`) |
| 403 Forbidden / policy denied | No Copilot license or org policy block | Check subscription / request org admin enable |
| Keychain unavailable | Missing system keychain | Install `libsecret` (Linux) or accept plaintext |
| Wrong account | Multiple accounts / env var override | Check env vars, use `/user switch` |

## Diagnosis Commands

```bash
# Check gh auth status
gh auth status

# Check env vars
echo $COPILOT_GITHUB_TOKEN
echo $GH_TOKEN
echo $GITHUB_TOKEN

# macOS keychain
security find-generic-password -s copilot-cli
security delete-generic-password -s copilot-cli  # remove stale entry

# Linux keyring
command -v secret-tool
secret-tool search copilot-cli

# Install libsecret (Debian/Ubuntu)
sudo apt install libsecret-1-0 gnome-keyring seahorse
```

## Detailed Resolutions

### No Authentication Information Found

CLI output:

```text
Error: No authentication information found
```

**Checklist**:
1. `gh auth status` — login with `gh auth login` if needed.
2. `echo $COPILOT_GITHUB_TOKEN` — set env var if empty.
3. `security find-generic-password -s copilot-cli` (macOS) — re-auth if missing.

### Token Expired or Revoked

CLI output:

```text
Error: Authentication failed
Your GitHub token may be invalid, expired, or lacking the required permissions.
```

**Fix**: Verify token is a fine-grained PAT (`github_pat_`) owned by personal account with **Copilot Requests** permission. Re-generate if needed.

### Classic PAT Rejected

Tokens starting with `ghp_` are silently ignored. Generate a fine-grained PAT instead.

### Access Denied (403)

CLI output:

```text
Error: Access denied by policy settings
```

**Fix**:
- Confirm active Copilot subscription.
- Request org admin to enable Copilot CLI in org policy settings.

### Keychain Access Failure

CLI prompt:

```text
System keychain unavailable. Store token in plaintext config file? (y/N)
```

**Fix**:
- **macOS/Windows**: Ensure credential manager is functional. If unavailable, use env var auth.
- **Linux**: `sudo apt install libsecret-1-0 gnome-keyring seahorse`, then re-auth.

### Wrong Account

**Fix**: `/user switch` at CLI prompt, or `/logout` then `/login` with correct account.

## References

- <https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/troubleshoot-copilot-cli-auth.md>
