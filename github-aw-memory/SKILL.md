---
name: github-aw-memory
description: Guide for persistent memory strategies in agentic workflows. You MUST load this skill when designing workflows that persist state across runs via cache-memory, repo-memory, or comment-memory.
license: MIT
---
# Skill github-aw-memory

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

Persistent memory strategy for GitHub Agentic Workflows (`cache-memory`, `repo-memory`, `comment-memory`).

## Core Principles

- **Prefer Built-in History**: Rely on Git history, issue timelines, and graph links before writing new persistent files. Store only stable watermarks (SHA, updated_at).
- **Default to `cache-memory`**: Use for deduplication, incremental processing, and metric baselines. It avoids repository noise but expires (default 7 days).
- **Use `repo-memory` Sparingly**: Use only for long-lived knowledge (e.g., security baselines) that must survive cache expiry. Produces Git commits.
- **Use `comment-memory`**: Persist workflow notes inline on the triggering issue/PR.

## Commands / Usage Patterns

**`cache-memory` (First Choice)**
```yaml
tools:
  cache-memory: true # Or specific config
```
- Path: `/tmp/gh-aw/cache-memory/`
- Safe timestamps: MUST use `YYYY-MM-DD-HH-MM-SS` (no colons, `T`, or `Z`) to prevent artifact upload failures.

**`repo-memory` (Persistent/Auditable)**
```yaml
tools:
  repo-memory:
    branch-name: memory/agent-notes
    allowed-extensions: [".json", ".md"]
```
- Path: `/tmp/gh-aw/repo-memory/`
- Engine restriction: Requires Claude or custom engine. Copilot NOT supported.
- Variants: Use `wiki: true` for GitHub Wiki backend.

**`comment-memory` (Issue/PR Scope)**
```yaml
tools:
  comment-memory: true
```
- Path: `/tmp/gh-aw/comment-memory/<memory_id>.md`

## What to Avoid

- Using `repo-memory` for ephemeral per-run state or as a synonym for `cache-memory`.
- Including colons in `cache-memory` filenames (breaks Windows-hosted runners artifact upload).
- Caching full issue payloads instead of canonical identifiers.

## Related Skills

- **gh-aw**:
  You MUST load this skill when working with the `gh aw` command.
