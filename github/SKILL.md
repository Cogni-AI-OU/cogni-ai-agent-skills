---
name: github
description: >-
  Provides guidance on GitHub-specific features, pull requests viewing modes,
  and collaborative practices.
  You MUST load this skill when working with GitHub-specific features or PR view modes.
license: MIT
---

# GitHub Skill

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- A user has shared a GitHub PR URL and you need to retrieve the diff or patch content for analysis.
- You need to view a pull request or commit in plain text format (`.diff` or `.patch`) for programmatic processing or ingestion by AI tools.
- A user has shared a GitHub file link with line number annotations (`#L123` or `#L10-L20`) and you need to inspect the specific lines referenced.
- You need to understand how GitHub's diff/patch URL extensions work for scripting and automation.
- You need to explain GitHub-specific collaborative features, PR view modes, or review workflows to users.

## When Not to Use
- You need to create, merge, comment on, or manage PRs — use the **gh-pr** skill for CLI-based PR operations.
- You need to search for repositories, code, issues, or commits — use the **gh-search** skill for CLI-based search.
- You need to interact with the GitHub API programmatically for complex queries — use the **gh-api** skill.
- You need to manage issues — use the **gh-issue** skill.
- You are troubleshooting GitHub Actions workflow failures — use the **github-actions** or **gh-run** skills.

## Common Pitfalls
- The `.diff` and `.patch` URL formats return **raw text** — they are not interactive and do not include comments, review status, or CI check information; they contain only the code changes (`.diff`) or changes plus commit metadata (`.patch`).
- `.patch` output is formatted for `git am` consumption — it includes author, date, and commit message metadata that `.diff` omits; choose the format that matches your use case.
- GitHub file links with line numbers (e.g., `#L10-L20`) reference the **current version** of the file on the default branch — if the file has changed since the link was shared, the line numbers may no longer correspond to the relevant code.
- Rate limiting applies to `.diff`/`.patch` URL fetches just like any other GitHub API endpoint — if you are fetching many PRs in sequence, you may encounter HTTP 429 responses.

Guidance on interacting with GitHub features, specifically around Pull Requests and diff viewing.

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
