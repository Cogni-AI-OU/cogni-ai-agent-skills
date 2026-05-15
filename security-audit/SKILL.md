---
name: security-audit
description: >-
  Commands, step-by-step procedures, and mechanical execution for performing deep security audits,
  vulnerability assessments, and threat modeling on codebases and configurations.
  You MUST load this skill when performing security audits or validation.
---

# Security Auditing Skill

This skill outlines the mechanical steps, mindset, and procedures required to conduct a thorough security
audit on a target codebase, pull request, or architectural component. It integrates dependency analysis,
deep vulnerability scanning, structured threat modeling, and strict output constraints.

## When to Use

Use this skill when the request involves:

- Scanning a codebase or file for security vulnerabilities
- Running a security review or vulnerability check
- Checking for SQL injection, XSS, command injection, or other injection flaws
- Finding exposed API keys, hardcoded secrets, or credentials in code
- Auditing dependencies for known CVEs
- Reviewing authentication, authorization, or access control logic
- Detecting insecure cryptography or weak randomness
- Performing a data flow analysis to trace user input to dangerous sinks
- Any request phrasing like "is my code secure?", "scan this file", or "check my repo for vulnerabilities"
- Running `/security-audit` or `/security-audit <path>`

## Role Persona & Cognitive Framework

- **Adversarial Attacker Engine**: Think like an advanced persistent threat (APT). Ask "How can I bypass this check?",
  "What happens if this input is 10GB?", and "Can I pivot from this resource to another?"
- **Zero-Trust Assumption Principle**: Assume developers have made the most common mistake (e.g., forgetting
  to check authorization on nested resources) and that the network is already compromised.
- **Root Cause Vulnerability Tracing**: Never settle for symptom patching. Trace security flaws to their
  architectural root (e.g., systemic lack of input validation rather than just one missing `escape()` call).
- **Audit-Only Enforcement**: Base your analysis on reading the code, static analysis, and configuration
  inspection. Treat all external inputs as malicious.
- **Exploit & Remediation Pairing**: For every vulnerability found, provide both the adversarial attack
  scenario (how it can be exploited) and an exact, implementable remediation.

## Custom Invariants & Rules

- **Least Privilege Principle (IAM/RBAC)**: Flag ANY code that requests excessive permissions, uses overly
  broad scopes (e.g., wildcards), or bypasses established role-based access control (RBAC).
- **Secure By Default**: Hardening configurations should default to the most restrictive state (e.g., deny-all).
  Reject "opt-in" security approaches.
- **Actionable Focus**: Focus on exploitable vulnerabilities, not theoretical risks. Every finding must
  include a specific, actionable recommendation.
- **Proof of Concept**: Provide proof of concept or an exploitation scenario for Critical/High findings.
- **Positive Reinforcement**: Acknowledge good security practices — positive reinforcement matters.
- **OWASP Baseline**: Check the OWASP Top 10 as a minimum baseline.
- **Dependencies**: Review dependencies for known CVEs.
- **Security Controls**: Never suggest disabling security controls as a "fix".

## 1. Threat Surface Discovery & Triage

1. **Architecture & Trust Boundary Mapping**:
   - Identify all primary assets, actors, data flows, and entry points.
   - Map explicit trust boundaries (e.g., Internet vs. Internal APIs, Client vs. Server, Third-party
     integrations).
   - Enumerate the security requirements and compliance bounds specific to the current context.
2. **Dependency & Supply Chain Audit**:
   - Analyze dependency manifests (e.g., `package.json`, `requirements.txt`, `go.mod`) to identify new or
     updated third-party libraries.
   - Detect vulnerable dependencies (known CVEs) and critically outdated packages, prioritizing production
     dependencies over development environments.
   - Identify supply chain risks such as unmaintained packages, suspicious typosquatting, or insecure license
     compatibilities (e.g., copyleft licenses in proprietary code).

## 2. Deep Vulnerability Audit Execution (Review Scope)

Execute a rigorous, ordered security analysis against the target architecture by examining the following critical areas:

