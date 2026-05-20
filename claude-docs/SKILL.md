---
name: claude-docs
description: 'Reference and APIs for retrieving Anthropic Claude documentation programmatically for LLMs. You MUST load this skill when asked to search or retrieve Claude or Claude Code documentation.'
license: MIT
---

# claude-docs

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- **Documentation Search**: Locating specific Claude Code or Anthropic Claude documentation articles.
- **Article Retrieval**: Fetching the full rendered markdown of a specific Claude docs page via its `llms.txt` or related context.

## When Not to Use

- **Claude API Operations**: Interacting with live Claude APIs to generate text. Use appropriate API endpoints or SDKs for that.

## Core Process

1. **Identify the Need**: Determine whether you need to search for a topic or fetch a specific known documentation path.
2. **Execute the Query**: Use `webfetch` to fetch the data from the llms.txt reference or relevant URLs.
3. **Process Content**: Extract the relevant information to answer the user's query or inform the ongoing task.

## References

- [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk.md)
  Includes: Get started, Capabilities (Built-in tools, Hooks, Subagents, MCP, Permissions, Sessions),
  Features (Agent SDK vs Client SDK, Agent SDK vs Claude Code CLI, Agent SDK vs Managed Agents),
  Compare the Agent SDK to other Claude tools, Guidelines.
- [Anthropic Developer Documentation](https://platform.claude.com/llms.txt)
- [Claude Docs](https://claude.com/llms.txt)
- [Claude Code Docs](https://code.claude.com/llms.txt)
