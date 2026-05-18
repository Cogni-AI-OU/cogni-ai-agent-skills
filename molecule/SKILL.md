---
name: molecule
description: >-
  How to run and manage Molecule tests for Ansible roles and playbooks.
  You MUST load this skill when running or managing Molecule tests for Ansible.
license: MIT
---

# Molecule Testing

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- When running Molecule tests to validate Ansible roles and playbooks across multiple scenarios.
- When debugging a failing `molecule test` by breaking it into individual steps (`create`, `converge`, `destroy`).
- When setting up Molecule testing inside a devcontainer or GitHub Codespace for local Ansible development.

## When Not to Use

- When testing can be done via lightweight syntax checks (`ansible-playbook --syntax-check`) without full container provisioning — Molecule is heavy and should be reserved for integration tests.
- When running outside a controlled environment without Docker or Podman — Molecule requires a container runtime for most drivers.
- When the Ansible role is not idempotent by design — Molecule tests will highlight this, but the role should be fixed first.

## Common Pitfalls
- `molecule test` runs the entire lifecycle and may hang indefinitely on slow operations — always use `timeout 600s` when automating Molecule commands.
- Ansible may use a different Python interpreter (e.g., pipx-managed) than the one where Python modules are installed — check `ansible --version` and install libraries in the correct environment.
- Broken conditional handling in upstream plugins may require `ANSIBLE_ALLOW_BROKEN_CONDITIONALS=1` to proceed — only use as a temporary workaround.
- When running inside a devcontainer, do NOT create separate Python virtual environments — use the container's existing Python environment and update `.devcontainer/requirements.txt` instead.

## Commands

```bash
# Run Molecule tests
molecule test

# Syntax check
molecule syntax
```

## Devcontainer Guidance

When running Molecule inside GitHub Codespaces or a repository's VS Code devcontainer:

- Treat the repository devcontainer as the default controller environment for local development and testing.
- Keep controller dependency installation in the devcontainer configuration so Molecule scenarios can assume those tools
are already available.
- Do not install controller-side Python dependencies during Molecule runs when the agent is already operating inside
Codespaces or the repo devcontainer.
- Do not create additional Python virtual environments such as `.venv` or `venv`; use the existing container Python
environment, which should already provide the required dependencies.
- If dependencies are missing in a Codespace or devcontainer, update `.devcontainer/requirements.txt` or
`.devcontainer/devcontainer.json` instead of introducing a per-run Molecule install step or a separate virtual
environment.

## Troubleshooting

### Molecule Testing issues

If you encounter problems or hangs during `molecule test`:

- Run molecule using separate commands (e.g., `molecule create`, `molecule converge`, `molecule destroy`)
  to isolate the issue.
- Always use a timeout prefix command when running separate commands to prevent indefinite hangs
  (e.g., `timeout 600s molecule create` for a max of 5-10 minutes).
- If dealing with upstream plugins that have broken conditionals, you may need to temporarily use
  the `ANSIBLE_ALLOW_BROKEN_CONDITIONALS=1` environment variable
  (e.g., `timeout 600s env ANSIBLE_ALLOW_BROKEN_CONDITIONALS=1 molecule create`).

### Ansible Environment issues

- **Ansible missing Python modules:** If a module such as `requests` or `docker` is installed for the main container
  Python but Ansible still cannot import it, check `ansible --version` to identify the interpreter in use. In
  Codespaces/devcontainers, Ansible may run from a pipx-managed environment, so install controller-side libraries there as
  well, for example with `pipx inject ansible -r .devcontainer/requirements-ansible.txt`.
