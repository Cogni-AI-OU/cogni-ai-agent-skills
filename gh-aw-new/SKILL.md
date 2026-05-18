---
name: gh-aw-new
description: >-
  Create new GitHub Agentic Workflows (gh-aw) from scratch using the CLI extension.
  You MUST load this skill when creating new Agentic Workflow files.
license: MIT
---
# Skill: gh-aw-new

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

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
