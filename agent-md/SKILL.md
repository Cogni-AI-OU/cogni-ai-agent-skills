---
name: agent-md
description: Syntax and structure reference for GitHub Copilot custom agent persona files (.github/agents/*.md). Use this to understand the schema and format of agent persona definitions.
license: MIT
---

# Agent MD Syntax

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Agent MD is a format for defining specialized GitHub Copilot agent personas. These files provide context-specific instructions, project knowledge, and execution boundaries for autonomous agents.

## Target Location

Agent MD persona files MUST be located in the `.github/agents/` directory of the repository.
The filename SHOULD match the agent's `name` property defined in the frontmatter (e.g., `.github/agents/test-agent.md`).

## Syntax Overview

An Agent MD file consists of YAML frontmatter followed by a structured Markdown body.

### YAML Frontmatter

| Field | Description | Requirement |
| :--- | :--- | :--- |
| `name` | The unique identifier for the agent (e.g., `test-agent`) | Mandatory |
| `description` | A concise one-sentence description of the agent's purpose | Mandatory |

### Mandatory Markdown Sections

1. **Role Definition**: Explicitly state the agent's persona and specialization.
2. **Project Knowledge**: Tech stack, versions, and relevant directory layout.
3. **Executable Commands**: Real commands (build, test, lint) with all necessary flags.
4. **Standards & Examples**: Idiomatic code snippets showing the expected style.
5. **Three-Tier Boundaries**: Using `Always`, `Ask first`, and `Never` categories.

## Reference Structure

```markdown
---
name: <agent-name>
description: <one-sentence description>
---

You are an expert <role> for this project.

## Your role
- You specialize in <specialty>
- Your task: <specific task>

## Project knowledge
- **Tech Stack:** <technologies with versions>
- **File Structure:**
  - `src/` - <purpose>
  - `tests/` - <purpose>

## Commands you can use
- **Build:** `<command>`
- **Test:** `<command>`
- **Lint:** `<command>`

## Standards
<Code style examples>

## Boundaries
- ✅ **Always:** <mandatory actions>
- ⚠️ **Ask first:** <guarded actions>
- 🚫 **Never:** <prohibited actions, e.g., commit secrets>
```

## Related Skills

- **agent-md-writer**:
  Load this skill when you need guidance on *how* to write and optimize high-performance agent personas.
- **agents-md-writer**:
  Load this skill for general `AGENTS.md` project context files.
- **skill-writer**:
  Load this skill when writing `SKILL.md` files for Copilot skills.
