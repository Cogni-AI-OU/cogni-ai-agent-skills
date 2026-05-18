---
name: gh-models
description: 'GitHub CLI models (`gh models`) operations for running and evaluating AI models. You MUST load this skill when working with the `gh models` command.'
license: MIT
---

# gh-models Skill

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- You need to run AI model inference from the command line, piping in repository content (issue bodies, PR diffs, commit messages) as context.
- You need to evaluate prompt quality with structured test cases and scorers via `gh models eval`.
- You need to auto-generate robust test suites for a prompt using PromptPex methodology via `gh models generate`.
- You are managing `.prompt.yml` files as version-controlled assets and need to validate them before committing.
- You need to list available models, inspect model details, or compare capabilities across providers.
- You are building agentic workflows that require LLM inference and need a CLI-native, eval-gated pipeline.

## When Not to Use
- You need to deploy a model to production or manage model endpoints — `gh models` is for experimentation and evaluation, not serving.
- You need fine-grained control over inference parameters not exposed by the CLI (e.g., logprobs, streaming callbacks) — use the provider's SDK or API directly.
- You are building a prompt that will be used in a non-GitHub context where `.prompt.yml` format is not supported — consider a standalone prompt management approach.
- You need to train or fine-tune a model — `gh models` only supports inference on existing models, not training.

## Gotchas
- Marketplace model IDs (e.g., `azureml-xai/grok-3-mini`) may differ from CLI model IDs (e.g., `xai/grok-3-mini`); always use `gh models list` to get the exact identifier rather than guessing from marketplace names.
- `gh models generate --effort high` can be token-expensive — monitor usage and start with `--effort low` or `--effort medium` for iterative prompt development before committing to full coverage.
- Never use a `.prompt.yml` without running `gh models eval --json` first — the eval gate catches 80%+ of failure modes including hallucinations, edge cases, and security risks.
- Prompts piped from repository events (issue bodies, PR diffs) contain real user data — ensure you have appropriate data handling policies in place, especially for private repositories.

**CLI extension for GitHub Models service** — `gh extension install github/gh-models` (requires authenticated `gh` CLI).

Run, evaluate, and auto-generate tests for AI prompts directly from the terminal. Ideal for CLI-centric
agentic workflows on issues, PRs, repo events, and prompt engineering at scale.

## Mindmap of Commands

```mermaid
mindmap
  root((gh models))
    eval
      Evaluate prompts
    generate
      Generate tests
    list
      List models
    run
      Run inference
    view
      View details
```

## Installation & Upgrade

```bash
gh extension install github/gh-models
gh extension upgrade github/gh-models
gh models list  # verify + list available model IDs (e.g. openai/gpt-4.1, openai/gpt-4o-mini)
```

## Model Catalog

View the full list of available models and their capabilities in the [GitHub Models Catalog](https://models.github.ai/catalog/models).

## Core Commands

### `gh models run` — Inference (single-shot, REPL, or piped repo content)

- **REPL (interactive chat)**: `gh models run` (select model; `/help`, `/model`, `/clear` supported).
- **Single prompt**: `gh models run openai/gpt-4o-mini "Summarize the following PR description in 3 bullets"`
- **Piped repo content** (issues/PRs/events):

  ```bash
  cat issue_body.txt | gh models run --file summarize.prompt.yml > /tmp/summary.txt
  gh issue view 123 --json body | jq -r .body | gh models run openai/gpt-4.1 "Extract action items and risks"
  ```

- **With model params**: `gh models run --temperature 0.2 --max-tokens 500 openai/gpt-4.1 "..."`

### `gh models eval` — Structured evaluation with test cases + scorers

```bash
gh models eval my_prompt.prompt.yml                    # human-readable summary + scores
gh models eval my_prompt.prompt.yml --json > /tmp/results.json  # parseable (test cases, outputs, scores, pass/fail)
```

- Uses same evaluators as GitHub Models UI (string match, similarity, LLM-as-judge, custom rules).

### `gh models generate` — Auto-generate robust test suites + evaluator (PromptPex methodology)

```bash
gh models generate my_prompt.prompt.yml
# Advanced (recommended for production prompts)
gh models generate \
  --effort high \
  --groundtruth-model "openai/gpt-4.1" \
  --instruction-intent "Focus on edge cases, hallucinations, and security risks" \
  --session-file my_prompt.session.json \
  my_prompt.prompt.yml
```

- **Process**: Intent analysis → Input spec → Output rules (pre/post-conditions) → Inverse rules (invalid inputs)
  → Diverse test cases + evaluator.
- Effort levels: `min` (fast) | `low` | `medium` | `high` (max coverage, higher token cost).
- Post-generate: immediately run `gh models eval` on the updated `.prompt.yml`.
- **Never skip**: Treat prompt changes like code changes — generate + eval before use.

## .prompt.yml — First-Class Version-Controlled Prompt Assets

Store prompts anywhere in repo (e.g. `.github/prompts/`). Structure enables:

- Model + params (temperature, max_tokens, etc.)
- System/user message templates with `{{variables}}`
- Test cases (inputs + expected outputs/ground truth)
- Evaluators (built-in + custom LLM judges)
- Metadata (name, description, tags)

**Benefits**:

- Git history, branching, rollback for prompts.
- Reproducible experiments across team/agents.
- Direct input to `eval`/`generate`/`run --file`.

## Best Practices (Entropy-Pruned for Max Efficiency)

- **Prompts as code**: Never edit prompts in UI only — commit `.prompt.yml` + generate/eval.
- **Generate-first**: On any prompt edit, run `gh models generate --effort high` then `eval` before use
  (catches 80%+ failure modes early).
- **JSON everywhere for agents**: `--json` + `jq` for pass/fail, metrics extraction, automated rollback.
- **Model selection discipline**: Use `gh models list`; prefer cheap/fast (gpt-4o-mini) for high-volume triage;
  reserve high-intelligence models for complex reasoning.
- **Model ID Accuracy**: Always use the identifier from `gh models list`. Marketplace IDs (e.g. `azureml-xai/grok-3-mini`) may differ from CLI IDs (e.g. `xai/grok-3-mini`). Use `gh models view <model-id>` to verify.
- **Modern Endpoint**: Prefer the modern `https://models.github.ai/inference` endpoint for broader model support.
- **Piping + context injection**: Always pipe exact repo event payload (issue body, PR diff, commit message) —
  avoid hard-coded examples.
- **Rate-limit & cost awareness**: Monitor via GitHub token; use `--max-tokens` + low temp for deterministic
  tasks; batch via multiple short runs.
- **REPL for exploration**: Use interactive `gh models run` for rapid prototyping before freezing
  into `.prompt.yml`.
- **Kaizen loop**: After each production use, append failure examples to test cases in `.prompt.yml` and re-generate.
- **Agent orchestration**: In multi-agent setups, designate one sub-agent to own `gh models` calls with
  strict contracts (input schema, output schema, eval gate).

## Termination Invariants

- Never commit/use a `.prompt.yml` without passing `gh models eval --json` (pass_rate ≥ target).
- Never use `run` without corresponding eval harness.
- Always version the exact model ID + parameters + prompt hash.
- On any regression: root-cause via single-variable delta (change one test case or param), re-generate, re-eval.

## Related Skills

- **gh-pr**:
  You MUST load this skill when working with the `gh pr` command.
- **gh-run**:
  You MUST load this skill when working with the `gh run` and the `gh workflow` commands.
