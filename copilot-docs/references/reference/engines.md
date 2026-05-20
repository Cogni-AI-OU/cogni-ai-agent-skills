# AI Engines (aka Coding Agents)

GitHub Agentic Workflows use AI Engines (normally a coding agent) to interpret and execute natural language instructions.

## Available Coding Agents

Set `engine:` in your workflow frontmatter and configure the corresponding secret:

| Engine | `engine:` value | Required Secret |
| :--- | :--- | :--- |
| **GitHub Copilot CLI** (default) | `copilot` | `COPILOT_GITHUB_TOKEN` |
| **Claude by Anthropic** | `claude` | `ANTHROPIC_API_KEY` |
| **OpenAI Codex** | `codex` | `OPENAI_API_KEY` |
| **Google Gemini CLI** | `gemini` | `GEMINI_API_KEY` |
| **Crush** (experimental) | `crush` | `COPILOT_GITHUB_TOKEN` |
| **OpenCode** (experimental) | `opencode` | `COPILOT_GITHUB_TOKEN` |
| **Pi** (experimental) | `pi` | `COPILOT_GITHUB_TOKEN` (default); switches to provider secret with `provider/model` format |

Copilot CLI is the default — `engine:` can be omitted when using Copilot.

## Engine Feature Comparison

| Feature | Copilot | Claude | Codex | Gemini | Crush | OpenCode | Pi |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `max-runs` (AWF invocation cap) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `max-turns` | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `max-continuations` (Autopilot) | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `engine.agent` (Custom agent file) | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| `engine.api-target` (Custom endpoint) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `engine.bare` (Disable context) | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |

## Extended Coding Agent Configuration

Workflows can specify extended configuration for the coding agent:

```yaml
engine:
  id: copilot
  version: latest                       # defaults to latest
  model: gpt-5                          # example override; omit to use engine default
  command: /usr/local/bin/copilot       # custom executable path
  args: ["--add-dir", "/workspace"]     # custom CLI arguments
  agent: agent-id                       # custom agent file identifier
  api-target: api.acme.ghe.com          # custom API endpoint hostname (GHEC/GHES)
```

### Pinning a Specific Engine Version

By default, workflows install the latest available version of each engine CLI.
To pin to a specific version, set `version` to the desired release:

```yaml
engine:
  id: copilot
  version: "0.0.422"
```

### Copilot Custom Configuration

Use `agent` to reference a custom agent file in `.github/agents/` (omit the `.agent.md` extension):

```yaml
engine:
  id: copilot
  agent: technical-doc-writer  # references .github/agents/technical-doc-writer.agent.md
```

### Bare Mode (`bare`)

Set `engine.bare: true` to disable automatic loading of context (memory files, `AGENTS.md`)
and custom instructions by the engine.

```yaml
engine:
  id: claude
  bare: true
```

## Timeout Configuration

| Timeout Knob | Description |
| :--- | :--- |
| `timeout-minutes` | Job-level wall clock limit (Default: 20m) |
| `tools.timeout` | Per tool-call limit in seconds |
| `max-turns` | Iteration budget (Claude only) |
| `max-continuations` | Autopilot run budget (Copilot only) |

## References

- [AI Engines (Coding Agents)](https://github.github.com/gh-aw/reference/engines/)
