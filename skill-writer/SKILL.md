---
name: skill-writer
description: 'When the user requests to create, update, or refine a GitHub Copilot skill, generate or revise a complete SKILL.md file that strictly adheres to the official format, validation rules, and progressive loading best practices. Use this when writing agent skills, defining capabilities, structuring SKILL.md, or bundling resources (scripts, templates, references).'
license: MIT
---

# Skill Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generate or update Agent Skills for GitHub Copilot coding agents, ensuring
precise activation, concise expert-level guidance, and full compliance with
the portable progressive loading architecture.

## When to Use This Skill

- User asks to create a new Copilot skill
- User needs to update or refine an existing `SKILL.md`
- User wants to bundle scripts, templates, or references with a skill
- User is troubleshooting skill activation or context limits

## Core Process

1. **Infer Name & Context**: Determine a unique, descriptive `name` in lowercase-hyphenated format (max 64 chars).
2. **Draft the Description**: Write a keyword-dense `description` (10–1024 characters) wrapped in single quotes that clearly states WHAT the skill does and WHEN to use it.
3. **Structure the File**: Follow the exact layout specified in `SKILL.md Required Format`.
4. **Enforce Style**: Write imperative, expert-level instructions. Focus on what Copilot doesn't know (quirks, internal conventions, gotchas). Skip standard language syntax.
5. **Manage Context Budget**: Keep `SKILL.md` under 500 lines (ideally <200). Split large workflows or detailed references into a `references/` directory.
6. **Output**: Output ONLY the complete, ready-to-commit file content without conversational wrappers. Do not explain changes unless requested.

## SKILL.md Required Format

Structure the generated file with the following sections (omit optional ones if unused):

1. **YAML Frontmatter** (Required)
   - `name`: Lowercase-hyphenated, max 64 chars.
   - `description`: Wrapped in single quotes. Must define WHAT, WHEN, and keywords.
   - `license`: Reference to `LICENSE.txt` or SPDX identifier.
2. **Title (`# Skill Name`)**: Brief overview of what the skill enables.
3. **Markdownlint Overrides** (e.g., `<!-- markdownlint-disable MD013 -->`)
4. **`## When to Use This Skill`**: Bullet list of concrete scenarios reinforcing description triggers.
5. **`## Prerequisites`** (Optional): Required tools, dependencies, or environment setup with install commands.
6. **`## Step-by-Step Workflows`** (Optional): Numbered steps strictly for repeatable procedures where sequence matters (e.g., build, deploy). Prefer flexible guidelines over rigid steps for open-ended tasks.
7. **`## Gotchas`** (High Signal): Proactive warnings about non-obvious behavior. Bold the key constraint, then explain why.
8. **`## Troubleshooting`** (Optional): Reactive fixes for known issues presented as a symptom → solution table.
9. **`## References`** (Optional): Links to bundled files or external resources. Use relative paths for bundled files.

## Bundling Resources

If the skill requires additional files, organize them into these specific folders and reference them via relative paths in `SKILL.md`:

| Directory | Purpose | Loaded into Context? |
| --------- | ------- | -------------------- |
| `scripts/` | Executable automation (`.py`, `.ps1`, `.ts`, `.sh`). | Only when executed |
| `references/` | Documentation the agent reads to inform decisions. Use for long content. | Yes, when referenced |
| `assets/` | Static files used AS-IS in output (not modified by the agent). | No |
| `templates/` | Starter code/scaffolds that the agent MODIFIES and builds upon. | Yes, when referenced |

**Script Requirements**: When bundling scripts, prefer cross-platform languages (Python, Node.js, PowerShell) or Bash for simple tasks. Scripts must handle errors gracefully and avoid storing credentials.

## Writing Style & Philosophy

- Use imperative mood: "Run", "Create", "Configure" (not "You should run").
- Be specific and actionable; include exact commands with parameters.
- **Gotchas are your highest-signal content**. Add gotchas for non-obvious defaults, version-specific quirks, and API traps.
- **Flexible over Rigid**: For tasks like debugging or refactoring, provide decision criteria rather than rigid numbered steps.

## What to Avoid

- Vague `description` fields that lack specific triggers, keywords, or capabilities.
- Explaining basic concepts that Copilot already knows from its training data.
- Excessively long `SKILL.md` files; use `references/` for progressive loading.
- Hardcoding file paths or repository names where placeholders are more appropriate.

## Related Skills

- **critical-thinking**:
  You MUST load this skill when deconstructing complex requirements into focused, atomic skill instructions.
- **docs-writer**:
  You MUST load this skill when asked to write, document, or generate new documentation.
