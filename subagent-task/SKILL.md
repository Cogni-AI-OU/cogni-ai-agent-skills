---
name: subagent-task
description: >-
  Guidance and protocols for spawning sub-agents via the task tool to handle complex, multi-step, or parallelizable tasks.
  You MUST load this skill when the task tool for invoking sub-agents is available.
---

# subagent-task

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Provides policies and examples for using the `task` tool to spawn sub-agents for specialized, parallel, or complex tasks.

## Core Principles

- **Specialization**: Delegate tasks to specialized project agents rather than attempting to handle broad contexts monolithically.
- **Parallelization**: Spawn multiple agents concurrently for independent sub-tasks (e.g., retrieving facts, analyzing logs, validating plans).
- **Context Encapsulation**: Spawning sub-agents prevents the primary agent's context from becoming cluttered. Synthesize results from sub-agents into the final response.

## SUBAGENT DELEGATION POLICY

The use of the `task` tool and spawning sub-agents is permitted for complex, multi-step tasks, but delegation is limited to the project agents explicitly configured by this runtime.

- **Allowed Delegation Targets**: Use only the named project agents exposed by this runtime configuration.
- **Built-in Subagents Disabled**: Built-in `explore` and `general` subagents are not approved for this runtime and MUST NOT be used, even if a host tool still lists them.
- **Maintain Context**: Ensure that the primary agent remains the coordinator and synthesizes the results from sub-agents into the final response.
- **Strategic Delegation**: Delegate only when the task involves broad codebase analysis or independent sub-tasks that can be executed in parallel.

## Example: Agent Delegation Protocol

```mermaid
%% --------------------------------------------------------
%% Agent Delegation Protocol
%% --------------------------------------------------------
flowchart TD
    subgraph Flow_Agent_Delegation ["Agent Delegation Protocol"]
        direction TB
        Arch((Cogni AI Architect))
        Arch -->|task tool| DevOps[cogni-ai-devops<br/>Task automation, CI/CD, IaC]
        Arch -->|task tool| FactOps[cogni-ai-fact-ops<br/>Maintain facts & info consistency]
        Arch -->|task tool| PyDev[cogni-ai-python-dev<br/>Write, test, debug Python]
        Arch -->|task tool| BrainOps[cogni-ai-brain-ops<br/>Gather facts, constraints, plan]
        Arch -->|task tool| GHOps[cogni-ai-github-ops<br/>Modify comments, issues, discussions]
        Arch -->|task tool| CodeRev[cogni-ai-code-reviewer<br/>PR analysis, quality, security]
        Arch -->|task tool| SecAud_Arch[cogni-ai-security-auditor<br/>Expert deep security audit]
        Arch -->|task tool| PlanRev[cogni-ai-plan-reviewer<br/>Architectural & plan validation]
        Arch -->|task tool| Tester[cogni-ai-tester<br/>Execute tests, verify behavior]
        Arch -->|task tool| C7Ops[cogni-ai-context7-ops<br/>Retrieve & filter documentation]
    end
```

## Example: Delegation Scenarios

```mermaid
flowchart TD
    Trigger{Task Requirement}

    Trigger -->|Automation/CI/CD/IaC| DevOps["devops<br/>CI/CD and automation tasks"]
    Trigger -->|Complex task| Brain["brain-ops<br/>Brainstorm and architect plan"]
    Trigger -->|Docs updated| Docs["docs-editor<br/>Review and update documentation"]
    Trigger -->|GitHub writes| GHOps["github-ops<br/>Invoke GitHub write operations"]
    Trigger -->|Plan validation| PlanRev["plan-reviewer<br/>Validate plan plausibility"]
    Trigger -->|Python needed| PyDev["python-dev<br/>Write and test Python code"]
    Trigger -->|Large diff| CodeRev["code-reviewer<br/>Final code quality review"]
    Trigger -->|Security audit| SecAud["security-auditor<br/>Perform deep security audit"]

    classDef scenario fill:#f9f,stroke:#333,stroke-width:2px;
    class Docs,Brain,PyDev,GHOps,PlanRev,CodeRev,SecAud,DevOps scenario
```

## Usage Patterns

- Always pass a clear `description` and a detailed `prompt` to the sub-agent.
- Provide the `subagent_type` argument to match the desired role. Ensure you check your available tools dynamically to find the currently supported list of project-specific agents rather than relying on a hardcoded list, as this functionality exists and is strongly recommended to be utilized for more specialized agents for relevant context.
- Ensure the primary agent acts as a coordinator, processing the `task_result` from each sub-agent before continuing the plan.
- If a sub-agent misbehaves (e.g., returning an unexpected reply) or fails to meet expectations, report this issue to the user with a clear explanation.

## Related Skills

- **critical-thinking**:
  You MUST load this skill when deconstructing complex tasks for sub-agent delegation.
- **gh**:
  You MUST load this skill when working with the `gh` command and its subcommands.
