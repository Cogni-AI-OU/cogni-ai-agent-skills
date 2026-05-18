---
name: gh-aw-compile
description: 'Regenerate and post-process all agentic workflows. You MUST load this skill when gh-aw is updated, workflow .md files change, or when asked to recompile/regenerate workflows.'
license: MIT
---

# Recompile Agentic Workflows

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- After modifying `.md` workflow source files to regenerate the corresponding `.lock.yml` files.
- After running `gh aw upgrade` to ensure all workflows are recompiled with the latest codemods.
- When repository automation is broken due to stale or mismatched lock files.
- As part of a CI/CD pipeline to verify that workflow definitions compile cleanly before deployment.
- After adding or removing agent files or actions that affect the workflow compilation output.

## When Not to Use

- Making changes to workflow behavior — modify the `.md` source files first, then compile. Compilation is a mechanical step, not an editing step.
- Debugging workflow execution failures at runtime — use `gh-aw-troubleshooting` or `github-actions` skills for runtime debugging.
- Creating new agentic workflows from scratch — use `gh-aw-new` skill for initial workflow creation.
- Editing `.lock.yml` files directly — these are auto-generated and will be overwritten.

## Common Pitfalls

- Verification after EVERY lock file change is mandatory — `pre-commit run --all-files` is not optional. Skipping it can result in broken workflows being committed.
- Strict mode violations (e.g., `contents: write` permissions) cause compilation failures — workflows should request only `read` permissions and use `safe-outputs` for write operations.
- Discussion category casing warnings ("General" vs "general") are non-blocking during compilation but may still need correction for consistency.
- After compilation, always run `git diff --stat` to review all changed files — expect changes in `.github/agents/`, `.github/aw/actions-lock.json`, and `.github/workflows/*.lock.yml`.

Use this skill when you need to regenerate all agentic workflow lock files and verify them.

## IMPORTANT: Verification is required after EVERY lock file change

Any time `.lock.yml` files are regenerated — whether via `gh aw compile`, `gh aw upgrade`, or any other gh-aw
command — you MUST run the repo-standard pre-commit hooks afterward. This is not optional.

## Steps

### 1. Compile or upgrade workflows

Use whichever command is appropriate:

```bash
# Full upgrade (updates agents, actions, codemods, then compiles)
gh aw upgrade

# Just recompile (when only .md workflow files changed)
gh aw compile
```

If any workflow fails to compile (e.g., due to permission violations), fix the `.md` source file and re-run.

### 2. Run verification

After recompiling, run the pre-commit hooks to ensure everything is valid:

```bash
pre-commit run --all-files
```

## Common Issues

### Strict mode violations

When compiling with `--strict` (or if enforced by the version), gh-aw disallows write permissions like `contents: write`,
`issues: write`, etc. Workflows should use `safe-outputs` for write operations and only request
`read` permissions.

### Discussion category warnings

Warnings about "General" vs "general" discussion category casing are non-blocking.

## Verification

After both steps, run `git diff --stat` to review all changed files. Expect changes in:

- `.github/agents/` - Updated agent files
- `.github/aw/actions-lock.json` - Updated action pins
- `.github/workflows/*.lock.yml` - Regenerated lock files
- `.github/workflows/*.md` - If codemods applied fixes

## References

- [Recompile Skill Reference](https://github.com/github/gh-aw-firewall/blob/main/.claude/skills/recompile-workflows/SKILL.md)
