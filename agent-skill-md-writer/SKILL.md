---
name: agent-skill-md-writer
description: 'Workflow and guidelines for generating or refining agent skills. You MUST load this skill when creating or updating SKILL.md files to ensure correct tone and writing style.'
license: MIT
---

# Agent Skill MD Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- **Capability Documentation**: Formalizing a specific agent capability into a portable `SKILL.md` playbook with verifiable, imperative steps.
- **Mechanical Workflow Design**: Authoring precise `bash`, `gh`, or API execution sequences that any agent can invoke regardless of their persona.
- **Activation Trigger Optimization**: Refining skill descriptions in YAML frontmatter to ensure reliable discovery and prevent false positives.
- **Resource Bundling**: Organizing scripts, templates, and reference docs into a structured directory for progressive context loading.
- **Skill Refactoring**: Decomposing bloated skills into atomic units or offloading detailed content to the `references/` directory to save context.

## When Not to Use

- **Persona Specification**: Defining a persistent agent identity, mandate, or internal reasoning protocol — use `agent-md-writer` instead.
- **General Project Context**: Setting repo-wide build/test commands or architectural constraints — use `agents-md-writer` (AGENTS.md) instead.
- **Formatting Standard Definition**: Authoring pure coding conventions, linting rules, or schema definitions — use `*.instructions.md` instead.

## Common Pitfalls

- **Vague Activation Triggers**: Using broad descriptions that lack specific CLI keywords, causing the skill to remain dormant or activate incorrectly.
- **Circular Loading Loops**: Creating `## Related Skills` references that point back to a parent or create cycles, leading to context corruption.
- **Interactive Hangs**: Including command examples that wait for human input (e.g., `gh pr merge` without flags) in autonomous agent workflows.

Generate or update Agent Skills for coding agents, ensuring
precise activation, concise expert-level guidance, and full compliance with
the portable progressive loading architecture.

## Core Process

1. **Infer Name & Context**: Determine a unique, descriptive `name` in lowercase-hyphenated format that will exactly match the folder name.
2. **Draft the Description**: Write a keyword-dense `description` (10–1024 characters) wrapped in single quotes that clearly states WHAT the skill does and WHEN to use it.
3. **Structure the File**: Follow the exact layout specified in `Skill Structure & Formatting`.
4. **Enforce Style**: Write imperative, expert-level instructions. Focus on what the agent doesn't know (quirks, internal conventions, Common Pitfalls). Skip standard language syntax.
5. **Manage Context Budget**: Keep `SKILL.md` under 500 lines (ideally <200). Split large workflows or detailed references into a `references/` directory.
6. **Preserve Quality**: When updating, always choose the better, clearer sections. If previous changes are better, leave them intact. Always pick the best format.
7. **Output**: Output ONLY the complete, ready-to-commit file content without conversational wrappers. Do not explain changes unless requested.

## Core Principles

- **Autonomous Execution Focus**: Write for non-interactive agent flow: self-contained loops, built-in error recovery, verification steps, and no user confirmation prompts except for safety-critical actions.
- **YAML Frontmatter is Mandatory**: Begin every SKILL.md with required fields `name` (lowercase-hyphenated, exactly matching folder name) and `description` (single-line, keyword-dense, wrapped in single quotes). Include `license` only if needed. YAML must pass all repository validation rules.
- **Description Precision**: Write the `description` as a single, highly specific sentence that matches user intent patterns without overlap—poor phrasing causes missed or false activations.
- **Avoid Hardcoding**: Never embed specific values, file paths, repository names, user details, or tool versions; instead, use clear placeholders (e.g., `<repository-name>`, `<file-path>`, `<version>`).
- **Pure Markdown Body**: Use only Markdown in the body; never include extraneous files, scripts, or resources unless explicitly required for the skill.
- **Common Pitfalls are High Signal**: Always include a `## Common Pitfalls` section for documenting proactive warnings about non-obvious behavior.

## Skill Structure & Formatting

Structure the generated file with the following sections (omit optional ones if unused):

1. **YAML Frontmatter block**
   Must include `name`, `description`, and `license` (MIT).
   For the `description`, append `"You MUST load this skill when <condition>"` ONLY for exact, unambiguous triggers (e.g., a specific CLI command).
   Omit this phrase for general-purpose skills. Split long sentences into multiple lines.
2. **Title (`# Skill Name`)**
3. **Markdownlint overrides** (e.g., `<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->`)
4. **`## When to Use`**:
   Concrete scenarios reinforcing description triggers.
   **Bullet points** (concise and strictly relevant).
   Use to clarify exact activation conditions. Skip generic filler.
5. **`## When Not to Use`**:
   Explicit non-triggers to prevent false activation.
   **Bullet points** (focus on non-obvious edge cases and overlaps).
   Use to set clear boundaries against similar out-of-scope tasks; skip obvious exclusions.
