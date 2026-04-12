<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->
---
name: github
description: >-
  Provides guidance on GitHub specific features, pull requests viewing modes, and collaborative practices.
---
# GitHub Skill

Guidance on interacting with GitHub features, specifically around Pull Requests and diff viewing.

## When to Activate

- When working with GitHub Pull Requests, comparing branches, or needing to view diffs/patches.
- When needing to extract plain text diffs from GitHub PRs.

## Pull Request Plain Text View Modes

GitHub allows viewing pull requests and commits in plain text formats by simply appending an extension to the URL.
This is highly useful for extracting patches or diffs for local tooling, scripting, or AI agents.

There are two modes for viewing Pull Requests in plain text:

- **`.diff` mode:** Append `.diff` to the end of a PR or commit URL to view the standard git diff.
  - Example: `https://github.com/<owner>/<repo>/pull/<id>.diff`

- **`.patch` mode:** Append `.patch` to the end of a PR or commit URL to view it as a git patch,
  which includes commit metadata (author, date, commit message) formatted for `git am`.
  - Example: `https://github.com/<owner>/<repo>/pull/<id>.patch`

Use these formats when user sends a GitHub PR URL
and you need to retrieve the diff or patch content for processing.

### References

- [GitHub Docs: About comparing branches in pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-comparing-branches-in-pull-requests)
