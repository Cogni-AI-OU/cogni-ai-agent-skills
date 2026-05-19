---
name: sbom
description: >-
  Commands and guidelines for generating a Software Bill of Materials (SBOM) locally in SPDX and CycloneDX formats using syft.
  You MUST load this skill when asked to create, generate, or update an SBOM.
license: MIT
---

# Skill: sbom

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Guidelines and commands for generating a Software Bill of Materials (SBOM) to provide visibility into the dependency tree, enabling compliance reporting, vulnerability tracking, and supply chain risk assessment.

## When to Use

- When required to generate compliance reports for software supply chain security.
- To produce an inventory of all third-party dependencies used in a project.
- When configuring a CI/CD pipeline step that requires SPDX or CycloneDX artifacts.

## When Not to Use

- For routine unit testing or local syntax linting.
- When specifically auditing source code for logic vulnerabilities (use `security-audit` instead).
- If the repository strictly uses another proprietary SBOM generator mandated by the organization.

## Common Pitfalls

- **Missing Transitive Dependencies**: Generating an SBOM from source code without resolving lockfiles, leading to an incomplete dependency tree.
- **Format Confusion**: Assuming a single JSON format is sufficient without verifying whether the downstream consumer requires SPDX or CycloneDX.
- **Stale Generation**: Generating the SBOM before the final build step, resulting in an inaccurate representation of the shipped artifact.

## Core Process

1. **Install Syft**: Ensure the `syft` CLI tool is installed for SBOM generation.
2. **Generate SBOM**: Run the project's build command to produce SBOM artifacts.
3. **Verify Output**: Confirm the generation of both SPDX and CycloneDX JSON formats.

## Quick Start

```bash
# 1. Install syft (if not already installed)
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

# 2. Generate SBOM
make sbom
```

## Commands / Usage Patterns

- **Install syft**: `curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin`
- **Generate Artifacts**: `make sbom`
- **Expected Artifacts**: The generation command typically produces `sbom.spdx.json` (SPDX JSON format) and `sbom.cdx.json` (CycloneDX JSON format).

## Best Practices

- Always ensure the SBOM generation captures both direct and transitive dependencies.
- Verify that package versions, licenses, and hashes are included in the generated output for integrity verification.
