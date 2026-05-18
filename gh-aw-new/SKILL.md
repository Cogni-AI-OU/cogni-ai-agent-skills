---
name: gh-aw-new
description: 'Create new GitHub Agentic Workflows (gh-aw) from scratch using the CLI extension. You MUST load this skill when creating new Agentic Workflow files.'
license: MIT
---
# Skill: gh-aw-new

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Creating a new GitHub Agentic Workflow from scratch that does not exist yet in the repository.
- Adding automation to a repository that has gh-aw initialized and needs a new workflow definition.
- Designing a shared agentic workflow that can be reused across multiple repositories in an organization.
- Scaffolding a new workflow that follows gh-aw conventions and best practices.
- Setting up the initial workflow structure before customizing the prompt logic.

## When Not to Use

- Editing or updating an existing workflow — use `github-aw` skill for modifying existing workflows.
- Debugging a failing workflow execution — use `gh-aw-troubleshooting` or `github-aw-troubleshooting` skills.
- Recompiling workflows after source changes — use `gh-aw-compile` skill for regeneration.
- Running or executing an existing workflow — use `gh-aw` skill with `gh aw run` instead.
- Working in a repository that has not been initialized with gh-aw — run `gh aw init` first.

## Common Pitfalls

- Never guess the workflow structure — always fetch and read the appropriate `create-*.md` prompt from the official gh-aw repository before proceeding, as the schema and requirements change between versions.
- Workflow creation produces multiple artifacts (`.md`, `.lock.yml`, agent files, action pins) — verify ALL expected files exist with `git status` before committing.
- The `.lock.yml` file is auto-generated and must NOT be edited manually — all behavioral changes go in the `.md` source file.
- After creation, always run `pre-commit run --all-files` to validate the new workflow meets quality and security standards before committing.

Create new GitHub Agentic Workflows (gh-aw) by installing the CLI extension and fetching official step-by-step creation instructions.

## Core Process

1. **Install or Upgrade gh-aw**:
   - Check installation: `gh extension list`
   - If not installed or needs upgrade: `gh extension install github/gh-aw` or `gh extension upgrade github/gh-aw`
2. **Fetch the Appropriate Prompt**:
   Use `webfetch` to retrieve the relevant instruction file based on the user's request, and read ALL instructions before proceeding:
   - **Create New Workflow**: `https://raw.githubusercontent.com/github/gh-aw/v0.74.3/.github/aw/create-agentic-workflow.md`
   - **Create Shared Workflow**: `https://raw.githubusercontent.com/github/gh-aw/v0.74.3/.github/aw/create-shared-agentic-workflow.md`
3. **Execute the Action**: Follow the fetched prompt's instructions exactly. Use `gh aw new <workflow-name>` to scaffold.
4. **Review Changes**: Run `git status`. Ensure the following are present:
   - `.github/workflows/<workflow-name>.md`
   - `.github/workflows/<workflow-name>.lock.yml`
   - `.github/agents/` (if new agents were created)
   - `.github/aw/actions-lock.json` (if new actions were pinned)
5. **Update .gitattributes**: Ensure `.gitattributes` contains: `.github/workflows/*.lock.yml linguist-generated=true merge=ours`.
6. **Validate**: Run repo-standard pre-commit hooks to ensure the new workflow meets quality and security standards:
   ```bash
   pre-commit run --all-files
   ```
7. **Commit and Push**: Commit the workflow files, lock files, agent files, and `.gitattributes`.

## Core Principles

- **Dynamic Loading**: Never guess the structure of a new workflow. Always fetch and read the appropriate `ROOT/.github/aw/create-*.md` prompt first.
- **Artifact Inclusion**: Always include regenerated lock files and agent definitions in the commit to ensure the workflow is ready for execution.

## When to Use

- When the user wants to create a new workflow from scratch, add automation, or design a workflow that doesn't exist yet.

## Commands / Usage Patterns

```bash
# Verify installation
gh extension list | grep gh-aw

# Create a new workflow (follow fetched guidelines)
gh aw new <workflow-name>

# Compile the new workflow
gh aw compile <workflow-name>
```

## Diagnostics and Troubleshooting

- If `gh aw` commands fail, verify that GitHub CLI (`gh`) is authenticated and that the `github/gh-aw` extension is installed with `gh extension list`.
- If a command is missing, ensure you have the latest version: `gh extension upgrade github/gh-aw`.
- Check `.lock.yml` files; workflows must be compiled successfully before they can run.

## Limitations

- This skill relies on fetching external Markdown files from the `gh-aw` repository. Ensure `webfetch` is available.

## References

- [Creating Agentic Workflows](https://github.com/github/gh-aw/blob/v0.74.3/create.md)
