---
name: github-topics
description: >-
  Search GitHub repositories by topics and keywords.
  You must load this skill when searching for relevant tools, libraries, or curated resources.
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


