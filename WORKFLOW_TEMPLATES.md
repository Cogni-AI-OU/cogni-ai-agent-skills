# Workflow Templates

This directory contains GitHub Actions workflow templates that are preserved for
reference and future use. These workflows are **not actively executed** by GitHub
Actions.

## Purpose

- **Reference Material**: Keep proven workflow configurations for documentation
- **Reusability**: Easy to copy to other repositories when needed
- **Archive**: Preserve workflows that may be useful in the future

## Usage

To use a workflow template:

1. Copy the desired workflow file from this directory
2. Paste it into `.github/workflows/` in your target repository
3. Customize the workflow (language matrix, triggers, etc.) as needed
4. Commit and push to activate the workflow

## Available Templates

- **codeql-analysis.yml**: GitHub CodeQL security scanning workflow
  - Supports multiple languages: C/C++, C#, Go, Java, JavaScript, Python
  - Configure the `language` matrix to match your project's languages
  - Runs on push, pull requests, and scheduled scans

## Notes

Workflows in this directory will not be executed by GitHub Actions. Only
workflows in `.github/workflows/` are active.
