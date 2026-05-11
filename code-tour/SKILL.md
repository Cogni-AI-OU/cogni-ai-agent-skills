---
name: code-tour
description: >-
  Create, update, and maintain VSCode CodeTour (.tour) JSON walkthrough files with full schema compliance and interactive step configuration.
  You MUST load this skill when creating or updating .tours/ files.
---

# Code Tour

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Expert guidance for creating and maintaining VSCode CodeTour files, providing structured onboarding walkthroughs with comprehensive schema support.

## Core Process

1. **Analyze Target**: Identify learning objectives, key architecture concepts, and codebase entry points.
2. **Scaffold Structure**: Create `.tours/` directory and `.tour` JSON files following standard CodeTour schema.
3. **Draft Sequence**: Define progressive steps using `file`, `line`, `directory`, or `pattern` selectors.
4. **Enrich Content**: Add CodeTour-flavored Markdown, `>>` shell commands, and `[link](command:...)` triggers.
5. **Verify Navigation**: Ensure step references (`[#stepNumber]`) and `nextTour` sequencing are valid.

## Core Principles

- **Progressive Disclosure**: Begin with high-level conceptual steps before diving into specific line-level implementations.
- **Robust Selectors**: Prefer regex `pattern` or `directory` over brittle `line` numbers where code is volatile.
- **Self-Contained Content**: Use Markdown code blocks for interactive tutorials and `{{VARIABLE_NAME}}` for environment specifics.

## Usage Patterns

### Primary Tour Initialization

```json
{
  "title": "1 - Getting Started",
  "isPrimary": true,
  "nextTour": "2 - Core Architecture",
  "steps": [
    {
      "title": "Introduction",
      "description": "# Welcome\n\nThis tour guides you through the primary application flow."
    }
  ]
}
```

### Advanced Step Configuration

```json
{
  "steps": [
    {
      "title": "Service Implementation",
      "description": "Notice how the [tests](command:workbench.action.tasks.test) evaluate this function.\n\n>> npm run test",
      "file": "src/service.ts",
      "pattern": "export class MainService",
      "commands": ["command.id?[\"arg1\"]"]
    }
  ]
}
```

## What to Avoid

- Avoid relying strictly on hardcoded `line` numbers for rapidly changing files; use `pattern` instead.
- Do not create excessively long tours; break them up and link via `nextTour`.
- Do not place tours outside of `.tours/`, `.vscode/tours/`, or `.github/tours/`.

## Limitations

- The agent cannot visually verify the CodeTour rendering; rely on strict JSON schema validation.
