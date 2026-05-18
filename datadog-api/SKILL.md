---
name: datadog-api
description: Execute Datadog API requests to fetch live objects, metrics, or monitor statuses using cURL and API keys. You MUST load this skill when interacting with the Datadog API.
license: MIT
---
# Skill: datadog-api

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Execute Datadog API requests to fetch live objects, metrics, or monitor statuses.

## When to Use

- When querying Datadog metrics, logs, or traces directly from the command line in an automated script.
- To retrieve and analyze the status of Datadog monitors.
- When you need to fetch a dashboard configuration JSON to inspect or backup its definition.

## When Not to Use

- When full MCP observability tools (`datadog-mcp`) are available, as they natively format data for LLM context windows.
- If the project uses Pulumi or Terraform for Datadog resource creation (use the respective Infrastructure-as-Code skill).
- When a simple web UI link to the Datadog dashboard would suffice for a human user.

## Common Pitfalls

- **Paginating Endlessly**: Running an API query that returns millions of log lines without using `jq` to truncate or filter the output, causing the agent to run out of memory.
- **Leaking API Keys**: Accidentally echoing the `DD-API-KEY` or `DD-APPLICATION-KEY` in the terminal during debugging, exposing it in the workflow logs.
- **Incorrect Endpoint Region**: Sending requests to `datadoghq.com` when the organization's Datadog instance is actually hosted on `datadoghq.eu` or `us3.datadoghq.com`, resulting in HTTP 403 or 404 errors.

## Core Process

1. **Verify Credentials**: Ensure `DD-API-KEY` and `DD-APPLICATION-KEY` are available in the environment.
2. **Determine Datadog Site**: Default is `datadoghq.com`, but it could be `datadoghq.eu`, `us3.datadoghq.com`, etc. based on the target environment.
3. **Execute API Call**: Use `curl` to construct the API request, passing necessary headers and query parameters.
4. **Process Response**: Use tools like `jq` to parse and extract relevant data from the JSON response.

## Core Principles

- **Secure Headers**: Always pass keys via headers, never in the URL path.
- **Data Pruning**: Use `jq` or `python` to prune large JSON responses, especially when fetching dashboards or monitors.
- **Pagination**: Handle pagination when querying lists of items using `start` or `page` parameters.

## Commands / Usage Patterns

Fetch a specific Dashboard by ID:

```bash
curl -s -X GET "https://api.datadoghq.com/api/v1/dashboard/<dashboard_id>" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

Search for Monitors by tag or name:

```bash
curl -s -X GET "https://api.datadoghq.com/api/v1/monitor/search?query=tag:env:prod" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

Query Timeseries Metrics (Unix epoch timestamps):

```bash
curl -s -X GET "https://api.datadoghq.com/api/v1/query?query=system.cpu.idle{*}&from=$(date -d '1 hour ago' +%s)&to=$(date +%s)" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

Get a specific Monitor's details:

```bash
curl -s -X GET "https://api.datadoghq.com/api/v1/monitor/<monitor_id>" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

## References

- Datadog API Documentation: <https://docs.datadoghq.com/api/latest/>

## Diagnostics and Troubleshooting

- `403 Forbidden`: Check `DD-API-KEY` and `DD-APPLICATION-KEY` validity and ensure they match the correct Datadog site (`datadoghq.com` vs `datadoghq.eu`).
- `429 Too Many Requests`: Implement exponential backoff if hitting API rate limits.
- `404 Not Found`: Verify the ID or endpoint path.

## What to Avoid

- Avoid logging or exposing `DD-API-KEY` or `DD-APPLICATION-KEY` in clear text outputs.
- Do not fetch massive metric datasets without strict `from` and `to` bounds to avoid overloading the context window.

## Limitations

- The agent context window can be easily overwhelmed by full dashboard JSONs. Always filter the response with `jq` when possible.
- For retrieving telemetry (logs, metrics, traces, monitors), **always prefer optimized MCP-based tools** over raw API calls if available, as they are specifically designed to optimize data size for the agent's context window.

## Related Skills

- **datadog-agent**: Configure the Datadog Agent for metric and log collection.
