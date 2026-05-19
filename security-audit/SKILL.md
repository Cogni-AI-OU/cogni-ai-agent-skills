---
name: security-audit
description: >-
  Commands, step-by-step procedures, and mechanical execution for performing deep security audits,
  vulnerability assessments, and report generation on codebases and configurations.
  You MUST load this skill when performing security audits or validation.
license: MIT
---

# Security Auditing Skill

This skill outlines the mechanical steps, mindset, and procedures required to conduct a thorough security
audit on a target codebase or architectural component. It integrates dependency analysis,
deep vulnerability scanning, structured threat modeling, and strict output constraints.

## When to Use

Use this skill when the request involves:

- Scanning a codebase or file for security vulnerabilities
- Running a security audit or vulnerability check
- Checking for SQL injection, XSS, command injection, or other injection flaws
- Finding exposed API keys, hardcoded secrets, or credentials in code
- Auditing dependencies for known CVEs
- Reviewing authentication, authorization, or access control logic
- Detecting insecure cryptography or weak randomness
- Performing a data flow analysis to trace user input to dangerous sinks
- Any request phrasing like "is my code secure?", "scan this file", or "check my repo for vulnerabilities"
- Running `/security-audit` or `/security-audit <path>`

## When Not to Use

- When performing a lightweight PR review (use `security-review`).
- When writing tests for functional validation (use `tester` or `tdd`).
- When optimizing code purely for performance without a security context.

## Common Pitfalls

- **False Positives**: Flagging code as vulnerable purely based on regex matches without considering existing sanitization or trust boundaries.
- **Ignoring the Supply Chain**: Auditing the source code meticulously but neglecting to check `package.json` or `requirements.txt` for known CVEs.
- **Suggesting Breaking Changes**: Recommending heavy-handed security controls that completely break the application's core business logic.

## Role Persona & Cognitive Framework

- **Adversarial Attacker Engine**: Think like an advanced persistent threat (APT). Ask "How can I bypass this check?",
  "What happens if this input is 10GB?", and "Can I pivot from this resource to another?"
- **Zero-Trust Assumption Principle**: Assume developers have made the most common mistake and that the network is already compromised.
- **Root Cause Vulnerability Tracing**: Trace security flaws to their architectural root.
- **Audit-Only Enforcement**: Base your analysis on reading the code, static analysis, and configuration inspection.
- **Exploit & Remediation Pairing**: For every vulnerability found, provide both the adversarial attack scenario and an exact, implementable remediation.

## 1. Threat Surface Discovery & Triage

1. **Architecture & Trust Boundary Mapping**:
   - Identify all primary assets, actors, data flows, and entry points.
   - Map explicit trust boundaries.
2. **Dependency & Supply Chain Audit**:
   - Analyze dependency manifests to identify vulnerable dependencies (known CVEs).

## 2. Deep Vulnerability Audit Execution

Execute a rigorous, ordered security analysis against the target architecture:

1. **Injection & Input Handling**: SQLi, XSS, command injection.
2. **Authentication & Authorization**: RBAC, IDOR, session management.
3. **Secrets, Cryptography & Data Protection**: Credential scanning, weak crypto.
4. **Security Headers & Network Config**: CSP, HSTS, CORS.
5. **Third-Party Integrations**: Webhooks, API keys.
6. **AI & Prompt Security**: Prompt injection boundaries.

## 3. Threat Modeling & Exploitability Assessment

1. **STRIDE Analysis**.
2. **Attack Scenario Formulation**.
3. **Blast-Radius Check**.
4. **Risk Ranking**.

## 4. Remediation Reporting

Output the full report in the structured format defined in `references/report-format.md`.

### Output Format

The report MUST include:
1. **Findings Summary Table**.
2. **Detailed Findings**.
3. **Dependency Audit**.
4. **Secrets Scan**.
5. **Patch Proposals**.

## Execution Workflow

### Step 1 — Scope Resolution
### Step 2 — Dependency Audit
### Step 3 — Secrets & Exposure Scan
### Step 4 — Vulnerability Deep Scan
### Step 5 — Cross-File Data Flow Analysis
### Step 6 — Self-Verification Pass
### Step 7 — Generate Security Report
### Step 8 — Propose Patches

## Severity Guide

| Severity | Meaning |
| :--- | :--- |
| 🔴 CRITICAL | Immediate exploitation risk, data breach likely |
| 🟠 HIGH | Serious vulnerability, exploit path exists |
| 🟡 MEDIUM | Exploitable with conditions or chaining |
| 🔵 LOW | Best practice violation, low direct risk |
| ⚪ INFO | Observation worth noting |

## Reference Files

- `references/vuln-categories.md`
- `references/secret-patterns.md`
- `references/language-patterns.md`
- `references/vulnerable-packages.md`
- `references/report-format.md`

## Related Skills

- **critical-thinking**
- **robust-commands**
- **security-review**
