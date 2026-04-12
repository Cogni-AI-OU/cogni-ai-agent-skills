---
name: molecule
description: >-
  How to run and manage Molecule tests for Ansible roles and playbooks.

  Maintained at: <https://github.com/Cogni-AI-OU/.github/blob/main/.github/skills/molecule/SKILL.md>

---

# Molecule Testing

## When to Activate

- Agent needs to execute syntax/lint/test checks for Ansible playbooks locally.
- Troubleshooting configuration logic inside devcontainers or codespaces.
- User needs to run or debug Ansible role testing frameworks using Molecule.

## Commands

```bash
# List available Molecule scenarios
molecule list

# Create a new Molecule test instance
molecule create

# Run the full test sequence (create, converge, verify, destroy)
molecule test

# Converge (apply playbook to instance)
molecule converge

# Login to instance for debugging
molecule login

# Destroy test instances
molecule destroy

# Run only the verify step
molecule verify

# Run syntax check
molecule syntax
```

## Notes

- Make sure the scenario directory (e.g. `molecule/default/`) exists for the role under test.
- If tests are failing, run `molecule converge` followed by `molecule login` to inspect the running
environment.
- If you install a Python library inside the devcontainer/codespace and it shows up `pip list` from
Python but Ansible still cannot import it, check `ansible --version` to identify the interpreter in use. In
Codespaces/devcontainers, Ansible may run from a pipx-managed environment, so install controller-side libraries there as
well, for example with `pipx inject ansible -r .devcontainer/requirements-ansible.txt`.

## Maintenance

Note that this file should be updated if outdated or steps/examples are not working.
