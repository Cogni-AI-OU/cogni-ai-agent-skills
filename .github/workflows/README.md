# GitHub Actions Workflows

Reusable and repository workflows that automate checks, reviews, and AI-powered tasks.

- For the agent-facing workflow catalog, see [AGENTS.md](AGENTS.md).
- For editing guidelines, follow [.github/instructions/github-workflows.instruction.md](../instructions/github-workflows.instruction.md).

## Using these workflows

- Reference a workflow from another repo with `uses: Cogni-AI-OU/.github/.github/workflows/<file>@main`.
- Consult the catalog in [AGENTS.md](AGENTS.md) for inputs, triggers, and job details.
- Keep branch protection and required checks enabled when consuming workflows that can push commits.
- Use `opencode.yml` and `opencode-review.yml` for slash-command-driven OpenCode automation.
