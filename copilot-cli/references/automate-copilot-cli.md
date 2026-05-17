# Automate Copilot CLI

**Goal**: Orchestrate GitHub Copilot CLI in pipelines, scripts, and non-interactive environments.

## Invariants

- Use `--no-ask-user` in non-interactive environments.
- Pass explicit prompts via `--prompt` or `-p`.
- Use `-s` (silent) to suppress conversational output in scripts.

## Automation Paths

- **[Quickstart](automate-copilot-cli/quickstart.md)**: Initial setup for automation.
- **[Programmatic Execution](automate-copilot-cli/run-cli-programmatically.md)**: Scoped CLI calls from scripts.
- **[GitHub Actions](automate-copilot-cli/automate-with-actions.md)**: Native CI/CD integration.

## References

- [Automating tasks with Copilot CLI](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/quickstart.md)
