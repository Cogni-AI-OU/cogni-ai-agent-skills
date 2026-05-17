---
name: agents-md-writer
description: >-
  Autonomous documentation editor responsible for creating, updating, and maintaining `AGENTS.md` files
  strictly adhering to the organizational baseline structure.
  You MUST load this skill when creating or updating `AGENTS.md` files.
license: MIT
---

# Agents MD Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Autonomous documentation editor responsible for creating, updating, and maintaining `AGENTS.md` files strictly adhering to the organizational baseline structure.

AGENTS.md is a simple, open format for guiding coding agents. It is where you define all the project specifics:
the agent's persona, the exact tech stack it should know, the project's file structure, workflows,
explicit commands it can run, code style examples, and clear boundaries of what not to do.
It is the cross-tool standard. One file, every agent.

## Setup & Environment Invariants

- Formatting must comply.
- Target file must be named `AGENTS.md` or `**/AGENTS.md`.

## Core Process

1. **Locate Target**: Identify the `AGENTS.md` file to be created or updated (e.g., in `.github/` or a subdirectory).
2. **Apply Structure**: Enforce the exact structure from the organizational baseline.
3. **Prune Entropy**: Ensure high-density, contract-style imperatives with zero conversational filler.
4. **Verify Validation**: Check against formatting and constraints and run verification gates.

## Core Principles

- **Agent-Focused Guidance**: Provide precise, agent-focused guidance that complements existing README and docs.
- **Avoid Hardcoding**: Never embed specific values, file paths, repository names, user details, job IDs, or tool versions when giving examples;
  instead, use clear placeholders (e.g., `<repository-name>`, `<file-path>`, `<job-id>`, `<version>`).
- **Be Specific About Stack**: Say "React 18 with TypeScript, Vite, and Tailwind CSS" not "React project." Include versions and key dependencies.
- **Code Examples Over Explanations**: One real code snippet showing your style beats three paragraphs describing it. Show what good output looks like.
- **Commands Early**: Put relevant executable commands in an early section. Include flags and options, not just tool names. Your agent will reference these often.
- **Concise READMEs**: Keep READMEs concise and focused on human contributors.
- **Contract Style**: Write dense, imperative, expert-level instructions assuming ninja proficiency; skip basics, favor one-liners.
- **Cover Six Core Areas**: Hitting these areas puts you in the top tier: commands, testing, project structure, code style, git workflow, and boundaries.
- **Living Documentation**: Treat `AGENTS.md` as living documentation.
- **No Duplication**: NEVER duplicate code-level comments or obvious steps.
- **Predictable Location**: Give agents a clear, predictable place for instructions.
- **Set Clear Boundaries**: Tell AI what it should never touch (e.g., secrets, vendor directories, production configs, or specific folders). "Never commit secrets" is a crucial constraint.
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
  by embedding class, flowchart, mind maps, requirements, user journeys, sequence diagrams or other when applicable.

## Testing & Verification Gates

- Verify formatting.
- Verify that the generated file contains all the required headers.

## Final Assurance Gates

- Inject full content into every sub-agent context.
- Keep this file entropy-pruned and up-to-date.

## References

- <https://agents.md/>
- <https://github.com/agentsmd/agents.md>

## Related Skills

- **docs-review**:
  You MUST load this skill when asked to review or check consistency of documentation.
- **mermaid**:
  You MUST load this skill when creating Mermaid diagrams within markdown files.
