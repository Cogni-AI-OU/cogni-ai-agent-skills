# PR Review Prompt

Review this pull request:

- Check for code quality issues
- In case the latest CI build fails, identify the main cause of failure.
- Look for potential bugs, logic errors, or incorrect behavior
- Missing error handling
- Performance issues with measurable impact
- Security vulnerabilities

Guidelines:

- Be concise. Only comment on high-value issues, not style preferences.
- Skip praise, summaries, and obvious observations.
- If no significant issues exist, state that briefly.
- Reference AGENTS.md if present for project conventions.
- For simple fixes, provide committable suggestions using a fenced code block
  with the language identifier `suggestion`.
- Use the gh cli to create comments on the files for the violations.
- Generally, write a comment instead of writing suggested change if you can help it.
- For inline comments, start with summarizing the issue in one line, include defect classification,
  then provide details.

Command MUST be like this and use values from `<repo>`, `<pr-number>`, and `<pr-sha>`:

```bash
gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  /repos/<repo>/pulls/<pr-number>/comments \
  -f 'body=[summary of issue]' \
  -f 'commit_id=<pr-sha>' \
  -f 'path=[path-to-file]' \
  -f 'side=RIGHT' \
  -F "line=[line]"
```
