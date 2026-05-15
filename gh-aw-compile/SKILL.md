---
name: gh-aw-compile
description: >-
  Regenerate and post-process all agentic workflows.
  You MUST load this skill when gh-aw is updated, workflow .md files change,
  or when asked to recompile/regenerate workflows.
---

# Recompile Agentic Workflows

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

- <https://github.com/github/gh-aw-firewall/blob/main/.claude/skills/recompile-workflows/SKILL.md>
