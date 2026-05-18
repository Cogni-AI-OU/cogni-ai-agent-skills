---
name: mot
description: Evaluate and classify machine learning models based on the Model Openness Framework (MOF), and extract model metadata such as architecture, origin, producer, and components.
license: MIT
---

# Skill: Model Openness Tool (MOT)

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- When finding a list of open models or specific model metadata from the Model Openness Tool repository.
- When classifying a machine learning model's degree of openness using MOF.
- When extracting specific model properties like architecture, release date, or components.
- When evaluating a model against MOF criteria for research or compliance documentation.
- When comparing openness levels across multiple models using the MOT classification system.

## When Not to Use
- When evaluating model performance (accuracy, latency, throughput) — MOT only assesses openness, not quality or capability.
- When determining license compatibility for production use — MOT classifies openness but does not provide legal advice or license compatibility analysis.
- When comparing models on non-openness criteria (e.g., training cost, dataset provenance beyond MOF) — use domain-specific tools instead.
- When the model is not registered in the MOT repository — the tool cannot evaluate unregistered models.

## Common Pitfalls
- The MOT classification is based on the Model Openness Framework (MOF), which evaluates components like training data, code, and parameters — a high openness score does not imply permissive licensing or usability.
- Model definitions in the MOT repository may lag behind new releases — always verify the model version and date against the official source.
- Raw YAML files from the MOT repository may contain nested structures that require careful `yq` querying — test your extraction queries against the actual file format.

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
