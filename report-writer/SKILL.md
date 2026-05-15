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

- **Comprehensive Execution**: The report must systemically explore all categories and document every discovered item.
- **Accurate Comparisons**: Cross-reference the live state against both the configuration mapping and the previous run's cache.
- **Auto-Correction**: Do not just report discrepancies; actively fix the underlying JSON mapping and open a Pull Request.
- **Structured Reporting**: Output a markdown report containing Executive Summary, Inconsistency Detection, JSON Mapping Comparison, Changes Since Last Report, Tools by Toolset, and Recommended Defaults.
- **Traceability**: Track added, removed, and moved tools using specific JSON output comparisons.

## Success Criteria

A successful report execution must satisfy:
- ✅ Loads previous tools list from cache if available
- ✅ Loads current JSON mapping from `pkg/workflow/data/github_toolsets_permissions.json` (or equivalent system mapping file)
- ✅ Systematically explores EACH of the individual toolsets
- ✅ Documents all tools available in the remote server or system
- ✅ Detects and reports any inconsistencies across toolsets (duplicates, miscategorization, naming issues)
- ✅ **Compares server tools with JSON mapping** and identifies discrepancies
- ✅ **Updates JSON mapping file** if discrepancies are found
- ✅ **Creates pull request** with updated JSON mapping if changes were made
- ✅ Compares with previous run and identifies changes (new/removed/moved tools)
- ✅ Saves current tools list to cache for next run
- ✅ **Creates/updates documentation files** (e.g. `.github/aw/...md`) with comprehensive documentation
- ✅ **Identifies and documents recommended default toolsets** with rationale
- ✅ **Updates default toolsets** in relevant documentation files
- ✅ Organizes tools by their appropriate toolset categories
- ✅ Provides clear descriptions and usage information
- ✅ Is formatted as a well-structured markdown document
- ✅ Is published as a GitHub discussion in the "audits" category for easy access and reference
- ✅ Includes change tracking and diff information when previous data exists
- ✅ Validates toolset integrity and reports any detected issues

## What to Avoid

- Reporting discrepancies without fixing the source JSON mapping.
- Failing to systematically explore all provided categories/toolsets.
- Omitting the comparison against the previous cache run.
- Generating unstructured or unformatted text output instead of proper markdown tables and sections.

## Related Skills

- **gh-pr**:
  You MUST load this skill when creating a pull request.
