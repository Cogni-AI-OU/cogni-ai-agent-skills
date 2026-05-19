---
name: security-review
description: >-
  Lightweight security review focused on Pull Requests and incremental changes.
  Uses a diff-centric approach to ensure no new vulnerabilities are introduced.
  You MUST load this skill when reviewing code changes in a PR.
license: MIT
---

# Security Review Skill

This skill provides a focused, diff-centric approach to security reviews. Unlike a full security audit, a review focuses on identifying vulnerabilities introduced by specific changes (Pull Requests).

## When to Use

Use this skill when:

- Reviewing a Pull Request for security implications.
- Conducting a quick check on a specific diff or a few files.
- Responding to a `/security-review` command on a PR thread.
- You need to verify that new code follows secure coding practices.

## When Not to Use

- When asked to perform a deep, repository-wide scan (use `security-audit`).
- When performing architectural threat modeling from scratch.

## Review Mindset

- **Focus on the Diff**: Prioritize code added or modified in the current change set.
- **Regression Prevention**: Ensure no existing security controls are removed or weakened.
- **Incremental Risk**: Ask "What new attack surface does this change expose?"

## Review Workflow

1. **Analyze the Diff**: Read the changed files and identify new entry points or data sinks.
2. **Check for Low-Hanging Fruit**:
   - Hardcoded secrets in the diff.
   - New dependencies with known vulnerabilities.
   - Unsanitized user input in new endpoints.
3. **Verify Security Logic**: If the PR touches auth or crypto code, verify it against `security-audit` references.
4. **Provide Contextual Feedback**: Comment directly on the lines of code where issues are found.

## Output Format

For PR reviews, provide a concise summary of findings. Use the format defined in `references/report-format.md`.

## Related Skills

- **github-pr-review**
- **security-audit**
