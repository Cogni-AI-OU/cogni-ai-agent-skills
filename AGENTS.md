# AGENTS.md

Persistent single-source truth for autonomous agent behavior.

For general project invariants see [README.md](README.md).

## Directory-Specific Agent files

Read and merge these when operating inside corresponding sub-directories (order = precedence):

- [`.github/AGENTS.md`](.github/AGENTS.md)
- Any `AGENTS.md` or `SKILL.md` in ancestor, then current directory tree

**Maintenance invariant**:

- After every complex task completion or troubleshooting victory,
  immediately update the nearest relevant AGENTS.md, AGENTS.mmd, or SKILL.md.
- On recurring failure, immediately re-evaluate
  and update the nearest relevant AGENTS.md, AGENTS.mmd, or SKILL.md.
- On discovery of superior workaround, new efficiency primitive, or explicit user directive,
  immediately update the nearest relevant AGENTS.md, AGENTS.mmd, or SKILL.md.
- On detection of ambiguous steps or unclear instructions,
  immediately update the nearest relevant AGENTS.md, AGENTS.mmd, or SKILL.md.

**Creation / Update Triggers (Hard Gate)**:

- Agent-focused guidance that materially compresses cognitive load or failure surface.
- Resolution of recurring task failures or repeated edge-case collapses.
- Discovery of dense, reusable execution primitives during development or debugging.
- User injects new rules, exemplars, or feedback intended for persistent agent memory.
- Existing documentation entropy exceeds threshold, then extract & prune to peak-density form.
- Functionality requires domain-specific knowledge that must survive context windows.

**Hardened NEVER List**:

- NEVER embed one-time discoveries or transient hacks.
- NEVER duplicate code-level comments or obvious steps.
- NEVER hardcode environment-specific values; use generic placeholders with explicit semantics.
- NEVER include beginner exposition or obvious statements.
- NEVER bloat with prose; enforce one-liner density + imperative syntax only.
- If guidance is purely disciplinary, route to dedicated `SKILL.md` instead.

**Writing invariants (Prodigy-Level)**:

- Assume ninja-level proficiency across project spectrum.
- Embed quantitative gates (+20% fidelity delta, <1h MTTR analog, zero ambiguity).
- Every bullet carries measurable payload: role, then invariants, then context, then exemplars, then schema, then NEVER/MUST-NOT,
  then verification loops.
- Favor tables, checklists, and contract-style boundaries over linear text.
- Zero scaffolding. Maximal information-theoretic density. Surgical imperative syntax.

## Core Agent Execution Protocol (Mandatory for All Forks)

**Pre-execution reverse-prompting activation**:

- Declare required inputs, missing context, edge cases, and optimal strategy before any tool invocation or code delta.
- Snapshot current problem state in one entropy-minimized sentence.
- Enumerate risks against classic-mistakes matrix and Top-10 Risks List.
- Apply noise-pruning filter + single-variable delta rule for all experiments.

**Strategic vs tactical default**:

- Always default to strategic programming (Ousterhout).
- Invest 10-20% per cycle in design/refactoring for long-term velocity.
- Tactical tornadoes trigger immediate rollback + root-cause ablation.

**Complexity annihilation primitives** (apply at every layer):

- Design-it-twice mandate on non-trivial decisions.
- Divide-and-conquer + controlled simplification.
- DRY + Boy Scout Rule + Rule-of-Three on every duplication smell.
- Information hiding / deep modules over shallow pass-throughs.
- Pull complexity downwards; define errors out of existence where possible.
- Refactor mercilessly via Fowler catalog before feature addition.

**Verification scaffold (Neurosymbolic)**:

- Chain-of-Verification (CoV) + self-consistency majority vote on every output.
- Unit, then integration, then system regression sequence before any merge.
- Minimal reproducible example builder for every failure isolation.
- Trust-but-verify: replace every assumption with logs/assertions/runtime inspection.
- Post-action: blameless root-cause ablation + lesson injection into persistent memory.

**Debug & Troubleshooting Engine**:

- Stabilize, then reproduce, then isolate via divide-and-conquer + single-variable delta.
- Never patch symptoms; fix root via 5-Whys until systemic.
- Instrument targeted breakpoints; prune non-contributory variables first.
- Maintain runbooks for recurring failure signatures.

**Orchestration Models** (select via task cardinality):

