---
name: datadog-monitors
description: Guidelines for designing, debugging, and troubleshooting Datadog monitor queries, handling common false positives, and operational edge cases.
license: MIT
---

# Datadog Monitors

<!-- markdownlint-disable MD013 MD024 MD031 MD032 -->

Use this skill to design, debug, and troubleshoot Datadog monitor evaluation logic, query semantics, and alert state management.

## When to Use

- When writing Pulumi, Terraform, or API payloads to create or update Datadog monitors.
- To debug Datadog alerts that are stuck in a "ghost" or frozen state.
- When reducing noise and false positives in infrastructure and application monitoring.

## When Not to Use

- For installing the actual Datadog Agent on a host (use `datadog-agent` instead).
- When querying raw log or trace telemetry directly (use `datadog-api` or `datadog-mcp` instead).
- If the user simply wants a link to the Datadog UI without altering query definitions.

## Common Pitfalls

- **Missing Evaluation Timeouts**: Forgetting to set a `timeoutH` on multidimensional alerts, resulting in "ghost alerts" when a pod or host terminates unexpectedly.
- **Ignoring Loop Devices**: Failing to exclude `device_name:loop*` in disk monitors, causing a flood of false alerts for 100% full SquashFS mounts.
- **Scope Creep**: Grouping a monitor by too many high-cardinality tags, causing massive evaluation lag and delayed alerting.

## Common Query Issues & Operational Fixes

### 1. Frozen Multidimensional Alerts (Ghost Alerts)

**Problem**: Monitors grouping by transient dimensions (e.g., workloads, short-lived hosts, or distinct network domains) remain stuck in an `Alert` state forever after the underlying entity disappears or stops sending metrics.

**Why**: Datadog does not auto-resolve an alert group if no new data arrives to bring the metric back below the threshold.

**Solution**: Enable automatic resolution after a period of missing data using the `timeout` parameter (in Pulumi: `timeoutH`) to instruct the engine to drop the alert.
*Example*: `timeoutH: 1` auto-resolves if no data is seen for 1 hour.

### 2. Disk Usage / Forecast False Positives

**Problem**: Disk monitors trigger on system mounts that are intended to be 100% full, leading to significant alerting noise.

**Why**: Linux `loop` devices (used by snap packages) are read-only SquashFS mounts and inherently have no free space. Temporary mount points like `tmpfs` can also occasionally falsely trigger forecast horizons.

**Solution**: Filter these devices out directly in the monitor query tag scope.
*Example*: `avg:system.disk.in_use{!device_name:loop*,!device_name:tmpfs} by {host,device_name}`

### 3. Missing NPM / Specialized Event Permissions

**Problem**: When investigating Network Performance Monitoring (NPM) or specialized Formula/Event-based monitors via scripts or MCP, the Datadog API returns `Unauthorized` or empty datasets.

**Solution**: Application Keys need explicitly elevated scopes for these datasets. Cloud Network Monitoring requires scopes like `network_connections_read` and `network_health_insights_read`, while broader query evaluation relies on `timeseries_query` and `events_read`.

## Core Principles

- Always filter out known system noise explicitly in the query scope to prevent evaluation bloat.
- Understand the difference between `on_missing_data: default` (what to do during normal evaluation) and explicit timeframe timeouts (what to do when an alerting entity vanishes).
- When a monitor seems "stuck," inspect the specific tag groupings using the UI or the API (`group_states=all`) to understand exactly what tags are frozen.

## Related Skills

- **datadog-pulumi**: For mapping these monitor definition principles to Pulumi YAML.
- **datadog-api**: For raw API state extraction (e.g., checking group states directly to find ghost tags).
- **datadog-mcp**: For using Model Context Protocol to query underlying telemetry and build queries.
