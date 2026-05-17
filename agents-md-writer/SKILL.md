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

Autonomous documentation editor responsible for creating, updating, and maintaining `AGENTS.md` files
strictly adhering to the organizational baseline structure.

AGENTS.md is a simple, open format for guiding coding agents.
Every AI coding agent starts a task by scanning your repository (file trees, package manifests, READMEs).
But READMEs are written for humans—they explain what a project does,
not how an agent should work on it. AGENTS.md fills that gap.

It is a plain markdown file, typically placed at the root of your repository
(no required fields, no YAML frontmatter, no special syntax),
that contains the context coding agents need to work effectively.
It is where you define project specifics:
build commands with exact flags, test procedures, code style rules that differ from defaults,
architectural constraints, and boundaries (files the agent should never touch).

The mechanism is straightforward.
Without AGENTS.md, the agent spends time exploring: reading directory structures,
inferring build systems, guessing test commands.
With AGENTS.md, that context is provided upfront.
The agent skips exploratory steps and works directly toward the solution.
It is the cross-tool standard—one file, every agent.

## Setup & Environment Invariants

- Formatting must comply.
- Target file must be named `AGENTS.md` or `**/AGENTS.md`.

## Core Process

1. **Locate Target**: Identify the `AGENTS.md` file to be created or updated (e.g., in `.github/` or a subdirectory).
2. **Apply Structure**: Enforce the exact structure from the organizational baseline.
3. **Prune Entropy**: Ensure high-density, contract-style imperatives with zero conversational filler.
4. **Verify Validation**: Check against formatting and constraints and run verification gates.

## Core Principles

- **Agent-Focused Guidance**: AGENTS.md complements your README and docs.
  It contains agent-specific context that would clutter human documentation
  (exact test flags, architectural constraints, files to never modify).
  Keep your README for humans, AGENTS.md for agents.
- **Be Specific About Stack**: Say "React 18 with TypeScript, Vite, and Tailwind CSS" not "React project." Include versions and key dependencies.
- **Code Examples Over Explanations**: One real code snippet showing your style beats three paragraphs describing it. Show what good output looks like.
- **Commands Early**: Put relevant executable commands in an early section. Include flags and options, not just tool names. Your agent will reference these often.
- **Contract Style**: Write dense, imperative, expert-level instructions assuming ninja proficiency; skip basics, favor one-liners.
- **Cover Six Core Areas**: Hitting these areas puts you in the top tier: commands, testing, project structure, code style, git workflow, and boundaries.
- **Directory Hierarchy**: Nested `AGENTS.md` files provide directory-specific context.
  The agent reads the nearest file to the code being edited.
  Root-level rules apply everywhere; subdirectory rules override for that subtree.
- **Keep it Short**: Shorter files perform better
  because agents spend less time parsing instructions and more time on the task.
- **Living Documentation**: Treat `AGENTS.md` as living documentation.
- **Predictable Location**: Give agents a clear, predictable place for instructions.
- **Set Clear Boundaries**: Tell AI what it should never touch
  (e.g., secrets, vendor directories, production configs, or specific folders).
  "Never commit secrets" is a crucial constraint.
- **Structural Strictness**: You must always format `AGENTS.md` files according to the canonical `AGENTS.md` structure.

## What to Include in AGENTS.md

- **Build & Test Commands**: Exact commands with flags. Include environment setup, migration scripts, and dev server startup.
- **Code Style Rules**: Only rules that differ from language defaults. Things the agent would get wrong without guidance.
- **Project Structure**: Map directories to responsibilities. E.g. route handlers vs business logic.
- **Testing Instructions**: Test runner, how to run a single test, what to mock and what not to.
- **Git Workflow**: Branch naming conventions, commit message format, PR requirements.
- **Boundaries**: What the agent should never touch. Never modify files in /generated/. Never commit .env files.

## What to Avoid

- **Dumping Entire Style Guides**: Don't include your whole linting config.
  Only include rules that the agent consistently gets wrong or that are unique to the project.
- **Being Too Vague**: Avoid phrases like "Follow best practices" or "Write clean code."
  These tell the agent nothing actionable.
- **Forgetting to Update**: Outdated instructions are worse than no instructions.
  If you change your build tool or test runner, update AGENTS.md immediately.
- **Making it Tool-Specific**: Don't put tool-specific config (like `@imports`)
  in AGENTS.md. Save those for tool-specific files (CLAUDE.md, GEMINI.md).
- **Hardcoding**: Never embed specific values, file paths, repository names,
  user details, job IDs, or tool versions in examples; use placeholders instead.
- **Duplication**: NEVER duplicate code-level comments or obvious steps
  that the agent can easily infer from the codebase.

## SKILL.md vs AGENTS.md

`AGENTS.md` tells agents about your project.
`SKILL.md` tells agents about a specific capability.
A skill is a portable directory containing a `SKILL.md` file plus optional scripts, references, and assets.

## AGENTS.md vs Tool-Specific Files (CLAUDE.md, GEMINI.md, .cursorrules)

If you use multiple coding agents, use `AGENTS.md` for shared instructions
and tool-specific files for features unique to those platforms.

Use a tool-specific file (`CLAUDE.md`, `GEMINI.md`, `.cursorrules`) when:
- You need to configure tool-specific behavior
  (like Claude Code's permission boundaries or Cursor's glob scoping).
- Your team standardizes on one tool.
- You want to leverage features unique to that tool.

Tool-specific files include:
- **CLAUDE.md**: For Claude Code features (like `@imports`, skills, or hooks).
- **GEMINI.md**: For Google Gemini CLI context and directory traversal rules.
- **.cursorrules**: For Cursor-specific rules and context.

If you only use one tool, its native file alone may be sufficient, but `AGENTS.md`
remains the cross-tool standard. Most tools automatically read both their
native file and `AGENTS.md` when both are present.

## Expected AGENTS.md Structure

**MUST** ensure the following initial structure is used in every `AGENTS.md` you create or update:

- `# AGENTS.md (subdir-specific)`
- `## Setup & Environment Invariants`
- `## Requirements`
- `## Key Files & Context Injection`
- `## Agent Directives (Contract Style)`
  - Begin with a role statement that defines the agent's scope and responsibilities.
  - Follow with invariant statements that capture non-negotiable assumptions, constraints, or operating rules.
  - **Hardened NEVER Constraints**: Include explicit `NEVER` bullets for prohibited behaviors (e.g., "NEVER commit secrets", "NEVER mutate vendor directories").
  - **Hardened MUST Constraints**: Include explicit `MUST` bullets for required behaviors (e.g., "MUST run tests before completion", "MUST follow conventional commits").
- `## Common Tasks`
- `## Related Prompts or Skills (load when relevant)`
- `## Testing & Verification Gates`
- `## Maintenance`
- `## Final Assurance Gates`
  - Keep this file entropy-pruned and up-to-date.
  - Inject full content into every sub-agent context.
- `## Troubleshooting Matrix`
  > signature error / smell
  - root-cause vector
  - isolation steps
  - verified fix + prevention

### Formatting

- Prefer compact, agent-friendly lists by default;
  use Markdown tables only when the content is inherently tabular
  and a table improves scanability.
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
