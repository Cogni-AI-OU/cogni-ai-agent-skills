---
name: codeql
description: 'Configure and execute CodeQL code scanning analysis via GitHub Actions workflows and the CodeQL CLI.'
license: MIT
---

# Skill: codeql

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- Configuring or troubleshooting CodeQL code scanning in GitHub Actions workflows
- Setting up advanced CodeQL analysis with custom build modes for compiled languages
- Diagnosing CodeQL workflow failures such as autobuild issues, permission errors, or SARIF upload failures
- Running standalone CodeQL CLI commands for local code analysis and database creation
- Enabling `security-extended` or `security-and-quality` query suites for comprehensive vulnerability detection

## When Not to Use
- Replacing dedicated SAST tools already configured and producing reliable results — avoid duplicate scanning pipelines
- Performing general-purpose code quality linting or style checks — CodeQL targets security and correctness vulnerabilities only
- Debugging application runtime behavior or performance issues — use APM and logging tools instead

## Gotchas
- Autobuild often fails for compiled languages with complex build systems; switch to `build-mode: manual` and provide explicit build commands
- SARIF files exceeding 10 MB will fail to upload — split across categories or reduce query scope
- Running two CodeQL workflows simultaneously (default setup + advanced) causes conflicts — disable one
- The `dependency-caching: true` flag on the `init` action is essential to avoid cache misses every run
- Kotlin analysis in no-build mode may require disabling and re-enabling default setup to switch to `autobuild`

This skill provides procedural guidance for configuring and running CodeQL code scanning — both through GitHub Actions workflows and the standalone CodeQL CLI.

## Core Process

1. **Choose Setup Type**: Select between Default setup or Advanced setup (`.github/workflows/codeql.yml`).
2. **Configure Triggers**: Define `push`, `pull_request`, `schedule`, or `merge_group` workflow triggers.
3. **Set Permissions**: Ensure `security-events: write` and `contents: read` permissions.
4. **Configure Language Matrix**: Specify languages (e.g., `c-cpp`, `javascript-typescript`, `python`).
5. **Initialize CodeQL**: Use `github/codeql-action/init@v4` specifying `build-mode` (`none`, `autobuild`, `manual`).
6. **Build (if needed)**: Provide explicit manual build steps for compiled languages lacking autobuild support.
7. **Analyze**: Use `github/codeql-action/analyze@v4` to perform analysis and upload SARIF results.

## Quick Start (Advanced Setup)

```yaml
name: "CodeQL Advanced"
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
jobs:
  analyze:
    name: Analyze (${{ matrix.language }})
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      contents: read
    strategy:
      fail-fast: false
      matrix:
        include:
          - language: javascript-typescript
            build-mode: none
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v4
      with:
        languages: ${{ matrix.language }}
        build-mode: ${{ matrix.build-mode }}
        queries: security-extended
        dependency-caching: true
    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v4
```

## Commands / Usage Patterns (CodeQL CLI)

- **Create Database**: `codeql database create codeql-db --language=javascript-typescript --source-root=src`
- **Create DB with Build Command**: `codeql database create codeql-db --language=c-cpp --command="make build"`
- **Analyze Database**: `codeql database analyze codeql-db javascript-code-scanning.qls --format=sarif-latest --output=results.sarif`
- **Upload Results**: `codeql github upload-results --repository=owner/repo --ref=refs/heads/main --commit=<commit-sha> --sarif=results.sarif`

## Diagnostics and Troubleshooting

- **Autobuild failure**: Switch `build-mode` to `manual` and add explicit build commands.
- **Out of disk/memory**: Use larger runners, reduce scope via `paths` config, or use `build-mode: none`.
- **Resource not accessible**: Verify `security-events: write` permission is granted.
- **SARIF upload fails**: Check if SARIF file exceeds 10 MB limit; ensure `GITHUB_TOKEN` is valid.

| Problem | Solution |
|---|---|
| Workflow not triggering | Verify `on:` triggers match event; check `paths`/`branches` filters; ensure workflow exists on target branch |
| `Resource not accessible` error | Add `security-events: write` and `contents: read` permissions |
| Autobuild failure | Switch to `build-mode: manual` and add explicit build commands |
| No source code seen | Verify `--source-root`, build command, and language identifier |
| C# compiler failure | Check for `/p:EmitCompilerGeneratedFiles=true` conflicts with `.sqlproj` or legacy projects |
| Fewer lines scanned than expected | Switch from `none` to `autobuild`/`manual`; verify build compiles all source |
| Kotlin in no-build mode | Disable and re-enable default setup to switch to `autobuild` |
| Cache miss every run | Verify `dependency-caching: true` on `init` action |
| Out of disk/memory | Use larger runners; reduce analysis scope via `paths` config; use `build-mode: none` |
| SARIF upload fails | Ensure token has `security-events: write`; check 10 MB file size limit |
| SARIF results exceed limits | Split across multiple uploads with different `--sarif-category`; reduce query scope |
| Two CodeQL workflows | Disable default setup if using advanced setup, or remove old workflow file |
| Slow analysis | Enable dependency caching; use `--threads=0`; reduce query suite scope |

## Best Practices

- Use `security-extended` or `security-and-quality` for comprehensive vulnerability coverage.
- Set `dependency-caching: true` on the `init` action to optimize run times.
- For monorepos, use the `category` parameter in the `analyze` step to separate component results.
- Pin GitHub actions to specific major versions (e.g., `@v4`) or commit SHAs for better security.

## What to Avoid

- Avoid using the standalone CodeQL CLI download; always use the CodeQL bundle which includes precompiled queries.
- Avoid using `autobuild` for complex compiled language setups where a custom build is required.

## References

- <https://github.com/github/awesome-copilot/blob/main/skills/codeql/SKILL.md>
