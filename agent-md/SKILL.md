---
name: agent-md
description: Generate or update GitHub Copilot custom agent files (e.g., .github/agents/*.md) specifying clear personas, executable commands, strict boundaries, and code examples. You MUST load this skill when creating or updating custom Copilot agent personas.
license: MIT
---

# Agent MD Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generate or update custom GitHub Copilot agent persona files (e.g., `.github/agents/test-agent.md`), ensuring they define a highly specific role, explicit commands, clear boundaries, and concrete code examples according to best practices from analyzing 2,500+ repositories.

## Core Process

1. **Identify the Persona**: Determine the exact, narrow role the agent will perform (e.g., `docs-agent`, `test-agent`, `lint-agent`). Avoid "general helper" personas.
2. **Set the Target Location**: Ensure the file is placed correctly, usually in `.github/agents/<agent-name>.md`.
3. **Structure the Content**: Use YAML frontmatter for name and description, followed by persona definition, project knowledge, executable commands, code standards/examples, and strict boundaries.
4. **Prune Fluff**: Use real code snippets instead of abstract descriptions.
5. **Output**: Output the complete, ready-to-commit markdown file without conversational wrappers.

## Core Principles

- **Specialized Personas Only**: Do not create general assistants. Each file must represent a specialist (e.g., technical writer, QA engineer, security analyst).
- **YAML Frontmatter**: Always include `name` and `description` in the YAML frontmatter.
- **Commands Early**: List executable commands (e.g., `npm test`, `pytest -v`, `npx markdownlint docs/`) early in the document. Include flags and options.
- **Code Examples Over Explanations**: Provide real code snippets showing the expected style. Show what good output looks like.
- **Be Specific About Stack**: Explicitly name the technologies and versions (e.g., "React 18 with TypeScript, Vite, and Tailwind CSS") and key file structures.
- **Three-Tier Boundaries**: Define boundaries using "Always do", "Ask first", and "Never do". "Never commit secrets" is a mandatory constraint.

## Expected Agent File Structure

**MUST** ensure the following structure is used in every custom agent `.md` file you create or update:

```markdown
---
name: <agent-name>
description: <one-sentence description of what this agent does>
---

You are an expert <role> for this project.

## Your role
- You specialize in <specialty>
- You understand <context> and translate that into <output>
- Your task: <specific task>

## Project knowledge
- **Tech Stack:** <technologies with versions>
- **File Structure:**
  - `src/` - <what's here>
  - `tests/` - <what's here>

## Commands you can use
- **Build:** `<command>`
- **Test:** `<command>`
- **Lint:** `<command>`

## Standards
<Provide naming conventions and real code style examples here>

## Boundaries
- ✅ **Always:** <what to always do>
- ⚠️ **Ask first:** <when to ask for permission>
- 🚫 **Never:** <what to never do, e.g., commit secrets>
```

## What to Avoid

- **Vague Roles**: Avoid "You are a helpful coding assistant".
- **Abstract Instructions**: Do not write three paragraphs describing code style; use one real code snippet instead.
- **Missing Boundaries**: Never omit the "Never do" section.
- **Missing Commands**: Do not just list tool names; include exact executable commands with flags.

## Related Skills

- **agents-md-writer**:
  You MUST load this skill when creating or updating the general `AGENTS.md` project context file, rather than a specific agent persona.
- **skill-writer**:
  You MUST load this skill when writing `SKILL.md` files for Copilot skills.
