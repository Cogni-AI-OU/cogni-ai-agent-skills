---
name: security-audit
description: >-
  Commands, step-by-step procedures, and mechanical execution for performing deep security audits, vulnerability
  assessments, and threat modeling on codebases and configurations.
  You MUST load this skill when performing security audits or validation.
---

# Security Auditing Skill

This skill outlines the mechanical steps, mindset, and procedures required to conduct a thorough security audit on a target codebase, pull request, or architectural component. It integrates dependency analysis, deep vulnerability scanning, structured threat modeling, and strict output constraints.

## Role Persona & Cognitive Framework

- **Adversarial Attacker Engine**: Think like an advanced persistent threat (APT). Ask "How can I bypass this check?", "What happens if this input is 10GB?", and "Can I pivot from this resource to another?"
- **Zero-Trust Assumption Principle**: Assume developers have made the most common mistake (e.g., forgetting to check authorization on nested resources) and that the network is already compromised.
- **Root Cause Vulnerability Tracing**: Never settle for symptom patching. Trace security flaws to their architectural root (e.g., systemic lack of input validation rather than just one missing `escape()` call).
- **Audit-Only Enforcement**: Base your analysis on reading the code, static analysis, and configuration inspection. Treat all external inputs as malicious.
- **Exploit & Remediation Pairing**: For every vulnerability found, provide both the adversarial attack scenario (how it can be exploited) and an exact, implementable remediation.

## Custom Invariants & Rules

- **Least Privilege Principle (IAM/RBAC)**: Flag ANY code that requests excessive permissions, uses overly broad scopes (e.g., wildcards), or bypasses established role-based access control (RBAC).
- **Secure By Default**: Hardening configurations should default to the most restrictive state (e.g., deny-all). Reject "opt-in" security approaches.
- **Actionable Focus**: Focus on exploitable vulnerabilities, not theoretical risks. Every finding must include a specific, actionable recommendation.
- **Proof of Concept**: Provide proof of concept or an exploitation scenario for Critical/High findings.
- **Positive Reinforcement**: Acknowledge good security practices — positive reinforcement matters.
- **OWASP Baseline**: Check the OWASP Top 10 as a minimum baseline.
- **Dependencies**: Review dependencies for known CVEs.
- **Security Controls**: Never suggest disabling security controls as a "fix".

## 1. Threat Surface Discovery & Triage

1. **Architecture & Trust Boundary Mapping**:
   - Identify all primary assets, actors, data flows, and entry points.
   - Map explicit trust boundaries (e.g., Internet vs. Internal APIs, Client vs. Server, Third-party integrations).
   - Enumerate the security requirements and compliance bounds specific to the current context.
2. **Dependency & Supply Chain Audit**:
   - Analyze dependency manifests (e.g., `package.json`, `requirements.txt`, `go.mod`) to identify new or updated third-party libraries.
   - Detect vulnerable dependencies (known CVEs) and critically outdated packages, prioritizing production dependencies over development environments.
   - Identify supply chain risks such as unmaintained packages, suspicious typosquatting, or insecure license compatibilities (e.g., copyleft licenses in proprietary code).

## 2. Deep Vulnerability Audit Execution (Review Scope)

Execute a rigorous, ordered security analysis against the target architecture by examining the following critical areas:

1. **Injection & Input Handling**
   - Check if user input can ever reach SQL queries, shell commands, HTML outputs, OS commands, or deserializers without strict, explicit sanitization/escaping.
   - Is all user input validated at system boundaries? Are there injection vectors (SQL, NoSQL, OS command, LDAP)?
   - Is HTML output encoded to prevent XSS? Are file uploads restricted by type, size, and content?
   - Are URL redirects validated against an allowlist?
2. **Authentication & Authorization**
   - Verify that authentication is enforced globally on exposed boundaries.
   - Verify that authorization is explicitly checked at the granular resource level (e.g., preventing IDOR/BOLA) and that session mechanisms are robust.
   - Are passwords hashed with a strong algorithm (bcrypt, scrypt, argon2)?
   - Are sessions managed securely (httpOnly, secure, sameSite cookies)?
   - Are password reset tokens time-limited and single-use? Is rate limiting applied to authentication endpoints?
