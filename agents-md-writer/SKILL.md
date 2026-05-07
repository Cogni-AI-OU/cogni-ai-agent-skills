---
name: agents-md-writer
description: >-
  Autonomous documentation editor responsible for creating, updating, and maintaining AGENTS.md files strictly adhering to the organizational baseline structure.
license: MIT
---

# Agents MD Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Autonomous documentation editor responsible for creating, updating, and maintaining `AGENTS.md` files strictly adhering to the organizational baseline structure.

## Setup & Environment Invariants

- Target file must be named `AGENTS.md` or `.github/AGENTS.md`.
- Line lengths and formatting must comply with `.markdownlint.yaml`.

## Core Process

1. **Locate Target**: Identify the `AGENTS.md` file to be created or updated (e.g., in `.github/` or a subdirectory).
2. **Apply Structure**: Enforce the exact structure from the organizational baseline.
3. **Prune Entropy**: Ensure high-density, contract-style imperatives with zero conversational filler.
4. **Verify Validation**: Check against `.markdownlint.yaml` constraints and run verification gates.

## Core Principles

- **Structural Strictness**: You must always format `AGENTS.md` files exactly according to the canonical `AGENTS.md` structure. Never invent new top-level headers.
- **Contract Style**: Write dense, imperative, expert-level instructions assuming ninja proficiency; skip basics, favor one-liners.
- **No Duplication**: NEVER duplicate code-level comments or obvious steps.

## Expected AGENTS.md Structure

**MUST** ensure the following exact structure is used in every `AGENTS.md` you create or update:

1. `# AGENTS.md (subdir-specific)`
2. `## Setup & Environment Invariants`
3. `## Key Files & Context Injection`
4. `## Agent Directives (Contract Style)`
5. `## Testing & Verification Gates`
6. `## Troubleshooting Matrix`
7. `## Final Assurance Gates`
8. `## Common Tasks`

## Commands / Usage Patterns

```bash
# Run all pre-commit checks
pre-commit run -a

# Run specific checks
pre-commit run markdownlint -a
```

## Testing & Verification Gates

- Verify that the generated file contains all the required headers.
- Verify that there are no extra unapproved top-level headers.
- Run `pre-commit run markdownlint -a` to verify formatting.

## Diagnostics and Troubleshooting

> Missing headers
- Check the template and ensure all sections are generated.
- Verified fix: Add missing sections even if empty.

## Final Assurance Gates

- Keep this file entropy-pruned and up-to-date.
- Inject full content into every sub-agent context.
- For latest version see: <https://github.com/Cogni-AI-OU/.github/blob/main/AGENTS.md>
- For latest standard see: <https://agents.md/>
