---
name: docs-writer
description: >-
  Create, update, and maintain documentation including Architectural Decision Records (ADRs), runbooks, READMEs, and code-level documentation.
  You MUST load this skill when asked to write, document, or generate new documentation.
license: MIT
---

# Docs Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Writing or generating Architectural Decision Records (ADRs) to capture rationale for significant technical decisions.
- Documenting non-obvious code or complex algorithms with "why" comments.
- Creating or updating runbooks for production processes, incident response, or operational tasks.
- Updating README files to reflect the current state, setup instructions, or architecture.
- Creating local `AGENTS.md` files for subdirectories with specific functionality or workflows.
- Writing project documentation after a significant architectural change or new feature addition.

## When Not to Use

- Reviewing existing documentation for correctness or consistency — use the `docs-review` skill instead.
- Making trivial formatting or spelling fixes that do not add new documentation content.
- Generating API reference documentation that should be auto-generated from code comments or OpenAPI specs.
- Writing documentation for unstable or experimental features that are likely to change before release.

## Common Pitfalls

- ADRs explain WHY, not WHAT — the code already explains what it does. A good ADR captures the context, alternatives considered, and consequences, not the implementation details.
- Code comments should document the WHY, not the WHAT — comments like `// Retry the request` add noise; `// Using exponential backoff — payment API limits to 3 req/sec` adds value.
- Runbooks must be verifiable: each step should be precise enough that someone with on-call access can execute it without asking for clarification.
- READMEs rot faster than code — always verify setup instructions by mentally walking through them on a hypothetical fresh machine, and update architecture diagrams after significant changes.

Guidance for writing core architecture, documentation, and constraint files. Use this skill when creating or updating repository documentation.

## When to Use

- Writing or generating Architectural Decision Records (ADRs).
- Documenting non-obvious code or complex algorithms.
- Creating or updating runbooks for production processes.
- Updating README files to reflect current state or instructions.
- Creating local `AGENTS.md` files for subdirectories.

## Architectural Decision Records (ADRs)

Code explains what. Documentation explains why. The most valuable documentation records decisions that aren't obvious from reading the code: why this architecture, why this tradeoff, why not the obvious alternative.

For every significant architectural decision, write an ADR with:
- **Context**: What was the situation requiring a decision?
- **Decision**: What was decided?
- **Alternatives considered**: What else was evaluated and why rejected?
- **Consequences**: What are the positive and negative consequences?
- **Status**: Proposed | Accepted | Deprecated | Superseded

(typically stored in `docs/decisions/`).

## Code-Level Documentation

- Document the WHY, not the WHAT:
  - ✅ `// Using exponential backoff here — the payment API has strict rate limits (3 req/sec)`
  - ❌ `// Retry the request`
- Document non-obvious algorithmic choices.
- Document external constraints (rate limits, API quirks, platform limitations).
- Remove comments that state the obvious — they add noise.

## Runbooks

For every production process that humans execute, write a runbook:
- When is this runbook used?
- What steps to execute?
- What does "done" look like?
- What could go wrong and how to recover?

(typically stored in `docs/runbooks/`).

## README Currency

- Ensure README reflects current state (not v1 state).
- Ensure setup instructions work on a fresh machine.
- Update architecture diagrams after significant changes.

## Subdirectory Agents (`AGENTS.md`)

When a subdirectory contains specific functionality, workflows, or architectural patterns that require clarification, create a dedicated `AGENTS.md` file within that folder.
- Use this file to provide targeted instructions, constraints, and context for autonomous agents operating in that specific folder.
- Ensure the local `AGENTS.md` aligns with the global repository invariants.

## Related Skills

- **critical-thinking**:
  You MUST load this skill when deconstructing complex requirements into clear, architectural documentation.
- **agents-md-writer**:
  You MUST load this skill when creating or updating AGENTS.md files.
