---
name: agent-md-writer
description: Guidelines and best practices for writing high-performance GitHub Copilot agent persona files (.github/agents/*.agent.md). Use this when you need to create or refine a specialized agent persona.
license: MIT
---

# Agent MD Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

This skill provides a structured process and set of principles for creating effective GitHub Copilot agent personas that reduce hallucination and increase task success rates.

## Core Process

1. **Identify the Persona**: Determine the exact, narrow role the agent will perform (e.g., `docs-agent`, `test-agent`). Avoid "general helper" personas.
2. **Structure the Content**: Follow the `agent-md` syntax: YAML frontmatter, persona, project knowledge, executable commands, code examples, and boundaries.
3. **Prune Fluff**: Use real code snippets instead of abstract descriptions.
4. **Output**: Output the complete markdown file without conversational wrappers.

## Core Principles

- **Specialization Over Generality**: Each agent must be a specialist (e.g., technical writer, QA engineer, security analyst).
- **Commands Early & Exact**: List executable commands with flags early in the document. Do not just list tool names.
- **Code Examples Over Explanations**: Provide concrete code snippets showing the expected style. One example is worth ten paragraphs.
- **Tech Stack Specificity**: Explicitly name technologies and versions (e.g., "React 18 with TypeScript").
- **Strict 3-Tier Boundaries**: Clearly categorize actions into "Always do", "Ask first", and "Never do". "Never commit secrets" is mandatory.

## What to Avoid

- **Vague Roles**: Avoid generic personas like "helpful assistant".
- **Abstract Style Guides**: Do not describe code style; show it.
- **Missing Boundaries**: Never omit the "Never do" section.
- **Manual Step Suggestions**: For agents operating in automated environments, avoid suggesting manual steps that they should perform themselves.

## Related Skills

- **agent-md**:
  Load this skill for the technical syntax reference and schema of Agent MD files.
- **skill-writer**:
  Load this skill when writing `SKILL.md` files for Copilot skills.
- **agents-md-writer**:
  Load this skill for general `AGENTS.md` project context files.
