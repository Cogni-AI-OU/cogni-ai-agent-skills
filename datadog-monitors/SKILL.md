---
name: datadog-monitors
license: MIT
description: Guidelines for designing, debugging, and troubleshooting Datadog monitor queries, handling common false positives, and operational edge cases.
license: MIT
---

# Datadog Monitors

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- Designing new Datadog monitors with correct query syntax, thresholds, and alert conditions
- Debugging frozen or ghost alerts where alert groups remain stuck in Alert state after entities disappear
- Troubleshooting false positives from disk usage, forecast, or system-level monitors
- Configuring `timeout` parameters for auto-resolving alerts on transient dimensions
- Investigating missing data, permission errors, or unexpected evaluation behavior in existing monitors

## When Not to Use
- Creating or managing Datadog dashboards, SLOs, or synthetics — this skill is scoped to monitors only
- Configuring the Datadog Agent or custom checks — use `datadog-agent` instead
- Querying raw telemetry data to build monitor queries from scratch — use `datadog-mcp` for exploration first

## Common Pitfalls
- Monitors grouping by transient dimensions (short-lived hosts, workloads) will NOT auto-resolve when the entity stops sending data unless `timeoutH` is explicitly configured
- Linux loop devices (Snap packages) and tmpfs mounts will trigger disk usage alerts if not excluded via `!device_name:loop*` and `!device_name:tmpfs`
- The `on_missing_data` setting controls behavior during normal evaluation windows, while `timeoutH` controls what happens when an alerting entity vanishes entirely — they serve different purposes
- NPM and advanced event permissions require explicitly scoped Application Keys (`network_connections_read`, `timeseries_query`) — missing scopes cause silent API authorization failures

Use this skill to design, debug, and troubleshoot Datadog monitor evaluation logic, query semantics, and alert state management.

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
