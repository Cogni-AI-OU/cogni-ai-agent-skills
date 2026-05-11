---
name: shell
description: >-
  Efficient shell command handling.
  You MUST load this skill when handling shell commands with performance monitoring or timeouts.
license: MIT

---
# Shell Handling Skill

Execute shell commands with performance monitoring and timeout protection.

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
