# AGENTS-RUNTIME.md

Persistent single-source truth for autonomous agent behavior.

## Skills

You MUST load the skills relevant to the user prompt, inferred intent,
and planned work into the current context.

**Tool Execution Invariants:**

- **Idempotent Skill Loading**:
  Avoid redundant `skill` tool calls for the same skill in the same conversation turn or session.
  Once a skill is loaded, its instructions are active for the duration of the agent's operation in that context.
- **Native Tool Calling ONLY**:
  When executing tools (including the `skill` tool, `bash`, or others),
  you MUST use the native tool calling mechanism provided by your environment.
  NEVER emit literal text strings like `[tool_call: ...]` or write out your intended tool calls as plain text in your response.
- **Parallel Tool Calls**:
  If you need to load multiple skills or call multiple tools, invoke the native tool call for each tool independently
  in the same turn. Do not write pseudo-code or text blocks mimicking tool calls.

- **[agent-log-analysis](agent-log-analysis/SKILL.md)**: Procedures and templates for analyzing agent session
  logs, extracting telemetry, and generating standardized visual audit reports.
  You MUST load this skill when auditing or analyzing autonomous agent log files.
- **[agent-md](agent-md/SKILL.md)**: Syntax and structure reference for GitHub Copilot custom agent persona files
  (.github/agents/*.agent.md), OpenCode agent definitions, and Claude Code (CLAUDE.md).
  You MUST load this skill to understand the schema and format of agent persona definitions across platforms.
- **[agent-md-writer](agent-md-writer/SKILL.md)**: Guidelines and best practices for writing high-performance
  agent persona files (*.agent.md, CLAUDE.md).
  You MUST load this skill when creating or refining a specialized agent persona.
- **[agents-md-writer](agents-md-writer/SKILL.md)**: Autonomous documentation editor responsible for creating,
  updating, and maintaining AGENTS.md files strictly adhering to the organizational baseline structure.
  You MUST load this skill when creating or updating AGENTS.md files.
- **[agentskills](agentskills/SKILL.md)**: Guidance on the Agent Skills open standard for creating
  portable, non-interactive, and secure Copilot agent skills.
  You MUST load this skill when designing or manually creating agent skills.
- **[ansible](ansible/SKILL.md)**: How to run and manage Ansible operations safely and prevent hangs.
  You MUST load this skill when working with the `ansible` command.
- **[brainstorm](brainstorm/SKILL.md)**: Activate brainstorming protocol to explore options, research, deconstruct
  complexities, and summarize available data into simple diagrams and MiniZinc constraints.
  You MUST load this skill when asked to brainstorm, explore options, or break down complex problems.
- **[brainstorm-agent-runs](brainstorm-agent-runs/SKILL.md)**: Activate agent-run brainstorming protocol to identify and
  analyze agent runs via GitHub API for a given Pull Request.
  You MUST load this skill when identifying agentic runs in CI/CD for a Pull Request.
- **[brainstorm-github-pr](brainstorm-github-pr/SKILL.md)**: Activate PR brainstorming protocol to analyze and visualize
  commit history, review threads, and CI pipeline checks using Mermaid diagrams.
  You MUST load this skill when asked to analyze or brainstorm a Pull Request.
- **[cat](cat/SKILL.md)**: Guidelines for safely using `cat` and avoiding shell hangs with heredocs.
  You MUST load this skill before running the `cat` command (especially with `EOF`).
- **[code-review](code-review/SKILL.md)**: Cognitive framework for expert-level code inspection to identify logical
  flaws, hygiene issues, and architectural drift.
  You MUST load this skill when reviewing code or Pull Requests.
- **[code-tour](code-tour/SKILL.md)**: Create, update, and maintain VSCode CodeTour (.tour) JSON walkthrough files with
  full schema compliance and interactive step configuration.
  You MUST load this skill when creating or updating .tours/ files.
- **[codeql](codeql/SKILL.md)**: Configure and execute CodeQL code scanning analysis via GitHub Actions workflows and
  the CodeQL CLI.
  You MUST load this skill when configuring CodeQL workflows or using the CodeQL CLI.
- **[coding-standard-writer](coding-standard-writer/SKILL.md)**: Write a coding standards document for a project using
  the coding styles inferred from provided file(s) or folder(s).
  You MUST load this skill when creating or updating coding standards from existing files.
- **[context-aware-ops](context-aware-ops/SKILL.md)**: Intelligent resource management with size checking and filtering
  to preserve context window.
  You MUST load this skill when managing large resources or context window limits.
- **[copilot-cli](copilot-cli/SKILL.md)**: Guidance for installing GitHub Copilot CLI on Debian/Ubuntu and executing
  commands using custom agents.
  You MUST load this skill when interacting with or installing the copilot-cli command.
- **[critical-thinking](critical-thinking/SKILL.md)**: Engage deep analytical reasoning, deconstruct assumptions,
  apply Socratic questioning, and perform adversarial red-teaming to solve complex problems and validate architectural plans.
  You MUST load this skill when facing challenges that require critical thinking.
- **[datadog-api](datadog-api/SKILL.md)**: Execute Datadog API requests to fetch live objects, metrics, or
  monitor statuses using cURL and API keys.
  You MUST load this skill when interacting with the Datadog API.
- **[datadog-agent](datadog-agent/SKILL.md)**: Expert-level guidance for installing, configuring, and extending the
  Datadog Agent.
  You MUST load this skill when installing, configuring, or updating Datadog Agent.
- **[datadog-mcp](datadog-mcp/SKILL.md)**: Query observability data via Datadog MCP, selecting minimal toolsets
  to optimize context window and scope.
  You MUST load this skill when a task needs Datadog telemetry analysis through MCP tools.
- **[datadog-monitors](datadog-monitors/SKILL.md)**: Guidelines for designing, debugging, and troubleshooting
  Datadog monitor queries, handling common false positives, and operational edge cases.
  You MUST load this skill when designing, debugging, or troubleshooting Datadog monitors.
- **[datadog-pulumi](datadog-pulumi/SKILL.md)**: Use when creating or debugging Datadog monitors in Pulumi YAML,
  especially for schema mismatches, monitor validation errors, and provider-specific field mapping.
  You MUST load this skill when working with Datadog monitors in Pulumi YAML.
- **[dictation](dictation/SKILL.md)**: Apply dictation correction protocols to fix common speech-to-text errors and
  improve text clarity.
  You MUST load this skill when fixing dictation or speech-to-text input.
- **[direnv](direnv/SKILL.md)**: How to maintain credentials and authenticate using direnv without exposing
  secrets to the output.
  You MUST load this skill when API keys are missing or when using direnv for environment variables.
- **[dockerfile](dockerfile/SKILL.md)**: Write, review, and optimize Dockerfiles applying multi-stage
  builds, non-root constraints, layer caching, and strict image pinning.
  You MUST load this skill when writing, reviewing, or optimizing Dockerfiles.
- **[docs-review](docs-review/SKILL.md)**:
  Enforce documentation quality, completeness, and mutual consistency across architecture, ADRs, runbooks, and code.
  You MUST load this skill when asked to review or check consistency of documentation.
- **[docs-writer](docs-writer/SKILL.md)**:
  Create, update, and maintain documentation including Architectural Decision Records (ADRs),
  runbooks, READMEs, and code-level documentation.
  You MUST load this skill when asked to write, document, or generate new documentation.
- **[fact-writer](fact-writer/SKILL.md)**: Guidance for writing, structuring, and maintaining verifiable project
  fact files without contradictions.
  You MUST load this skill when managing canonical project fact files.
- **[gdpr-compliant](gdpr-compliant/SKILL.md)**: Apply GDPR-compliant engineering practices across your codebase.
  You MUST load this skill whenever you are designing APIs, writing data models,
  implementing logging, handling user data, or reviewing pull requests for
  privacy compliance.
- **[gh](gh/SKILL.md)**: GitHub CLI (`gh`) operations for issues, pull requests, workflow runs, reviews, and API.
  You MUST load this skill when working with the `gh` command and its subcommands.
- **[gh-agent-task](gh-agent-task/SKILL.md)**: GitHub CLI (`gh agent-task`) operations for creating, listing,
  and viewing preview agent tasks.
  You MUST load this skill when working with the `gh agent-task` command.
- **[gh-api](gh-api/SKILL.md)**: Advanced GitHub CLI (`gh api`) queries and mutations via REST or GraphQL.
  You MUST load this skill when working with the `gh api` command.
- **[gh-aw](gh-aw/SKILL.md)**: GitHub Agentic Workflows (`gh aw`) operations for repository automation,
  creating workflows, running coding agents, and auditing workflow runs.
  You MUST load this skill when working with the `gh aw` command.
- **[gh-aw-compile](gh-aw-compile/SKILL.md)**: Regenerate and post-process all agentic workflows.
  You MUST load this skill when gh-aw is updated, workflow .md files change,
  or when asked to recompile/regenerate workflows.
- **[gh-aw-debug](gh-aw-debug/SKILL.md)**: Diagnose and fix GitHub Agentic Workflows (`gh-aw`) failures
  by analyzing logs for missing tools, permissions, or MCP configurations.
  You MUST load this skill when diagnosing or fixing `gh aw` workflow failures.
- **[gh-aw-firewall-debug](gh-aw-firewall-debug/SKILL.md)**: Debug the AWF firewall by inspecting Docker containers,
  analyzing Squid access logs, checking iptables rules, and troubleshooting network issues.
  You MUST load this skill when debugging the awf firewall.
- **[gh-aw-new](gh-aw-new/SKILL.md)**: Create new GitHub Agentic Workflows (gh-aw) from scratch using the CLI extension
  and fetching official remote creation prompts.
  You MUST load this skill when creating new agentic workflows.
- **[gh-issue](gh-issue/SKILL.md)**: GitHub CLI (`gh issue`) operations for managing, viewing, and editing issues.
  You MUST load this skill when working with the `gh issue` command.
- **[gh-models](gh-models/SKILL.md)**: GitHub CLI models (`gh models`) operations for running and evaluating AI
  models.
  You MUST load this skill when working with the `gh models` command.
- **[gh-pr](gh-pr/SKILL.md)**: GitHub CLI (`gh pr`) operations for pull requests, reviews, PR checks, and PR
  branches.
  You MUST load this skill when working with the `gh pr` command.
- **[gh-run](gh-run/SKILL.md)**: GitHub CLI (`gh run`) and (`gh workflow`) operations for workflow runs, jobs,
  logs, and attempts.
  You MUST load this skill when working with the `gh run` and the `gh workflow` commands.
- **[gh-search](gh-search/SKILL.md)**: GitHub CLI (`gh search`) operations for searching code, commits, issues,
  pull requests, and repositories with structured JSON output.
  You MUST load this skill when working with the `gh search` command.
- **[gh-skill](gh-skill/SKILL.md)**: Expert-level guidance on GitHub CLI (`gh skill`) operations for
  searching, previewing, installing, updating, and publishing Copilot agent skills.
  You MUST load this skill when managing agent skills via the GitHub CLI.
- **[git](git/SKILL.md)**: Guide for using git with non-interactive, safe operations.
  You MUST load this skill when performing standard git operations.
- **[git-expert](git-expert/SKILL.md)**: Advanced Git operations including reflog recovery,
  bisecting, complex conflict resolution, and history manipulation.
  You MUST load this skill when performing advanced git operations or repository recovery.
- **[git-filter-branch](git-filter-branch/SKILL.md)**: Extract a specific subdirectory with history using git filter-branch
  when modern tools like filter-repo are unavailable.
  You MUST load this skill when extracting a subdirectory with history.
- **[git-merge](git-merge/SKILL.md)**: Guide and safety rules for performing git merges,
  ensuring no conflict markers and no duplicate lines are present.
  You MUST load this skill before performing a git merge.
- **[git-rebase](git-rebase/SKILL.md)**: Advanced Git rebase operations including
  interactive history cleanup and non-interactive scripted rewrites.
  You MUST load this skill when performing Git rebase operations.
- **[github](github/SKILL.md)**: GitHub-specific features and collaborative practices.
  You MUST load this skill when working with GitHub-specific features or PR view modes.
- **[github-actions](github-actions/SKILL.md)**: Diagnosing and debugging failing GitHub Actions workflows.
  You MUST load this skill when diagnosing or debugging GitHub Actions workflow failures.
- **[github-aw](github-aw/SKILL.md)**: Safely update existing GitHub Agentic Workflows (gh-aw), distinguishing between
  frontmatter configuration that requires recompilation and markdown body prompt edits that do not.
  You MUST load this skill when updating or modifying an existing GitHub Agentic Workflow.
- **[github-aw-debug](github-aw-debug/SKILL.md)**: Debug and refine GitHub Agentic Workflows (gh-aw) by analyzing
  execution logs, auditing runs, and resolving missing tool errors or prompt inefficiencies.
  You MUST load this skill when asked to debug, audit, or analyze a failing GitHub Agentic Workflow.
- **[github-aw-memory](github-aw-memory/SKILL.md)**: Guide for persistent memory strategies in agentic workflows.
  You MUST load this skill when designing workflows that persist state across runs via
  cache-memory, repo-memory, or comment-memory.
- **[github-aw-syntax](github-aw-syntax/SKILL.md)**: Complete reference for GitHub Agentic Workflows (gh-aw) frontmatter
  schema, engine configuration, network access, tools, and imports syntax.
  You MUST load this skill when writing or debugging Agentic Workflow files.
- **[github-issue](github-issue/SKILL.md)**: Skills for working with GitHub Issues.
  You MUST load this skill when working with issues or when the runtime was triggered by an issue comment.
  Load this before any gh skills.
- **[github-mcp-server](github-mcp-server/SKILL.md)**: Guide for configuring and using the GitHub MCP server within
  Agentic Workflows, including toolset selection, authentication modes, and available GitHub API tools.
  You MUST load this skill when configuring the GitHub MCP server or its toolsets.
- **[github-pr](github-pr/SKILL.md)**: Skills for working with changes on a GitHub Pull Request.
  You MUST load this skill when working with changes associated with a pull request
  or when the runtime was triggered by a PR comment.
  Load this before any gh skills.
- **[github-pr-review](github-pr-review/SKILL.md)**: Comprehensive PR review workflow for verifying code quality,
  metadata accuracy, and merge readiness.
  You MUST load this skill when reviewing, auditing, or verifying a GitHub Pull Request.
- **[github-script](github-script/SKILL.md)**: Advanced use cases and examples for using actions/github-script.
  You MUST load this skill when using actions/github-script in workflows.
- **[github-topics](github-topics/SKILL.md)**: Search GitHub repositories by topics and keywords.
  You MUST load this skill when searching for relevant tools, libraries, or curated resources.
- **[lsp-setup](lsp-setup/SKILL.md)**: Enable code intelligence by installing and configuring an LSP server for Copilot CLI.
  You MUST load this skill when asked to set up, install, or configure an LSP server.
- **[mcp-cli](mcp-cli/SKILL.md)**: Interface for MCP (Model Context Protocol) servers via CLI.
  You MUST load this skill when interacting with external tools, APIs, or data sources through MCP servers via CLI.
- **[mermaid](mermaid/SKILL.md)**: Guide for creating and maintaining stable Mermaid.js diagrams.
  You MUST load this skill when creating or maintaining Mermaid.js diagrams.
- **[mermaid-beta](mermaid-beta/SKILL.md)**: Guide for creating and maintaining experimental Mermaid.js beta diagrams.
  You MUST load this skill when working with experimental Mermaid.js beta diagrams.
- **[minizinc](minizinc/SKILL.md)**: Expert MiniZinc modeling for constraint satisfaction and combinatorial
  problems.
  You MUST load this skill when addressing constraint satisfaction or combinatorial problems using MiniZinc.
- **[molecule](molecule/SKILL.md)**: Molecule testing workflows for Ansible roles.
  You MUST load this skill when running or managing Molecule tests for Ansible.
- **[mot](mot/SKILL.md)**: Evaluate and classify machine learning models based on the Model Openness Framework (MOF).
  You MUST load this skill to find model metadata like architecture, producer, components, etc.,
  from the Model Openness Tool.
- **[opencode](opencode/SKILL.md)**: Manage OpenCode configuration, credentials, and access the OpenCode Zen API.
  You MUST load this skill when working with OpenCode configuration or listing models.
- **[pdf](pdf/SKILL.md)**: PDF file inspection, object-level editing, and lossless size reduction.
  You MUST load this skill when inspecting, editing, or optimizing PDF files.
- **[pipenv](pipenv/SKILL.md)**: Manage Python project dependencies, virtual environments, and security using the
  pipenv CLI.
  You MUST load this skill when using pipenv to manage environments or dependencies.
- **[pipfile](pipfile/SKILL.md)**: Create, update, and manage Python project dependencies via Pipfile and Pipfile.lock.
  You MUST load this skill when creating or updating Pipfile or Pipfile.lock.
- **[pre-commit](pre-commit/SKILL.md)**: Using pre-commit to validate code formatting, linting, and security checks.
  You MUST load this skill when using pre-commit hooks for validation.
- **[python](python/SKILL.md)**: Execute Python inline scripts via heredocs for complex log processing,
  summarization, or JSON parsing.
  You MUST load this skill when processing large logs.
- **[rfc2119](rfc2119/SKILL.md)**: Enforce correct usage of RFC 2119 requirement level keywords
  (MUST, SHOULD, MAY, etc.) in documentation and specifications.
  You MUST load this skill when writing or reviewing standards, specifications, or when applying RFC 2119 terminology.
- **[robust-commands](robust-commands/SKILL.md)**: Resilient command execution with automatic fallbacks and error
  recovery.
  You MUST load this skill when executing commands requiring resilient error recovery or fallbacks.
- **[sbom](sbom/SKILL.md)**: Guidelines and commands for generating a Software Bill of Materials (SBOM) using syft.
  You MUST load this skill when asked to create, generate, or update an SBOM.
- **[security-audit](security-audit/SKILL.md)**: Commands, step-by-step procedures, and mechanical execution for
  performing deep security audits, vulnerability assessments, and threat modeling.
  You MUST load this skill when performing security audits or validation.
- **[shell](shell/SKILL.md)**: Efficient shell command execution with timing, timeouts, and best practices.
  You MUST load this skill when handling shell commands with performance monitoring or timeouts.
- **[skill-writer](skill-writer/SKILL.md)**: Generate or update SKILL.md files for coding agents.
  You MUST load this skill when creating or updating agent skill files.
- **[subagent-task](subagent-task/SKILL.md)**: Guidance and protocols for spawning sub-agents via the task tool.
  You MUST load this skill when delegating complex tasks to sub-agents.
- **[tdd](tdd/SKILL.md)**: Commands, step-by-step procedures, and mechanical execution for test engineering,
  testability audits, and the TDD lifecycle.
  You MUST load this skill when executing test tasks, designing tests, doing TDD, or verifying system behavior.
- **[tester](tester/SKILL.md)**: Elite autonomous test engineering kernel focused on proving software correctness,
  preventing regressions, and designing refactor-resilient behavioral tests.
  You MUST load this skill when designing tests, analyzing test coverage, or acting as a test engineer.
- **[vim-ex](vim-ex/SKILL.md)**: Non-interactive file editing with Vim Ex mode (in favor of sed, shell or Python
  editing).
  You MUST load this skill when using Vim Ex mode for non-interactive file editing.
- **[yaml](yaml/SKILL.md)**: Generic guidelines for YAML formatting, linting, and structural rules.
  You MUST load this skill when formatting or linting YAML files.
- **[yq](yq/SKILL.md)**: Safely parse, edit, merge, and transform YAML files using yq, providing robust
  command-line examples for extraction and in-place modifications.
  You MUST load this skill when using the yq tool.

Note: **Path Resolution**: For GitHub runtime within runner when triggered by `cogni-ai-agent-action`, these
instructions may be loaded from a temporary directory (e.g., `${{ runner.temp }}/.skills/`). When reading a skill
file below, you MUST resolve its relative path against the directory where this `AGENTS-RUNTIME.md` file is located
(check the "Instructions from: `<path>`" header in your system prompt), NOT your current working directory.

### Structural Invariant

- **Skills Location**: Skills are located directly in the root directory of this repository.
