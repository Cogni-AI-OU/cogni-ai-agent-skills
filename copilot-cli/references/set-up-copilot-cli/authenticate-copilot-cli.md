# Authenticate Copilot CLI

**Source**: `github/docs` — Authenticating GitHub Copilot CLI.

## Invariants

- BYOK (bring-your-own-LLM-provider) mode: GitHub authentication is NOT required.
- Without GitHub auth: `/delegate`, GitHub MCP server, and GitHub Code Search are unavailable.
- Offline mode (`COPILOT_OFFLINE=true`): no GitHub auth attempted, telemetry disabled, only BYOK network requests.
- Token priority order: `COPILOT_GITHUB_TOKEN` > `GH_TOKEN` > `GITHUB_TOKEN` > system keychain > `gh auth token` fallback.
- Environment variables silently override stored OAuth tokens.
- BYOK provider env vars (`COPILOT_PROVIDER_BASE_URL`, `COPILOT_PROVIDER_API_KEY`) are used regardless of GitHub auth status.

## Supported Token Types

| Type | Prefix | Supported | Notes |
|---|---|---|---|
| OAuth token (device flow) | `gho_` | Yes | Default via `copilot login`. |
| Fine-grained PAT | `github_pat_` | Yes | Must be owned by personal account (not org) with **Copilot Requests** account permission. |
| GitHub App user-to-server | `ghu_` | Yes | Via env variable. |
| Classic PAT | `ghp_` | **No** | Not supported. |

## Credential Storage

Default: system keychain under service name `copilot-cli`.

| Platform | Keychain |
|---|---|
| macOS | Keychain Access |
| Windows | Credential Manager |
| Linux | libsecret (GNOME Keyring, KWallet) |

If keychain unavailable (e.g. headless Linux without libsecret), CLI prompts for plaintext storage in `~/.copilot/config.json`.

## Authentication Commands

```bash
# OAuth device flow (interactive)
copilot login
# or from CLI session: /login

# GHEC with data residency
copilot login --host HOSTNAME

# Check authenticated user (CLI session)
/user
# List available accounts
/user list
# Switch account (CLI session)
/user switch

# Sign out (removes local token, does not revoke)
/logout

# Check gh auth status (fallback method)
gh auth status
gh auth status --hostname HOSTNAME
```

## Environment Variable Auth (non-interactive)

```bash
export COPILOT_GITHUB_TOKEN="github_pat_..."
# or
export GH_TOKEN="github_pat_..."
# or
export GITHUB_TOKEN="github_pat_..."
```

## References

- <https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli.md>
