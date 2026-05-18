---
name: tdd
license: MIT
description: >-
  Commands, step-by-step procedures, and mechanical execution for test engineering, testability audits, and the TDD lifecycle.
  You MUST load this skill when executing test tasks, designing tests, doing TDD, or verifying system behavior.
---

# Test-Driven Development (TDD) & Test Engineering Execution

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Writing unit, integration, or end-to-end tests with strict Red-Green-Refactor discipline.
- Performing testability audits on existing code before introducing test coverage.
- Reproducing and fixing bugs by first writing a failing test that demonstrates the defect.

## When Not to Use

- Exploratory coding or prototyping where the API surface is too unstable to commit to test contracts.
- One-off scripts, utilities, or throwaway code that will not be maintained or reused.
- When the project has no test infrastructure (runner, assertions, mocks) and setting it up exceeds the value of the tests themselves.

## Common Pitfalls

- The Red-Green-Refactor cycle must be followed strictly—writing tests after implementation violates the TDD contract and produces implementation-biased rather than behavior-specified tests.
- "Test names as behavioral specifications" is easy to neglect; vague names like `test_login()` obscure what is actually being verified.
- The anti-rationalization invariants ("I'll add tests later", "This is too simple to test") must be actively enforced by the agent—they represent the most common TDD failure modes in autonomous development.
- Intermittent/flaky tests must be treated as hard failures, not dismissed as environmental noise; the root cause (race condition, timing dependency, shared mutable state) must be identified and fixed.

**Skill Focus**: Commands, step-by-step procedures, and mechanical execution for test engineering, testability audits, and the TDD lifecycle.

## Related Skills

- **critical-thinking**:
  You MUST load this skill when performing deep testability audits and deconstructing complex behavioral requirements.
- **tester**: Elite autonomous test engineering kernel for proving software correctness and behavioral contracts.
- **pre-commit**: For integration with testing hooks and validation.

## 1. Pre-Execution: Code Testability Audit

Before writing test code, execute this mechanical audit on the target module:

1. **Inversion of Control**: Identify if dependencies are hardcoded. If yes, extract them into constructor or method parameters before testing.
2. **State Accessibility**: Locate internal state mutations. Determine if state can be verified through public APIs. If not, isolate the pure logic into a verifiable function.
3. **Negative Space Matrix**: Generate a list of explicitly untested paths:
   - Error paths (exceptions thrown, null inputs)
   - Hidden boundaries (max lengths, 0 values)
   - Security input vectors (untrusted strings, out-of-bounds access)
4. **Intent Documentation Check**: Ensure test names read as explicit behavioral specifications.
   - *Pattern*: `"returns 404 when user strictly lacks tenant access"`
   - *Anti-Pattern*: `"test_user_error"`

## 2. TDD Lifecycle Execution Protocol

When instructed to address requirements or fix bugs, perform these exact steps:

### Step 2.1: Assert the Gap (Red)

1. Write a strict, failing test *first*.
2. Execute the test suite.
3. **Verification**: The test MUST fail. If it passes, the test is invalid or the test setup is flawed.

### Step 2.2: Dimensional Scaling

Expand the failing test (or add new tests) to cover the following permutations:

- **Happy Path**: The optimal flow.
- **Boundary Conditions**: Edges of scale, min/max limits.
- **Error Handling**: Graceful degradation, expected failure states.

### Step 2.3: Resolve the Gap (Green)

1. Implement the minimal atomic code required to turn the failing test green.
2. Do not add speculative features or abstract prematurely.
3. Run the test suite: Verify the test now passes.

### Step 2.4: Optimize (Refactor)

1. Restructure the implementation for readability, DRY (Don't Repeat Yourself), and adherence to architecture rules.
2. Run the test suite: Verify the test still passes.

## 3. Signal Extraction & Execution Rules

When executing test commands (e.g., `npm test`, `pytest`, `cargo test`):

- **Filter Mass-Logs**: Do not output raw mass-logs to the user. Extract the exact stack trace and pinpoint the assertion violation locus.
- **Flakiness Eradication**: If a test fails intermittently during standard runs, treat it as a hard failure. Identify the race condition or timeline dependency and patch the test harness.
- **Non-Destructive Testing Check**: Ensure the test command runs in isolation. If testing databases, verify transactional rollbacks or tear-down commands are executed post-run.

## 4. Anti-Rationalization Invariants

Autonomous agents must strictly reject attempts to bypass the TDD lifecycle. Enforce these axiomatic rebuttals:

- **Reject "I'll add tests after"**: Post-hoc tests validate implementation artifacts, not behavioral contracts. Tests MUST precede implementation.
- **Reject "Integration tests are enough"**: High-level tests lack root-cause localization precision. Adhere strictly to the test pyramid; prioritize fast, isolated unit tests.
- **Reject "This code is too simple to test"**: Simplicity is volatile. Un-tested code breaks silently during lifecycle evolution. Guarantee verifiable behavior through tests.
- **Reject "We don't have time for TDD"**: Unverified code generates exponential debugging debt. Enforce TDD to compress the total verification timeline.

## 5. Architectural Red Flags

Halt execution and refactor if any of these conditions are detected:

- Coverage metrics inflated by testing trivial auto-generated code (e.g., getters/setters).
- Tests authored post-implementation.
- Tests binding to internal implementation details (e.g., asserting private methods or raw DB schemas) rather than public API contracts.
- Tests passing despite intentional fault-injection (indicates over-mocking or tautological assertions).
- Verification restricted to "Happy Path" vectors, omitting negative space constraints.

## 6. Final Assurance Gates

Before concluding a test-engineering cycle, assert these completion invariant gates:

- [ ] **Behavioral Specification**: Every test maps to a distinct, traceable business behavior.
- [ ] **Contract-First**: Tests were explicitly authored prior to the implementation block (or concurrently for bug reproductions).
- [ ] **Critical Path Coverage**: No blind spots remain in core execution invariants based on coverage analysis.
- [ ] **Lifecycle Adherence**: The strict Red-Green-Refactor phase progression was respected.
- [ ] **Negative Space Verified**: Key edge cases (null injections, boundary limitations, empty states) are actively asserted.
- [ ] **Zero-Defect Run**: 100% of tests pass consistently without flakiness.
