---
name: brainstorm
description: >-
  Activate brainstorming protocol to explore options, research, deconstruct complexities, and summarize available data into simple diagrams and MiniZinc constraints.
  You MUST load this skill when asked to brainstorm, explore options, or break down complex problems.
---

# Skill brainstorm

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

A cognitive framework and protocol for exploring options, breaking down complexities, and summarizing information.

## Core Process

1. **Context Gathering & Research**: Aggressively gather facts, existing data, and constraints before formulating any conclusions.
2. **Explore Options**: Generate multiple orthogonal approaches or alternative options. Do not settle for the first apparent solution.
3. **Deconstruct Complexities**: Break down the problem space into atomic, manageable components.
4. **Visual Summarization**: Synthesize the gathered data and complexities into simple, easy-to-read Mermaid diagrams (e.g., mindmaps, block diagrams, or flowcharts).
5. **Constraint Formulation (MiniZinc)**: When applicable, formally model the problem's constraints by writing dry-code definitions in MiniZinc to expose hidden dependencies and restrictions.

## Core Principles

- **Divergent Before Convergent**: Ensure a broad exploration of the problem space (divergent thinking) before narrowing down to specific recommendations (convergent thinking).
- **Fact-Based Exploration**: Anchor all generated options in empirical data retrieved from the codebase, project memory, or provided context.
- **Formal Constraint Mapping**: Use MiniZinc snippets as a dry-code exercise to rigorously define problem boundaries, resources, and requirements.
- **Visual Clarity First**: Use diagrams early to establish a shared mental model before diving into deep technical or textual analysis.

## Diagnostics and Usage Patterns

- **Diagramming Focus**:
  Default to high-level topological or structural diagrams (`block-beta`, `flowchart`, `mindmap`) to visualize options.
- **MiniZinc Dry-Code**:
  Write MiniZinc `.mzn` snippets to formally declare the parameters, decision variables, and constraints of the problem space, even if you do not execute the solver immediately.

## What to Avoid

- **Assumption-Driven Brainstorming**: Relying on guesses instead of factual context gathered through tools.
- **Overcomplicated Diagrams**: Creating massive, unreadable diagrams. Break them into smaller, focused visual summaries.
- **Premature Convergence**: Proposing a final solution without explicitly documenting the discarded alternative options.

## Related Skills

- **brainstorm-agent-runs**: You MUST load this skill when identifying agentic runs in CI/CD for a Pull Request.
- **brainstorm-github-pr**: You MUST load this skill when asked to analyze or brainstorm a Pull Request.
- **critical-thinking**: You MUST load this skill when evaluating the options generated during brainstorming.
- **mermaid**: You MUST load this skill when constructing standard Mermaid diagrams.
- **mermaid-beta**: You MUST load this skill when using experimental Mermaid diagrams.
- **minizinc**: You MUST load this skill when executing or deeply modeling constraint satisfaction problems.
