# AGENTS-RUNTIME.md

Persistent single-source truth for autonomous agent behavior.

For general project invariants see [README.md](README.md).

## Skills

**CRITICAL Path Resolution**: For GitHub runtime within runner when triggered by `cogni-ai-agent-action`, these
instructions may be loaded from a temporary directory (e.g., `${{ runner.temp }}/.skills/`). When reading a skill
file below, you MUST resolve its relative path against the directory where this `AGENTS-RUNTIME.md` file is located
(check the "Instructions from: `<path>`" header in your system prompt), NOT your current working directory.

You must load the skills relevant to the user prompt, inferred intent,
and planned work into the current context:

- **[ansible](ansible/SKILL.md)**: How to run and manage Ansible operations safely and prevent hangs
- **[context-aware-ops](context-aware-ops/SKILL.md)**: Intelligent resource management with size checking and filtering
- **[fact-writer](fact-writer/SKILL.md)**: Guidance for writing, structuring, and maintaining verifiable project
  fact files without contradictions
- **[gh](gh/SKILL.md)**: GitHub CLI (`gh`) operations for issues, PRs, workflows, and API
- **[git](git/SKILL.md)**: Guide for using git with non-interactive, safe operations
- **[git-expert](git-expert/SKILL.md)**: Advanced Git operations including interactive rebasing, reflog recovery,
  bisecting, complex conflict resolution, and history manipulation
- **[github](github/SKILL.md)**: GitHub specific features and collaborative practices
- **[github-actions](github-actions/SKILL.md)**: Diagnosing and debugging failing GitHub Actions workflows
- **[github-script](github-script/SKILL.md)**: Advanced use cases and examples for using actions/github-script
- **[mermaid](mermaid/SKILL.md)**: Guide for creating and maintaining stable Mermaid.js diagrams
- **[mermaid-beta](mermaid-beta/SKILL.md)**: Guide for creating and maintaining experimental Mermaid.js beta diagrams
- **[minizinc](minizinc/SKILL.md)**: Expert MiniZinc modeling for constraint satisfaction and combinatorial problems
- **[molecule](molecule/SKILL.md)**: Molecule testing workflows for Ansible roles
- **[pdf](pdf/SKILL.md)**: PDF file inspection, object-level editing, and lossless size reduction
- **[pre-commit](pre-commit/SKILL.md)**: Using pre-commit to validate code formatting, linting, and security checks
- **[robust-commands](robust-commands/SKILL.md)**: Resilient command execution with automatic fallbacks and error recovery
- **[shell](shell/SKILL.md)**: Efficient shell command execution with timing, timeouts, and best practices
- **[skill-writer](skill-writer/SKILL.md)**: Generate or update SKILL.md files for GitHub Copilot coding agents
- **[vim-ex](vim-ex/SKILL.md)**: Non-interactive file editing with Vim Ex mode (in favor of sed, shell or Python editing)

### Structural Invariant

- **Skills Location**: Skills are located directly in the root directory of this repository.
- **Do Not Add To Subdirectories**: Do not create or add new skills inside `.github/skills/` or other subdirectories.

### Final Assurance Gates

- Keep this file entropy-pruned and up-to-date.
- Inject full content into every sub-agent context.
- For latest standard see: <https://agents.md/>
