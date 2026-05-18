---
name: datadog-agent
description: Use when installing, configuring, or updating Datadog Agent;
license: MIT
---

# Skill: datadog-agent

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Expert-level guidance for installing, configuring, and extending the Datadog Agent, including Ansible orchestration and custom OpenMetrics checks.

## When to Use

- When configuring, installing, or troubleshooting the Datadog Agent on a Linux host.
- To write custom Python check scripts (`AgentCheck` or `OpenMetricsBaseCheckV2`) for the agent.
- When updating Ansible playbooks that deploy the `datadog.dd.agent` role.

## When Not to Use

- For querying Datadog APIs to read telemetry or dashboard data (use `datadog-api` instead).
- When managing Datadog SaaS configurations like Monitors or SLOs (use `datadog-monitors`).
- If you are deploying Datadog strictly via a Helm chart in Kubernetes without needing custom host-level Python checks.

## Common Pitfalls

- **Subprocess Hangs**: Using Python's native `subprocess` module inside a custom check instead of `get_subprocess_output()`, which deadlocks the Agent's Go-runtime.
- **Misnamed Files**: Creating a custom check script named `my_check.py` but naming the configuration file `custom_check.yaml`, causing the Agent to silently ignore it.
- **Root Level Logs**: Defining `- type: file` at the root of a check's YAML configuration instead of properly nesting it under a `logs:` key.

## Core Principles

- **Agent Immutability**: Prefer immutable configuration deployments (e.g., Ansible) over manual modifications to `datadog.yaml` or `conf.d/`.
- **API Key Handling**: Never hardcode `datadog_api_key` in playbooks; utilize vault secrets or environment variables.
- **Python Compatibility**: Custom Agent checks must be Python 3 compatible for modern Agent versions (v7+).
- **File Matching**: The custom check script name (e.g., `my_check.py`) must exactly match its configuration file name (e.g., `my_check.yaml`).

## Ansible Integration & Logs Configuration

When using the `datadog.dd.agent` (or legacy `datadog.datadog`) Ansible role, ensure correct YAML hierarchy, especially for log collection.

- **Requirements**: Ansible v2.10+, `ansible-galaxy collection install datadog.dd`
- **Avoid Array Root**: Do not map a check directly to an array. A common mistake with logs is defining `- type: file` at the root check level.
- **Correct Logs Structure**: Logs must be encapsulated under a `logs:` key within the specific check dictionary.

```yaml
# Correct Ansible definition for logs attached to a custom/syslog check
datadog_checks:
  syslog: # Creates /etc/datadog-agent/conf.d/syslog.d/conf.yaml
    logs:
      - type: file
        path: /var/log/syslog
        service: syslog
        source: syslog
```

## Custom Agent Checks

Create custom Python checks by extending `AgentCheck` for simple metrics or `OpenMetricsBaseCheckV2` for Prometheus endpoints.

- **Directory Paths**:
  - Scripts: `/etc/datadog-agent/checks.d/`
  - Configs: `/etc/datadog-agent/conf.d/<CHECK_NAME>.d/conf.yaml`
- **Naming Convention**: Prefix custom checks with `custom_` (e.g., `custom_postfix.py`) to avoid conflicts with out-of-the-box integrations.
- **Check Verification**: `sudo -u dd-agent -- datadog-agent check <CHECK_NAME>`

### Simple Python Check

```python
from datadog_checks.base import AgentCheck

class CustomCheck(AgentCheck):
    def check(self, instance):
        self.gauge('custom.metric', 1, tags=instance.get('tags', []))
```

### OpenMetrics Base Check (V2)

Advanced scraping from Prometheus endpoints. Requires `openmetrics_endpoint` in the check config.

```python
from datadog_checks.base import OpenMetricsBaseCheckV2, ConfigurationError

class CustomOpenMetricsCheck(OpenMetricsBaseCheckV2):
    __NAMESPACE__ = "my_namespace"

    def __init__(self, name, init_config, instances):
        super(CustomOpenMetricsCheck, self).__init__(name, init_config, instances)
        self.metrics_map = {
            'prom_metric_name': 'datadog.metric.name',
        }

    def get_default_config(self):
        return {'metrics': self.metrics_map}

    def check(self, instance):
        endpoint = instance.get('openmetrics_endpoint')
        if not endpoint:
            raise ConfigurationError("Missing 'openmetrics_endpoint'")
        super().check(instance)
```

## Integrations & Developer Platform

- **Tiles & Dashboards**: Official integrations must include out-of-the-box dashboards and telemetry logic. API integrations require OAuth 2.0.
- **Platform Separation**: Agent-based integrations collect from local hosts, whereas API-based integrations ingest directly via Datadog REST endpoints.

## Diagnostics and Troubleshooting

- Check agent status: `datadog-agent status`
- **Subprocess execution**: Never use Python's native `subprocess` module due to the Agent's Go-runtime multithreading constraints. Always use `get_subprocess_output()` from `datadog_checks.base.utils.subprocess_output`.

```python
from datadog_checks.base.utils.subprocess_output import get_subprocess_output
out, err, retcode = get_subprocess_output(["ls", "."], self.log, raise_on_empty_output=True)
```
