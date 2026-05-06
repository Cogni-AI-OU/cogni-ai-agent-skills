---
name: awesome
description: Scan GitHub topics for awesome lists and extract relevant information for the current context based on a curated list of awesome software and resources.
---
# Skill: awesome

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Scan GitHub topics for awesome lists and extract relevant information for the current context from curated resources.

## Core Process

1. **Identify Awesome Lists**: Use `gh` to search for relevant repositories under the `awesome` topic matching the user's query context.
2. **Extract Resources**: Parse the README or curated lists from the identified repositories to extract software, tools, or resources.
3. **Filter and Format**: Filter the extracted items based on the current project's stack or user constraints and format them cleanly.

## Core Principles

- **Leverage CLI**: Prefer `gh api` or `gh search repos` to find awesome lists over web scraping when possible.
- **Contextual Filtering**: Do not dump the entire list; always filter for relevance to the current context.

## Commands / Usage Patterns

- Search for awesome lists by topic:
  ```bash
  gh search repos "awesome <topic>" --topic awesome --limit 5
  ```
- Fetch the README of an awesome list to extract links:
  ```bash
  gh api -H "Accept: application/vnd.github.v3.raw" repos/<owner>/<repo>/readme
  ```

## What to Avoid

- Avoid dumping unfiltered awesome lists.
- Avoid interactive prompts or web browsers requiring user input.
