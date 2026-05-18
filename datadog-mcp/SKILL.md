---
name: datadog-mcp
description: Query observability data via Datadog MCP, selecting minimal toolsets to optimize context window and scope.
license: MIT
---

# Datadog MCP

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Query Datadog telemetry (logs, metrics, traces, monitors, incidents, services, notebooks) directly via MCP to preserve agent context window and avoid context switching.

## Core Process

1. **Identify Required Data**: Determine the specific observability telemetry needed (e.g., traces vs. monitors).
2. **Select Minimal Toolset**: Choose the narrowest toolset that provides the required data.
3. **Execute Queries**: Use targeted MCP tool calls to retrieve data.
4. **Synthesize Findings**: Analyze the telemetry within the current context.

## Core Principles

- **Context Optimization**: Aggressively minimize toolset surface area. Prefer specialized toolsets over the `core` toolset whenever possible.
- **MCP Exclusivity**: Exclusively use MCP tools for telemetry. Never attempt SSH access to hosts or request UI navigation.

## Commands / Usage Patterns

Load the appropriate toolset based on the task:

- `core`: Broad access (logs, metrics, traces, dashboards, monitors, incidents, hosts, services, events, notebooks). Use only when multiple domains are needed simultaneously.
- `alerting`: Monitor validation, monitor group search, monitor templates.
- `apm`: Advanced trace analysis, span search, Watchdog insights, performance investigation.
- `cases`: Case Management workflows (create/search/update, Jira linking).
- `dbm`: Database Monitoring queries and investigations.
- `ddsql`: Preview DDSQL tools for logs, metrics, RUM, spans, and infrastructure data.
- `error-tracking`: Error Tracking issue search and retrieval.
- `feature-flags`: Feature flag listing, creation, updates, and environment configuration.
- `llmobs`: LLM Observability spans and experiment analysis.
- `product-analytics`: Product Analytics query tooling.
- `networks`: Cloud Network Monitoring and Network Device Monitoring analysis.
- `security`: Security scans, security signals, and security findings analysis.
- `software-delivery`: CI Visibility and Test Optimization analysis.
- `synthetics`: Synthetics test retrieval and updates.
- `workflows`: Workflow Automation listing, inspection, execution, and trigger updates.

## Access Control

### Application Key Scopes

Application Key Scopes restrict what applications can access in your Datadog data
without granting new capabilities - they simply limit the scope of existing permissions.

If you require additional scopes to complete the task,
check the full list of scopes (Datadog Role Permissions) and report to the user.

## Reference

- Datadog for VSCode: [GitHub repository](https://github.com/DataDog/datadog-for-vscode)
- Datadog MCP Server Toolsets: [Datadog docs](https://docs.datadoghq.com/bits_ai/mcp_server/#toolsets)
- [Datadog Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions/#permissions-list)

## What to Avoid

- Loading the `core` toolset by default when a narrow toolset (e.g., `apm` or `alerting`) is sufficient.
- Reverting to manual Datadog UI navigation, SSH access, or raw `curl` requests (`datadog-api`) for standard telemetry retrieval when the MCP server is available.

## Limitations

- Query depth and visibility are constrained by the active Datadog role and the implemented MCP server capabilities.

## Related Skills

- **datadog-agent**: Use when installing, configuring, or updating Datadog Agent.
- **datadog-api**: Execute raw Datadog API requests. Fallback when MCP lacks a specific capability or for administrative actions.