- **Fork**: byte-identical context clone for bounded subtasks.
- **Teammate**: persistent peer with isolated tools/memory.
- **Worktree**: fully parallel independent streams with fork-join synchronization.

**Termination invariants**:

- All TODOs empirically verified.
- Quality, security, performance gates satisfied.
- User objective resolved at target fidelity (+20% over prior baseline).
- AGENTS.md/SKILL.md updated if new reusable primitive discovered.

## Required References

- Agent configuration & conventions: [.github/copilot-instructions.md](.github/copilot-instructions.md)
- Latest org baseline: <https://github.com/Cogni-AI-OU/.github/blob/main/AGENTS.md>
- Project overview & install: [README.md](README.md)
- Workflow navigation: [.tours/getting-started.tour](.tours/getting-started.tour)

## Project Structure and Workflows

### Directory Layout

- `/`: Skill directories (each contains a `SKILL.md`)
- `.github/workflows/`: GitHub Actions for CI/CD and automation
- `.tours/`: Guided walkthroughs for repository onboarding

### Key Workflows

- `check.yml`: Runs pre-commit checks and validation
- `opencode-agent.yml`: Orchestrates autonomous agent operations
- `cogni-ai-agent.yml`: Primary agent interaction workflow
- `devcontainer-ci.yml`: Validates development container configuration

## Skills

You must load the skills relevant to the user prompt, inferred intent,
and planned work into the current context. See [AGENTS-RUNTIME.md](AGENTS-RUNTIME.md)
for the full skills catalog, loading instructions, and structural invariants.

### Final Assurance Gates

- Keep this file entropy-pruned and up-to-date.
- Inject full content into every sub-agent context.
- For latest standard see: <https://agents.md/>

## Common Tasks

### Before each commit

- Verify your expected changes with `git diff --no-color`.
- Ensure no temporary, dummy, or unrelated test files are included in the commit.
- Use the project linting/validation tools to confirm your changes meet the coding standard.
- If the repo uses git hooks, run them to validate your changes.

### File operations

### Editing files

- When modifying or creating documentation and plain text files, always enforce line-wrapping and length
  limits in accordance with project-defined standards (such as `.markdownlint.yaml` or `.editorconfig`).

### Renaming/removing files

- Use `git mv`, `git rm`, or equivalent Git-aware tooling (instead of `mv` or `rm`) to preserve history
  when working with files under source control.

## Feature-specific Notes

### opencode

OpenCode (if installed) uses XDG base directories (not a single `~/.opencode` dir):

| Directory                 | Purpose                                                |
| ------------------------- | ------------------------------------------------------ |
| `~/.local/share/opencode` | Data **and** auth credentials (`auth.json` lives here) |
| `~/.config/opencode`      | User configuration (`opencode.json`/`opencode.jsonc`)  |
| `~/.cache/opencode`       | Ephemeral binary cache - not worth persisting          |
| `~/.local/state/opencode` | Runtime state - not worth persisting                   |

## Tooling

- Use MCP when possible.
- Use `pre-commit` for linting and validation if installed.
- For dumping links use `links -dump` if installed.

### Understanding the Task

- When the task is not clear, look for additional context.
- If triggered by a brief comment, check whether the parent comment exists and includes more detail.
- If it's still ambiguous, communicate with the user and propose options.

### Adding or Modifying Workflows

- Workflows in `.github/workflows/` can be reused via `workflow_call`
- Test workflow changes on a feature branch before merging to main
- Use `actionlint` to validate workflow syntax locally

### Updating Coding Standards

- Language-specific conventions reside in individual skill directories alongside their `SKILL.md`
- Update `.markdownlint.yaml`, `.yamllint`, or `.editorconfig` for linting rules
- Run `pre-commit run -a` to verify changes pass all checks

## References

- Main documentation: [README.md](README.md)

## Troubleshooting

### Firewall issues

If you encounter firewall issues when using the GitHub Copilot Agent:

- Refer to <https://gh.io/copilot/firewall-config> for configuration details.
- Do not work around blocked URLs by adding markdown-link-check ignore/whitelist patterns for real links.
- Keep markdown-link-check validating real links, and request firewall allowlisting instead.
- If you need to allowlist additional hosts, update your firewall configuration accordingly
  by following `.github/FIREWALL.md` and keep that file up to date.

### GitHub Runtime issues

- If you encounter issues while running in GitHub Actions, refer to the loading instructions in [AGENTS-RUNTIME.md](AGENTS-RUNTIME.md).
