---
name: gh-aw-firewall-debug
description: 'Debug the AWF firewall by inspecting Docker containers, analyzing Squid access logs, checking iptables rules, and troubleshooting network issues.'
license: MIT
---

# AWF Firewall Debugging

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Debugging unexpected network blocks or access failures in AWF-protected commands.
- Inspecting Squid proxy logs to determine which domains are being allowed or blocked.
- Checking iptables rules to verify firewall enforcement in the Docker network.
- Troubleshooting DNS resolution failures within the AWF container environment.
- Analyzing AWF container state (running, exited, network config) after a failed execution.

## When Not to Use

- Setting up or configuring the AWF firewall for the first time — use `gh-aw-firewall` skill for initial setup and basic usage.
- Debugging application-level code issues unrelated to network connectivity.
- Diagnosing issues in non-AWF environments — this skill is specific to the AWF Docker-based firewall.
- Performance profiling or load testing — this skill focuses on connectivity debugging, not throughput analysis.

## Gotchas

- Logs inside normal AWF executions are moved after cleanup — always access archived logs via `/tmp/squid-logs-*/access.log` instead of relying on container inspection, which may find empty directories.
- Leaving debug containers running (`--keep-containers`) without cleanup leaves iptables rules and Docker networks active — always run manual cleanup (`docker rm -f awf-squid awf-agent && docker network rm awf-net`) after inspection.
- The `TCP_DENIED` status in Squid logs shows the Host header (3rd column), which may differ from the original requested domain — a subdomain may need explicit allowlisting even if the parent domain is allowed.
- iptables changes made outside the `FW_WRAPPER` lifecycle are not automatically cleaned up — avoid making persistent iptables modifications manually.

## Core Principles

- **Non-Interactive Debugging**: Rely on `docker exec` and `grep`/`awk` pipelines to extract logs and states.
- **Identify Access Blocks**: Quickly trace `TCP_DENIED` in Squid logs or `FW_BLOCKED` in dmesg.

## Commands / Usage Patterns

### Check Container Status

```bash
docker ps | grep awf
docker inspect awf-squid --format='{{.State.Running}}'
docker inspect awf-agent --format='{{.State.ExitCode}}'
```

### View and Analyze Logs

Squid proxy container (IP: `172.30.0.10`) & Agent execution container (IP: `172.30.0.20`).

```bash
docker exec awf-squid cat /var/log/squid/access.log
docker exec awf-squid grep "TCP_DENIED" /var/log/squid/access.log | awk '{print $3}' | sort -u
docker exec awf-squid tail -f /var/log/squid/access.log | grep --line-buffered TCP_DENIED
```

### Inspect iptables Rules

```bash
sudo iptables -t filter -L FW_WRAPPER -n -v
docker exec awf-agent iptables -t nat -L OUTPUT -n -v
sudo dmesg | grep "FW_BLOCKED"
```

### Network Inspection

```bash
docker network inspect awf-net
docker exec awf-agent nc -zv 172.30.0.10 3128
docker exec awf-agent cat /etc/resolv.conf
```

## Diagnostics and Troubleshooting

**Debug Mode Workflow:**
1. Run with debug logging and keep containers: `sudo awf --allow-domains github.com --log-level debug --keep-containers 'curl https://api.github.com'`
2. Inspect containers: `docker ps | grep awf`
3. Check iptables: `sudo iptables -t filter -L FW_WRAPPER -n`
4. Manual cleanup when done: `docker rm -f awf-squid awf-agent && docker network rm awf-net`

**Domain blocked unexpectedly:** Look at the Host header (3rd column) in `/var/log/squid/access.log` - it may need a subdomain allowlisted.

**DNS resolution failing:** Verify DNS allowed in iptables with `sudo dmesg | grep "FW_DNS"`.

## What to Avoid

- Avoid leaving debug containers running indefinitely. Always run cleanup (`docker rm -f awf-squid awf-agent && docker network rm awf-net`).
- Do not make persistent iptables changes outside of the `FW_WRAPPER` lifecycle.

## Limitations

- Logs inside normal executions are moved after cleanup and not accessible inside the container anymore. Access them via `/tmp/squid-logs-*/access.log` instead.

## Related Skills

- **robust-commands**: You MUST load this skill when executing commands requiring resilient error recovery or fallbacks.
- **shell**: You MUST load this skill when handling shell commands with performance monitoring or timeouts.
