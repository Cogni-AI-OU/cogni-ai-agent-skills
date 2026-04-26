<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->
---
name: fact-writer
description: >-
  Guidelines for creating, structuring, and maintaining verifiable project fact files (e.g., FACTS.md) without contradictions.
---
# Fact Writer

Guidance for writing, structuring, and maintaining verifiable project fact files without contradictions. Use this skill when managing `FACTS.md`, `FACTS.mmd` (in mermaid format), or similar canonical stores of project facts.

## When to Activate

- Documenting verifiable facts, architectural decisions, and ecosystem properties.
- Managing, creating, or updating a canonical fact store (e.g., `FACTS.md` or `FACTS.mmd`) in the project root.
- Resolving state conflicts or contradictions in project documentation.

## Core Process

1. **Verify Before Writing**: Always read the existing fact file (e.g., `FACTS.md`) thoroughly before proposing or writing updates to ensure you do not introduce conflicting information.
2. **Contradiction Transparency**: Reject silent overwrites. If a newly proposed fact contradicts an existing fact, explicitly surface the conflict and resolve it by replacing the outdated fact, not appending a conflicting one.
3. **Verifiable Facts**: Only record objective, verifiable facts based on the repository's configuration, code, and explicit documentation. Avoid subjective language or assumptions.
4. **Structured Formatting**: Maintain a rigid, hierarchical format (such as Mermaid mindmaps or strictly nested Markdown lists). Group facts by logical domains (e.g., Architecture, Ecosystem, Settings).
5. **Lexical Sorting**: Insert new facts in strict alphabetical or lexical order within their respective sections to minimize diff noise and ensure deterministic versioning.
6. **Reversibility Focus**: Offload history, diffs, and rollback mechanics entirely to the Version Control System (Git). Do not clutter the fact file with historical change logs, sequence IDs, or obsolete states.

## Diagnostics and Revisions

- **Contradiction Check**: Before finalizing edits, perform a self-review of the entire file to ensure no `A ≠ ¬A` condition exists.
- **Orphan Pruning**: Remove redundant, outdated, or orphaned facts seamlessly to maintain a high-density, strictly necessary state compression.

## What to Avoid

- **NEVER** append nodes or lists out of alphabetical order.
- **NEVER** mix unrelated prose or narratives into the structured fact lists.
- **NEVER** guess or hallucinate facts; if a fact cannot be traced to the repository state, do not record it.
- **NEVER** leave unresolved contradictions in the file.

## Related Skills

- [mermaid](../mermaid/SKILL.md): Guide for creating and maintaining stable Mermaid.js diagrams.
- [mermaid-beta](../mermaid-beta/SKILL.md): Guide for creating and maintaining experimental Mermaid.js beta diagrams.
