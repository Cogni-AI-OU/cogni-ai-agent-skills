# github-script

This skill provides advanced examples and best practices for using `actions/github-script` in GitHub Actions to interact with the GitHub API.

## Core Concepts

`actions/github-script` allows you to write JavaScript within your workflow to interact directly with the GitHub API via an authenticated `octokit` client.

- **`github`**: A pre-authenticated `octokit/rest.js` client.
- **`context`**: An object containing the workflow run context.
- **`core`**: A reference to `@actions/core`.
- **`glob`**: A reference to `@actions/glob`.
- **`io`**: A reference to `@actions/io`.
- **`exec`**: A reference to `@actions/exec`.
- **`getOctokit`**: A factory function to create additional clients with different tokens.

## Common Use Cases

### 1. Comment on an Issue

```yaml
on:
  issues:
    types: [opened]

jobs:
  comment:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '👋 Thanks for reporting!'
            })
```

### 2. Apply a Label to an Issue

```yaml
on:
  issues:
    types: [opened]

jobs:
  apply-label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.addLabels({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              labels: ['Triage']
            })
```

### 3. Create or Update File Contents (Poller Example)

Useful when polling repositories and updating a `README.md` periodically.

```yaml
on:
  workflow_dispatch:
  schedule:
    - cron: "0 12 * * *"
jobs:
  poll:
    runs-on: ubuntu-latest
    steps:
      - name: Fetch all
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.ORG_PAT }}
          script: |
            const repos = await github.paginate(github.rest.search.repos, {
              q: "<query string>",
            })

            let newReadme = `
            <updating the README>
            `
            const existingReadme = await github.rest.repos.getContent({
              owner: context.repo.owner,
              repo: "<repo>",
              path: "README.md",
            })

            await github.rest.repos.createOrUpdateFileContents({
              owner: context.repo.owner,
              repo: "<repo>",
              path: "README.md",
              message: "Update README",
              content: btoa(newReadme),
              sha: existingReadme.data.sha,
            })
```

### 4. Welcome a First-Time Contributor

```yaml
on: pull_request_target

jobs:
  welcome:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v9
        with:
          script: |
            const creator = context.payload.sender.login
            const opts = github.rest.issues.listForRepo.endpoint.merge({
              ...context.issue,
              creator,
              state: 'all'
            })
            const issues = await github.paginate(opts)
            for (const issue of issues) {
              if (issue.number === context.issue.number) {
                continue
              }
              if (issue.pull_request) {
                return // Creator is already a contributor.
              }
            }
            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `**Welcome**, new contributor!
                Please make sure you've read our [contributing guide](CONTRIBUTING.md) and we look forward to reviewing your Pull request shortly ✨`
            })
```

### 5. Executing Commands Cross-Platform

Use the `@actions/exec` package directly inside your script:

```yaml
on: push

jobs:
  use-exec:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/github-script@v9
        with:
          script: |
            const {
              exitCode,
              stdout,
              stderr
            } = await exec.getExecOutput('echo', ['hello']);
            console.log(exitCode, stdout, stderr)
```

## Security Best Practices

1. **Avoid Script Injections**: Do NOT evaluate expressions directly in the `script`. Pass them as environment variables.
   ```yaml
   # BAD: vulnerable to script injection
   script: console.log('${{ github.event.pull_request.title }}')
   
   # GOOD: pass via env
   env:
     TITLE: ${{ github.event.pull_request.title }}
   script: console.log(process.env.TITLE)
   ```
2. **Require Authentication for External Repo Access**: The default `GITHUB_TOKEN` is scoped only to the current repository. To access other repos, configure a PAT and pass it to `github-token`.
