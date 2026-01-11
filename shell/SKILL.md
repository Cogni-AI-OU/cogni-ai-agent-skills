<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->

---
name: shell
description: Efficient shell command execution with timing and timeout controls
license: MIT
---

# Shell Handling Skill

Execute shell commands with performance monitoring and timeout protection.

## When to Use

- Long-running commands (builds, tests, deployments)
- Commands that might hang indefinitely
- Performance optimization and debugging

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

- Use `time` for all long operations to track performance
- Set `timeout` based on expected runtime plus buffer
- Combine with `||` for error handling fallbacks
- `timeout --kill-after=5s 30s` for forceful termination if needed