7. **Section Discipline**: Use standard sections in a logical progression:
   - `## Prerequisites` (Optional):
     Required tools, dependencies, or environment setup.
     **Requirement → Why it's needed**.
     Use when the skill cannot function without specific external setup.
   - `## Core Process` or `## Step-by-Step Workflows`:
     Sequential, repeatable procedure(s).
     **Numbered steps**, each imperative and verifiable.
     Use `## Core Process` for a single canonical flow; use `## Step-by-Step Workflows` when the skill covers several related tasks (e.g., "Create", "Update", "Migrate").
     - `### Workflow` (Optional):
       Named sub-flow within a process section.
       **Workflow Name → ordered steps**.
       Use when a single process branches into multiple distinct named variants.
   - `## Core Principles`:
     Non-negotiable rules that shape every decision.
     **Principle → Rationale** (short).
     Use for invariants the agent must always uphold, regardless of task.
   - `## Best Practices`:
     Recommended (but not mandatory) techniques.
     **Practice → Why it helps**.
     Use for guidance that improves quality but isn't strictly required.
   - `## What to Avoid`:
     Anti-patterns and forbidden behaviors.
     **Anti-pattern → Why it's harmful**.
     Use for explicit "do NOT do this" guidance distinct from preventable mistakes (Common Pitfalls).
   - `## Limitations`:
     Known boundaries of what this skill can accomplish.
     **Limitation → Workaround (if any)**.
     Use to set realistic expectations and prevent the agent from attempting impossible tasks.
   - `## Common Pitfalls`:
     Proactive prevention for non-obvious traps and edge cases.
     **Pitfall → Prevention/Solution**.
     Use to stop likely agent mistakes; skip generic or obvious advice.
   - `## Troubleshooting`:
     Reactive recovery.
     **Symptom → Diagnosis/Fix**.
     Use to help the agent identify, isolate, and recover from problems that already occurred.
   - `## References`:
     Links to `references/` files or external resources.
     **Title → URL or relative path**.
     Use to enable progressive loading of long-form content without bloating `SKILL.md`.
   - `## Related Skills`:
     Other skills that complement this one.
     **Skill name → When to load it**.
     Use to suggest companion skills while avoiding circular dependencies (e.g. don't link parent skills).

Note: Keep unordered lists in order for better readability.

## Bundling Resources

If the skill requires additional files, organize them into these specific folders and reference them via relative paths in `SKILL.md` (up to 2 levels deep from the skill root):

| Directory | Purpose | Loaded into Context? |
| --------- | ------- | -------------------- |
| `scripts/` | Executable automation (`.py`, `.ps1`, `.ts`, `.sh`). | Only when executed |
| `references/` | Documentation the agent reads to inform decisions. | Yes, when referenced |
| `assets/` | Static files used AS-IS in output (not modified by agent). | No |
| `templates/` | Starter code/scaffolds that the agent MODIFIES. | Yes, when referenced |

**Script Requirements**: Prefer cross-platform languages (Python, Node.js, PowerShell). Scripts must handle errors gracefully and avoid storing credentials.

## Writing Style & Philosophy

- Write dense, imperative, expert-level instructions assuming ninja proficiency.
- Skip basics, favor one-liners, pack maximum depth.
- **Example Discipline**: Use fewer, shorter examples. Include only essential examples that demonstrate key patterns. Quality over quantity.
- **Command-Line Tool Examples**: Derive usage dynamically via read/glob operations. Provide concise examples of key commands—focus on complex, multi-flag, piped, or non-standard operations.
- **Skill Length Management**: Keep `SKILL.md` under 500 lines (ideally <200). Use `references/` for progressive loading of long content.

## Common Pitfalls to Avoid

- **Too Vague**: "Make the code better" → Specify exactly what "better" means.
- **Too Restrictive**: Over-constraining can prevent useful optimizations.
- **Missing Context**: Include relevant domain knowledge and terminology.
- **No Examples**: Concrete examples guide LLM better than abstract descriptions.
- **Ignoring Artifacts**: Don't refine prompts based on error feedback.

## What to Avoid

- Vague `description` fields that lack specific triggers, keywords, or capabilities.
- Using interactive command examples without explicitly warning against them.
- Creating excessively long files with redundant examples.
- Explaining basic concepts that a proficient developer or AI agent would already know.
- Outputting conversational filler. ONLY output the file content.

## Limitations

- The skill writer cannot test the activation triggers of the new skill in real-time; it relies on following the description precision rule to ensure proper loading.

## References

- [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)

## Related Skills

- **critical-thinking**:
  You MUST load this skill when deconstructing complex requirements into focused, atomic skill instructions.
- **docs-writer**:
  You MUST load this skill when asked to write, document, or generate new documentation.
- **agentskills**:
  You MUST load this skill when designing or manually creating agent skills.
