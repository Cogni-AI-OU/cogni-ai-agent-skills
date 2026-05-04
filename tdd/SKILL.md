---
name: tdd
description: >-
  Commands, step-by-step procedures, and mechanical execution for test engineering, testability audits, and the TDD lifecycle.
  You must load this skill when executing test tasks, designing tests, doing TDD, or verifying system behavior.
---

<!-- markdownlint-disable MD013 -->

# Test-Driven Development (TDD) & Test Engineering Execution

**Skill Focus**: Commands, step-by-step procedures, and mechanical execution for test engineering, testability audits, and the TDD lifecycle.

## When to Activate

- When executing test tasks, designing tests, or verifying system behavior.
- When requested to write tests or practice Test-Driven Development (TDD).
- When conducting testability audits on existing or new codebases.
- When addressing bugs that require regression test coverage.

## Relevant Skills

- `pre-commit`: For integration with testing hooks and validation.
- `test-engineering` / `integration-testing` (if applicable).

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
