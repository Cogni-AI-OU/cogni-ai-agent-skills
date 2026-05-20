---
name: github-docs
description: 'Reference and APIs for retrieving GitHub documentation, page lists, and article content programmatically for LLMs. You MUST load this skill when asked to search or retrieve GitHub documentation.'
license: MIT
---

# github-docs

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- **Documentation Search**: Locating specific GitHub documentation articles via search queries.
- **Article Retrieval**: Fetching the full rendered markdown of a specific GitHub docs page.
- **Documentation Browsing**: Programmatically listing available pages, languages, or versions of GitHub docs.

## When Not to Use

- **GitHub API/Operations**: Interacting with live repositories, issues, or PRs. Use `gh`, `gh-api`, or the `github-mcp-server` directly for operational data.
- **REST/GraphQL Endpoint Usage**: Executing REST/GraphQL queries for repo data, unless looking up the *documentation* of how those APIs work.

## Core Process

1. **Identify the Need**: Determine whether you need to search for a topic or fetch a specific known documentation path.
2. **Select the Endpoint**: Use the appropriate API based on the context.
   - For searching: `/api/search/v1`
   - For listing available pages: `/api/pagelist/{language}/{version}`
   - For retrieving full markdown: `/api/article/body`
3. **Execute the Query**: Use `webfetch` or `curl` to fetch the data. The documentation APIs return structured JSON or markdown, which are optimized for LLM consumption.
4. **Process Content**: Extract the relevant information to answer the user's query or inform the ongoing task.

## APIs & Usage

All endpoints are hosted at `https://docs.github.com/`. Use `webfetch` or `curl` to access them.

- **Versions API**: Lists all available documentation versions.
  `curl "https://docs.github.com/api/pagelist/versions"`
- **Languages API**: Lists all available languages.
  `curl "https://docs.github.com/api/pagelist/languages"`
- **Page List API**: Returns every docs page path for a given language and version.
  `curl "https://docs.github.com/api/pagelist/en/free-pro-team@latest"`
- **Article API**: Returns the full rendered content and context of any docs page as JSON.
  `curl "https://docs.github.com/api/article?pathname=/en/get-started/start-your-journey/about-github-and-git"`
- **Article Body API**: Returns the full rendered content of any docs page as markdown (preferred for context loading).
  `curl "https://docs.github.com/api/article/body?pathname=/en/get-started/start-your-journey/about-github-and-git"`
- **Search API**: Search across all docs content.
  `curl "https://docs.github.com/api/search/v1?query=actions&language=en&version=free-pro-team@latest"`

## Core Principles

- **Prefer Markdown Extraction**: When reading articles for context, use the `/api/article/body` endpoint rather than `/api/article`, as the body endpoint directly returns markdown which minimizes token usage and avoids JSON unwrapping.
- **Always Specify Language and Version**: When using the Page List or Search APIs, specify `language=en` and `version=free-pro-team@latest` (or the relevant enterprise version) to ensure accurate results.

## Common Pitfalls

- **Confusing Docs API with GitHub API**: The `docs.github.com/api/` endpoints are exclusively for retrieving documentation content, not for operating on GitHub resources (which use `api.github.com`).
- **Missing Pathname Parameter**: The Article and Article Body APIs require the `pathname` query parameter to be URL-encoded if it contains special characters, though typically paths start with `/en/`.
- **Search vs. MCP Tools**: The GitHub MCP server (`github-mcp-server`) provides operational tools but *does not* include docs search. You must use the REST `Search API` listed here to find documentation.

## References

- <https://docs.github.com/llms.txt> - The official GitHub documentation curated for LLMs.
- <https://github.com/llms.txt> - Curated links for GitHub-related projects and resources.

## Related Skills

- **gh**:
  You MUST load this skill when interacting with the GitHub CLI for operational tasks (as opposed to docs retrieval).
- **gh-api**:
  You MUST load this skill when interacting with the main GitHub API (`api.github.com`).
