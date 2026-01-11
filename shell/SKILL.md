<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->

---
name: shell
description: Efficient shell command execution with timing, timeouts, and best practices
license: MIT
---

# Shell Handling Skill

Execute shell commands efficiently with proper timing measurements, timeout controls,
and error handling patterns for robust automation.

## When to Use This Skill

- When executing shell commands that need performance monitoring
- When dealing with potentially long-running commands
- When you need to prevent commands from hanging indefinitely
- When debugging command execution issues
- When optimizing command performance

## Core Practices

### Measure Execution Time

Prefix commands with `time` for visibility into execution duration:

```bash
# Basic timing
time command

# Time with detailed output
time long_running_script.sh

# Time with stderr redirect
time command 2>&1
```

### Limit Execution Time

Use `timeout` to prevent commands from running indefinitely:

```bash
# Timeout after 30 seconds
timeout 30s command

# Timeout with custom signal (SIGTERM)
timeout 30s command

# Timeout with SIGKILL after grace period
timeout --kill-after=5s 30s command

# Timeout with fallback
timeout 10s risky_command || echo "Command timed out or failed"
```

### Combined Timing and Timeout

```bash
# Measure time and enforce limit
time timeout 60s build_script.sh

# With error handling
time timeout 30s test_suite.sh || {
  echo "Tests failed or timed out after 30s"
  exit 1
}
```

## Pattern Examples

### Safe Long-Running Commands

```bash
# Build with timeout and timing
time timeout 300s npm run build

# Test with reasonable limit
time timeout 120s npm test

# Deploy with timeout
time timeout 600s ./deploy.sh
```

### Interactive Command Protection

```bash
# Prevent interactive prompts from hanging
echo "y" | timeout 10s apt-get install package

# Use timeout for potentially interactive tools
timeout 30s command < /dev/null
```

### Retry with Timeout

```bash
# Retry up to 3 times, each with 30s timeout
for i in {1..3}; do
  timeout 30s flaky_command && break
  echo "Attempt $i failed, retrying..."
  sleep 2
done
```

## Best Practices

1. **Always time long operations**: Use `time` for builds, tests, deployments
2. **Set reasonable timeouts**: Prevent infinite hangs with `timeout`
3. **Choose timeout values wisely**: Consider typical runtime + buffer
4. **Combine with error handling**: Chain with `||` for fallbacks
5. **Log timing data**: Capture duration for performance analysis
6. **Use kill signals appropriately**: Default SIGTERM, then SIGKILL if needed

## Remember

- `time` adds negligible overhead - use it liberally
- `timeout` prevents resource waste from hung commands
- Always test timeout values in realistic conditions
- Document expected execution times in comments
