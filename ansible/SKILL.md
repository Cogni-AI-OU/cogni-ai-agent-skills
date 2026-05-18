---
name: ansible
description: >-
  How to run and manage Ansible operations.
  You MUST load this skill when working with the `ansible` command.
license: MIT
---

# Ansible Operations

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Running Ansible playbooks or ad-hoc commands in automated CI/CD or agentic environments.
- Debugging Ansible execution hangs or failures, especially when interacting with package managers on Debian/Ubuntu hosts.
- Profiling playbook execution performance to identify slow-running tasks and optimize automation.

## When Not to Use

- Managing infrastructure that uses a different configuration management tool (e.g., Terraform, Pulumi, Chef, CloudFormation).
- Writing Ansible roles or collections from scratch — role scaffolding and best practices are beyond this skill's scope.
- Debugging network connectivity, DNS resolution, or SSH issues unrelated to Ansible's execution environment.

## Common Pitfalls

- **Package Manager Hangs**: Ansible's `apt` module can hang indefinitely waiting for interactive prompts on Debian/Ubuntu systems. Always set `DEBIAN_FRONTEND=noninteractive` in your playbook environment or as an environment variable.
- **Mocking is Prohibited**: Never use `mock_modules` or `mock_roles` to bypass tasks that are failing due to environment-specific issues. Masking failures with mocks hides root causes and can lead to production incidents. Fix the underlying issue directly.
- **Profile Tasks for Optimization**: The `profile_tasks` callback plugin (`ansible.posix.profile_tasks`) is essential for identifying slow tasks. Enable it via `ANSIBLE_CALLBACKS_ENABLED=profile_tasks` or in `ansible.cfg` before troubleshooting performance.
- **Idempotency Verification**: Always verify that playbooks are idempotent by running them twice and checking that the second run produces zero changes.

## Troubleshooting

### Ansible Environment issues

If you encounter hangs during Ansible execution, especially when interacting with package managers
like `apt` on Debian/Ubuntu systems:

- Use the `DEBIAN_FRONTEND` environment variable to prevent prompts from hanging the process.
- Set `DEBIAN_FRONTEND=noninteractive` when running your Ansible commands or in your playbook environment.
- Example: `DEBIAN_FRONTEND=noninteractive ansible-playbook playbook.yml`

### Prohibiting Mocking for Workarounds

Do NOT use mocking to work around unexpected errors:

- Never use `mock_modules` or `mock_roles` to bypass tasks that are failing due to environment-specific issues or other "shouldn't happen" errors.
- Underlying issues must be fixed directly; do not mask failures with mocks to unblock progress.

## Performance Profiling

To profile the execution time of your playbooks and roles, you can enable the `profile_tasks` callback plugin.
This is useful for identifying slow tasks and optimizing your automation.

- Enable the plugin by adding it to your `ansible.cfg` file under `[defaults]` or via environment variables.
- Using environment variables: `ANSIBLE_CALLBACKS_ENABLED=profile_tasks ansible-playbook playbook.yml`
- In `ansible.cfg`:

  ```ini
  [defaults]
  callbacks_enabled = ansible.posix.profile_tasks
  ```

## Related Skills

- **molecule**:
  You MUST load this skill when running or managing Molecule tests for Ansible.
