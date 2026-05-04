---
name: security-audit
description: >-
  Commands, step-by-step procedures, and mechanical execution for performing deep security audits, vulnerability
  assessments, and threat modeling on codebases and configurations.
  You must load this skill when performing security audits or validation.
---

# Security Auditing Skill

This skill outlines the mechanical steps and procedures required to conduct a thorough security audit on a target
codebase, pull request, or architectural component. It integrates dependency analysis, deep vulnerability scanning, and structured threat modeling.

## 1. Threat Surface Discovery & Triage

1. **Architecture & Trust Boundary Mapping**:
   - Identify all primary assets, actors, data flows, and entry points.
   - Map explicit trust boundaries (e.g., Internet vs. Internal APIs, Client vs. Server, Third-party integrations).
   - Enumerate the security requirements and compliance bounds specific to the current context.
2. **Dependency & Supply Chain Audit**:
   - Analyze dependency manifests (e.g., `package.json`, `requirements.txt`, `go.mod`) to identify new or updated third-party libraries.
   - Detect vulnerable dependencies (known CVEs) and critically outdated packages, prioritizing production dependencies over development environments.
   - Identify supply chain risks such as unmaintained packages, suspicious typosquatting, or insecure license compatibilities (e.g., copyleft licenses in proprietary code).

## 2. Deep Vulnerability Audit Execution

Execute a rigorous, ordered security analysis against the target architecture by examining the following critical areas:

1. **Injection & Input Validation**
   - Check if user input can ever reach SQL queries, shell commands, HTML outputs, OS commands, or deserializers without strict, explicit sanitization/escaping.
2. **Authentication & Authorization**
   - Verify that authentication is enforced globally on exposed boundaries.
   - Verify that authorization is explicitly checked at the granular resource level (e.g., preventing IDOR/BOLA) and that session mechanisms are robust.
3. **Secrets & Cryptography**
   - Search the target code/diff for strings that resemble credentials, SSH keys, API tokens, or passwords.
   - Verify that weak cryptographic algorithms or hardcoded initialization vectors (IVs) are not in use.
4. **Security Headers & Network Configuration**
   - Evaluate the presence and strength of critical security configurations (e.g., HTTP security headers like CSP and HSTS) for network-facing components.
   - Identify missing or misconfigured settings (e.g., overly permissive CORS policies, missing `HttpOnly`/`Secure` flags on cookies).
5. **AI & Prompt Security**
   - If AI features are modified, check if untrusted user inputs are injected into system prompts without strong boundary delimiters.
   - Ensure AI outputs are treated as untrusted and validated before execution or parsing.
6. **Data Exposure & Privacy**
   - Check if an API returns entire database objects rather than specific, authorized views (over-fetching).
   - Ensure PII/PHI or sensitive telemetry data is explicitly masked and handled securely.

## 3. Threat Modeling & Exploitability Assessment

When evaluating architecture or suspected vulnerabilities, systematically model the risk:

1. **STRIDE Analysis**: Map identified risks against the STRIDE framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) to ensure comprehensive coverage.
2. **Attack Scenario Formulation**: Define the specific vector and sequence of operations an attacker would use to abuse the flaw. Consider both external attackers and malicious insiders.
3. **Blast-Radius Check**: Model the lateral movement achievable if the identified weakness is exploited. Determine if the component is isolated by strict privilege boundaries.
4. **Risk Ranking**: Rank the identified threats based on likelihood and impact (e.g., Critical, High, Medium, Low).

## 4. Remediation Reporting

1. **Structured Feedback**: Generate clear feedback for the identified issues, labeling them with a severity prefix (e.g., `[CRITICAL]`, `[HIGH]`, `[MEDIUM]`, `[LOW]`).
2. **Actionable Mitigations**: Provide specific, implementable code remediations or configuration blocks for each vulnerability. Avoid generic advice (e.g., instead of "secure the headers", provide the exact required configuration).
3. **Prioritized Action Plan**: Present a clear, prioritized remediation plan focusing on the highest impact vulnerabilities first.
