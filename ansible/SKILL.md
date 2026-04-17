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

If you encounter hangs during Ansible execution, especially when interacting with package managers like `apt` on Debian/Ubuntu systems:

- Use the `DEBIAN_FRONTEND` environment variable to prevent prompts from hanging the process.
- Set `DEBIAN_FRONTEND=noninteractive` when running your Ansible commands or in your playbook environment.
- Example: `DEBIAN_FRONTEND=noninteractive ansible-playbook playbook.yml`

## Maintenance

Note that this file should be updated if outdated or steps/examples are not working.