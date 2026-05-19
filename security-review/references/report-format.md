# Security Review Report Format

Use this template for concise PR security reviews.

## PR Review Summary

```text
🛡️ SECURITY REVIEW: <Status: PASS / FAIL / NEEDS ATTENTION>

Summary of findings in this PR:
- [ ] No hardcoded secrets found
- [ ] No vulnerable dependencies added
- [ ] Input validation appears sufficient for new entry points

### Findings
| Severity | Location | Description |
| :--- | :--- | :--- |
| <SEV> | <File:Line> | <Short description of risk and fix> |

### Recommendation
<Concise recommendation for merge readiness>
```
