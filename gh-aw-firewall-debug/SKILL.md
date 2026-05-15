---
name: gh-aw-firewall-debug
description: Debug the AWF firewall by inspecting Docker containers, analyzing Squid access logs, checking iptables rules, and troubleshooting network issues.
---

# AWF Firewall Debugging

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Use this skill when you need to debug the awf firewall, inspect container state, analyze traffic, or troubleshoot network issues.

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
