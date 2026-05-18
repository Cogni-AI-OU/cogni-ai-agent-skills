---
name: out-yaml
license: MIT
description: Instructs the agent to produce output strictly in valid YAML format, ensuring no conversational filler or markdown wrappers.
license: MIT
---
# Skill: out-yaml

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- When the task explicitly requires machine-parseable YAML output for pipeline consumption or automation.
- When producing structured data output that will be fed into downstream tools (e.g., CI/CD systems, config management, data processing).
- When the user asks for "YAML only" or "raw YAML" without any conversational wrapper or markdown formatting.
- When generating configuration files in YAML format that must be directly written to disk without extraction steps.

## When Not to Use
- When the output is intended for human reading — conversational context, explanations, and formatting aid comprehension.
- When the requested data cannot be represented in valid YAML (e.g., binary data, multi-line freeform text) — use appropriate output formats instead.
- When the user expects Markdown-formatted responses with code blocks — this skill strips all Markdown wrapping.
- When the output needs Markdown code block fencing for copy-paste convenience in chat interfaces.

## Common Pitfalls
- The agent cannot validate output against an arbitrary schema — it enforces YAML syntax only, not semantic correctness against a specific schema.
- Invisible characters, trailing spaces, or mixed indentation can cause YAML parse failures — the output must be strictly valid per the YAML spec.
- Comments in YAML use `#` — other comment styles (`//`, `/* */`, `<!-- -->`) are not valid YAML and will cause parsing errors.
- Non-YAML comment styles or explanations outside the YAML structure violate the zero-conversational-output constraint.

Instructs the agent to produce output strictly in valid YAML format, ensuring no conversational filler, markdown wrappers (like ```yaml), or additional explanations are present.

## Core Process

1. **Activate**: Triggered when the goal requires YAML output.
2. **Format**: Format the output entirely as valid YAML.
3. **Verify**: Ensure no text exists outside the YAML structure.
4. **Emit**: Output the YAML string directly.

## Core Principles

- **Strict Schema Adherence**: Output must be 100% valid YAML, parsable by standard YAML parsers.
- **Zero Conversational Output**: Absolutely no preambles, postambles, or explanatory text.
- **No Markdown Formatting**: Do not wrap the output in Markdown code blocks. Only emit raw YAML.

## Commands / Usage Patterns

Produce raw YAML as shown below:

```yaml
key: value
list:
  - item1
  - item2
```

## Diagnostics and Troubleshooting

- If parsers fail, check for invisible characters, invalid indentation, or unescaped strings.

## What to Avoid

- Including "Here is the YAML you requested:" or similar conversational text.
- Enclosing the output in Markdown backticks (e.g., ` ```yaml ... ``` `).
- Including non-YAML comment styles (e.g., `//`, `/* */`, `<!-- -->`) or omit comments entirely unless explicitly allowed.

## Limitations

- The agent cannot validate the output against a specific schema unless one is provided.
- Only enforces syntax, not semantic correctness.
