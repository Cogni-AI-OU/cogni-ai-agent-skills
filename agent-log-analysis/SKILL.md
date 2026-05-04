---
name: agent-log-analysis
description: >-
  Procedures and templates for analyzing agent session logs, extracting telemetry, and generating
  standardized visual audit reports.
  You must load this skill when auditing or analyzing autonomous agent log files.
---

# Agent Log Analysis & Reporting

This skill dictates the mechanical execution and rigid formatting requirements for auditing AI agent session logs.

## 1. Log Retrieval Mechanics

If logs are not directly provided in the prompt, retrieve them using:

- **GitHub Actions Runs**: `gh run view <run-id> --log` or `gh run view <run-id> --log-failed`
- **Local Artifacts**: Parse directories under `temp/extract/` or `logs/` using `grep`, `cat`, or file search tools.

Raw logs from GitHub runs can be filtered by:

```bash
awk '/PROMPT:/,/Post job cleanup/ { $1=""; print substr($0,2) }'
```

## 2. Standardized Reporting Structure

You MUST systematically output your findings adhering to this strict standardized structure.
Do not invent new structures or deviate from these templates.

### 2.1 Text Report (Markdown)

```markdown
The agent session for **github.run_id [Run ID] (attempt [Attempt Number])** was
[successful / unsuccessful / partially successful] and [followed / deviated from]
established protocols. Operating as the `[Agent Persona]`, the agent completed
the task of [Brief Task Description] while maintaining strict adherence to the
project's initialization and verification workflows.

#### Session Summary
* **Primary Task:** [What was the agent explicitly instructed to do?]
* **Workflow Compliance:** [Did the agent load the necessary constraints, flows, and instructions?]
* **Conclusion:** [What was the final state?]

#### Key Actions & Decisions
* **Context Gathering:** [How did the agent acquire necessary information?]
* **Task/Workflow Management:** [How did it track progress?]
* **Execution / Tracing:** [What were the core actions taken?]
* **Self-Verification:** [Did it verify the environment state?]

#### Root Cause Identified (If Applicable)
The agent discovered a **[brief description of the core issue]**:
1. **[Step 1]**: [Description]

#### Issues Encountered
* **[Issue / None]:** [Describe any tool failures or explicitly state "None".]

#### Recommendation Provided (Optional)
[Summarize any recommendations]
```

### 2.2 Comprehensive Visual Audit Suite (Mermaid & Data)

#### A. Agent Radar Analysis

Generate a `radar-beta` diagram to score the agent from 1 to 10 on core competencies:

```mermaid
radar-beta
    title "Agent Performance Alignment"
    axis Task_Completion, Protocol_Compliance, Tool_Proficiency, Self_Verification, Analytical_Depth, Execution_Efficiency
    curve Agent {8, 9, 7, 8, 9, 7}
```

#### B. Agent Execution Flow (Sequence Diagram)

Generate a Mermaid `sequenceDiagram` visualizing chronological actions.

- **Participants**: `Workflow`, `Agent`, `Tools`, `FileSystem`, `GitHub`
- **Focus**: Initialization, Context Gathering, Execution, Verification.

#### C. Agent Cognitive & Execution Loop (State Diagram)

Generate a Mermaid `stateDiagram-v2` modeling the internal state machine.

- **States**: `Initializing`, `ContextGathering`, `Executing`, `ErrorRecovery`, `Verifying`.
- **Transitions**: Explain *why* the agent moved states (e.g., "Syntax Error Detected").

#### D. Agent Execution Journey (Friction & Success Map)

Generate a Mermaid `journey` diagram of problem-solving friction.

- **Score 1-5**: (5: Flawless, 1: Error/Hard failure).
- **Sections**: `Initialization`, `Investigation`, `Execution`, `Verification`.
- **Actors**: `Agent`, `Bash`, `GitHubAPI`, `FileSystem`.

#### E. Agent Execution Alignment (Venn Diagram)

Generate a Mermaid `venn-beta` diagram visualizing action alignment. Ensure strings are properly delimited.

```mermaid
venn-beta
    title "Action Alignment"
    set Intent["User Request"]
    set Actions["Agent Tool Calls"]
    set Rules["System Protocols"]

    union Intent,Actions["Targeted Actions"]
    union Intent,Rules["Expected Protocol"]
    union Actions,Rules["Compliant Actions"]
    union Intent,Actions,Rules["Perfect Execution"]
```

#### F. Root Cause & System Architecture (If Errors Occurred)

If failures or bugs hit the agent, you MUST generate:

1. **`ishikawa-beta`**: Evaluate branches to find the root cause of the failure.

   ```mermaid
   ishikawa-beta
       Agent Failure Description
       Context & Prompts
           Missing instructions
       Tools & Capabilities
           Bash restricted
       Logic & Reasoning
           Hallucinated path
       Workflow & Protocols
           Skipped verification
       Environment
           Read-only repo
   ```

2. **`architecture-beta`**: Visualize mechanical boundaries to show where data dropped or the chain failed.

   ```mermaid
   architecture-beta
       group api(cloud) [API Gateway]
       service auth(server) [Auth Service] in api
       service db(database) [Session DB] in api

       user(user) [Agent Session]
       user -> auth: Request Logs
       auth -> db: Query Session
   ```
