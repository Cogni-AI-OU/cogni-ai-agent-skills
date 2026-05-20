---
name: llmstxt
description: 'A proposal to standardise on using an /llms.txt file to provide information to help LLMs use a website at inference time. You MUST load this skill when reading websites, llms.txt, or when creating/updating that file.'
license: MIT
---

# llmstxt

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- When using the `webfetch` tool to read documentation from a website.
- When creating, updating, or maintaining an `/llms.txt` file for a project.
- When retrieving context about a website to help LLMs understand its structure.

## When Not to Use

- When reading local files that do not correspond to web documentation.
- When the task does not involve fetching external documentation or creating LLM context files.

## Core Process

1. **Check for `llms.txt` before reading docs**: When you need to read documentation from a new website, always attempt to fetch `https://<domain>/llms.txt` first. This file often contains a curated overview of the documentation and links to LLM-friendly markdown files.
2. **Look for expanded context files**: Some sites provide `/llms-ctx.txt` (expanded context without optional URLs) or `/llms-ctx-full.txt` (full expanded context). Fetching these can provide all the documentation in a single context-friendly file.
3. **Check for `.md` versions of pages**: If reading a specific page `https://<domain>/path/page.html`, try fetching `https://<domain>/path/page.html.md` (or `index.html.md` for directories) as it might provide a clean markdown version.
4. **Creating or updating `llms.txt`**: When asked to create an `llms.txt` file for a site:
   - Ensure it's located in the root path `/llms.txt` (or a subpath if specified).
   - Use an `H1` with the project name (required).
   - Follow with a blockquote `>` containing a short summary.
   - Include zero or more markdown sections with detailed information.
   - Include zero or more `H2` (`##`) sections containing "file lists" of URLs.
   - In file lists, use standard markdown links `[name](url)` optionally followed by `:` and notes.
   - Use a `## Optional` section for URLs that can be skipped if a shorter context is needed.

## Best Practices

- Use concise, clear language in `llms.txt` files.
- When linking to resources, include brief, informative descriptions.
- Prefer markdown formats as they are easily understood by language models.

## What to Avoid

- Do not use `llms.txt` as a full sitemap (use `sitemap.xml` for search engines).
- Avoid putting large unstructured data directly in `/llms.txt`; link to detailed `.md` files instead.

## Common Pitfalls

- **Forgetting to check `llms.txt` first**: Jumping straight to searching individual HTML pages can lead to parsing complex HTML and missing curated LLM context. Always fetch `/llms.txt` or `/llms-ctx.txt` first.
- **Incorrect file structure**: Failing to include the required H1 or blockquote summary when generating the file.
- **Overlooking `.md` extensions**: Wasting tokens on raw HTML when appending `.md` to the URL could yield clean markdown.

## References

- [llms.txt Official Specification](https://llmstxt.org/)
- <https://llmstxt.org/llms.txt>
