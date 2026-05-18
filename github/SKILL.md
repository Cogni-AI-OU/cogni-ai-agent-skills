---
name: github
description: >-
  Provides guidance on GitHub-specific features, pull requests viewing modes,
  and collaborative practices.
  You MUST load this skill when working with GitHub-specific features or PR view modes.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->
# GitHub Skill

Guidance on interacting with GitHub features, specifically around Pull Requests and diff viewing.

## When to Use

- When working with GitHub Pull Requests, comparing branches, or needing to view diffs/patches.
- When needing to extract plain text diffs from GitHub PRs.

## When Not to Use

- For scripting bulk issue creation or complex repository management (use the `gh` CLI or `gh-api` skills instead).
- When resolving Git merge conflicts directly in the local repository (use `git` or `git-expert`).
- If you need deep code-level semantic analysis that a raw `.patch` or `.diff` format doesn't provide.

## Common Pitfalls

- **Ignoring Context**: Looking only at the few lines of a `.diff` file and missing the broader architectural implications of a Pull Request.
- **Scraping HTML**: Attempting to curl and scrape the standard GitHub web UI instead of using the `.diff`/`.patch` extensions or the GitHub API.
- **Misinterpreting Line Numbers**: Taking a user's `#L123` link out of context, failing to realize the code has shifted significantly since the permalink was generated.

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

## GitHub File Links

- **Line Numbers (`#L<number>`)**: When a user provides a link to a file on GitHub that includes a line number reference (e.g., `#L123` or `#L10-L20`), always check the specified line(s) to determine whether it is relevant to the current context or task.

### References

- [GitHub Docs: About comparing branches in pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-comparing-branches-in-pull-requests)

## Related Skills

- **gh-pr**:
  You MUST load this skill when working with the `gh pr` command.
- **github-topics**:
  You MUST load this skill when searching for relevant tools, libraries, or curated resources.
