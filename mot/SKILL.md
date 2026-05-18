---
name: mot
description: Evaluate and classify machine learning models based on the Model Openness Framework (MOF), and extract model metadata such as architecture, origin, producer, and components.
license: MIT
---

# Skill: Model Openness Tool (MOT)

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

MOT provides a list of all the models currently registered and how they rank against the MOF classes.

## Core Process

1. **Locate Models**: Identify models within the target repository (`https://github.com/lfai/model_openness_tool/tree/main/models`).
2. **Extract Metadata**: Parse model files to extract architecture, origin, producer, type, date of release, framework, and components.
3. **Classify Openness**: Evaluate the model against the Model Openness Framework (MOF) criteria based on its components.
4. **Format Output**: Present the classification and metadata in a structured, concise format.

## Core Principles

- **Direct Extraction**: Fetch and parse raw metadata directly from the source JSON/YAML files.
- **Strict MOF Adherence**: Always map components to the official MOF evaluation criteria for accurate classification.
- **Concise Reporting**: Return only the requested fields (e.g., framework, architecture, producer) and the final MOF classification.

## When to Use

- When finding a list of open models or specific model metadata from the Model Openness Tool repository.
- When classifying a machine learning model's degree of openness using MOF.
- When extracting specific model properties like architecture, release date, or components.

## When Not to Use

- When searching for general-purpose software libraries or non-AI code repositories (use `github-topics` instead).
- For evaluating the runtime performance, latency, or accuracy benchmarks of an LLM.
- If you need to actually download and run the weights of a machine learning model.

## Common Pitfalls

- **Ignoring the Framework**: Classifying a model simply as "open source" without actually evaluating it against the specific tiers and definitions of the Model Openness Framework (MOF).
- **Outdated Metadata**: Relying on external web searches for model licensing instead of parsing the official YAML files maintained within the MOT repository.
- **Hallucinating Components**: Assuming a model includes training data or specific architecture details without explicitly extracting that information from its metadata file.

## Commands / Usage Patterns

Fetch and parse a model definition directly from the source repository using `curl` and `yq`:

```bash
curl -s https://raw.githubusercontent.com/lfai/model_openness_tool/main/models/<model-file>.yaml | yq '.'
```

## References

- [List of Models](https://mot.isitopen.ai/) (Name, Organization, Classification)
- [Licenses](https://mot.isitopen.ai/licenses)
- [Model Openness Tool Repository](https://github.com/lfai/model_openness_tool)
- [Models Directory](https://github.com/lfai/model_openness_tool/tree/main/models)
