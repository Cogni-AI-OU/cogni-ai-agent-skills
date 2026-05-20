# Run CLI Programmatically

**Goal**: Execute Copilot CLI prompts via scripts and automation without interactive sessions.

## Invariants

- Use `-p` or `--prompt` for non-interactive execution: `copilot -p "Explain this file: ./complex.ts"`.
- Piped input is supported: `echo "Explain this file: ./complex.ts" | copilot`.
- Piped input is ignored if `-p`/`--prompt` is also provided.
- Use `-s` (silent) to suppress session metadata and capture clean text output.
- Use `--no-ask-user` to prevent the agent from asking clarifying questions.
- Use `--model` for consistent behavior across environments.
- Use `--allow-tool=[TOOLS...]` and `--allow-url=[URLs...]` for minimal permissions.
- Avoid `--allow-all` outside sandbox environments.

## Tips

- **Precise prompts**: clear, unambiguous instructions produce better results.
- **Quote carefully**: use single quotes to avoid shell interpretation of special characters.
- **Minimal permissions**: grant only the tools/URLs necessary for the task.

## Programmatic Usage Examples

### Generate a commit message

```bash
copilot -p 'Write a commit message in plain text for the staged changes' -s \
  --allow-tool='shell(git:*)'
```

### Summarize a file

```bash
copilot -p 'Summarize what src/auth/login.ts does in no more than 100 words' -s
```

### Write tests for a module

```bash
copilot -p 'Write unit tests for src/utils/validators.ts' \
  --allow-tool='write, shell(npm:*), shell(npx:*)'
```

### Fix lint errors

```bash
copilot -p 'Fix all ESLint errors in this project' \
  --allow-tool='write, shell(npm:*), shell(npx:*), shell(git:*)'
```

### Explain a diff

```bash
copilot -p 'Explain the changes in the latest commit on this branch and flag any potential issues' -s
```

### Code review a branch

```bash
copilot -p '/review the changes on this branch compared to main. Focus on bugs and security issues.' \
  -s --allow-tool='shell(git:*)'
```

### Generate documentation

```bash
copilot -p 'Generate JSDoc comments for all exported functions in src/api/' \
  --allow-tool=write
```

### Export session to file

```bash
copilot -p "Audit this project's dependencies for vulnerabilities" \
  --allow-tool='shell(npm:*), shell(npx:*)' \
  --share='./audit-report.md'
```

### Export session to Gist

```bash
copilot -p 'Summarize the architecture of this project' --share-gist
```

> Gists are not available to EMUs or GHEC with data residency (\*.ghe.com).

## Shell Scripting Patterns

### Capture output in a variable

```bash
result=$(copilot -p 'What version of Node.js does this project require? \
  Give the number only. No other text.' -s)
echo "Required Node version: $result"
```

### Use in a conditional

```bash
if copilot -p 'Does this project have any TypeScript errors? Reply only YES or NO.' -s \
  | grep -qi "no"; then
  echo "No type errors found."
else
  echo "Type errors detected."
fi
```

### Process multiple files

```bash
for file in src/api/*.ts; do
  echo "--- Reviewing $file ---" | tee -a review-results.md
  copilot -p "Review $file for error handling issues" -s --allow-all-tools | tee -a review-results.md
done
```

## CI/CD Integration

```yaml
- name: Generate test coverage report
  env:
    COPILOT_GITHUB_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
  run: |
    copilot -p "Run the test suite and produce a coverage summary" \
      -s --allow-tool='shell(npm:*), write' --no-ask-user
```

## References

- [Running GitHub Copilot CLI programmatically](https://github.com/github/docs/blob/main/content/copilot/how-tos/copilot-cli/automate-copilot-cli/run-cli-programmatically.md)
