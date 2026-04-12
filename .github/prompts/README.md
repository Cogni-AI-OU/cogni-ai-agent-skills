# Agent Prompts

This directory contains prompt files that can be used with AI agents (OpenCode, GitHub Copilot, etc.)
to perform standardized tasks across repositories.

- For the agent-facing prompt catalog, see [AGENTS.md](AGENTS.md).

## Prompt File Formats

This directory supports two types of prompt formats:

### Markdown Format (`.md`)

Markdown prompts (`.prompt.md`) are human-readable prompt templates designed for use in:

- **VS Code**: Reference these prompts in GitHub Copilot Chat or other AI assistants within your IDE
- **Claude Code**: Copy and paste content directly or reference the file URL
- **Manual use**: Easy to read and adapt for any AI tool

Markdown prompts are ideal for detailed, structured instructions with checklists and examples.

### YAML Format (`.yml` or `.yaml`)

YAML prompts (`.prompt.yml` or `.prompt.yaml`) follow the [GitHub Models prompt format](https://docs.github.com/en/github-models/use-github-models/storing-prompts-in-github-repositories)
and are designed for:

- **GitHub Models**: Direct integration with GitHub's AI model playground
- **Programmatic use**: Machine-readable format for automated workflows
- **API integration**: Use with GitHub Models API and other model providers

YAML prompts define structured message exchanges with specific roles (system, user, assistant) and
model configuration.

## How to Use

### Markdown Prompts (`.prompt.md`)

#### With OpenCode

1. **In an Issue or PR**: Use `/oc` or `/opencode` command and provide the prompt content or reference the file:

   ```text
   /opencode Please follow the checklist in
   https://github.com/Cogni-AI-OU/.github/blob/main/.github/prompts/repository-setup.prompt.md
   to review and update this repository's configuration.
   ```

2. **Directly**: Copy the prompt content and paste it into an OpenCode conversation.

#### With GitHub Copilot (VS Code)

1. **In VS Code Chat**: Open Copilot Chat and reference the prompt:

   ```text
   @workspace Please follow the repository setup checklist from
   .github/prompts/repository-setup.prompt.md to standardize this repository.
   ```

2. **In Pull Request**: Create a PR and ask Copilot to review using the prompt guidelines.

### YAML Prompts (`.prompt.yml` or `.prompt.yaml`)

#### With GitHub Models

1. **In GitHub Models Playground**: Navigate to [GitHub Models](https://github.com/marketplace/models)
2. **Load prompt**: Import or reference the YAML prompt file
3. **Run**: Execute the prompt with your chosen model
4. **Integrate**: Use the prompt in automated workflows via GitHub Models API

### Standalone Usage

You can also use these prompts with other AI tools by:

1. Reading the prompt file
2. Copying the content to your AI tool of choice
3. Adjusting as needed for your specific use case

## Customizing Prompts

Feel free to create your own prompt files for common tasks:

1. Choose the appropriate format:
   - Use `.prompt.md` for human-readable templates and VS Code integration
   - Use `.prompt.yml` (or `.prompt.yaml`) for GitHub Models and programmatic use
2. Structure it with clear sections and checklists (for Markdown) or proper message roles (for YAML)
3. Include references to relevant documentation and templates
4. Test it with an AI agent
5. Submit a PR to add it to the organization's prompt library

## Prompt File Guidelines

When creating prompt files:

### For Markdown Prompts (`.prompt.md`)

- **Use clear structure**: Organize with headers, lists, and phases
- **Include context**: Explain the purpose and background
- **Provide references**: Link to templates and documentation
- **Use checklists**: Make it easy to track progress
- **Be specific**: Include exact commands, file paths, and examples
- **Add customization notes**: Guide agents on when/how to adapt
- **Include validation steps**: Ensure work can be verified

### For YAML Prompts (`.prompt.yml` or `.prompt.yaml`)

- **Follow GitHub Models format**: Use `messages` array with role-based structure
- **Define model settings**: Specify `model` and `responseFormat`
- **System prompt**: Include context and instructions in the `system` role message
- **Conversation flow**: Structure user and assistant messages logically
- **Keep it focused**: YAML prompts work best for specific, well-defined tasks
- **Test with GitHub Models**: Validate in the GitHub Models playground before committing

## Examples

### Example 1: Complete Repository Setup

```text
/oc I need you to set up this repository following organization standards.
Please use the repository-setup.prompt.md checklist and:

1. Review all configuration files
2. Create missing files
3. Set up workflows using remote references
4. Configure devcontainer
5. Create documentation
6. Validate everything works

Report progress after each phase.
```

### Example 2: Partial Setup (Workflows Only)

```text
/opencode Please follow Phase 3 of the repository-setup.prompt.md to add
GitHub Actions workflows to this repository. Use workflow_call to reference
remote workflows from Cogni-AI-OU/.github.
```

### Example 3: Validation Only

```text
/opencode Please follow Phase 9 of repository-setup.prompt.md to validate
all configuration files in this repository. Run linters and report any issues.
```

## Contributing

To contribute new prompts or improve existing ones:

1. Fork the repository
2. Create or update prompt files in `.github/prompts/`
3. Test the prompt with an AI agent
4. Update this README if adding a new prompt
5. Submit a PR with your changes

## Tips for Effective Prompts

- **Be explicit**: Don't assume the agent knows context
- **Use examples**: Show what you want, don't just describe it
- **Break into phases**: Make complex tasks manageable
- **Include validation**: Help agents verify their work
- **Reference standards**: Link to style guides and templates
- **Allow flexibility**: Balance standardization with customization

## Prompt structure

Prompts have two key parts:

- Runtime information (required)
- Development information (optional)

See: [Storing prompts in GitHub repositories](https://docs.github.com/en/github-models/use-github-models/storing-prompts-in-github-repositories)

## Additional Resources

- [AGENTS.md](../../AGENTS.md) - General agent guidance
- [Copilot Instructions](../copilot-instructions.md) - Coding standards
- [GitHub Actions Workflows](../workflows/) - Reusable workflows
- [Instructions](../instructions/) - Language-specific guidelines
