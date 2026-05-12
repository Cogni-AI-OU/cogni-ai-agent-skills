---
name: critical-thinking
description: >-
  Engage deep analytical reasoning, deconstruct assumptions, apply Socratic questioning, and perform adversarial red-teaming
  to solve complex problems and validate architectural plans.
  You MUST apply this skill when facing challenges which require critical thinking.
---
# critical-thinking

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

A cognitive framework for deep analytical reasoning.

## Core Process

1. **Deconstruct & Frame**: Separate the final goal (Conclusion) from the underlying logic (Premises).
2. **Surface Hidden Dependencies**: Identify what must be true for the current logic to hold (assumptions, state, concurrency).
3. **Generate Hypotheses**: Explicitly list alternative explanations or missing context before acting.
4. **Adversarial Red-Teaming**: Aggressively attempt to break your proposed plan. Identify the exact line or condition most likely to fail.
5. **Verify Systemically**: Evaluate the decision against immediate needs, technical debt accrual, and long-term maintainability.

## Core Principles

- **Active Disconfirmation**: Do not seek evidence that confirms your theory; design experiments that would prove your favorite hypothesis wrong.
- **Burden of Proof Calibration**: Align evidence requirements with risk. High-risk changes demand formal-level proof; low-risk changes require empirical checks.
- **Internal Tension Scan**:
  Search for self-contradictions within the plan (e.g., claiming a system is "high-performance" while introducing O(n²) complexity in a critical
- **Information Gain Optimization**: Prioritize actions that maximize information about the system's state over actions that merely "try to fix it."
- **Socratic Depth**: Apply a minimum "3-Why" drill-down for any anomaly. Move from the immediate symptom to the behavioral anomaly, to the foundational flaw.
- **The Steelman Protocol**: Before critiquing a plan, articulate it in its strongest possible form. If you cannot Steelman it, you are not ready to reject it.
path).

## What to Avoid

- **Confirmation Bias**: Over-weighting evidence that supports an initial guess while ignoring contradictory anomalies.
- **False Dichotomies**: Assuming only two opposing solutions exist without exploring orthogonal architectural paths.
- **Shallow Fixes**: Patching symptoms instead of addressing the architectural or structural root causes.
- **The Sunk Cost Fallacy**: Persisting with a failing approach or refactor just because effort was already invested.

## Limitations

- This skill provides a cognitive framework but does not execute external tooling; it relies on the agent to apply these principles internally during planning, execution, and review phases.
