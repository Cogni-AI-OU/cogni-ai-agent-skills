# Overview

**Goal**: Establish foundational usage, interactions, and core capabilities of the GitHub Copilot CLI.

### Invariants
- Primary interfaces are `suggest` and `explain`.
- Context is prioritized toward terminal commands, shell syntax, and active environments.

### Schema / Configuration
- Executes as a native subcommand of the GitHub CLI (`gh`).

### Commands / Execution
```bash
# General invocation for command syntax help
gh copilot suggest "How do I untar a file?"

# Explain an existing command
gh copilot explain "tar -xvf file.tar.gz"
```

## References
- [Overview](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/use-copilot-cli/overview.md)