---
name: report-writer
description: Generate comprehensive audit reports, compare current state with baseline definitions, document discrepancies, update documentation files, and track changes via pull requests. You MUST load this skill when asked to generate a comprehensive system audit report.
license: MIT
---
# Skill: report-writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Generates a comprehensive report of available resources or system state by self-inspecting, comparing against expected state definitions, and updating documentation accordingly.

## Core Process

1. **Load Previous Data**: Check persistent storage or historical logs to load the previous state for comparison.
2. **Load Baseline Definitions**: Parse existing configuration or metadata from the repository to extract the expected state and configurations.
3. **Systematic Exploration**: Explore EACH individual resource category comprehensively. Document all available items or functions.
4. **Detect Inconsistencies**: Actively detect and report any duplicates, miscategorizations, naming issues, or orphaned items.
5. **Compare and Identify Discrepancies**: Compare the discovered items with the baseline definitions to identify missing, extra, or modified items.
6. **Update Baseline**: If discrepancies are found, update the baseline definitions to reflect the true current state, preserving established structure and sorting.
7. **Create Pull Request**: If changes were made to the baseline definitions, create a local branch and submit the updates via a pull request with a descriptive title and body.
8. **Compare with Previous Run**: Analyze changes (new/removed/moved items) by comparing current state with the previous snapshot.
9. **Update State Snapshot**: Save the newly discovered state to a persistent location for future runs.
10. **Generate Comprehensive Documentation**: Create or update reference documentation files organizing items by appropriate categories, providing descriptions and usage information.
11. **Identify Defaults**: Identify and document recommended default settings or items with supporting rationale, and update any references to defaults in documentation files.
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
- ✅ Organizes items by their appropriate categories
- ✅ Provides clear descriptions and usage information
- ✅ Is formatted as a well-structured markdown document
- ✅ Is published as a GitHub discussion category for easy access and reference
- ✅ Includes change tracking and diff information when previous data exists
- ✅ Validates resource integrity and reports any detected issues

## What to Avoid

- Generating unstructured or unformatted text output instead of proper markdown tables and sections.
