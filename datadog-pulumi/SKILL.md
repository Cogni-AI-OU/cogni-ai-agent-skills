---
name: datadog-pulumi
description: >-
  Use when creating or debugging Datadog monitors in Pulumi YAML,
  especially for schema mismatches, monitor validation errors, and provider-specific field mapping.
license: MIT
---

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

# Datadog Pulumi

Use this skill to work with Datadog API examples using Pulumi.

## Core Process

1. Read the current `Pulumi.yaml` before editing; preserve recent user changes.
2. Convert API or Terraform examples into Pulumi field names, not raw JSON.
3. Run `pulumi preview --non-interactive` immediately after each monitor edit.
4. If preview output is large, extract only monitor validation and type errors.
5. Do not stop at schema errors; rewrite the monitor to the provider's actual type shape and rerun preview.

## Core Principles

- Keep threshold math consistent with the query comparator (e.g., query `> 0` requires `monitorThresholds.critical: 0`, not `1`).
- Treat Pulumi YAML as a typed schema, not a passthrough to Datadog's raw API.
- For advanced monitors, verify whether the provider expects `camelCase` names, wrapper objects, or different nesting than Terraform or API JSON.
- Preserve existing Pulumi resource IDs when only monitor content changes; renaming resource keys causes replacements.

## Commands / Usage Patterns

### Schema Discovery for YAML Format

Use this flow when working with new Datadog resource types:

1. Confirm provider version: `pulumi plugin ls`
2. Export schema for that version: `pulumi package get-schema datadog@<version> > /tmp/datadog-schema.json`
3. Inspect inputs via `jq` to determine exact Pulumi types (e.g., `datadog:index/MonitorVariables:MonitorVariables`).
4. Inspect widget unions and nested types when fields fail type-checking.
5. Map Datadog API JSON names to Pulumi schema names (e.g., `groupBy` to `groupBies`) and rerun preview.

## Known Datadog Pulumi Patterns

- Log alerts grouped per host can use Datadog template variables in monitor text, but the query itself must group by host explicitly.
- Service checks often need `notifyNoData`, `noDataTimeframe`, and status thresholds aligned with the service-check query shape.
- Formula/event-platform monitors may require wrapper fields under `variables` (e.g., use `variables.eventQueries`, not a raw list of query objects).
- Some schema names are intentionally awkward in this provider version (e.g., event query grouping uses `groupBies`, not `groupBy`).
- For formula/event-query monitors, avoid empty search strings. Use `search.query: '*'` instead of an empty string, because preview may pass while `pulumi up` can crash the Datadog provider during create.

## Diagnostics and Troubleshooting

- **`400 Bad Request`**: From `/api/v1/monitor/validate` usually means monitor logic, thresholds, or query syntax is wrong.
- **`is not assignable`**: From Pulumi usually means the YAML shape does not match the provider schema (e.g., mismatch between API JSON and YAML format); check `get-schema` before guessing.
- **Provider Panic**: During `Create` after a clean preview usually means a provider bug or an edge-case payload. Minimize optional fields first, then compare against the provider's monitor schema and upstream Terraform docs.
- **Auth Failure**: If provider auth fails before monitor creation, inspect stack config and env credentials separately before changing monitor code.

## What to Avoid

- Assuming Datadog API JSON keys map 1:1 to Pulumi YAML.
- Stopping at the first validation error; rewrite to the provider's actual shape and retry.
- Guessing schema structures without running `pulumi package get-schema datadog@<version>`.

## Limitations

- Some complex widgets and nested variables in Datadog API might have poorly mapped Pulumi YAML unions, requiring careful extraction of schemas via `jq`.

## Related Skills

- **datadog-api**: Useful for fetching existing monitor JSON definitions via API to compare against Pulumi schema mapping.
- **datadog-mcp**: Query existing observability data to help design and validate monitor thresholds.
- **datadog-agent**: Datadog Agent configuration and custom checks.
