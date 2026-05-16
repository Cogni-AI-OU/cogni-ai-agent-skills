---
name: pipfile
description: >-
  Create, update, and manage Python project dependencies via Pipfile and Pipfile.lock using pipenv.
  This skill MUST be loaded when creating/updating Pipfile or Pipfile.lock.
---
# pipfile

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Use this skill for managing Python project dependencies through `Pipfile` and `Pipfile.lock` utilizing the `pipenv` tool.

## Core Process

1. **Initialization**: Create a `Pipfile` if none exists by installing packages or using `pipenv install`.
   **Crucial**: Once a `Pipfile` is created, you MUST create a `README.md` in the project root detailing how to use the environment (e.g., `pipenv install`, `pipenv shell`).
2. **Adding Dependencies**: Use `pipenv install <package>` for production or `pipenv install --dev <package>` for development dependencies.
3. **Locking**: Run `pipenv lock` to deterministically pin dependencies into `Pipfile.lock`.
4. **Testing**: Execute tests within the environment using `pipenv run <test-command>` (e.g., `pipenv run pytest`).
5. **Execution**: Use `pipenv run <command>` or `pipenv shell` to execute code within the isolated virtual environment.

## Core Principles

- **Deterministic Environments**: Rely on `Pipfile.lock` to guarantee exact versions and hashes. Never edit `Pipfile.lock` manually.
- **Group Separation**: Strictly separate production (`[packages]`) and development (`[dev-packages]`) dependencies.
- **TOML Compliance**: Manually editing the `Pipfile` is allowed but must adhere strictly to standard TOML syntax. Prefer CLI commands over manual edits when possible.
- **Security-First**: Utilize `Pipfile.lock`'s stored hashes to prevent supply-chain attacks. Regularly run vulnerability scans.
- **CI/CD Invariance**: Use `--deploy` to ensure `Pipfile.lock` is up-to-date and fails if not. Use `--system` when running in Docker containers.

## Commands / Usage Patterns

- **Install new dependency**: `pipenv install <package>`
- **Install dev dependency**: `pipenv install <package> --dev`
- **Install specific version**: `pipenv install "<package>==<version>"`
- **Update a dependency**: `pipenv update <package>`
- **Generate lockfile**: `pipenv lock`
- **Install from lockfile**: `pipenv sync` (or `pipenv install --deploy` for CI/CD environments)
- **Uninstall a dependency**: `pipenv uninstall <package>`
- **Check for vulnerabilities**: `pipenv check` (Note: Treat this as one layer of security, not a complete supply-chain safeguard).
- **Generate SBOM**: `syft scan Pipfile.lock -o spdx-json > sbom.json` (Requires `syft` and `sbom` skill).

## Diagnostics and Troubleshooting

- **Lockfile Hash Mismatch**: If `Pipfile.lock out of date` error occurs, run `pipenv lock` to sync the lockfile with recent `Pipfile` changes.
- **Dependency Resolution Failures**: Clear cache with `pipenv lock --clear` or relax constraints inside the `Pipfile`.
- **BackendUnavailable on Editable Installs**: When having parallel install issues, set `PIP_NO_BUILD_ISOLATION=1`.

## What to Avoid

- **Manual Lockfile Edits**: NEVER manually edit `Pipfile.lock`. Always use `pipenv lock` to regenerate.
- **Using requirements.txt blindly**: Migrate via `pipenv install -r requirements.txt`. If the project requires `requirements.txt` for specific deployment or legacy tooling, keep them in sync instead of abandoning it completely.
- **Deploying without sync**: Do not use `pipenv update` or `pipenv lock` in CI/CD. Use `pipenv install --deploy` to enforce consistency.
- **Avoid Global Installs**: Do NOT use `pip install` outside the `pipenv` environment to avoid dependency drift and contamination.

## Limitations

- Editable installs in parallel can cause race conditions if build isolation is disabled.
- Generating a `Pipfile` automatically creates a virtual environment, which consumes disk space.

## Related Skills

- **python**:
  You MUST load this skill when dealing with Python code execution, debugging, or log processing.