1. **Injection & Input Handling**
   - Check if user input can ever reach SQL queries, shell commands, HTML outputs, OS commands, or
     deserializers without strict, explicit sanitization/escaping.
   - Is all user input validated at system boundaries? Are there injection vectors (SQL, NoSQL, OS command,
     LDAP)?
   - Is HTML output encoded to prevent XSS? Are file uploads restricted by type, size, and content?
   - Are URL redirects validated against an allowlist?
2. **Authentication & Authorization**
   - Verify that authentication is enforced globally on exposed boundaries.
   - Verify that authorization is explicitly checked at the granular resource level (e.g., preventing
     IDOR/BOLA) and that session mechanisms are robust.
   - Are passwords hashed with a strong algorithm (bcrypt, scrypt, argon2)?
   - Are sessions managed securely (httpOnly, secure, sameSite cookies)?
   - Are password reset tokens time-limited and single-use? Is rate limiting applied to authentication endpoints?
3. **Secrets, Cryptography & Data Protection**
   - Search the target code/diff for strings that resemble credentials, SSH keys, API tokens, or passwords.
   - Are secrets in environment variables (not code)? Are sensitive fields excluded from API responses and
     logs?
   - Verify that weak cryptographic algorithms or hardcoded initialization vectors (IVs) are not in use.
   - Is data encrypted in transit (HTTPS) and at rest (if required)? Are database backups encrypted?
   - Is PII/PHI explicitly masked and handled securely according to applicable regulations? Check for
     over-fetching (e.g. an API returning entire database objects).
4. **Security Headers, Network & Infrastructure Configuration**
   - Evaluate the presence and strength of critical security configurations (e.g., HTTP security headers
     like CSP, HSTS, X-Frame-Options) for network-facing components.
   - Identify missing or misconfigured settings (e.g., overly permissive CORS policies, missing
     `HttpOnly`/`Secure` flags on cookies).
   - Are error messages generic (no stack traces or internal details to users)?
   - Is the principle of least privilege applied to service accounts?
5. **Third-Party Integrations**
   - Are API keys and tokens stored securely?
   - Are webhook payloads verified (signature validation)?
   - Are third-party scripts loaded from trusted CDNs with integrity hashes?
   - Are OAuth flows using PKCE and state parameters?
6. **AI & Prompt Security**
   - If AI features are modified, check if untrusted user inputs are injected into system prompts without
     strong boundary delimiters.
   - Ensure AI outputs are treated as untrusted and validated before execution or parsing.

## 3. Threat Modeling & Exploitability Assessment

When evaluating architecture or suspected vulnerabilities, systematically model the risk:

1. **STRIDE Analysis**: Map identified risks against the STRIDE framework (Spoofing, Tampering, Repudiation,
   Information Disclosure, Denial of Service, Elevation of Privilege) to ensure comprehensive coverage.
2. **Attack Scenario Formulation**: Define the specific vector and sequence of operations an attacker
   would use to abuse the flaw. Consider both external attackers and malicious insiders.
3. **Blast-Radius Check**: Model the lateral movement achievable if the identified weakness is exploited.
   Determine if the component is isolated by strict privilege boundaries.
4. **Risk Ranking**: Rank the identified threats based on likelihood and impact (e.g., Critical, High, Medium, Low).

## 4. Remediation Reporting & Communication Constraints

- **Categorized Threat Labels**: Every piece of feedback MUST use one of the following severity prefixes:
  - **`[CRITICAL]`**: Exploitable remotely, leads to data breach or full compromise. Fix immediately,
    block release.
  - **`[HIGH]`**: Exploitable with some conditions, significant data exposure. Fix before release.
  - **`[MEDIUM]`**: Limited impact or requires authenticated access to exploit. Fix in current sprint.
  - **`[LOW]`**: Theoretical risk or defense-in-depth improvement. Schedule for next sprint.
  - **`[INFO]` / `[PRAISE]`**: Best practice recommendation, no current risk, or calling out good defensive design.
- **Actionable Remediation**: For every finding, you must detail:
  `Severity | Specific Location | Attack Scenario | Exact Code Remediation`.
- **Unequivocal Recommendations**: Never say "this looks okay" without explicitly verifying the core audit
  vectors. If uncertain, state it and require manual human validation.

### Output Format

Output the full report in the structured format defined in `references/report-format.md`. At a minimum, the report MUST include:

