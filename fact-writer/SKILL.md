---
name: fact-writer
description: 'Strict guidelines for creating, writing, and maintaining verifiable project fact files (e.g., FACTS.md or FACTS.mmd) without contradictions, ensuring state compression and lexical ordering. You MUST load this skill when managing canonical project fact files.'
license: MIT
---

# Fact Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Creating or updating a canonical fact file (`FACTS.md`, `FACTS.mmd`) that captures immutable project knowledge.
- Adding a new verifiable fact about project architecture, context, or ecosystem after a confirmed codebase change.
- Pruning outdated or superseded facts to maintain high-density state compression.
- Reconciling contradictions between existing fact entries and current repository state.
- Preparing a fact file for agent context injection to reduce hallucination and improve decision consistency.

## When Not to Use

- Recording subjective opinions, plans, or speculative future states — facts must be objectively verifiable from the repository.
- Keeping historical changelogs or version histories — Git handles history; fact files hold only the current canonical state.
- Writing narrative documentation, tutorials, or explanations — use `docs-writer` instead for prose documentation.
- Adding facts that duplicate existing entries — always check for existing facts before insertion.

## Common Pitfalls

- Insertion order is strict lexical sorting (case-insensitive, natural number sorting) — inserting out of order breaks the structure and wastes reviewer time.
- Contradictions must be surfaced immediately: when a proposed fact conflicts with an existing `A ≠ ¬A` state, reject the silent overwrite and flag the conflict rather than accepting either value blindly.
- Facts MUST be objectively verifiable — if the repository state does not support a claim (no code, no config, no documentation), reject ingestion entirely. Never hallucinate project details.
- Offload all history and rollback to Git — never include changelogs, sequence IDs, or obsolete states in the fact file itself. Replace, do not append.

Guidance for structuring and maintaining verifiable project fact files. Use this skill when managing `FACTS.md`,
`FACTS.mmd`, or similar canonical stores.

## Core Process

1. **Verify State**:
    Read existing fact files entirely before proposing updates; never infer missing state.
2. **Contradiction Transparency**:
    Surface conflicts immediately; reject silent overwrites when a proposed fact contradicts an existing `A ≠ ¬A` state.
    Replace, do not append.
3. **Verifiable Facts Only**:
    Record objective facts grounded in repository configuration, code, and explicit documentation. Zero subjective prose.
4. **Structured Format**:
    Enforce rigid hierarchical structures (e.g., Mermaid `mindmap` or perfectly nested Markdown lists). Group by logical
    domains like `Architecture`, `Context`, `Ecosystem`.
5. **Lexical Sorting**:
    Insert new facts in strict alphabetical order within their domain/level.
    - **Case**: Case-insensitive (e.g., `A` and `a` share same priority; `App` before `apple`).
    - **Numbers**: Natural sort (e.g., `v2` < `v10`).
    - **Special Characters**: Sort symbols (e.g., `@`, `_`) before alphanumeric characters.
6. **Reversibility Focus**:
    Offload history, diffs, and rollback logic entirely to Git. Eradicate historical changelogs, sequence IDs, and
    obsolete states from the fact file itself.

## Diagnostics and Revisions

- **Contradiction Sweep**: Pre-commit self-review to guarantee zero logical conflicts.
- **Orphan Pruning**: Seamlessly drop redundant, outdated, or superseded facts (e.g., deprecated libraries) to
  maintain high-density state compression.

## What to Avoid

- **NEVER** insert nodes or lists out of alphabetical order.
- **NEVER** include conversational prose, narratives, or explanations in fact structures.
- **NEVER** hallucinate project details. If unsupported by repo state, reject ingestion.
- **NEVER** preserve historical states when superseded. Replace with the new fact.

## Related Skills

- **mermaid**:
  You MUST load this skill when creating or maintaining Mermaid.js diagrams.
- **mermaid-beta**:
  You MUST load this skill when working with experimental Mermaid.js beta diagrams.
