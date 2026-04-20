---
name: ansible
description: >-
  How to run and manage Ansible operations safely and prevent hangs.

  Maintained at: <https://github.com/Cogni-AI-OU/cogni-ai-agent-skills>

---
# Ansible Operations

## When to Activate

- Agent needs to execute Ansible playbooks or commands.
- User needs to run Ansible automation scripts.
- Troubleshooting hanging issues during Ansible execution.

## Troubleshooting

### Ansible Environment issues

If you encounter hangs during Ansible execution, especially when interacting with package managers
like `apt` on Debian/Ubuntu systems:

- Use the `DEBIAN_FRONTEND` environment variable to prevent prompts from hanging the process.
- Set `DEBIAN_FRONTEND=noninteractive` when running your Ansible commands or in your playbook environment.
- Example: `DEBIAN_FRONTEND=noninteractive ansible-playbook playbook.yml`

## Performance Profiling

To profile the execution time of your playbooks and roles, you can enable the `profile_tasks` callback plugin. This is useful for identifying slow tasks and optimizing your automation.

- Enable the plugin by adding it to your `ansible.cfg` file under `[defaults]` or via environment variables.
- Using environment variables: `ANSIBLE_CALLBACKS_ENABLED=profile_tasks ansible-playbook playbook.yml`
- In `ansible.cfg`:
  ```ini
  [defaults]
  callbacks_enabled = profile_tasks
  ```

## Maintenance

Note that this file should be updated if outdated or steps/examples are not working.
