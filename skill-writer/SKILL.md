---
name: skill-writer
description: >-
  When the user requests to create, update, or refine a GitHub Copilot skill,
  generate or revise a complete SKILL.md file that strictly adheres to the
  official format, validation rules, and community best practices.
  You MUST load this skill when creating or updating GitHub Copilot skill files.
license: MIT
---

# Skill Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generate or update SKILL.md files for GitHub Copilot coding agents, ensuring
precise activation, concise expert-level guidance, and full compliance with
repository standards.

## Core Process

1. **Infer Name & Context**: Determine a unique, descriptive `name` in lowercase-hyphenated format that will exactly match the folder name.
2. **Draft the Description**: Write a single, highly precise `description` sentence capturing exact activation triggers without overlap.
3. **Structure the File**: Follow the exact layout specified in `Skill Structure & Formatting`.
4. **Enforce Style**: Write dense, imperative, expert-level instructions assuming ninja proficiency; skip basics, favor one-liners.
5. **Output**: Output ONLY the complete, ready-to-commit SKILL.md content without conversational wrappers. Do not explain the changes unless requested.

## Core Principles

- **Autonomous Execution Focus**: Write for non-interactive agent flow: self-contained loops, built-in error recovery, verification steps, and no user confirmation prompts except for safety-critical actions.
- **YAML Frontmatter is Mandatory**: Begin every SKILL.md with required fields `name` (lowercase-hyphenated, exactly matching folder name) and `description` (one precise, activation-triggering sentence). Include `license` only if needed. YAML must pass all repository validation rules.
- **Description Precision**: Write the `description` as a single, highly specific sentence that matches user intent patterns without overlap—poor phrasing causes missed or false activations.
- **Avoid Hardcoding**: Never embed specific values, file paths, repository names, user details, or tool versions; instead, use clear placeholders (e.g., `<repository-name>`, `<file-path>`, `<version>`).
- **Pure Markdown Body**: Use only Markdown in the body; never include extraneous files, scripts, or resources unless explicitly required for the skill.

## Skill Structure & Formatting

Structure the file exactly as:

1. **YAML frontmatter block**
2. **Title (`# Skill Name`)**
3. **Markdownlint overrides** (e.g., `<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->`)
4. **Brief Intro** (1-2 sentences)
5. **Section Discipline**: Use standard sections in a logical progression:
   - `## Core Process` (if a step-by-step flow is needed)
   - `## Core Principles`
   - `## Commands / Usage Patterns`
   - `## Diagnostics and Troubleshooting`
   - `## What to Avoid`
   - `## Limitations`
   - `## Related Skills`

## Writing Style & Philosophy

- Write dense, imperative, expert-level instructions assuming ninja proficiency.
- Skip basics, favor one-liners, pack maximum depth.
- **Example Discipline**: Use fewer, shorter examples. Include only essential examples that demonstrate key patterns. Prefer single-line examples over multi-line blocks. Quality over quantity.
- **Command-Line Tool Examples**: When the skill involves command-line tools, derive their usage dynamically via read/glob operations to maximize skill generality. Provide concise examples of key commands—focus on complex, multi-flag, piped, or non-standard operations.
- **Skill Length Management**: Keep skills concise and focused. If a skill approaches 300 lines, or if content becomes unfocused, split it into multiple specialized skills with narrow, non-overlapping activation descriptions.

## What to Avoid

- Overly broad `description` fields that might trigger the skill when not needed.
- Using interactive command examples (e.g., `git rebase -i`) without explicitly warning against them or providing non-interactive alternatives.
- Creating excessively long files with redundant examples.
- Explaining basic concepts that a proficient developer or AI agent would already know.
- Outputting conversational filler. ONLY output the file content.

## Limitations

- The skill writer cannot test the activation triggers of the new skill in real-time; it relies on following the description precision rule to ensure proper loading.

## Related Skills

- **docs-writer**:
  You MUST load this skill when asked to write, document, or generate new documentation.
