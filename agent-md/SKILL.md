---
name: agent-md
description: Syntax and structure reference for custom agent persona files (*.agent.md, CLAUDE.md, opencode.json). Use this to understand the schema, format, and architecture of agent definitions across platforms.
license: MIT
---

# Agent MD Syntax

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Agent MD is a format for defining specialized agent personas. These files provide context-specific instructions, project knowledge, and execution boundaries for autonomous agents in GitHub Copilot, OpenCode, and Claude Code. Unlike broad custom instructions, custom agents are selected for specific tasks and maintain their configuration throughout the workflow.

## When to Use

- **Platform Syntax Reference**: Defining and validating the exact YAML frontmatter and Markdown structure for `.agent.md`, `CLAUDE.md`, and `opencode.json`.
- **Architectural Alignment**: Correctly partitioning logic between Agents ("Who"), Skills ("How"), and Instructions ("Rules") to minimize context window bloat.
- **Scoped Persona Definition**: Creating specialized agents with tailored roles, tech stacks, and execution boundaries for repository or organizational use.
- **Tool & Permission Guardrails**: Mapping autonomous capabilities to specific tools (built-in or MCP) and defining safety boundaries via `Never`/`Ask first` rules.
- **Multi-Platform Configuration**: Standardizing agent behavior across GitHub Copilot, OpenCode, and Claude Code environments within a single codebase.

## When Not to Use

- **Domain Formatting Rules**: Setting pure coding conventions or style guides — these belong in `*.instructions.md`.
- **Mechanical Execution**: Defining step-by-step terminal commands or API workflows — these belong in `SKILL.md`.
- **One-off Interaction**: Simple chat prompts or quick clarifications that don't require a persistent persona or complex tool mapping.

## Common Pitfalls

- **The 500 KiB Wall**: GitHub truncates agent files beyond this limit; avoid embedding large documentation files directly—use relative links instead.
- **Absolute Path Breakage**: Using absolute URLs or paths within a repository; always use relative links to ensure portability across clones.
- **Role Overlap**: Creating multiple agents with ambiguous or overlapping scopes, which causes model confusion and activation drift.

## Architecture Principles: Agents vs Skills vs Instructions

To prevent redundancy and context drift, always enforce a strict conceptual boundary when authoring system components:

1. **Agents (`*.agent.md`) - The "Who" and "Why"**:
   - **Focus**:
     Persona, invariants, cognitive framework, escalation gates, and output constraints.
   - **Rule**:
     Do not embed explicit execution tutorials or command-by-command scripts here.
     Instruct the agent *who* they are, *what* constraints they must obey (e.g. "Never mutate files directly"),
     and explicitly tell them to invoke specific skills for mechanical processes.

2. **Skills (`SKILL.md`) - The "How" (Execution Playbooks)**:
   - **Focus**:
     Tools, commands, step-by-step procedures, and mechanical execution.
   - **Rule**:
     Isolates the exact `bash`, `gh`, or API mechanics.
     A skill is agnostic to *who* uses it.
     It exists strictly to define *how* an audit, a build, or a commit sync is correctly executed.

3. **Instructions (`*.instructions.md`) - The "Rules" (Domain Standards)**:
   - **Focus**:
     Formatting standards, coding conventions, and structural rules (e.g. JSON schema, Python dependencies).
   - **Rule**:
     Applied dynamically based on the file-type or project paths being modified.
     They govern the output structure regardless of which agent or skill generated it.

### When to Use What (Copilot Context)

- **Prompts**: Direct questions or commands in chat for one-off requests and quick clarifications (single conversation).
- **Instructions**: Global or workspace-level rules applied to all Copilot interactions (setting coding standards, preferences).
- **Chat Modes**: Pre-configured conversation contexts like `/explain` or `/fix` (single conversation session).
- **Custom Agents**: Specialized AI assistants with specific roles, capabilities, and deep context for complex workflows (activated per conversation).

## Target Locations

### GitHub Copilot

Agent persona files for GitHub Copilot can be defined at different levels:

- **Repository level:** Create `.github/agents/` in your repository for project-specific agents.
  - The filename SHOULD match the agent's `name` property with `.agent.md` extension (e.g., `.github/agents/test-agent.agent.md`).
- **Organization or enterprise level:** Create `/agents/` in a `.github-private` repository for broader availability.

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

Agent profiles are Markdown files with YAML frontmatter. In their simplest form, they include:

- **Name** (optional): A display name for the custom agent. If omitted, the agent's filename is used as its identifier and default display name.
- **Description**: Explains the agent's purpose and capabilities.
- **Version** (optional): Semantic versioning for tracking agent changes.
- **ApplyTo** (optional): File patterns (e.g., `['**/*.js']`) or scopes (e.g., `fileTypes`, `directories`) where the agent is most relevant.
- **Prompt**: Custom instructions that define the agent's behavior and expertise (the Markdown body).
- **Tools** (optional): Specific tools the agent can access. Common built-in tools include `read_file`, `write_file`, `search_files`, `list_directory`, and `run_terminal`. By default, agents can access all available tools, including built-in tools, and MCP server tools. Be cautious when granting `write_file` and `run_terminal` together.
- **MCP Servers** (optional): Configurations for MCP servers using the `mcp-servers` property.

### Technical Constraints (GitHub Copilot)

- **Size Limit**: Keep content under 500 KiB. GitHub truncates content beyond this limit.
- **Relative Links**: Use relative links (e.g., `docs/CONTRIBUTING.md`) instead of absolute URLs for files within the repository to ensure they work when the repository is cloned.

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
3. **File Types**: List specific file extensions or directories the agent is authorized to work with.
4. **Executable Commands**: Real commands (build, test, lint) with all necessary flags.
5. **Standards & Examples**: Idiomatic code snippets showing the expected style.
6. **Important Limitations**: Explicit "Negative Scope" (what the agent MUST NOT do).
7. **Three-Tier Boundaries**: Using `Always`, `Ask first`, and `Never` categories.

## Reference Structure (GitHub Copilot)

```markdown
---
name: <agent-name>
description: <one-sentence description>
version: 1.0.0
applyTo:
  - '**/*.js'
  - '**/*.ts'
tools:
  - read_file
  - search_files
  - list_directory
---

You are an expert <role> for this project.

## Your role
- You specialize in <specialty>
- Your task: <specific task>

## File types you work with
- `<extension/pattern>` (primary focus)
- `<other file type>`

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

## Important Limitations
- Do NOT <prohibited action related to scope>
- Do NOT <another scope boundary>

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
- **agent-skill-md-writer**:
  Load this skill when writing `SKILL.md` files for Copilot skills.

## References

- [About custom agents](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents)
- [Creating and using custom agents for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
- [Your first custom agent](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents/your-first-custom-agent)
- [OpenCode Agents Documentation](https://opencode.ai/docs/agents/)
- [Claude Code Documentation](https://code.claude.com/docs/en/memory)
- [Preparing to use custom agents in your organization](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents)
- [The Complete Guide to Configuring AI Coding Agents](https://vibecoding.app/blog/agents-md-guide)
