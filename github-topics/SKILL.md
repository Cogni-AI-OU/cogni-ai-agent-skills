---
name: github-topics
description: Search GitHub repositories by topics and keywords to find relevant tools, libraries, or curated resources.
---
# Skill: github-topics

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

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

## What to Avoid

- Avoid broad, unfiltered searches that return too many irrelevant results.
- Avoid relying on interactive web scraping when CLI tools are available.
