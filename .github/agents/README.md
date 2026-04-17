# Custom Agents

This folder contains custom agents designed to enhance your development workflow.
These agents are tailored to specific tasks and integrate seamlessly with GitHub Copilot and MCP servers.

## Available Agents

### [Code Tour Expert](code-tour.agent.md)

Expert agent for creating and maintaining VSCode CodeTour files. Features:

- Creating `.tours/` files with proper CodeTour schema
- Designing step-by-step walkthroughs for complex codebases
- Implementing interactive tours with command links and code snippets
- Setting up primary tours and tour linking sequences

**When to use**: Anytime you need to create or update `.tour` files for repository onboarding.

## How to Use Custom Agents

### Installation

- Download the desired agent configuration file (`*.agent.md`) and add it to your repository.
- Use the Copilot CLI for local testing: [Copilot CLI](https://gh.io/customagents/cli).
- Merge the agent configuration file into the default branch of your repository.
- Access installed agents through the VS Code Chat interface, Copilot CLI,
  or assign them in Copilot Coding Agent (CCA).

For more details, see:

- [About custom agents](https://gh.io/customagents)
- [Custom Agents Documentation](https://gh.io/customagents/config).
- [Create custom agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
- [Copilot CLI](https://gh.io/customagents/cli)
- [GitHub Awesome Copilot repository](https://github.com/github/awesome-copilot)
- [Supported Models](https://docs.github.com/en/copilot/reference/ai-models/supported-models)

## Customizing development environment

See: [Customizing the development environment for GitHub Copilot coding agent][customize-env].

## Firewall

See: [Customizing or disabling the firewall for GitHub Copilot coding agent][firewall-config].

### Firewall allowlist

See [FIREWALL.md](FIREWALL.md) for recommended hosts to allow and the official guidance link.

<!-- Named links -->

[customize-env]: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment
[firewall-config]: https://gh.io/copilot/firewall-config

### MCP Server Setup

Some agents require MCP servers to function. The Claude Code Action provides
built-in MCP servers for GitHub operations (`github_comment` and
`github_inline_comment`).

#### Custom MCP Servers

You can add custom MCP servers for additional integrations.

**Important notes:**

- File-based config cannot use GitHub Actions secrets (`${{ secrets.* }}`). Use
  inline config for secrets.
- HTTP-based MCP servers (using `"type": "http"`) may work with inline config
  but can fail with file-based config due to how the Claude Code process loads
  external files.
- **Current configuration**: This repository uses inline `--mcp-config` for the
  GitHub Copilot MCP endpoint (see `.github/workflows/claude-review.yml`) as it's
  an HTTP-based server. File-based config is available for custom command-based
  MCP servers if needed.

Follow the instructions in the agent's documentation to configure the necessary MCP servers.

## Security Considerations

### Claude Code Agent Git Access

When using Claude Code (triggered via `@claude` in comments), the agent has broad
git access via `Bash(git:*)` to enable autonomous code changes. This requires
proper repository safeguards.

**Access controls in place:**

- Only trusted users (OWNER, MEMBER, COLLABORATOR, CONTRIBUTOR) can trigger Claude
- PR/issue authors can only trigger Claude on their own content
- External contributors are explicitly blocked

**Required repository protections:**

Repository administrators must configure:

1. **Branch protection rules** on main/protected branches requiring PR reviews
   and status checks
2. **GitHub audit log monitoring** for `github-actions[bot]` commit activity
3. **CODEOWNERS** files for sensitive directories requiring specific approvals

**Best practices:**

- Review Claude's commits before merging PRs
- Use draft PRs for Claude's work requiring explicit promotion
- Monitor workflow logs for unexpected behavior
- Rotate API keys periodically

## Troubleshooting

### Claude Not Responding to Comments

If Claude isn't responding to your comments, verify:

1. **Permissions**: You must have one of these roles:
   - Repository OWNER, MEMBER, COLLABORATOR, or CONTRIBUTOR
   - PR/issue author (on your own content only)

2. **Trigger conditions** for PR review comments:
   - Your comment contains `@claude`, OR
   - You're replying to a comment from `github-actions[bot]` (Claude's responses), OR
   - You're replying to a comment that contains `@claude`

The workflow uses a two-stage filter to prevent abuse while allowing natural
conversation flow. Check the Actions tab in your repository for workflow run details
if Claude doesn't respond as expected.
