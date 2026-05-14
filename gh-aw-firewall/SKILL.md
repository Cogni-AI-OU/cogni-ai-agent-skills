---
name: gh-aw-firewall
description: Execute commands with network isolation and strict L7 HTTP/HTTPS domain whitelisting using the Agentic Workflow Firewall (AWF).
---

# gh-aw-firewall

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Execute commands with network isolation and strict L7 HTTP/HTTPS domain whitelisting using the Agentic Workflow Firewall (AWF). Use this when running AI agents or testing code that requires controlled, sandboxed network access.

## Core Process

1. **Identify Required Domains**: Determine the minimal set of domains needed for the workflow to function.
2. **Execute with Isolation**: Run the target command using `sudo awf --allow-domains <domains> -- <command>`.
3. **Analyze and Adjust**: Use `awf logs` or `awf logs stats` to identify blocked requests (TCP_DENIED) and adjust the allowed domains as necessary.

## Core Principles

- **Host-Level Enforcement**: Network isolation is applied to all container egress via iptables.
- **Default Chroot Access**: Transparent access to host binaries (Python, Node.js, Go) is enabled by default while retaining network isolation.
- **Subdomain Matching**: Allowing a root domain (e.g., `github.com`) automatically permits its subdomains (`api.github.com`).
- **Command Separation**: The `--` separator strictly isolates firewall configuration options from the executed command.

## Commands / Usage Patterns

```bash
# Basic isolation for an agent
sudo awf --allow-domains github.com,anthropic.com -- copilot --prompt "List my repositories"

# Pass specific environment variables and mount a volume
sudo awf --allow-domains api.github.com -e GITHUB_TOKEN="$GITHUB_TOKEN" -v /host/path:/container/path:ro -- npm test

# Playwright testing against localhost (auto-configures host access)
sudo awf --allow-domains localhost,playwright.dev -- npx playwright test

# SSL Bump for precise URL path filtering
sudo awf --allow-domains github.com --ssl-bump --allow-urls "https://github.com/myorg/*" -- curl https://github.com/myorg/repo
```

## Diagnostics and Troubleshooting

```bash
# Get summary statistics of allowed and blocked requests
awf logs stats

# Find specific blocked requests
awf logs --format json | jq 'select(.isAllowed == false)'

# Keep containers alive for deep inspection of a failing command
sudo awf --allow-domains github.com --keep-containers -- failing-command

# Inspect Squid and agent containers when kept alive
docker logs awf-squid
docker exec awf-agent iptables -t nat -L OUTPUT -n -v
```

## What to Avoid

- Avoid using `--env-all` to prevent leaking sensitive host environment variables; explicitly use `-e KEY=VALUE`.
- Do not rely on direct IP access (e.g., `curl http://1.2.3.4`); AWF routes traffic by domain name.
- Avoid using wildcard domains (`*`) unless absolutely required; prefer targeted wildcards (e.g., `*.github.com`).

## Limitations

- **No IPv6 / HTTP/3**: Only IPv4 and HTTP/1.1 or HTTP/2 are supported.
- **Direct IP Access Blocked**: Requests without an SNI or Host header domain are denied.
- **HTTP to HTTPS Redirects**: These may occasionally fail; it is safer to use HTTPS directly.

## Related Skills

- **debug-firewall**: Manual Docker debugging commands for AWF.
- **awf-debug-tools**: Python scripts for log parsing and diagnostics.
