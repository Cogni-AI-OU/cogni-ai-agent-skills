---
name: gh-search
description: >-
  GitHub CLI (`gh search`) operations for searching code, commits, issues,
  pull requests, and repositories with structured JSON output.
  You must load this skill when working with the `gh search` command.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# gh-search Skill

Use `gh search` to query GitHub for code, commits, issues, pull requests, and repositories.
Prefer structured JSON output over manual text parsing.

## Commands / Usage Patterns

- **Search Repositories**:
  `gh search repos "query" --limit 5 --json nameWithOwner,description,url`
  Example output:
  `[{"description":"RAG Framework...","nameWithOwner":"truefoundry/cognita","url":"..."}]`

- **Search Pull Requests**:
  `gh search prs --state=open --limit 5 --json number,title,repository`
  Example output:
  `[{"number":123,"repository":{"name":"repo"},"title":"Fix issue"}]`

- **Search Issues**:
  `gh search issues --state=open --label="bug" --limit 5 --json number,title,url`
  Example output:
  `[{"number":456,"title":"Bug description","url":"..."}]`

- **Search Code**:
  `gh search code "functionName" --extension="js" --json path,url`
  Example output:
  `[{"path":"src/index.js","url":"https://github.com/.../src/index.js"}]`

- **Search Commits**:
  `gh search commits "fix regex" --limit 5 --json sha,message,author`
  Example output:
  `[{"author":{"login":"user"},"message":"fix regex","sha":"abcdef"}]`

## Mindmap of Commands

```mermaid
mindmap
  root((gh search))
    code
      Search within code
    commits
      Search for commits
    issues
      Search for issues
    prs
      Search for pull requests
    repos
      Search for repositories
```

## Core Principles

- Use `--json` to request specific fields and output in structured JSON format. This avoids fragile parsing of tabular shell output.
- Always use `--limit` to bound the results, especially when searching across all of GitHub. Default limit is often 30, but explicit bounds ensure efficiency.
- When searching within a specific repository, use the `--repo="owner/repo"` flag to narrow the search scope.
- For complex data extraction, combine `--json` with `--jq` to filter results on the client side.

## Diagnostics and Troubleshooting

- If a search returns no results, try broadening the query or removing filters like `--extension` or `--label` to isolate the problem.
- Remember that code search has indexing delays; very recent changes might not appear immediately.

## What to Avoid

- Do not use `grep` or `awk` to parse the default tabular output of `gh search`. Always use `--json`.
- Avoid unbounded searches (without `--limit`) if you only need a few examples or the latest item.


