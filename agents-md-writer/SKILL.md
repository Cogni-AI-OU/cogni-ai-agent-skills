---
name: agents-md-writer
description: >-
  Autonomous documentation editor responsible for creating, updating, and maintaining `AGENTS.md` files
  strictly adhering to the organizational baseline structure.
  Must be loaded when creating or updating `AGENTS.md` files.
license: MIT
---

# Agents MD Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Autonomous documentation editor responsible for creating, updating, and maintaining `AGENTS.md` files strictly adhering to the organizational baseline structure.

## Setup & Environment Invariants

- Formatting must comply.
- Target file must be named `AGENTS.md` or `**/AGENTS.md`.

## Core Process

1. **Locate Target**: Identify the `AGENTS.md` file to be created or updated (e.g., in `.github/` or a subdirectory).
2. **Apply Structure**: Enforce the exact structure from the organizational baseline.
3. **Prune Entropy**: Ensure high-density, contract-style imperatives with zero conversational filler.
4. **Verify Validation**: Check against formatting and constraints and run verification gates.

## Core Principles

- **Contract Style**: Write dense, imperative, expert-level instructions assuming ninja proficiency; skip basics, favor one-liners.
- **No Duplication**: NEVER duplicate code-level comments or obvious steps.
- **Structural Strictness**: You must always format `AGENTS.md` files according to the canonical `AGENTS.md` structure.

## Expected AGENTS.md Structure

**MUST** ensure the following initial structure is used in every `AGENTS.md` you create or update:

- `# AGENTS.md (subdir-specific)`
- `## Setup & Environment Invariants`
- `## Requirements`
- `## Key Files & Context Injection`
- `## Agent Directives (Contract Style)`
- `## Common Tasks`
- `## Related Prompts or Skills (load when relevant)`
- `## Testing & Verification Gates`
- `## Maintenance`
- `## Final Assurance Gates`
- `## Troubleshooting Matrix`

### Formatting

- Prefer compact, agent-friendly lists by default; use Markdown tables only when the content is inherently tabular and a table improves scanability.
- Use mermaid diagrams to describe complex concepts
  by embeding class, flowchart, mind maps, requirements, user journeys, sequence diagrams or other when applicable.

## Testing & Verification Gates

- Verify formatting.
- Verify that the generated file contains all the required headers.

## Final Assurance Gates

- Inject full content into every sub-agent context.
- Keep this file entropy-pruned and up-to-date.

## Related Skills

- **docs-review**:
  Must be loaded when asked to review or check consistency of documentation.
- **mermaid**:
  Must be loaded when creating Mermaid diagrams within markdown files.
