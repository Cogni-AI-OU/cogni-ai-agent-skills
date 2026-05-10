# GitHub Actions Workflows

Reusable and repository workflows that automate checks, reviews, and AI-powered tasks.

- For the agent-facing workflow catalog, see [AGENTS.md](AGENTS.md).
- For editing guidelines, rely on `actionlint`, `yamlfix`, and `.yamllint` along with `.github/copilot-instructions.md`.

## Using these workflows

- Reference a workflow from another repo with `uses: Cogni-AI-OU/.github/.github/workflows/<file>@main`.
- Consult the catalog in [AGENTS.md](AGENTS.md) for inputs, triggers, and job details.
- Keep branch protection and required checks enabled when consuming workflows that can push commits.

## Workflows

### Check Workflow

The `check.yml` workflow runs on pull requests, pushes, and weekly schedule to
ensure code quality and correctness.

Jobs:

- **actionlint**: Validates GitHub Actions workflow files
- **link-checker**: Checks for broken links in Markdown files using Lychee
- **pre-commit**: Runs pre-commit hooks for code formatting and linting

#### Link Checker

The link checker job uses [Lychee](https://github.com/lycheeverse/lychee) to
scan all Markdown files for broken links. It includes caching to avoid rate
limits and can be configured via `.lycheeignore` at the repository root to
exclude specific URLs or patterns.

**Local Testing**: You can test links locally with the configured
`markdown-link-check` pre-commit hook:

```bash
# Install from requirements.txt
pip install -r .devcontainer/requirements.txt

# Check a single file
pre-commit run markdown-link-check --files path/to/file.md

# Check all Markdown files
pre-commit run markdown-link-check -a
```

The hook uses `.markdown-link-check.json` and checks both local file references
and remote URLs before you push changes.

#### Using Check as a Reusable Workflow

You can use the Check workflow in your repository by referencing it via `workflow_call`:

```yaml
---
name: Check
on:
  pull_request:
  push:
  schedule:
    - cron: 0 0 * * 1  # Run every Monday at 00:00 UTC
  workflow_dispatch:
jobs:
  check:
    uses: Cogni-AI-OU/cogni-ai-agent-skills/.github/workflows/check.yml@main
    with:
      submodules: 'false'  # Set to 'true' or 'recursive' if repository uses submodules
```

### Cogni AI Agent Workflow (`cogni-ai-agent.yml`)

The `cogni-ai-agent.yml` workflow provides the underlying logic to run the Cogni AI Agent. It runs on issue
comments, pull request review comments, and manual triggers (`workflow_dispatch`). It installs Python dependencies
from `.devcontainer/requirements.txt` and calls the `Cogni-AI-OU/cogni-ai-agent-action` to process natural language
instructions and automate repository tasks using selected LLM models.

### Copilot Setup Steps Workflow (`copilot-setup-steps.yml`)

The `copilot-setup-steps.yml` workflow is a utility workflow that checks out the repository, sets up Python 3.12,
restores the Python user site cache, and installs dependencies from `.devcontainer/requirements.txt`. It is triggered
on pushes and pull requests that modify the workflow file or the requirements file.

### Devcontainer CI Workflow (`devcontainer-ci.yml`)

The `devcontainer-ci.yml` workflow builds and tests the development container image.

**Purpose**: It ensures that all required command-line tools (e.g., `docker`, `gh`, `pre-commit`) and Python packages
(e.g., `ansible-lint`, `molecule`) are properly installed and functional inside the devcontainer. It runs on changes
to the `.devcontainer` directory, on a weekly schedule, and can also be used as a reusable workflow (requires
`packages: write` permission for the caller).

#### Using Devcontainer CI as a Reusable Workflow

```yaml
jobs:
  devcontainer:
    uses: Cogni-AI-OU/cogni-ai-agent-skills/.github/workflows/devcontainer-ci.yml@main
    permissions:
      contents: read
      packages: write  # Required for pushing to GitHub Container Registry
```

## Problem Matchers

GitHub Actions problem matchers automatically annotate files with errors and
warnings in pull requests, making it easier to identify and fix issues.

### Available Matchers

- [**actionlint-matcher.json**](../actionlint-matcher.json): Captures errors from actionlint workflow linting
- [**pre-commit-matcher.json**](../pre-commit-matcher.json): Captures errors from pre-commit hooks

### Pre-commit Problem Matcher

The pre-commit problem matcher supports two output formats:

1. **Generic format** (`file:line:col: message`): Used by flake8, actionlint,
   and other tools that provide column information
2. **No-column format** (`file:line message`): Used by markdownlint and other
   tools that only provide line numbers

Note: Some hooks like yamllint and ansible-lint already output GitHub Actions
annotations directly and don't need the problem matcher.

### Configuration

Problem matchers are registered in the `check.yml` workflow
before running the corresponding tools.

### Using Matchers in Reusable Workflows

When using the `check.yml` workflow as a reusable workflow (via `workflow_call`),
the matcher files are automatically provided from this repository. You don't need
to copy the matcher files to your repository.

If you want to use custom matcher files, you can specify them using the inputs:

```yaml
jobs:
  check:
    uses: Cogni-AI-OU/cogni-ai-agent-skills/.github/workflows/check.yml@main
    with:
      actionlint-matcher-path: .github/custom-actionlint-matcher.json
      pre-commit-matcher-path: .github/custom-pre-commit-matcher.json
```

If these inputs are not provided, the workflow will automatically use the default
matcher files from this repository.

## OpenCode Tools

### OpenCode (MCP) Tools

When operating via OpenCode in the GitHub Actions runtime, the following MCP tools are available and
should be utilized to perform tasks effectively:

- **vscode**: `getProjectSetupInfo`, `installExtension`, `memory`, `newWorkspace`, `resolveMemoryFileUri`, `runCommand`,
  `vscodeAPI`, `extensions`, `askQuestions`
- **execute**: `runNotebookCell`, `testFailure`, `getTerminalOutput`, `killTerminal`, `sendToTerminal`,
  `createAndRunTask`, `runInTerminal`
- **read**: `getNotebookSummary`, `problems`, `readFile`, `viewImage`, `terminalSelection`, `terminalLastCommand`
- **edit**: `createDirectory`, `createFile`, `createJupyterNotebook`, `editFiles`, `editNotebook`, `rename`
- **search**: `changes`, `codebase`, `fileSearch`, `listDirectory`, `textSearch`, `usages`
- **web**: `fetch`, `githubRepo`
- **browser**: `openBrowserPage`
- **agent**: `runSubagent`
- **misc**: `vscode.mermaid-chat-features/renderMermaidDiagram`, `ms-python.python/getPythonEnvironmentInfo`,
  `ms-python.python/getPythonExecutableCommand`, `ms-python.python/installPythonPackage`, `todo`

### OpenCode Core Native Agent Tools

In addition to the MCP integrations, the agent runtime provides a set of core built-in capabilities
(often logged during builds as `Glob`, `Todo` or `TodoWrite`, `Edit`, etc.). These are executed directly by
the agent's core engine, rather than through the OpenCode MCP protocol.

Available native tools include:

- **File System & Search**: `Glob` (fast file pattern matching), `Grep` (fast content search),
  `Read` (read files/directories)
- **File Mutation**: `Edit` (exact string replacements), `Write` (overwrite/create files)
- **Execution**: `Bash` (persistent shell session for terminal operations like git, npm, etc.)
- **Agentic Tracking**: `Todo` / `TodoWrite` (creates and manages structured task lists for complex sessions)
- **Research & Sub-agents**: `Task` (launch specialized subagents), `Webfetch`, `Websearch`, `Codesearch`

*Note: The native tools `Glob`, `Read`, `Grep`, `Edit`, and `Write` are explicitly prioritized over their shell
equivalents (such as `find`, `cat`, `grep`, `sed`) to ensure precise context retention and safety.*
