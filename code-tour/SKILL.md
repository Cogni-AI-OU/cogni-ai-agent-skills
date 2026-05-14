---
name: code-tour
description: >-
  Use this skill to create CodeTour .tour files — persona-targeted, step-by-step walkthroughs that link to real files and line numbers.
  You MUST load this skill when creating or updating .tours/ files. Trigger for: "create a tour", "make a code tour", "generate a tour", "onboarding tour", "architecture tour", etc.
---

# Code Tour Skill

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

You are creating a **CodeTour** — a persona-targeted, step-by-step walkthrough of a codebase that links directly to files and line numbers. CodeTour files live in `.tours/` and work with the [VS Code CodeTour extension](https://github.com/microsoft/codetour).

A great tour is not just annotated files. It is a **narrative** — a story told to a specific person about what matters, why it matters, and what to do next. Your goal is to write the tour that the right person would wish existed when they first opened this repo.

**CRITICAL: Only create `.tour` JSON files. Never create, modify, or scaffold any other files.**

---

## Step 1: Discover the repo

Before asking the user anything, explore the codebase:
- List the root directory, read the README, and check key config files.
- Identify the language(s), framework(s), and what the project does.
- Map the folder structure 1–2 levels deep.
- Find entry points: main files, index files, app bootstrapping.
- **Note which files actually exist** — every path you write in the tour must be real.

If the repo is sparse or empty, say so and work with what exists.

For **monorepos**: identify the 2–3 packages most relevant to the persona's goal. Don't try to tour everything — open the tour with a step that explains how to navigate the workspace, then stay focused.

### Large repo strategy

For repos with 100+ files: don't try to read everything.
1. Read entry points and the README first.
2. Build a mental model of the top 5–7 modules.
3. For the requested persona, identify the **2–3 modules that matter most** and read those deeply.
4. For modules you're not covering, mention them in the intro step as "out of scope".
5. Use `directory` steps for areas you mapped but didn't read — they orient without requiring full knowledge.

---

## Step 2: Read the intent — infer everything you can

**One message from the user should be enough.** Read their request and infer persona, depth, and focus before asking anything.

### Intent map

- **"tour for this PR" / "#123"** $\rightarrow$ `pr-reviewer` (standard depth). Add `uri` step for PR. Use `ref` for branch.
- **"why did X break" / "RCA"** $\rightarrow$ `rca-investigator` (standard). Trace failure causality chain.
- **"debug X" / "find the bug"** $\rightarrow$ `bug-fixer` (standard). Entry $\rightarrow$ fault points $\rightarrow$ tests.
- **"onboarding" / "new joiner"** $\rightarrow$ `new-joiner` (standard). Directories, setup, business context.
- **"quick tour" / "vibe check"** $\rightarrow$ `vibecoder` (quick, 5-8 steps). Fast path only.
- **"explain how X works"** $\rightarrow$ `feature-explainer` (standard). UI $\rightarrow$ API $\rightarrow$ backend $\rightarrow$ storage.
- **"architecture" / "tech lead"** $\rightarrow$ `architect` (deep). Boundaries, decisions, tradeoffs.
- **"security" / "auth review"** $\rightarrow$ `security-reviewer` (standard). Auth flow, validation, sinks.
- **"refactor" / "safe to extract?"** $\rightarrow$ `refactorer` (standard). Seams, hidden deps.

**Ask only if you genuinely can't infer.** Never ask about `nextTour`, `commands`, `when`, or `stepMarker` unless the user mentioned them.

### User-provided customization — always honor these

- **"cover `src/auth.ts`"**: Those files are required stops.
- **"pin to `v2.3.0` tag"**: Set `"ref": "v2.3.0"`.
- **"link to PR #456"**: Add a `uri` step at the right narrative moment.
- **"lead into the security tour"**: Set `"nextTour": "Security Review"`.
- **"make this the main onboarding tour"**: Set `"isPrimary": true`.
- **"open a terminal at this step"**: Add `"commands": ["workbench.action.terminal.focus"]`.

---

## Step 3: Read the actual files — no exceptions

**Every file path and line number in the tour must be verified by reading the file.** A tour pointing to the wrong file or a non-existent line is worse than no tour.
For every planned step:
1. Read the file.
2. Find the exact line of the code you want to highlight.
3. Understand it well enough to explain it to the target persona.

---

## Step 4: Write the tour

Save to `.tours/<persona>-<focus>.tour` (kebab-case).

### Tour root

```json
{
  "$schema": "https://aka.ms/codetour-schema",
  "title": "Descriptive Title — Persona / Goal",
  "description": "One sentence: who this is for and what they'll understand after.",
  "ref": "main",
  "isPrimary": false,
  "nextTour": "Title of follow-up tour",
  "steps": []
}
```
Omit any field that doesn't apply.

### Step types — full reference

All step types: **content** (intro/closing, max 2), **directory**, **file+line** (workhorse), **selection** (code block), **pattern** (regex match), **uri** (external link), **view** (focus VS Code panel), **commands** (run VS Code commands).
> **Path rule:** `"file"` and `"directory"` must be relative to repo root. No absolute paths, no leading `./`.

**When to use each:**
- **content**: Tour intro or closing
- **directory**: "Here's what lives in this folder"
- **file + line**: One line tells the whole story
- **selection**: A function/class body is the point
- **pattern**: Line numbers shift, file is volatile
- **uri**: PR / issue / doc gives the "why"
- **view or commands**: Reader should open terminal or explorer

### Step count calibration

- **Quick**: 5–8 steps (Vibecoder, fast explorer)
- **Standard**: 9–13 steps (Most personas)
- **Deep**: 14–18 steps (Architect, RCA)

### Writing excellent descriptions — the SMIG formula

Every description should answer four questions:
- **S — Situation**: What is the reader looking at?
- **M — Mechanism**: How does this code work?
- **I — Implication**: Why does this matter for *this persona's goal specifically*?
- **G — Gotcha**: What would a smart person get wrong here? What's non-obvious or fragile?

---

## Narrative arc — every tour, every persona

1. **Orientation** — **must be a `file` or `directory` step, never content-only.** A content-only first step renders as a blank page in VS Code.
2. **High-level map** (1–3 directory or uri steps) — major modules and how they relate.
3. **Core path** (file/line, selection, pattern, uri steps) — the specific code that matters.
4. **Closing** (content) — what the reader now understands, what they can do next, 2–3 suggested follow-up tours. If `nextTour` is set, reference it by name here.

---

## What CodeTour cannot do

- **Auto-advance / Timer**: Not supported. Navigation is manual.
- **Embed video/GIF**: Not supported. Markdown text only.
- **Run arbitrary shell commands**: Not supported. `commands` only executes VS Code commands.
- **Branch / conditional next step**: Not supported. Tours are linear.

---

## Anti-patterns

- **File listing**: Visiting files with "this file contains..." Tell a story instead.
- **Generic descriptions**: Name the specific pattern/gotcha unique to *this* codebase.
- **Line number guessing**: Never write a line number you didn't verify by reading the file.
- **Ignoring the persona**: Cut every step that doesn't serve their specific goal.
- **Hallucinated files**: If a file doesn't exist, skip the step.

---

## Quality checklist — verify before writing the file

- [ ] Every `file` path is **relative to the repo root** (no leading `/` or `./`).
- [ ] Every `file` path read and confirmed to exist.
- [ ] Every `line` number verified by reading the file.
- [ ] Every `pattern` regex would match a real line in the file.
- [ ] Only `.tour` JSON files created — no source code touched.
- [ ] First step has a `file` or `directory` anchor.
- [ ] Tour ends with a closing content step.
- [ ] Every description answers SMIG.
