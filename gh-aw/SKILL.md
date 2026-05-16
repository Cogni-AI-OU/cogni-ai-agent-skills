---
name: gh-aw
description: >-
  GitHub Agentic Workflows (`gh aw`) operations for repository automation,
  creating workflows, running coding agents, and auditing workflow runs.
  You MUST load this skill when working with the `gh aw` command.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# gh-aw Skill

Use `gh aw` to orchestrate GitHub Agentic Workflows for repository automation.

## How to Install the Extension

To install the GitHub Agentic Workflows extension for the GitHub CLI, run:

```bash
gh extension install github/gh-aw
```

If `gh extension install` is unavailable or fails (e.g., in environments
without GitHub CLI extension support), you can download and run the
installation script:

```bash
curl -sL https://raw.githubusercontent.com/github/gh-aw/main/install-gh-aw.sh -o install-gh-aw.sh
head -n 50 install-gh-aw.sh # Review the script before executing
bash install-gh-aw.sh
```

## Mindmap of Commands

```mermaid
mindmap
  root((gh aw))
    Setup Commands
      add
        Add workflows
      add-wizard
        Interactively add workflows
      init
        Initialize repository
      new
        Create new workflow
      remove
        Remove workflow files
      secrets
        Manage secrets
      update
        Update workflows
      upgrade
        Upgrade repository
    Development Commands
      compile
        Compile workflows into YAML
      domains
        List network domains
      fix
        Apply automatic fixes
      lint
        Lint workflows
      mcp
        Manage MCP servers
      validate
        Validate workflows
    Execution Commands
      disable
        Disable workflows
      enable
        Enable workflows
      run
        Run workflows on GitHub Actions
      trial
        Run in trial mode
    Analysis Commands
      audit
        Audit workflow run
      checks
        Classify CI check state
      health
        Display health metrics
      list
        List workflows
      logs
        Analyze workflow logs
      status
        Show status of workflows
    Utilities
      completion
        Generate shell completion
      hash-frontmatter
        Compute frontmatter hash
      mcp-server
        Run MCP server
      pr
        Pull request utilities
      project
        Create Projects V2 boards
```

## Agentic Workflow Prompts

When asked to create, update, debug, or upgrade GitHub Agentic Workflows, use `webfetch` to retrieve and read the appropriate instruction prompt from the official repository before proceeding:

- **Create New Workflow**: `https://raw.githubusercontent.com/github/gh-aw/main/.github/aw/create-agentic-workflow.md`
- **Update Existing Workflow**: `https://raw.githubusercontent.com/github/gh-aw/main/.github/aw/update-agentic-workflow.md`
- **Debug Workflow**: `https://raw.githubusercontent.com/github/gh-aw/main/.github/aw/debug-agentic-workflow.md`
- **Upgrade Agentic Workflows**: `https://raw.githubusercontent.com/github/gh-aw/main/.github/aw/upgrade-agentic-workflows.md`
- **Create Shared Agentic Workflow**: `https://raw.githubusercontent.com/github/gh-aw/main/.github/aw/create-shared-agentic-workflow.md`

## Core Process

1. **Setup**: Use `gh aw init` to initialize a repository, followed by `gh aw new <workflow-name>` or `gh aw add-wizard`.
2. **Development**: Workflows are markdown files compiled via `gh aw compile` into GitHub Actions YAML (`.lock.yml`).
3. **Execution**: Use `gh aw run <workflow-name>` to execute a workflow or `gh aw trial` for simulated runs.
4. **Analysis**: If a run fails, use `gh aw audit <run-id-or-url>` to debug the failed run. View logs with `gh aw logs <workflow-name> | head -n 100`.
5. **Updating**: Run `gh aw upgrade` to get the latest agent files and apply codemods.

## What to Avoid

- Always review the changes made by the AI agent, especially considering security and context.
- Do not manually edit the generated `.lock.yml` files; they are intended to be compiled from the markdown workflows.

## References

- <https://gh.io/gh-aw>
- <https://github.com/github/gh-aw>
- <https://github.com/github/gh-aw/blob/main/.github/aw/runbooks/workflow-health.md>

## Related Skills

- **gh-aw-compile**:
  You MUST load this skill when recompiling Agentic Workflows.
- **gh-run**:
  You MUST load this skill when working with GitHub Actions workflow runs.
