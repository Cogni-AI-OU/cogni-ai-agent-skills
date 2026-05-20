---
name: apache-airflow-dags
description: 'Expert-level guide for authoring Apache Airflow DAGs, focusing on the skeleton strategy, contract-driven logic, and environment context. You MUST load this skill when asked to write, refactor, or structure Airflow DAGs.'
license: MIT
---

# Apache Airflow DAGs

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- Generating or writing new Apache Airflow DAGs.
- Refactoring, debugging, or analyzing existing Airflow DAGs.
- Architecting data pipelines using Airflow's TaskFlow API.

## When Not to Use

- Interacting with the Airflow REST API to trigger DAG runs or manage connections (use `apache-airflow-api` instead).

## Core Process

1. **Define the Universe**: Explicitly declare the context (Airflow version, executor type, cloud provider, and constraints) before generating code to avoid deprecated syntax.
2. **Apply the Skeleton Strategy**:
   - Step 1: Draft the high-level plan in natural language without generating code.
   - Step 2: Generate the DAG structure graph using placeholders (e.g., `EmptyOperator` from `airflow.providers.standard.operators.empty`). Do not add business logic or documentation yet.
   - Step 3: Iteratively replace placeholders with actual business logic and TaskFlow decorators.
   - Step 4: Add selective comments explaining the *why* (not the *what*), configure retries, and set up notifications.
3. **Establish Data Contracts**: Specify explicit input schemas, output targets, and idempotency constraints (e.g., using `MERGE` or `UPSERT`) rather than vague transformation requests.
4. **Format as a Technical Spec**: Structure requests and workflows using Markdown headers (`## Goal`, `## Context`, `## Data Contract`) and pseudo-XML tags (`<schema>`, `<code_snippet>`) for raw data.
5. **Force the Source of Truth**: Inject exact snippets from official documentation (e.g., `llms.txt`) to anchor the execution and prevent context contamination from older Airflow versions.

## Core Principles

- **Code is a Liability**: Auto-generated code without clear guardrails leads to maintainability issues. Ensure the *why* and the *schema constraints* are thoroughly defined.
- **Context is King**: Always prioritize explicit constraints over general assumptions, matching the target environment perfectly.

## Best Practices

- **Use Golden Records**: Reference established, production-ready DAGs (golden records) to enforce organizational naming conventions and architectural patterns.
- **Embrace TaskFlow API**: Leverage `@task` and `@dag` decorators for cleaner data passing over legacy XCom patterns, unless constrained otherwise.

## What to Avoid

- **Vibe Coding Large Blocks**: Generating hundreds of lines of DAG logic in a single shot without verifying the structural skeleton first.
- **Over-commenting**: Creating comments that simply narrate Python syntax.
- **Assuming Idempotency**: Never assume a task will automatically be idempotent; explicitly define boundaries like `logical_date` and insert strategies.

## Common Pitfalls

- **Context Contamination**: Defaulting to deprecated Airflow paradigms (e.g., `schedule_interval` instead of `schedule` or `timetable`). *Prevention: Always define the target Airflow version (e.g., Airflow 3.1) in the context block.*
- **Hallucinated Schemas**: Generating column names or relationships that do not exist. *Prevention: Use contract-driven definitions with explicit schemas.*
- **Missing Provider Packages**: Referencing operators that the environment lacks. *Prevention: Verify that the imported operators align with the available or defined providers.*
