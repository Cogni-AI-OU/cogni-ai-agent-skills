---
name: shell
description: >-
  Efficient shell command handling.
  You MUST load this skill when handling shell commands with performance monitoring or timeouts.
license: MIT

---
# Shell Handling Skill

Execute shell commands with performance monitoring and timeout protection.

## When to Use

- Commands that might hang indefinitely
- Long-running commands (builds, tests, deployments)
- Performance optimization and debugging

## When Not to Use

- Quick, reliable commands that execute in milliseconds
- Interactive terminal sessions requiring human input
- Operations better handled by specialized built-in agents or native APIs

## Common Pitfalls

- **Ignoring Exit Codes**: Piping with `time` or `timeout` can mask the exit code of the underlying command. Use `set -o pipefail` or check `$?` carefully.
- **Overly Aggressive Timeouts**: Setting a timeout too close to the expected duration can cause false failures on slower environments (like CI/CD). Add a healthy buffer.
- **Runaway Child Processes**: `timeout` might not kill child processes spawned by the target command unless used with `--kill-after` or running in a new process group.

## Core Patterns

### Measure Execution Time

Prefix commands with `time` for duration visibility:

```bash
time command
time npm run build
```

### Limit Execution Time

Use `timeout` to prevent indefinite hangs:

```bash
timeout 30s command
timeout 60s npm test || echo "Failed or timed out"
```

### Combined Usage

```bash
time timeout 300s build_script.sh
```

## Key Points

- Combine with `||` for error handling fallbacks
- Set `timeout` based on expected runtime plus buffer
- Use `time` for all long operations to track performance
- `timeout --kill-after=5s 30s` for forceful termination if needed
- If command results are unexpected, briefly explain what happened and why.

## Related Skills

- **robust-commands**:
  You MUST load this skill when executing commands requiring resilient error recovery or fallbacks.
