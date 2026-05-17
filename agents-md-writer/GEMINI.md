# GEMINI.md (agents-md-writer)

## Setup & Environment Invariants

- Follow the organizational baseline structure for `AGENTS.md` files.
- Ensure high-density, contract-style imperatives.

## Requirements

- Gemini CLI for Google Gemini.
- Markdown linting tools.

## Key Files & Context Injection

- `SKILL.md`: Source of truth for the `agents-md-writer` skill.
- `AGENTS.md`: Shared project-wide instructions.

## Agent Directives (Contract Style)

- Use Gemini CLI's `/memory show` to verify combined context if needed.
- Adhere to the structure defined in `SKILL.md` when generating or updating `AGENTS.md` files.
- Prioritize subdirectory-specific `GEMINI.md` or `AGENTS.md` context.

## Common Tasks

- Generate new `AGENTS.md` files in subdirectories.
- Update existing `AGENTS.md` files to match the baseline.

## Related Prompts or Skills (load when relevant)

- `agents-md-writer`: The primary skill for managing these files.

## Testing & Verification Gates

- Run `markdownlint` on any generated content.
- Verify headers match the mandatory list in `SKILL.md`.

## Maintenance

- Keep `GEMINI.md` synchronized with `SKILL.md` and `AGENTS.md`.

## Final Assurance Gates

- Ensure no conversational filler is present.
- Use placeholders for environment-specific values.

## Troubleshooting Matrix

- If context is missing, check `/memory show` to ensure `GEMINI.md` was correctly loaded.
