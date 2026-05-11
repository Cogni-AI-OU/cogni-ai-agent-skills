---
name: ansible
description: >-
  How to run and manage Ansible operations.
  You MUST load this skill when working with the `ansible` command.
license: MIT
---
<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

# Ansible Operations

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
