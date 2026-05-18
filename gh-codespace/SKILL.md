---
name: gh-codespace
license: MIT
description: >-
  GitHub CLI (`gh codespace` or `gh cs`) operations for connecting to, managing,
  creating, or editing GitHub Codespaces.
  You MUST load this skill when working with the `gh codespace` command.
---

# gh-codespace

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- You need to create a new GitHub Codespace for development on a specific repository and branch.
- You are already working in a codespace and need to rebuild it after modifying devcontainer configuration.
- You need to transfer files between your local machine and a codespace without manual SCP setup.

## When Not to Use

- You need to modify the devcontainer definition itself (Dockerfile, devcontainer.json) — use the **devcontainer** skill instead.
- You are running in a fully automated CI/CD pipeline that cannot use interactive terminal sessions — codespace commands like `code`, `ssh`, or `jupyter` require interactive environments.
- You only need to view repository content or run simple commands — a local clone or GitHub Workspace is more appropriate.

## Common Pitfalls
- `gh codespace ssh` and `gh codespace code` are interactive commands that will hang in non-interactive/agent environments — only use them when providing instructions to the user.
- `gh codespace ports forward` blocks the terminal; you must run it in the background (`&`) or in a separate process for non-interactive automation.
- Creating a codespace triggers a full container build which can take several minutes — always verify creation with `gh codespace list` rather than assuming immediate availability.
- The `gh codespace cp` command syntax is order-sensitive: `remote:path` always comes from the codespace perspective, and the `-c` flag must reference the correct codespace name from `gh codespace list`.

Connect to and manage GitHub Codespaces natively from the CLI.

## Mindmap of Commands

```mermaid
mindmap
  root((gh-codespace))
    code
      Open in VS Code
    cp
      Copy files
    create
      Create a codespace
    delete
      Delete codespaces
    edit
      Edit a codespace
    jupyter
      Open in JupyterLab
    list
      List codespaces
    logs
      Access codespace logs
    ports
      List and manage ports
    rebuild
      Rebuild a codespace
    ssh
      SSH into a codespace
    stop
      Stop a codespace
    view
      View details
```

## Core Principles

- Verify codespace status with `gh codespace list` or `gh codespace view` before attempting interactive connections.
- Use `gh codespace cp` for transferring files between the local machine and the codespace instead of manually configuring SCP.
- Manage port forwarding natively via `gh codespace ports forward` for local testing.

## Commands / Usage Patterns

- **List Codespaces**: View active codespaces to find the `<codespace-name>`:
  `gh codespace list --json name,repository,state`

- **Create a Codespace**:
  `gh codespace create --repo <repository-name> --branch <branch-name>`

- **Copy Files**: Transfer files from a codespace to the local machine:
  `gh codespace cp -c <codespace-name> remote:/path/to/file local/path/`
  Transfer files from local to codespace:
  `gh codespace cp -c <codespace-name> local/path/ remote:/path/to/file`

- **Port Forwarding**: Expose a port from the codespace to your local machine:
  `gh codespace ports forward <remote-port>:<local-port> -c <codespace-name>`

- **Stop/Delete Codespace**: Clean up resources when done:
  `gh codespace stop -c <codespace-name>`
  `gh codespace delete -c <codespace-name>`

## Diagnostics and Troubleshooting

- **Connection Failures**: If `gh codespace ssh` hangs or fails, check codespace logs:
  `gh codespace logs -c <codespace-name>`
- **Rebuilding Environment**: If the Devcontainer configuration is modified or corrupted, trigger a rebuild:
  `gh codespace rebuild -c <codespace-name>`

## What to Avoid

- Do not attempt to SSH manually without using `gh codespace ssh` as it requires specific key exchanges handled by the CLI.
- Avoid using interactive commands (like `gh codespace code` or `gh codespace ssh`) in automated agent workflows. Use them only when providing instructions to the user.

## Limitations

- The CLI depends on active network connections and the GitHub Codespaces service availability.
- Port forwarding `gh codespace ports forward` blocks the terminal and requires background execution (`&`) or a separate process in non-interactive environments.

## References

- [gh codespace manual](https://cli.github.com/manual/gh_codespace)
