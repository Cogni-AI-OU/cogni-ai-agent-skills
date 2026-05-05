---
name: ansible
description: >-
  How to run and manage Ansible operations.
  You must load this skill when working with the `ansible` command.
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

## Best Practices

### Idempotency and Changed State

When using the `shell` or `command` modules, Ansible cannot automatically determine if a change was made.
Always use `creates` or `removes` to ensure idempotency:

```yaml
- name: Install custom tool
  command: /usr/local/bin/install_tool.sh
  args:
    creates: /usr/local/bin/custom_tool
```

Alternatively, use `changed_when` to manually control the task status:

```yaml
- name: Check if tool is up to date
  command: /usr/local/bin/custom_tool --version
  register: tool_version
  changed_when: "'1.2.3' not in tool_version.stdout"
```
