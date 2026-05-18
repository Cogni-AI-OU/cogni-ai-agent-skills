# Automate Copilot CLI

**Goal**: Orchestrate GitHub Copilot CLI in pipelines, scripts, and non-interactive environments.

## Automation Paths

- **[Quickstart](automate-copilot-cli/quickstart.md)**: Build a simple automation script using `-p` flag and shell scripting.
- **[Programmatic Execution](automate-copilot-cli/run-cli-programmatically.md)**: Pass prompts via `-p`/`--prompt`, pipe input, silence metadata with `-s`, restrict tools with `--allow-tool`.
- **[GitHub Actions](automate-copilot-cli/automate-with-actions.md)**: Install `@github/copilot`, authenticate with `COPILOT_GITHUB_TOKEN`, run in CI/CD.

## Invariants

- Use `--no-ask-user` in non-interactive environments to prevent prompt hangs.
- Pass explicit prompts via `--prompt` or `-p`.
- Use `-s` (silent) to suppress conversational output in scripts.
- Authenticate via `COPILOT_GITHUB_TOKEN` environment variable.

## References

- [Automate with GitHub Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/index.md)