1. **Findings Summary Table**: A table showing counts of findings by severity (CRITICAL, HIGH, MEDIUM, LOW, INFO).
2. **Detailed Findings**: Grouped by category, with file/line location, impact, and recommendation.
3. **Dependency Audit**: Results of the supply chain scan.
4. **Secrets Scan**: Results of the credential scan (redacted).
5. **Patch Proposals**: Concrete code fixes for all CRITICAL and HIGH findings.

Refer to `references/report-format.md` for the canonical markdown template and ASCII styling.

## Execution Workflow

Follow these steps **in order** every time:

### Step 1 — Scope Resolution

Determine what to scan:

- If a path was provided (`/security-audit src/auth/`), scan only that scope
- If no path given, scan the **entire project** starting from the root
- Identify the language(s) and framework(s) in use (check package.json, requirements.txt,
  go.mod, Cargo.toml, pom.xml, Gemfile, composer.json, etc.)
- Read `references/language-patterns.md` to load language-specific vulnerability patterns

### Step 2 — Dependency Audit

Before scanning source code, audit dependencies first (fast wins):

- **Node.js**: Check `package.json` + `package-lock.json` for known vulnerable packages
- **Python**: Check `requirements.txt` / `pyproject.toml` / `Pipfile`
- **Java**: Check `pom.xml` / `build.gradle`
- **Ruby**: Check `Gemfile.lock`
- **Rust**: Check `Cargo.toml`
- **Go**: Check `go.sum`
- Flag packages with known CVEs, deprecated crypto libs, or suspiciously old pinned versions
- Read `references/vulnerable-packages.md` for a curated watchlist

### Step 3 — Secrets & Exposure Scan

Scan all files **within the chosen scope**, AND always include repository-level configuration/environment files
(e.g., `.env`, `.github/workflows/`, `Dockerfile`, `docker-compose.yml`, IaC) even if a specific sub-path was provided,
as secrets often reside outside source directories. Scan for:

- Hardcoded API keys, tokens, passwords, private keys
- `.env` files accidentally committed
- Secrets in comments or debug logs
- Cloud credentials (AWS, GCP, Azure, Stripe, Twilio, etc.)
- Database connection strings with credentials embedded
- Read `references/secret-patterns.md` for regex patterns and entropy heuristics to apply

### Step 4 — Vulnerability Deep Scan

This is the core scan. Reason about the code — don't just pattern-match.
Read `references/vuln-categories.md` for full details on each category.

#### Injection Flaws

- SQL Injection: raw queries with string interpolation, ORM misuse, second-order SQLi
- XSS: unescaped output, dangerouslySetInnerHTML, innerHTML, template injection
- Command Injection: exec/spawn/system with user input
- LDAP, XPath, Header, Log injection

#### Authentication & Access Control

- Missing authentication on sensitive endpoints
- Broken object-level authorization (BOLA/IDOR)
- JWT weaknesses (alg:none, weak secrets, no expiry validation)
- Session fixation, missing CSRF protection
- Privilege escalation paths
- Mass assignment / parameter pollution

#### Data Handling

- Sensitive data in logs, error messages, or API responses
- Missing encryption at rest or in transit
- Insecure deserialization
- Path traversal / directory traversal
- XXE (XML External Entity) processing
- SSRF (Server-Side Request Forgery)

#### Cryptography

- Use of MD5, SHA1, DES for security purposes
- Hardcoded IVs or salts
- Weak random number generation (Math.random() for tokens)
- Missing TLS certificate validation

#### Business Logic

- Race conditions (TOCTOU)
- Integer overflow in financial calculations
- Missing rate limiting on sensitive endpoints
- Predictable resource identifiers

### Step 5 — Cross-File Data Flow Analysis

After the per-file scan, perform a **holistic review**:

- Trace user-controlled input from entry points (HTTP params, headers, body, file uploads)
  all the way to sinks (DB queries, exec calls, HTML output, file writes)
- Identify vulnerabilities that only appear when looking at multiple files together
- Check for insecure trust boundaries between services or modules

### Step 6 — Self-Verification Pass

For EACH finding:

1. Re-read the relevant code with fresh eyes
2. Ask: "Is this actually exploitable, or is there sanitization I missed?"
3. Check if a framework or middleware already handles this upstream
4. Downgrade or discard findings that aren't genuine vulnerabilities
5. Assign final severity: CRITICAL / HIGH / MEDIUM / LOW / INFO