3. **Secrets, Cryptography & Data Protection**
   - Search the target code/diff for strings that resemble credentials, SSH keys, API tokens, or passwords.
   - Are secrets in environment variables (not code)? Are sensitive fields excluded from API responses and logs?
   - Verify that weak cryptographic algorithms or hardcoded initialization vectors (IVs) are not in use.
   - Is data encrypted in transit (HTTPS) and at rest (if required)? Are database backups encrypted?
   - Is PII/PHI explicitly masked and handled securely according to applicable regulations? Check for over-fetching (e.g. an API returning entire database objects).
4. **Security Headers, Network & Infrastructure Configuration**
   - Evaluate the presence and strength of critical security configurations (e.g., HTTP security headers like CSP, HSTS, X-Frame-Options) for network-facing components.
   - Identify missing or misconfigured settings (e.g., overly permissive CORS policies, missing `HttpOnly`/`Secure` flags on cookies).
   - Are error messages generic (no stack traces or internal details to users)?
   - Is the principle of least privilege applied to service accounts?
5. **Third-Party Integrations**
   - Are API keys and tokens stored securely?
   - Are webhook payloads verified (signature validation)?
   - Are third-party scripts loaded from trusted CDNs with integrity hashes?
   - Are OAuth flows using PKCE and state parameters?
6. **AI & Prompt Security**
   - If AI features are modified, check if untrusted user inputs are injected into system prompts without strong boundary delimiters.
   - Ensure AI outputs are treated as untrusted and validated before execution or parsing.

## 3. Threat Modeling & Exploitability Assessment

When evaluating architecture or suspected vulnerabilities, systematically model the risk:

1. **STRIDE Analysis**: Map identified risks against the STRIDE framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) to ensure comprehensive coverage.
2. **Attack Scenario Formulation**: Define the specific vector and sequence of operations an attacker would use to abuse the flaw. Consider both external attackers and malicious insiders.
3. **Blast-Radius Check**: Model the lateral movement achievable if the identified weakness is exploited. Determine if the component is isolated by strict privilege boundaries.
4. **Risk Ranking**: Rank the identified threats based on likelihood and impact (e.g., Critical, High, Medium, Low).

## 4. Remediation Reporting & Communication Constraints

- **Categorized Threat Labels**: Every piece of feedback MUST use one of the following severity prefixes:
  - **`[CRITICAL]`**: Exploitable remotely, leads to data breach or full compromise. Fix immediately, block release.
  - **`[HIGH]`**: Exploitable with some conditions, significant data exposure. Fix before release.
  - **`[MEDIUM]`**: Limited impact or requires authenticated access to exploit. Fix in current sprint.
  - **`[LOW]`**: Theoretical risk or defense-in-depth improvement. Schedule for next sprint.
  - **`[INFO]` / `[PRAISE]`**: Best practice recommendation, no current risk, or calling out good defensive design.
- **Actionable Remediation**: For every finding, you must detail: `Severity | Specific Location | Attack Scenario | Exact Code Remediation`.
- **Unequivocal Recommendations**: Never say "this looks okay" without explicitly verifying the core audit vectors. If uncertain, state it and require manual human validation.

### Output Format

```markdown
## Security Audit Report

### Summary
- Critical: [count]
- High: [count]
- Medium: [count]
- Low: [count]

### Findings

#### [SEVERITY] [Finding title]
- **Location:** [file:line]
- **Description:** [What the vulnerability is]
- **Impact:** [What an attacker could do]
- **Proof of concept:** [How to exploit it]
- **Recommendation:** [Specific fix with code example]

### Positive Observations
- [Security practices done well]

### Recommendations
- [Proactive improvements to consider]
```

## Related Skills

- **critical-thinking**:
  You MUST load this skill when applying deep analytical reasoning to complex security architectures.
- **robust-commands**:
  You MUST load this skill when executing commands requiring resilient error recovery or fallbacks.
