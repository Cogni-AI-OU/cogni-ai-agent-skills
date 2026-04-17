---
description: 'Guidelines for the main repository README.md'
applyTo:
  - README.md
---

# README Instructions

## Badge Guidance

- Use dynamic badges from shields.io; keep them on one line below the title.
- Include a PR reviews badge using reference links, e.g.:
  - `[![PR Reviews][pr-reviews-image]][pr-reviews-link]`
  - `[pr-reviews-image]: https://img.shields.io/github/issues-pr/{org}/{repo}?label=PR+Reviews&logo=github`
  - `[pr-reviews-link]: https://github.com/{org}/{repo}/pulls`
- Include a license badge linked to TLDRLegal using reference links, e.g.:
  - `[![License][license-image]][license-link]`
  - `[license-image]: https://img.shields.io/badge/License-MIT-blue.svg`
  - `[license-link]: https://tldrlegal.com/license/mit-license`
- If project has any tags, add a tags badge:
  - `[![Tags][tags-image]][tags-link]`
  - `[tags-image]: https://img.shields.io/github/tag/{org}/{repo}.svg?logo=github`
  - `[tags-link]: https://github.com/{org}/{repo}/tags`
- If project uses GitHub Actions, include a build status badge:
  - `[![Status][gha-image-{workflow}-{branch}]][gha-link-{workflow}-{branch}]`
  - `[gha-link-{workflow}-{branch}]: https://github.com/{org}/{repo}/actions?query=workflow%3A{name}%3A{branch}`
  - `[gha-image-{workflow}-{branch}]: https://github.com/{org}/{repo}/workflows/{name}/badge.svg`
- Include project status badges as available (update workflow names as needed):
  - Optional: Docs/site badge if a published site exists.

## Structure

- Start with a concise summary of the project purpose and scope.
- Add a "Getting Started" section covering prerequisites, setup, and a minimal quickstart.
- Add a "Development" section for local workflows (e.g., `pre-commit run --all-files`, running tests).
- Add a "Project Layout" section describing key directories (e.g., `.github/instructions/`, `.github/agents/`).
- Add a "Contributing" section summarizing contribution expectations and linking to any contributing guide if present.
- Add a "License" section that links to the local `LICENSE` file if it exists in the repository,
  otherwise link to the TLDRLegal page (e.g. <https://www.tldrlegal.com/license/mit-license>) for the project's license.
- For lengthy READMEs, include a Table of Contents using a TOC block, e.g.:

  ```markdown
  ## Table of contents

  <!-- TOC -->

  - [About the project](#about-the-project)
  ...

  <!-- /TOC -->
  ```

  Update the TOC block as needed.

## Formatting

- Keep lines <=120 characters.
- Use bullet lists for steps; prefer numbered lists for ordered procedures.
- Use fenced code blocks with languages for commands (e.g., `bash`).
- Use reference-style links for long, repeated URLs or badges after `<!-- Named links -->` for clarity.
- Place badges immediately under the main heading (right after the H1), on separate lines.

## Validation

- Run `pre-commit run --all-files` before committing to catch markdownlint issues.
