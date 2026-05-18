---
name: sbom
description: >-
  Commands and guidelines for generating a Software Bill of Materials (SBOM) locally in SPDX and CycloneDX formats using syft.
  You MUST load this skill when asked to create, generate, or update an SBOM.
license: MIT
---

# Skill: sbom

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Generating an SBOM for compliance with supply chain security standards (e.g., EO 14028, NTIA minimum elements, OWASP CycloneDX).
- Creating dependency visibility for vulnerability scanning and CVE tracking across direct and transitive dependencies.
- Producing SBOM artifacts in SPDX or CycloneDX format for integration with security tooling or GRC platforms.
- Auditing a project's dependency tree before a release, acquisition, or third-party review.

## When Not to Use

- Quick dependency checks where a simple `pip freeze` or `npm list` provides sufficient information without formal SBOM format.
- Projects with no external dependencies or only development dependencies that are not distributed.
- When the build environment lacks internet access required to install syft or resolve transitive dependency metadata.

## Common Pitfalls

- syft must be installed separately—it is not available in most base OS images or CI runner environments by default.
- The generated SBOM is only as accurate as the build environment at the time of generation; stale or incomplete build artifacts produce incomplete SBOMs.
- CycloneDX and SPDX formats have different schema versions and tooling support—ensure downstream consumers can parse the format you generate.
- Transitive dependency resolution may pull in different versions depending on the resolver implementation (syft vs. lockfile vs. actual install); the SBOM may not exactly match what is deployed.

Guidelines and commands for generating a Software Bill of Materials (SBOM) to provide visibility into the dependency tree, enabling compliance reporting, vulnerability tracking, and supply chain risk assessment.

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
