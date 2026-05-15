---
name: report-writer
description: Generate comprehensive audit reports, compare current state with JSON mappings, document discrepancies, update documentation files, and track changes via pull requests. You MUST load this skill when asked to generate a comprehensive system audit report.
---
# Skill: report-writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generates a comprehensive report of available tools or system state by self-inspecting, comparing against expected JSON mappings, and updating documentation accordingly.

## Core Process

1. **Load Previous Data**: Check cache memory (e.g., `/tmp/cache-memory/previous-report.json`) to load previous state for comparison.
2. **Load Current JSON Mapping**: Parse existing JSON configuration/mapping from the repository to extract expected tools and configurations.
3. **Systematic Exploration**: Explore EACH individual toolset/category comprehensively. Document all available tools or functions.
4. **Detect Inconsistencies**: Actively detect and report any duplicates, miscategorizations, naming issues, or orphaned items.
5. **Compare and Identify Discrepancies**: Compare the discovered tools with the JSON mapping to identify missing, extra, or moved items.
6. **Update JSON Mapping**: If discrepancies are found, update the JSON file to reflect the true current state, preserving structure and alphabetical sorting.
7. **Create Pull Request**: If changes were made to the JSON mapping, create a local branch and use a pull request tool to submit the updates with a descriptive title and body.
8. **Compare with Previous Run**: Analyze changes (new/removed/moved tools) by comparing current tools with the previous cache.
9. **Update Cache**: Save the newly discovered tools list to the cache location for future runs.
10. **Generate Comprehensive Documentation**: Create or update reference documentation files organizing tools by appropriate categories, providing descriptions and usage information.
11. **Identify Defaults**: Identify and document recommended default toolsets with supporting rationale, and update any references to default toolsets in documentation files.
12. **Publish Report**: Format the final output as a well-structured markdown document and publish it (e.g., as a GitHub discussion in an "audits" category).

## Core Principles

- **Comprehensive Reporting**: The report must systemically explore all categories and document every discovered item.
- **Structured Reporting**: Output a markdown report containing Summary, Inconsistency, Comparison, Changes Since Last Report, and Recommended Defaults.

## Success Criteria

A successful report execution must satisfy:
- ✅ Explores EACH of the options
- ✅ Documents all available options
- ✅ Detects and reports any inconsistencies across report (duplicates, miscategorization, naming issues)
- ✅ Compares and identifies discrepancies
- ✅ Compares with previous changes (new/removed/moved)
- ✅ **Creates/updates documentation files** with comprehensive documentation
- ✅ **Identifies and documents recommended default** with rationale
- ✅ **Updates default** in relevant documentation files
- ✅ Organizes tools by their appropriate categories
- ✅ Provides clear descriptions and usage information
- ✅ Is formatted as a well-structured markdown document
- ✅ Is published as a GitHub discussion category for easy access and reference
- ✅ Includes change tracking and diff information when previous data exists
- ✅ Validates toolset integrity and reports any detected issues

## What to Avoid

- Generating unstructured or unformatted text output instead of proper markdown tables and sections.
