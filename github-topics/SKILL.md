---
name: github-topics
license: MIT
description: >-
  Search GitHub repositories by topics and keywords.
  You MUST load this skill when searching for relevant tools, libraries, or curated resources.
license: MIT
---
# Skill: github-topics

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- You need to find curated "awesome" lists for a specific technology or domain (e.g., "awesome python", "awesome machine learning").
- You need to discover high-quality libraries, tools, or frameworks for a given programming language or task.
- Searching for reference implementations, starter templates, or example projects for a given topic.
- The user asks "find me a library that does X" or "what are the best tools for Y?"
- You need to evaluate repository quality by fetching README content and metadata for comparison.

## When Not to Use
- The user needs specific code search within a known repository — use `gh search code` with the `gh-api` skill instead.
- The user is asking for documentation on a known tool or library — a direct web search or URL fetch is more efficient.
- The user needs to search issues, pull requests, or discussions — topic search is for repositories only; use `gh search` subcommands for other content types.
- The user already knows the exact repository name — no need for topic search; go directly to the repository.

## Common Pitfalls
- Broad searches without topic filters return too many irrelevant results — always combine keyword searches with `--topic` filters for precision (e.g., `gh search repos "ansible" --topic python`).
- GitHub's search index may be stale — recently created or updated repositories may not appear in search results immediately.
- The `--limit` flag caps results but doesn't guarantee quality — the first page of results is ordered by relevance, but you should still fetch READMEs to evaluate actual suitability.
- Topic tags are user-assigned and may be inaccurate or missing — a repository without the topic tag you search for won't appear, even if it's a perfect fit.

Search GitHub repositories using topics and keywords to discover relevant software and resources.

## Core Process

1. **Identify Repositories**: Use `gh search repos` to find repositories matching specific topics or keywords.
2. **Extract Resources**: Fetch README content or API data to understand the repository's purpose and contents.
3. **Filter and Format**: Select the most relevant repositories or tools based on the current project's stack or user constraints.

## Core Principles

- **Leverage CLI**: Use the GitHub CLI (`gh`) for efficient searching and data retrieval.
- **Topic Precision**: Combine keyword searches with `--topic` filters to narrow down results.
- **Contextual Filtering**: Always filter results for relevance to the current task or environment.

## Commands / Usage Patterns

- Search for curated "awesome" lists by topic:
  ```bash
  gh search repos "awesome python" --topic awesome --limit 10
  ```
- Search for specific tools within a topic:
  ```bash
  gh search repos "ansible" --topic python --limit 10
  ```
- Fetch the README of a repository to extract more details:
  ```bash
  gh api -H "Accept: application/vnd.github.v3.raw" repos/<owner>/<repo>/readme
  ```

## Featured Topics

Use these popular GitHub topics to find high-quality resources and projects:

- **awesome**: Curated lists of awesome things.
- **chrome**: Projects related to the Chrome browser.
- **code-quality**: Tools for style, quality, security, and test-coverage.
- **compiler**: Software for translating programming languages.
- **css**: Cascading Style Sheets projects and libraries.
- **database**: Structured sets of data and database management systems.
- **frontend**: User interface programming and layout.
- **javascript**: Projects using the JavaScript programming language.
- **nodejs**: JavaScript runtime environments and tools.
- **npm**: Package management for JavaScript.
- **project-management**: Tools for scope and goal execution.
- **python**: Projects using the Python programming language.
- **react**: JavaScript libraries for designing user interfaces.
- **react-native**: Mobile frameworks for iOS and Android.
- **scala**: Projects using the Scala programming language.
- **typescript**: Typed supersets of JavaScript.

## What to Avoid

- Avoid broad, unfiltered searches that return too many irrelevant results.
- Avoid relying on interactive web scraping when CLI tools are available.
