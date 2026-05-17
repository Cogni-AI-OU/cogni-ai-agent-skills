---
name: skill-writer
description: 'Generate or refine agent skills. You MUST load this skill when creating, updating, or structuring SKILL.md files and bundling their resources.'
license: MIT
---

# Skill Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generate or update Agent Skills for coding agents, ensuring
precise activation, concise expert-level guidance, and full compliance with
the portable progressive loading architecture.

## When to Use This Skill

- User asks to create a new agent skill
- User needs to update or refine an existing `SKILL.md`
- User wants to bundle scripts, templates, or references with a skill
- User is troubleshooting skill activation or context limits

## Core Process

1. **Infer Name & Context**: Determine a unique, descriptive `name` in lowercase-hyphenated format that will exactly match the folder name.
2. **Draft the Description**: Write a keyword-dense `description` (10–1024 characters) wrapped in single quotes that clearly states WHAT the skill does and WHEN to use it.
3. **Structure the File**: Follow the exact layout specified in `Skill Structure & Formatting`.
4. **Enforce Style**: Write imperative, expert-level instructions. Focus on what the agent doesn't know (quirks, internal conventions, gotchas). Skip standard language syntax.
5. **Manage Context Budget**: Keep `SKILL.md` under 500 lines (ideally <200). Split large workflows or detailed references into a `references/` directory.
6. **Output**: Output ONLY the complete, ready-to-commit file content without conversational wrappers. Do not explain changes unless requested.

## Core Principles

- **Autonomous Execution Focus**: Write for non-interactive agent flow: self-contained loops, built-in error recovery, verification steps, and no user confirmation prompts except for safety-critical actions.
- **YAML Frontmatter is Mandatory**: Begin every SKILL.md with required fields `name` (lowercase-hyphenated, exactly matching folder name) and `description` (single-line, keyword-dense, wrapped in single quotes). Include `license` only if needed. YAML must pass all repository validation rules.
- **Description Precision**: Write the `description` as a single, highly specific sentence that matches user intent patterns without overlap—poor phrasing causes missed or false activations.
- **Avoid Hardcoding**: Never embed specific values, file paths, repository names, user details, or tool versions; instead, use clear placeholders (e.g., `<repository-name>`, `<file-path>`, `<version>`).
- **Pure Markdown Body**: Use only Markdown in the body; never include extraneous files, scripts, or resources unless explicitly required for the skill.
- **Gotchas are High Signal**: Always include a `## Gotchas` section for documenting proactive warnings about non-obvious behavior.

## Skill Structure & Formatting

Structure the generated file with the following sections (omit optional ones if unused):

1. **YAML Frontmatter block**
2. **Title (`# Skill Name`)**
3. **Markdownlint overrides** (e.g., `<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->`)
4. **`## When to Use This Skill`**: Concrete scenarios reinforcing description triggers.
5. **Section Discipline**: Use standard sections in a logical progression:
   - `## Prerequisites` (Optional): Required tools, dependencies, or environment setup.
   - `## Core Process` or `## Step-by-Step Workflows`: For repeatable procedures where sequence matters.
   - `## Core Principles`
   - `## Gotchas`: Proactive warnings (Bold the key constraint, then explain why).
   - `## Troubleshooting`: Reactive fixes (Symptom → Solution table).
   - `## Best Practices`
   - `## What to Avoid`
   - `## Limitations`
   - `## References`: Links to bundled files or external resources.
   - `## Related Skills`

## Bundling Resources

If the skill requires additional files, organize them into these specific folders and reference them via relative paths in `SKILL.md`:

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
