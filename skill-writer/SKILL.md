<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->

---
name: skill-writer
description: >-
  When the user requests to create, update, or refine a GitHub Copilot skill,
  generate or revise a complete SKILL.md file that strictly adheres to the
  official format, validation rules, and community best practices.
---

# Skill Writer

Generate or update SKILL.md files for GitHub Copilot coding agents, ensuring
precise activation, concise expert-level guidance, and full compliance with
repository standards.

## When to Activate

- User explicitly asks to create or update a skill for a specific issue, topic
  or task.
- User requests to update, improve, or refactor an existing SKILL.md.
- User provides new rules, examples, or feedback intended to guide skill
  authoring.
- Capture Agent Insights: When the agent struggles with a recurring task,
  encounters repeated failures, or discovers an effective new solution/workaround
  not already documented, update the relevant existing skill (or create a new
  one) to incorporate the insight, ensuring future activations handle the case
  more efficiently.

## Core Process

1. Infer a unique, descriptive `name` in lowercase-hyphenated format that will
   exactly match the intended folder name.

2. Write a single, highly precise `description` sentence that captures exact
   activation triggers without overlap.

3. Validate that the YAML frontmatter follows all repository-defined schema,
   linting, and validation rules (e.g., required fields, no extra keys, correct
   formatting).

4. Structure the file exactly as:
   - First line: `<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->`
   - YAML frontmatter block
   - Pure Markdown body with minimal, value-adding sections only

5. Write dense, imperative, expert-level instructions assuming ninja
   proficiency; skip basics, favor one-liners, pack maximum depth.

6. Design for fully autonomous agent execution: include self-contained loops,
   error recovery, verification steps; avoid any user confirmation except
   safety-critical cases.

7. Keep total length to minimum.

8. Section Discipline: Use sections sparingly and only when they clearly improve
   readability or organization; always follow a logical progression
   (e.g., Brief Intro → When to Activate → Core Process → Diagnostics
   → Patterns → What to Avoid → Limitations → Safety).

9. Output only the complete, ready-to-commit SKILL.md content.

## Guidance on Creating or Updating Skills

When creating or updating a skill file, ensure the following format:

- **YAML Frontmatter is Mandatory**: Begin every SKILL.md with required fields
  `name` (lowercase-hyphenated, exactly matching folder name) and `description`
  (one precise, activation-triggering sentence explaining exactly what the skill
  does and when Copilot should load it). Include `license` only if needed. YAML
  must pass all repository validation and linting rules.

- **Start with Lint Disable**: Always open the file with
  `<!-- markdownlint-disable MD022 MD026 MD041 -->` to suppress common
  markdownlint warnings.

- **Description Precision**: Write the `description` as a single, highly
  specific sentence that matches user intent patterns without overlap—poor
  phrasing causes missed or false activations.

- **Pure Markdown Body**: Use only Markdown in the body; never include
  extraneous files, scripts, or resources unless explicitly required for the
  skill.

- **Section Discipline**: Use sections sparingly and only when they add clear
  value; prioritize logical flow (e.g., Core Process → Diagnostics → Patterns →
  Limitations → Safety).

- **Autonomous Execution Focus**: Write for non-interactive agent flow:
  self-contained loops, built-in error recovery, verification steps, and no user
  confirmation prompts except for safety-critical actions.

- **Skill Length Management**: If a skill exceeds or approaches 400 lines, or
  if content becomes unfocused, split it into multiple specialized skills with
  narrow, non-overlapping activation descriptions to maintain conciseness,
  precise triggering, and efficient token usage.

- **Avoid Hardcoding**: Never embed specific values, file paths, repository
  names, user details, or tool versions; instead, use clear placeholders (e.g.,
  `<repository-name>`, `<file-path>`, `<version>`).

- **Command-Line Tool Examples**: When the skill involves command-line tools,
  derive them dynamically via tools/read operations to maximize skill generality
  and cross-project reusability. Always provide useful examples of key
  commands—especially for complex, multi-flag, piped, or non-standard
  operations—to ensure precise reproduction, minimize agent misinterpretation,
  and reduce execution failures.