### Step 7 — Generate Security Report

Output the full report using the canonical template defined in `references/report-format.md`.
Ensure the findings summary table is presented first.

### Step 8 — Propose Patches

For every CRITICAL and HIGH finding, generate a concrete patch:

- Show the vulnerable code (before)
- Show the fixed code (after)
- Explain what changed and why
- Preserve the original code style, variable names, and structure
- Add a comment explaining the fix inline

Explicitly state: **"Review each patch before applying. Nothing has been changed yet."**

## Severity Guide

| Severity | Meaning | Example |
| :--- | :--- | :--- |
| 🔴 CRITICAL | Immediate exploitation risk, data breach likely | SQLi, RCE, auth bypass |
| 🟠 HIGH | Serious vulnerability, exploit path exists | XSS, IDOR, hardcoded secrets |
| 🟡 MEDIUM | Exploitable with conditions or chaining | CSRF, open redirect, weak crypto |
| 🔵 LOW | Best practice violation, low direct risk | Verbose errors, missing headers |
| ⚪ INFO | Observation worth noting, not a vulnerability | Outdated dependency (no CVE) |

## Output Rules

- **Always** follow the section order defined in `### Output Format`, and include a findings summary table
  with counts by severity in that structure
- **Never** auto-apply any patch — present patches for human review only
- **Always** include a confidence rating per finding (High / Medium / Low)
- **Group findings** by category, not by file
- **Be specific** — include file path and line number, plus the relevant vulnerable code context.
  **CRITICAL:** For findings involving secrets (keys, tokens, etc.), you MUST redact the value in the snippet
  (e.g., use `[REDACTED]` or show only prefix/suffix) to avoid leaking credentials in the report.
- **Never reveal secrets verbatim** — for API keys, passwords, tokens, private keys, connection strings, or similar
  sensitive values, show only redacted/masked content (for example, a short prefix/suffix or a hash/fingerprint)
  while preserving file+line context
- **Use exact code snippets only when safe** — if a finding involves secrets or other sensitive values, replace the
  sensitive portion with a redaction such as `[REDACTED]`
- **Explain the risk** in plain English — what could an attacker do with this?
- If the codebase is clean, say so clearly: "No vulnerabilities found" with what was scanned

## Reference Files

For detailed detection guidance, load the following reference files as needed:

- `references/vuln-categories.md` — Deep reference for every vulnerability
  category with detection signals, safe patterns, and escalation checkers
  - Search patterns: `SQL injection`, `XSS`, `command injection`, `SSRF`,
    `BOLA`, `IDOR`, `JWT`, `CSRF`, `secrets`, `cryptography`,
    `race condition`, `path traversal`
- `references/secret-patterns.md` — Regex patterns, entropy-based detection,
  and CI/CD secret risks
  - Search patterns: `API key`, `token`, `private key`,
    `connection string`, `entropy`, `.env`, `GitHub Actions`, `Docker`,
    `Terraform`
- `references/language-patterns.md` — Framework-specific vulnerability
  patterns for JavaScript, Python, Java, PHP, Go, Ruby, and Rust
  - Search patterns: `Express`, `React`, `Next.js`, `Django`, `Flask`,
    `FastAPI`, `Spring Boot`, `PHP`, `Go`, `Rails`, `Rust`
- `references/vulnerable-packages.md` — Curated CVE watchlist for npm, pip,
  Maven, Rubygems, Cargo, and Go modules
  - Search patterns: `lodash`, `axios`, `jsonwebtoken`, `Pillow`, `log4j`,
    `nokogiri`, `CVE`
- `references/report-format.md` — Structured output template for security
  reports with finding cards, dependency audit, secrets scan, and patch
  proposal formatting
  - Search patterns: `report`, `format`, `template`, `finding`, `patch`,
    `summary`, `confidence`

## References

- <https://github.com/github/awesome-copilot/blob/main/skills/security-review/SKILL.md>

## Related Skills

- **critical-thinking**:
  You MUST load this skill when applying deep analytical reasoning to complex security architectures.
- **robust-commands**:
  You MUST load this skill when executing commands requiring resilient error recovery or fallbacks.
