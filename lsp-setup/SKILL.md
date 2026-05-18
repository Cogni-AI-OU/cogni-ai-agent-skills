---
name: lsp-setup
description: 'Enable code intelligence (go-to-definition, find-references, hover, type info) for any programming language by installing and configuring an LSP server for Copilot CLI.'
license: MIT
---

# LSP Setup for GitHub Copilot CLI

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

**UTILITY SKILL** — installs and configures Language Server Protocol servers for Copilot CLI.

## When to Use

- When the user asks to enable code intelligence, go-to-definition, or hover information for Copilot CLI.
- When configuring a new development environment that lacks Language Server Protocol support.
- If Copilot CLI fails to provide contextual code completions due to a missing language server.

## When Not to Use

- When configuring LSP servers for a full IDE like VS Code or Neovim (this is specifically for Copilot CLI).
- If the language does not have a widely supported or functioning Language Server Protocol implementation.
- For simple syntax highlighting tasks.

## Common Pitfalls

- **Missing Binary on PATH**: Configuring the LSP JSON correctly but failing to ensure the installed binary is actually accessible in the system `$PATH`.
- **Overwriting Configs**: Using `>` to write the config file instead of safely merging, thereby destroying previously configured LSP servers for other languages.
- **Forgetting to Restart**: Assuming the new configuration takes effect immediately without instructing the user to exit and restart the Copilot CLI session.

## Core Process

1. **Ask the language** — use `ask_user` to ask which programming language(s) the user wants LSP support for.
2. **Detect the OS** — run `uname -s` (or check for Windows via `$env:OS` / `%OS%`) to determine macOS, Linux, or Windows.
3. **Look up the LSP server** — read `references/lsp-servers.md` for known servers, install commands, and config snippets.
4. **Ask scope** — use `ask_user` to ask whether the config should be user-level (`~/.copilot/lsp-config.json`) or repo-level (`lsp.json` at the repo root or `.github/lsp.json`).
5. **Install the server** — run the appropriate install command for the detected OS.
6. **Write the config** — merge the new server entry into the chosen config file (`~/.copilot/lsp-config.json` for user-level; `lsp.json` or `.github/lsp.json` for repo-level). Create the file if missing and preserve existing entries.
7. **Verify** — confirm the LSP binary is on `$PATH` and the config file is valid JSON.

## Core Principles

- Always use `ask_user` with `choices` when asking the user to pick a language or scope.
- If the language is not listed in `references/lsp-servers.md`, search the web for `"<language> LSP server"` and guide the user through manual configuration.
- If a package manager is not available (e.g. no Homebrew on macOS), suggest alternative install methods from the reference file.
- After installation, run `which <binary>` (or `where.exe` on Windows) to confirm the binary is accessible.
- Show the user the final config JSON before writing it.
- If the config file already exists, read it first and merge — do not clobber.

## Commands / Usage Patterns

Copilot CLI reads LSP configuration from user-level or repo-level locations, and repo-level config takes precedence over user-level config:

- **User-level**: `~/.copilot/lsp-config.json`
- **Repo-level**: `lsp.json` (repo root) or `.github/lsp.json`

The JSON structure:

```json
{
  "lspServers": {
    "<server-key>": {
      "command": "<binary>",
      "args": ["--stdio"],
      "fileExtensions": {
        ".<ext>": "<languageId>",
        ".<ext2>": "<languageId>"
      }
    }
  }
}
```

- `command` is the binary name (must be on `$PATH`) or an absolute path.
- `args` almost always includes `"--stdio"` to use standard I/O transport.
- `fileExtensions` maps each file extension (with leading dot) to a [Language ID](https://code.visualstudio.com/docs/languages/identifiers#_known-language-identifiers).
- Multiple servers can coexist in `lspServers`.
- When merging into an existing file, **never overwrite** other server entries — only add or update the target language key.

## Diagnostics and Troubleshooting

After setup, tell the user:

1. Type `/exit` to quit Copilot CLI — this is **required** so the new LSP configuration is loaded on next launch.
2. Re-launch `copilot` in a project with files of the configured language.
3. Run `/lsp` to check the server status.
4. Try code intelligence features like go-to-definition or hover.

## What to Avoid

- Do not overwrite existing servers inside the configuration.
- Do not assume a package manager is installed; verify first.
- Do not use for IDE/editor LSP configuration, only for Copilot CLI setups.

## Limitations

- Some LSP servers might require additional dependencies (like Node.js, Python) which should be checked.

## References

- [`copilot-cli/set-up-copilot-cli`](https://github.com/github/docs/tree/main/content/copilot/how-tos/copilot-cli/set-up-copilot-cli)
- [`lsp-setup/SKILL.md`](https://github.com/github/awesome-copilot/blob/main/skills/lsp-setup/SKILL.md)
- [Adding LSP servers for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/add-lsp-servers)
- [Using LSP servers with GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/lsp-servers)

## Related Skills

- **critical-thinking**: You MUST load this skill when troubleshooting why an LSP isn't working or properly registering.
