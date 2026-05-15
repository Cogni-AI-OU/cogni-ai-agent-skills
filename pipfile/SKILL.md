---
name: pipfile
description: Create, update, and manage Python project dependencies via Pipfile and Pipfile.lock using pipenv.
---
# pipfile

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Use this skill for managing Python project dependencies through `Pipfile` and `Pipfile.lock` utilizing the `pipenv` tool.

## Core Process

1. **Initialization**: Create a `Pipfile` if none exists by installing packages or using `pipenv install`.
2. **Adding Dependencies**: Use `pipenv install <package>` for production or `pipenv install --dev <package>` for development dependencies.
3. **Locking**: Run `pipenv lock` to deterministically pin dependencies into `Pipfile.lock`.
4. **Execution**: Use `pipenv run <command>` or `pipenv shell` to execute code within the isolated virtual environment.

## Core Principles

- **Deterministic Environments**: Rely on `Pipfile.lock` to guarantee exact versions and hashes. Never edit `Pipfile.lock` manually.
- **Group Separation**: Strictly separate production (`[packages]`) and development (`[dev-packages]`) dependencies.
- **TOML Compliance**: Manually editing the `Pipfile` is allowed but must adhere strictly to standard TOML syntax. Prefer CLI commands over manual edits when possible.
- **Security Check**: Utilize `Pipfile.lock`'s stored hashes to prevent supply-chain attacks.

## Commands / Usage Patterns

- **Install new dependency**: `pipenv install <package>`
- **Install dev dependency**: `pipenv install <package> --dev`
- **Install specific version**: `pipenv install "<package>==<version>"`
- **Generate lockfile**: `pipenv lock`
- **Install from lockfile**: `pipenv sync` (or `pipenv install --deploy` for CI/CD environments)
- **Uninstall a dependency**: `pipenv uninstall <package>`
- **Check for vulnerabilities**: `pipenv check`

## Diagnostics and Troubleshooting

- **Lock File Hash Mismatch**: If `Pipfile.lock out of date` error occurs, run `pipenv lock` to sync the lockfile with recent `Pipfile` changes.
- **Dependency Resolution Failures**: Clear cache with `pipenv lock --clear` or relax constraints inside the `Pipfile`.
- **BackendUnavailable on Editable Installs**: When having parallel install issues, set `PIP_NO_BUILD_ISOLATION=1`.

## What to Avoid

- **Manual Lockfile Edits**: NEVER manually edit `Pipfile.lock`. Always use `pipenv lock` to regenerate.
- **Using requirements.txt blindly**: Stop using `requirements.txt` directly; migrate via `pipenv install -r requirements.txt`.
- **Deploying without sync**: Do not use `pipenv update` or `pipenv lock` in CI/CD. Use `pipenv install --deploy` to enforce consistency.

## Limitations

- Editable installs in parallel can cause race conditions if build isolation is disabled.
- Generating a `Pipfile` automatically creates a virtual environment, which consumes disk space.

## Related Skills

- **python**:
  You MUST load this skill when dealing with Python code execution, debugging, or log processing.
- **robust-commands**:
  You MUST load this skill when executing complex commands requiring resilient error recovery.