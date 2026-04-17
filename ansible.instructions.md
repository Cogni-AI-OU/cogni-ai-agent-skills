---
description: 'Ansible conventions and best practices'
applyTo:
  - 'ansible/**/*.{yaml,yml}'
  - 'defaults/**/*.{yaml,yml}'
  - 'handlers/**/*.{yaml,yml}'
  - 'meta/**/*.{yaml,yml}'
  - 'tasks/**/*.{yaml,yml}'
  - 'tests/**/*.{yaml,yml}'
  - 'vars/**/*.{yaml,yml}'
  - 'molecule/**/*.{yaml,yml}'
---

# Ansible Conventions and Best Practices

## General Instructions

- Use Ansible to configure and manage infrastructure.
- Use version control for your Ansible configurations.
- Keep things simple; only use advanced features when necessary.
- Ensure all tasks are idempotent - running them multiple times should produce the same result without unintended side effects.
- Follow the standard Ansible role structure (`tasks/`, `handlers/`, `templates/`,
  `defaults/`, `vars/`, `meta/`).
- Give every play, block, and task a concise but descriptive `name`:
  - Start names with an action verb that indicates the operation being performed,
    such as "Install," "Configure," or "Copy"
  - Capitalize the first letter of the task name
  - Omit periods from the end of task names for brevity
  - When writing tasks inside a role (in the role's `tasks/` directory), omit the
    role name from task names since Ansible automatically prefixes them with the
    role name during execution
  - When including tasks from a separate file, you may include the filename in each
    task name to make tasks easier to locate (e.g., `<TASK_FILENAME> : <TASK_NAME>`)
- Use comments to provide additional context about **what**, **how**, and/or **why**
  something is being done, especially for non-obvious decisions, workarounds, or complex logic
  - Prefer comments that explain reasoning, caveats, or links to external context (e.g., ticket IDs, docs)
  - Avoid comments that simply restate what the task already does (for example, do not add `# Install package`
    above a task whose `name:` is "Install package")
- Use dynamic inventory for cloud resources
  - Use tags to dynamically create groups based on environment, function, location, etc.
  - Use `group_vars` to set variables based on these attributes
- Use idempotent Ansible modules whenever possible; avoid `shell`, `command`, and `raw`, as they break idempotency.
  - If you must use `shell` or `command`, use `creates:` or `removes:` to prevent unnecessary execution.
- Use [fully qualified collection names (FQCN)](https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Fully-Qualified-Collection-Name-FQCN)
  everywhere to satisfy ansible-lint (e.g., `ansible.builtin.template`) and to
  ensure the correct module or plugin is selected.
  - Use the `ansible.builtin` collection for
    [builtin modules and plugins](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/index.html#plugin-index).
- Group related tasks together to improve readability and modularity
- For modules where `state` is optional, explicitly set `state: present` or `state:
  absent` to improve clarity and consistency
- Use the lowest privileges necessary to perform a task.
  - Only set `become: true` at the play level or on an `include:` statement if all
    included tasks require super user privileges; otherwise, set it per task.
  - Only set `become: true` on a task if it requires super user privileges.

## Secret Management

- When using Ansible alone, store secrets using Ansible Vault
  - Use the following process to make it easy to find where vaulted variables are
    defined:
    1. Create a `group_vars/` subdirectory named after the group
    2. Inside this subdirectory, create two files named `vars` and `vault`
    3. In the `vars` file, define all of the variables needed, including any
       sensitive ones
    4. Copy all of the sensitive variables over to the `vault` file and prefix
       these variables with `vault_`
    5. Adjust the variables in the `vars` file to point to the matching `vault_`
       variables using Jinja2 syntax: `db_password: "{{ vault_db_password }}"`
    6. Encrypt the `vault` file to protect its contents
    7. Use the variable name from the `vars` file in your playbooks
- When using other tools with Ansible (e.g., Terraform), store secrets in a
  third-party secrets management tool (e.g., Hashicorp Vault, AWS Secrets
  Manager, etc.).
  - This allows all tools to reference a single source of truth for secrets and
    prevents configurations from getting out of sync

## Style

- Use 2-space indentation and always indent lists (matches `.editorconfig`).
- Separate each of the following with a single blank line:
  - Two host blocks
  - Two task blocks
  - Host and include blocks
- Use `snake_case` for variable names
- Sort variables alphabetically when defining them in `vars:` maps or variable files
- Always use multi-line map syntax, regardless of how many pairs exist in the map
  - It improves readability and reduces changeset collisions for version control
- Prefer single quotes over double quotes.
  - Use double quotes only when nested within single quotes or when you need YAML escape
    sequences (for example, `"Line 1\nLine 2"` to embed a newline).
  - For long strings, use folded (`>`) or literal (`|`) block scalars and omit extra quoting.
- The `host` section of a play should follow this general order:
  - `hosts` declaration
  - Host options in alphabetical order (e.g., `become`, `remote_user`, `vars`)
  - `pre_tasks`
  - `roles`
  - `tasks`
- Each task should follow this general order:
  - `name`
  - Task declaration (e.g., `service:`, `package:`)
  - Task parameters (using multi-line map syntax)
  - Loop operators (e.g., `loop`)
  - Task options in alphabetical order (e.g. `become`, `ignore_errors`,
    `register`)
  - `tags`
- For `include` statements, quote filenames and only use blank lines between
  `include` statements if they are multi-line (e.g., they have tags).

## Linting

- Use `ansible-lint` and `yamllint` to check syntax and enforce project standards.
- Use `ansible-playbook --syntax-check` to check for syntax errors.
- Use `ansible-playbook --check --diff` to perform a dry-run of playbook execution.
- Use `pre-commit run ansible-lint -a` to verify Ansible files locally if pre-commit is
  available.
- Prefer Molecule for role testing when available (e.g., `molecule test`).

<!--
These guidelines were based on, or copied from, the following sources:

- [Ansible Documentation - Tips and Tricks](https://docs.ansible.com/ansible/latest/tips_tricks/index.html)
- [Whitecloud Ansible Styleguide](https://github.com/whitecloud/ansible-styleguide)
-->
