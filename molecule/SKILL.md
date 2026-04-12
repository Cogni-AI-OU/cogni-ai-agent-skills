---
name: molecule
description: >-
  How to run and manage Molecule tests for Ansible roles and playbooks.

  Maintained at: <https://github.com/Cogni-AI-OU/.github/blob/main/.github/skills/molecule/SKILL.md>

---
# Molecule Testing

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

- **Ansible missing Python modules:** If a module such as `requests` or `docker` is installed for the main container
Python but Ansible still cannot import it, check `ansible --version` to identify the interpreter in use. In
Codespaces/devcontainers, Ansible may run from a pipx-managed environment, so install controller-side libraries there as
well, for example with `pipx inject ansible -r .devcontainer/requirements-ansible.txt`.

## Maintenance

Note that this file should be updated if outdated or steps/examples are not-working.
