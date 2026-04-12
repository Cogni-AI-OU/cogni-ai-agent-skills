<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->
---
description: git commit and push
model: opencode/glm-4.6
subtask: true
---

commit and push

make sure it includes a prefix like
docs:
tui:
core:
ci:
ignore:
wip:

For documentation, prompts, or onboarding changes use the docs: prefix.

For workflow, devcontainer, or automation changes prefer the ci: prefix.

prefer to explain WHY something was done from an end user perspective instead of
WHAT was done.

do not do generic messages like "improved agent experience" be very specific
about what user facing changes were made

if there are changes do a git pull --rebase
if there are conflicts DO NOT FIX THEM. notify me and I will fix them
