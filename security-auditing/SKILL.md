---
name: security-auditing
description: >-
  Commands, step-by-step procedures, and mechanical execution for performing deep security audits, vulnerability
  assessments, and threat modeling on codebases and configurations.
  You must load this skill when performing security audits or validation.
---

# Security Auditing Skill

This skill outlines the mechanical steps and procedures required to conduct a thorough security audit on a target
codebase, pull request, or architectural component.

## 1. Threat Surface Discovery & Triage

1. **Constraint Analysis**:
   - Enumerate the security requirements and compliance bounds specific to the current context.
   - Map the exact attack surface exposed by the PR, codebase, or configuration (e.g., exposed API endpoints, new input
     vectors).
2. **Dependency & Supply Chain Audit**:
   - Identify any new or updated third-party libraries.
   - Check these components for known CVEs or supply-chain poisoning risks using available scanning or analysis tools.

## 2. Deep Vulnerability Audit Execution

Execute a rigorous, ordered security analysis against the target codebase by examining the following critical areas:

1. **Injection & Input Validation**
   - Check if user input can ever reach SQL queries, shell commands, HTML outputs, OS commands, or deserializers without
     strict, explicit sanitization/escaping.
2. **Authentication & Authorization**
   - Verify that authentication is enforced globally on exposed boundaries.
   - Verify that authorization is explicitly checked at the granular resource level (e.g., preventing IDOR/BOLA).
3. **Secrets & Cryptography**
   - Search the target code/diff for strings that resemble credentials, SSH keys, API tokens, or passwords.
   - Verify that weak cryptographic algorithms or hardcoded initialization vectors (IVs) are not in use.
4. **AI & Prompt Security**
   - If AI features are modified, check if untrusted user inputs are injected into system prompts without strong
     boundary delimiters.
   - Ensure AI outputs are treated as untrusted and validated before execution or parsing.
5. **Data Exposure & Privacy**
   - Check if an API returns entire database objects rather than specific, authorized views (over-fetching).
   - Ensure PII/PHI or sensitive telemetry data is explicitly masked.

## 3. Exploitability Assessment Mechanics

When a vulnerability is suspected or found:

1. **Attack Scenario Formulation**: Define the specific vector and sequence of operations an attacker would use to
   abuse the flaw.
2. **Blast-Radius Check**: Model the lateral movement achievable if the identified weakness is exploited.
  Determine if the component is isolated by strict privilege boundaries.

## 4. Remediation Reporting

1. Generate feedback for the identified issues, labeling them with a severity prefix (e.g., `[CRITICAL]`, `[HIGH]`,
   `[MEDIUM]`, `[LOW]`).
2. Include the exact location, the formulated attack scenario, and a concrete, implementable code remediation for each
   vulnerability discovered.
