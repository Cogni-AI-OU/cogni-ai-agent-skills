---
name: brainstorm
license: MIT
description: >-
  Activate brainstorming protocol to explore options, research, deconstruct complexities, and summarize available data into simple diagrams.
  You MUST load this skill when asked to brainstorm, explore options, or break down complex problems.
---

# Skill brainstorm

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Exploring multiple architectural paths or design options before committing to a single solution (Design-It-Twice protocol).
- Breaking down a complex, ambiguous problem into atomic, manageable components for structured analysis.
- Gathering facts, constraints, and empirical data from the codebase before formulating any conclusions.

## When Not to Use

- Executing a known, well-defined procedure with a single correct approach — use a task-specific skill instead.
- Performing deep analytical reasoning, validation, or adversarial testing of a single option — load the `critical-thinking` skill instead.
- Making direct edits or committing changes to the codebase — brainstorming is for exploration only, not execution.

## Common Pitfalls

- **Premature Convergence**: The most common failure is settling on the first viable solution. Always generate at least two distinct architectural paths (Design-It-Twice) before recommending a preferred option.
- **Diagram Overload**: Large, complex Mermaid diagrams with too many nodes become unreadable. Break them into focused, single-concept visualizations — one mindmap, one quadrant chart, etc.
- **Assumption Drift**: Brainstorming without factual grounding produces speculative results. Always gather empirical data from the codebase, project memory, or provided context before diverging into options.
- **False Dichotomies**: Avoid framing problems as binary choices (Option A vs. Option B). Explore the full orthogonal axes of the design space before narrowing down.
- **No Premature Convergent Thinking**: Explicitly document and present the discarded alternatives. If only one option is shown, the reader cannot evaluate whether the best path was chosen.

A cognitive framework and protocol for exploring options, breaking down complexities, and summarizing information.

## Core Process

1. **Context Gathering & Research**: Aggressively gather facts, existing data, and constraints before formulating any conclusions.
2. **Explore Options**: Generate multiple orthogonal approaches or alternative options. Do not settle for the first apparent solution.
3. **Deconstruct Complexities**: Break down the problem space into atomic, manageable components.
4. **Visual Summarization**: Synthesize the gathered data and complexities into simple, easy-to-read Mermaid diagrams (e.g., mindmaps, block diagrams, or flowcharts).

## Core Principles

- **Design-It-Twice Protocol**: ALWAYS generate at least two distinct architectural paths before recommending a preferred solution.
- **Divergent Before Convergent**: Ensure a broad exploration of the problem space (divergent thinking) before narrowing down to specific recommendations (convergent thinking).
- **Fact-Based Exploration**: Anchor all generated options in empirical data retrieved from the codebase, project memory, or provided context.
- **Recursive Decomposition**: Break every complex objective into its atomic components to manage cognitive load and ensure precision.
- **Visual Clarity First**: Use diagrams early to establish a shared mental model before diving into deep technical or textual analysis.

## Diagnostics and Usage Patterns

- **Component Architecture Visualization**: Map high-level structural components with a Mermaid `block-beta` diagram.
- **Context & Ecosystem Mapping**: Map out the current ecosystem, constraints, and known unknowns using a Mermaid `mindmap` before defining architectural changes.
- **Diagramming Focus**:
  Default to high-level topological or structural diagrams (`block-beta`, `flowchart`, `mindmap`, `quadrantChart`, `radar-beta`) to visualize options and establish facts.
- **Flow & Logic Breakdown**: Detail sequential states and dependencies using a Mermaid `flowchart`.
- **Root Cause & Priority Mapping**: Use `ishikawa-beta`, `quadrantChart`, or `radar-beta` for evaluating alternatives, prioritization, and deep-dive problem exploration.

## Brainstorming - Problem Breakdown

When you need to explore a complex problem, use this step-by-step visual approach to ensure all facts are gathered and complexity is reduced:

### Step 1: Context & Ecosystem Mapping

Before proposing any changes, gather all relevant facts and constraints. Map the existing environment using a `mindmap`.

```mermaid
%% This diagram visualizes the existing ecosystem and constraints
mindmap
  root((System Context))
    Dependencies
      External API
      Database
    Constraints
      Performance
      Security
    Known Unknowns
      Rate limits
```

### Step 2: Component Architecture Visualization

Break the problem into structural parts and orthogonal options using a `block-beta` diagram so the options can be compared effectively.

```mermaid
%% This block diagram shows multiple architectural options
block-beta
  columns 3
  space Option1 space
  FrontendA DatabaseA CacheA
  space Option2 space
  FrontendB DatabaseB CacheB
```

### Step 3: Flow & State Modeling

Finally, visualize the behavior, state changes, or sequential logic required for the proposed options using a `flowchart`.

```mermaid
%% This flowchart explores a process logic option
flowchart LR
    Start --> CheckState{Is Valid?}
    CheckState -->|Yes| Process[Process Data]
    CheckState -->|No| Reject[Reject Request]
```

### Step 4: Root Cause Exploration (If Applicable)

When brainstorming around a systemic issue or failure, use an `ishikawa-beta` (fishbone) diagram to aggressively deconstruct contributing factors before jumping to conclusions.

```mermaid
%% This diagram categorizes contributing factors to a problem
ishikawa-beta
    Core Problem or Failure
    Infrastructure
        Network latency
    Codebase
        Tech debt
        Missing tests
    Dependencies
        Deprecated API
```

### Step 5: Prioritization Mapping

When multiple paths, options, or tasks are generated, map them onto a `quadrantChart` to evaluate trade-offs like effort versus impact.

```mermaid
%% This diagram visualizes task or option prioritization
quadrantChart
    title Option Prioritization
    x-axis Low Effort --> High Effort
    y-axis Low Impact --> High Impact
    quadrant-1 Quick Wins
    quadrant-2 Strategic
    quadrant-3 Time Sinks
    quadrant-4 Fill-ins
    "Option A": [0.2, 0.8]
    "Option B": [0.8, 0.9]
    "Option C": [0.7, 0.3]
```

### Step 6: Trade-off Analysis

For complex architectural decisions, use a `radar-beta` diagram to score options across multiple competing dimensions.

```mermaid
%% This diagram scores options across various constraints
radar-beta
    title Architectural Trade-offs
    axis Performance, Security, Maintainability, Cost-Efficiency, Scalability
    curve Performance {8, 7, 6, 4, 9}
    curve Scalability {6, 9, 8, 7, 5}
```

## What to Avoid

- **Assumption-Driven Brainstorming**: Relying on guesses instead of factual context gathered through tools.
- **False Dichotomies**: Assuming only two opposing solutions exist without exploring orthogonal architectural paths.
- **Overcomplicated Diagrams**: Creating massive, unreadable diagrams. Break them into smaller, focused visual summaries.
- **Premature Convergence**: Proposing a final solution without explicitly documenting the discarded alternative options.

## Related Skills

- **brainstorm-agent-runs**: You MUST load this skill when identifying agentic runs in CI/CD for a Pull Request.
- **brainstorm-github-pr**: You MUST load this skill when asked to analyze or brainstorm a Pull Request.
- **critical-thinking**: You MUST load this skill when evaluating the options generated during brainstorming.
- **mermaid**: You MUST load this skill when constructing standard Mermaid diagrams.
- **mermaid-beta**: You MUST load this skill when using experimental Mermaid diagrams.
- **minizinc**: You MUST load this skill when executing or deeply modeling constraint satisfaction problems.
