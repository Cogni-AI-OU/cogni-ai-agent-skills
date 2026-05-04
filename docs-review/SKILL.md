---
name: docs-review
description: >-
  Enforce documentation quality, completeness, and mutual consistency across
  architecture files, ADRs, runbooks, READMEs, and code-level documentation.
  You must load this skill when asked to review or check consistency of documentation (such as *.md/*.mmd files).
license: MIT
---

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

# Docs Review

Guidance for reviewing core architecture, documentation, and constraint files for mutual consistency and accuracy. Use this skill when checking or updating repository documentation.

## When to Activate

- Checking core architecture files (`*.mmd`, `*.mzn`) for consistency.
- Reviewing documentation (`**/AGENTS.md`, `**/README.md`) for outdated references.
- After any significant architectural decision to verify documentation.
- When encountering complex code that future maintainers will question.
- When an operational procedure isn't self-evident.
- When a non-obvious tradeoff was made.

## Core Process

1. **Analyze Relationships**:
   Cross-reference the relationships, definitions, rules, and configurations defined across these files.
2. **Identify Inconsistencies**:
   Look for contradictions, outdated references, missing updates, or structural mismatches between files.
3. **Verify Up-to-Date Status**:
   Check if any of the documentation lags behind the current state of the repository.
4. **Conditional Edits**:
   **CRITICAL INSTRUCTION:** ONLY apply changes to these files if actual inconsistencies, contradictions,
   or outdated information are found. If all files are mutually consistent and up-to-date,
   do not make any edits—simply report back that the files are in order.

## Architectural Decision Records (ADRs)

Code explains what. Documentation explains why. The most valuable documentation records decisions that aren't obvious from reading the code: why this architecture, why this tradeoff, why not the obvious alternative.

For every significant architectural decision, verify or write an ADR with:
- **Context**: What was the situation requiring a decision?
- **Decision**: What was decided?
- **Alternatives considered**: What else was evaluated and why rejected?
- **Consequences**: What are the positive and negative consequences?
- **Status**: Proposed | Accepted | Deprecated | Superseded

**Verify:** Every significant decision has an ADR (typically stored in `docs/decisions/`).

## Code-Level Documentation

- Document the WHY, not the WHAT:
  - ✅ `// Using exponential backoff here — the payment API has strict rate limits (3 req/sec)`
  - ❌ `// Retry the request`
- Document non-obvious algorithmic choices.
- Document external constraints (rate limits, API quirks, platform limitations).
- Remove comments that state the obvious — they add noise.

**Verify:** Every non-obvious code block has a "why" comment.

## Runbooks

For every production process that humans execute, verify or write a runbook:
- When is this runbook used?
- What steps to execute?
- What does "done" look like?
- What could go wrong and how to recover?

**Verify:** Every on-call alert has a linked runbook (typically stored in `docs/runbooks/`).

## README Currency

- README reflects current state (not v1 state).
- Setup instructions work on a fresh machine.
- Architecture diagrams are updated after significant changes.

## Verification

- [ ] ADRs written for significant architectural decisions
- [ ] Non-obvious code blocks have "why" comments
- [ ] Every production alert has a linked runbook
- [ ] README is current and setup instructions work
