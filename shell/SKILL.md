---
name: shell
description: >-
  Efficient shell command handling.
  You MUST load this skill when handling shell commands with performance monitoring or timeouts.
license: MIT

---
# Shell Handling Skill

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Executing shell commands that may take a long time to complete and need performance timing.
- Running commands in automated or agent-driven workflows where indefinite hangs must be prevented.
- Building CI/CD pipeline steps that need explicit timeout guards and duration tracking.

## When Not to Use

- Quick, known-fast commands where time measurement overhead and timeout setup add unnecessary complexity.
- Interactive debugging sessions where the user can manually interrupt a hanging command.
- Commands that must run in the background or as daemons—timeout will terminate them prematurely.

## Common Pitfalls

- `timeout` sends SIGTERM by default, which some commands may catch and ignore; use `--kill-after` for a hard SIGKILL after a grace period.
- The `time` command's output format differs between bash built-in and `/usr/bin/time`—when parsing output, use the built-in `TIMEFORMAT` variable or redirect to stderr.
- Wrapping a command in `time timeout` can mask the original command's exit code—always check that the original command succeeded, not just that the wrapper completed.
- Timeouts should include a reasonable buffer above expected runtime; too tight a timeout causes flaky failures in CI, too loose defeats the purpose.

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
