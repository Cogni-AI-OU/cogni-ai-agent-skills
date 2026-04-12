# Code Tours

This directory contains interactive code tours that provide guided walkthroughs of the repository structure,
development setup, and contribution guidelines.

## What are Code Tours?

Code Tours are interactive, guided walkthroughs of a codebase that help developers quickly understand the structure,
conventions, and workflows of a project. They're powered by the
[CodeTour VS Code extension](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.codetour) and allow
repository maintainers to create step-by-step tours that navigate through files and provide contextual explanations.

### Benefits

- **Faster Onboarding**: New contributors can quickly understand the project structure without reading extensive
  documentation
- **Interactive Learning**: Tours guide you through the actual code, making learning more engaging and practical
- **Contextual Documentation**: Documentation lives alongside the code it describes, making it easier to keep up-to-date
- **Self-Paced**: Users can navigate through tours at their own speed, pause, and revisit steps as needed

## Available Tours

### Getting Started Tour

**File**: `getting-started.tour`

This is the primary tour for new contributors and provides a comprehensive walkthrough of:

- Repository structure and organization
- Development environment setup with devcontainers
- Coding standards and best practices for Python, Markdown, YAML, and Ansible
- Pre-commit hooks and automated validation tools
- GitHub Actions CI/CD workflows, including OpenCode automation
- Contribution guidelines and workflow

**When to use**: Start here if you're new to the repository or want to understand the overall project structure.

## How to Use Code Tours

### Prerequisites

1. **VS Code**: Code Tours work with Visual Studio Code
2. **CodeTour Extension**: Install the [CodeTour extension](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.codetour)
   from the VS Code marketplace

### Using the Devcontainer (Recommended)

This repository includes a pre-configured devcontainer that automatically includes the CodeTour extension:

1. Open the repository in VS Code
2. When prompted, click "Reopen in Container" (or use Command Palette: "Remote-Containers: Reopen in Container")
3. Once the container is built, the CodeTour extension will be available automatically

### Manual Setup

If you're not using the devcontainer:

1. Install the CodeTour extension from the VS Code marketplace
2. Open the repository in VS Code
3. Tours will be automatically detected from the `.tours` directory

### Starting a Tour

There are several ways to start a code tour:

1. **From the CodeTour Panel**:
   - Click on the CodeTour icon in the Activity Bar (looks like a map with a route)
   - Select a tour from the list
   - Click the play button to start

2. **From Command Palette**:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
   - Type "CodeTour: Start Tour"
   - Select the tour you want to begin

3. **Automatic Start**:
   - Tours marked with `"isPrimary": true` may start automatically when you open the repository

### Navigating Through a Tour

Once a tour is started, you can:

- **Next Step**: Click the "Next" button or press `Ctrl+Right` (or `Cmd+Right` on macOS)
- **Previous Step**: Click the "Previous" button or press `Ctrl+Left` (or `Cmd+Left` on macOS)
- **Exit Tour**: Click the "End Tour" button or press `Esc`
- **Jump to Step**: Click on any step in the CodeTour panel to jump directly to it

### Tour Features

Code tours can:

- Navigate to specific files and line numbers
- Display rich markdown descriptions with code blocks, lists, and formatting
- Highlight specific code sections
- Show directory structures
- Provide contextual explanations and best practices

## Creating New Tours

If you're a maintainer looking to create or update tours, here are some guidelines:

### Tour File Format

Tours are JSON files with the following structure:

```json
{
  "$schema": "https://aka.ms/codetour-schema",
  "title": "Tour Title",
  "description": "Brief description of what this tour covers",
  "isPrimary": false,
  "steps": [
    {
      "title": "Step Title",
      "description": "Markdown-formatted description",
      "file": "path/to/file.ext",
      "line": 42
    }
  ]
}
```

### Best Practices

- **Clear Titles**: Use descriptive titles that indicate what the tour covers
- **Logical Flow**: Structure steps in a logical order that builds understanding progressively
- **Rich Descriptions**: Use markdown formatting to make descriptions clear and engaging
- **Focused Content**: Keep each step focused on one concept or area
- **Update Regularly**: Keep tours up-to-date with code changes to avoid confusion
- **Mark Primary Tours**: Set `"isPrimary": true` for the main onboarding tour

### Creating a Tour

1. **Using the Extension**:
   - Open Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
   - Type "CodeTour: Record Tour"
   - Follow the prompts to create steps

2. **Manual Creation**:
   - Create a new `.tour` file in the `.tours` directory
   - Follow the JSON structure above
   - Add steps with file paths, line numbers, and descriptions

3. **Testing**:
   - Start the tour to ensure all steps navigate correctly
   - Verify that descriptions display properly
   - Check that file paths and line numbers are accurate

## Maintaining Tours

Tours should be updated when:

- File paths or structure changes
- Line numbers referenced in tours shift due to code changes
- New features or workflows are added
- Coding standards or conventions are updated
- Dependencies or tooling changes significantly

**Tip**: When making significant changes to referenced files, check if any tours need updating.

## Additional Resources

- [CodeTour Documentation](https://github.com/microsoft/codetour)
- [CodeTour VS Code Extension](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.codetour)
- [VS Code Devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

## Questions or Issues?

If you encounter problems with tours or have suggestions for new tours, please:

- Open an issue in the repository
- Tag it with appropriate labels (e.g., `documentation`, `enhancement`)
- Provide details about what tour content would be helpful

Happy touring! 🗺️
