---
name: agent-md
description: Syntax and structure reference for GitHub Copilot custom agent persona files and OpenCode agent definitions. Use this to understand the schema and format of agent persona definitions across platforms.
license: MIT
---

# Agent MD Syntax

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Agent MD is a format for defining specialized agent personas. These files provide context-specific instructions, project knowledge, and execution boundaries for autonomous agents in GitHub Copilot and OpenCode.

## Target Locations

### GitHub Copilot

Agent persona files for GitHub Copilot MUST be located in:
- `.github/agents/` directory of the repository.
- The filename SHOULD match the agent's `name` property with `.agent.md` extension (e.g., `.github/agents/test-agent.agent.md`).

### Claude Code

Claude Code uses `CLAUDE.md` for project-level instructions:
- **Project-level:** `CLAUDE.md` at the repository root.
- **Subdirectory-level:** `CLAUDE.md` within a specific directory (applies to that subtree).
- **Global:** `~/.claude/CLAUDE.md` for machine-wide preferences.
- **Local overrides:** `CLAUDE.local.md` (typically gitignored).

### OpenCode

OpenCode agents can be defined globally or per-project:
- **Global:** `~/.config/opencode/agents/`
- **Per-project:** `.opencode/agents/`
- **Configuration:** Configure agents in your `opencode.json` config file under the `agent` key.

## GitHub Copilot Agent Syntax

An Agent MD file for Copilot consists of YAML frontmatter followed by a structured Markdown body.

### Agent profile format

Agent profiles are Markdown files with YAML frontmatter.

| Field | Description | Requirement |
| :--- | :--- | :--- |
| `name` | The unique identifier for the agent (e.g., `test-agent`) | Mandatory |
| `description` | A concise one-sentence description of the agent's purpose | Mandatory |
| `tools` | List of enabled tools (e.g., `['read', 'search', 'edit']`) | Recommended |

## OpenCode Agent Syntax

OpenCode supports both JSON configuration and Markdown files for agent definitions.

### JSON Configuration (`opencode.json`)

```json
{
  "agent": {
    "my-agent": {
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:./prompts/my-agent.txt}",
      "permission": {
        "edit": "allow",
        "bash": "allow"
      }
    }
  }
}
```

### Markdown Agent Frontmatter

Markdown files in the OpenCode agent directories use more extensive frontmatter:

| Field | Description |
| :--- | :--- |
| `description` | Concise description of the agent's purpose (Required). |
| `mode` | `primary`, `subagent`, or `all` (Defaults to `all`). |
| `model` | Override the model for this agent (e.g., `openai/gpt-5`). |
| `temperature` | Control randomness (0.0 to 1.0). |
| `permission` | Fine-grained tool permissions (`allow`, `ask`, `deny`). |
| `steps` | Max agentic iterations before forcing a response. |
| `prompt` | Path to a custom system prompt file. |
| `hidden` | `true` to hide from `@` autocomplete (subagents only). |

## Claude Code Syntax (`CLAUDE.md`)

Claude Code uses a simple Markdown-based format. It does not require YAML frontmatter.

### Common Sections

| Section | Description |
| :--- | :--- |
| **Build Commands** | Exact strings to build the project. |
| **Test Commands** | Exact strings to run tests (e.g., `npm test`). |
| **Lint Commands** | Commands to check/fix code style. |
| **Code Style** | Specific preferences (e.g., "Use named exports"). |
| **Architecture** | High-level map of the codebase. |

### Advanced Syntax

- **`@imports`**: Use `@path/to/file` to include other files (e.g., `@AGENTS.md`).
- **`Read when:`**: Conditional trigger for loading detailed documentation (e.g., `Read when: Modifying database schema`).

## Core Markdown Sections

Regardless of the platform, a high-quality agent definition should include:

1. **Role Definition**: Explicitly state the agent's persona and specialization.
2. **Project Knowledge**: Tech stack, versions, and relevant directory layout.
3. **Executable Commands**: Real commands (build, test, lint) with all necessary flags.
4. **Standards & Examples**: Idiomatic code snippets showing the expected style.
5. **Three-Tier Boundaries**: Using `Always`, `Ask first`, and `Never` categories.

## Reference Structure (GitHub Copilot)

```markdown
---
name: <agent-name>
description: <one-sentence description>
tools: ['read', 'search', 'edit']
---

You are an expert <role> for this project.

## Your role
- You specialize in <specialty>
- Your task: <specific task>

## Project knowledge
- **Tech Stack:** <technologies with versions>
- **File Structure:**
  - `src/` - <purpose>
  - `tests/` - <purpose>

## Commands you can use
- **Build:** `<command>`
- **Test:** `<command>`
- **Lint:** `<command>`

## Standards
<Code style examples>

## Boundaries
- ✅ **Always:** <mandatory actions>
- ⚠️ **Ask first:** <guarded actions>
- 🚫 **Never:** <prohibited actions, e.g., commit secrets>
```

## Related Skills

- **agent-md-writer**:
  Load this skill when you need guidance on *how* to write and optimize high-performance agent personas.
- **agents-md-writer**:
  Load this skill for general `AGENTS.md` project context files.
- **skill-writer**:
  Load this skill when writing `SKILL.md` files for Copilot skills.

## References

- [About custom agents](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents)
- [Your first custom agent](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents/your-first-custom-agent)
- [OpenCode Agents Documentation](https://opencode.ai/docs/agents/)
- [Claude Code Documentation](https://code.claude.com/docs/en/memory)
