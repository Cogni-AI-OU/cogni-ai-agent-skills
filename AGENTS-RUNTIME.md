# AGENTS-RUNTIME.md

Persistent single-source truth for autonomous agent behavior.

## Skills

You must load the skills relevant to the user prompt, inferred intent,
and planned work into the current context:

- **[ansible](ansible/SKILL.md)**: How to run and manage Ansible operations safely and prevent hangs.
  You must load this skill when working with the `ansible` command.
- **[cat](cat/SKILL.md)**: Guidelines for safely using `cat` and avoiding shell hangs with heredocs.
  You must load this skill before running `cat` command (especially with `EOF`).
- **[context-aware-ops](context-aware-ops/SKILL.md)**: Intelligent resource management with size checking and filtering
  to preserve context window.
  You must load this skill when managing large resources or context window limits.
- **[fact-writer](fact-writer/SKILL.md)**: Guidance for writing, structuring, and maintaining verifiable project
  fact files without contradictions.
  You must load this skill when managing canonical project fact files.
- **[gh](gh/SKILL.md)**: GitHub CLI (`gh`) operations for issues, pull requests, workflow runs, reviews, and API.
  You must load this skill when working with the `gh` command and its subcommands.
- **[gh-api](gh-api/SKILL.md)**: Advanced GitHub CLI (`gh api`) queries and mutations via REST or GraphQL.
  You must load this skill when working with the `gh api` command.
- **[gh-issue](gh-issue/SKILL.md)**: GitHub CLI (`gh issue`) operations for managing, viewing, and editing issues.
  You must load this skill when working with the `gh issue` command.
- **[gh-models](gh-models/SKILL.md)**: GitHub CLI models (`gh models`) operations for running and evaluating AI
  models.
  You must load this skill when working with the `gh models` command.
- **[gh-pr](gh-pr/SKILL.md)**: GitHub CLI (`gh pr`) operations for pull requests, reviews, PR checks, and PR
  branches.
  You must load this skill when working with the `gh pr` command.
- **[gh-run](gh-run/SKILL.md)**: GitHub CLI (`gh run`) and (`gh workflow`) operations for workflow runs, jobs,
  logs, and attempts.
  You must load this skill when working with the `gh run` and `gh workflow` commands.
- **[git](git/SKILL.md)**: Guide for using git with non-interactive, safe operations.
  You must load this skill when performing standard git operations.
- **[git-expert](git-expert/SKILL.md)**: Advanced Git operations including interactive rebasing, reflog recovery,
  bisecting, complex conflict resolution, and history manipulation.
  You must load this skill when performing advanced git operations or repository recovery.
- **[github](github/SKILL.md)**: GitHub-specific features and collaborative practices.
  You must load this skill when working with GitHub-specific features or PR view modes.
- **[github-actions](github-actions/SKILL.md)**: Diagnosing and debugging failing GitHub Actions workflows.
  You must load this skill when diagnosing or debugging GitHub Actions workflow failures.
- **[github-issue](github-issue/SKILL.md)**: Skills for working with GitHub Issues.
  You must load this skill when working with issues or when the runtime was triggered by an issue comment.
  Load this before any gh skills.
- **[github-pr](github-pr/SKILL.md)**: Skills for working with changes on a GitHub Pull Request.
  You must load this skill when working with changes associated with a pull request
  or when the runtime was triggered by a PR comment.
  Load this before any gh skills.
- **[github-pr-review](github-pr-review/SKILL.md)**: Comprehensive PR review workflow for verifying code quality,
  metadata accuracy, and merge readiness.
  You must load this skill when reviewing, auditing, or verifying a GitHub Pull Request.
- **[github-script](github-script/SKILL.md)**: Advanced use cases and examples for using actions/github-script.
  You must load this skill when using actions/github-script in workflows.
- **[mermaid](mermaid/SKILL.md)**: Guide for creating and maintaining stable Mermaid.js diagrams.
  You must load this skill when creating or maintaining Mermaid.js diagrams.
- **[mermaid-beta](mermaid-beta/SKILL.md)**: Guide for creating and maintaining experimental Mermaid.js beta diagrams.
  You must load this skill when working with experimental Mermaid.js beta diagrams.
- **[minizinc](minizinc/SKILL.md)**: Expert MiniZinc modeling for constraint satisfaction and combinatorial
  problems.
  You must load this skill when addressing constraint satisfaction or combinatorial problems using MiniZinc.
- **[molecule](molecule/SKILL.md)**: Molecule testing workflows for Ansible roles.
  You must load this skill when running or managing Molecule tests for Ansible.
- **[pdf](pdf/SKILL.md)**: PDF file inspection, object-level editing, and lossless size reduction.
  You must load this skill when inspecting, editing, or optimizing PDF files.
- **[pre-commit](pre-commit/SKILL.md)**: Using pre-commit to validate code formatting, linting, and security checks.
  You must load this skill when using pre-commit hooks for validation.
- **[robust-commands](robust-commands/SKILL.md)**: Resilient command execution with automatic fallbacks and error
  recovery.
  You must load this skill when executing commands requiring resilient error recovery or fallbacks.
- **[shell](shell/SKILL.md)**: Efficient shell command execution with timing, timeouts, and best practices.
  You must load this skill when handling shell commands with performance monitoring or timeouts.
- **[skill-writer](skill-writer/SKILL.md)**: Generate or update SKILL.md files for GitHub Copilot coding agents.
  You must load this skill when creating or updating GitHub Copilot skill files.
- **[vim-ex](vim-ex/SKILL.md)**: Non-interactive file editing with Vim Ex mode (in favor of sed, shell or Python
  editing).
  You must load this skill when using Vim Ex mode for non-interactive file editing.

Note: **Path Resolution**: For GitHub runtime within runner when triggered by `cogni-ai-agent-action`, these
instructions may be loaded from a temporary directory (e.g., `${{ runner.temp }}/.skills/`). When reading a skill
file below, you MUST resolve its relative path against the directory where this `AGENTS-RUNTIME.md` file is located
(check the "Instructions from: `<path>`" header in your system prompt), NOT your current working directory.

### Structural Invariant

- **Skills Location**: Skills are located directly in the root directory of this repository.
