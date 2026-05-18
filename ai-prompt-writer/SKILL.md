---
name: ai-prompt-writer
description: Design, review, and optimize secure AI prompts using advanced prompt engineering patterns, safety frameworks, and injection mitigation strategies.
license: MIT
---

# Skill: AI Prompt Writer

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Design, review, and optimize secure AI prompts using advanced prompt engineering patterns, safety frameworks, and injection mitigation strategies.

## Core Process

1. **Contextualize**: Define explicit tasks, target audience, and precise constraints (format, length, tone).
2. **Pattern Selection**: Apply Zero-Shot for simple tasks, Few-Shot for formats, Chain-of-Thought for reasoning, and Role Prompting for specialized contexts.
3. **Harden**: Sanitize all dynamic inputs to prevent prompt injection and data leakage.
4. **Validate**: Red-team against bias, harmful outputs, and edge cases.

## Core Principles

- **Clarity over Verbosity**: Issue concise, unambiguous directives. Drop conversational filler.
- **Strict Constraints**: Dictate exact output structures (JSON, markdown) and scope boundaries.
- **Secure Construction**: Never directly interpolate untrusted input. Use parameterization or robust sanitization (e.g., `Translate this text: [SANITIZED_USER_INPUT]`).
- **Data Minimization**: Exclude sensitive, personal, or proprietary data from prompts.
- **Neutrality**: Enforce inclusive language; eliminate demographic or contextual assumptions.

## When to Use

- Engineering system prompts, LLM templates, or Copilot instructions.
- Auditing existing prompts for injection vulnerabilities or data leakage risks.
- Defining automated prompt evaluation metrics or safety checklists.

## Commands / Usage Patterns

- **Role Setup**: `You are a <role> with <years> experience in <domain>. Review <target> and identify <issues>.`
- **Chain-of-Thought**: `Solve this step-by-step: 1. <step 1> ...`
- **Few-Shot Validation**: `Input: <example_in> \n Output: <example_out>`
- **Injection Defense**: Replace `` `Text: ${userInput}` `` with `` `Text: ${sanitizeInput(userInput)}` ``.

## Best Practices

- Standardize inputs using clear delimiters (e.g., `"""`, `###`, `<tag>`).
- Implement content moderation pre/post-processing for user-facing AI pipelines.
- Establish A/B testing and automated evaluation for continuous prompt refinement.
- Document prompt purpose, scope, assumptions, and limitations.

## Common Pitfalls to Avoid

- **Too Vague**: "Make the code better" → Specify exactly what "better" means.
- **Too Restrictive**: Over-constraining can prevent useful optimizations.
- **Missing Context**: Include relevant domain knowledge and terminology.
- **No Examples**: Concrete examples guide an LLM better than abstract descriptions.
- **Ignoring Artifacts**: Don't refine prompts based on error feedback.

## What to Avoid

- **Unbounded Inputs**: Permitting raw user input to override system instructions.
- **Overfitting**: Hardcoding constraints tied to specific training data examples.
- **Echoing Secrets**: Designing prompts that inadvertently reflect sensitive inputs.

## References

- [AI Prompt Engineering & Safety Best Practices](https://github.com/github/awesome-copilot/blob/main/instructions/ai-prompt-engineering-safety-best-practices.instructions.md)
