---
description: 'Blog post specific content standards and validation'
applyTo:
  - 'docs/blog/**/*.md'
  - 'blog/**/*.md'
  - 'posts/**/*.md'
---

# Blog Post Instructions

## Front Matter Requirements

All blog posts must include YAML front matter at the beginning of the file with the following required fields:

- `post_title`: The title of the post.
- `author1`: The primary author of the post.
- `post_slug`: The URL slug for the post.
- `microsoft_alias`: The Microsoft alias of the author.
- `featured_image`: The URL of the featured image.
  - **File Format**: Use JPEG or PNG format. WebP is also acceptable for modern browsers.
  - **Size/Aspect Ratio**: Recommended minimum width of 1200px with a 16:9 or 2:1 aspect
    ratio for optimal display across devices.
  - **Accessibility**: Store alt text in a separate `featured_image_alt` field to describe
    the image content for screen readers.
  - **Licensing**: Ensure images are properly licensed for use. Include attribution in
    `featured_image_attribution` field if required by the license.
- `categories`: The categories for the post. These categories must be from the list in /categories.txt.
- `tags`: The tags for the post.
- `ai_note`: A boolean value (`true` or `false`) indicating whether AI was used in the creation of the post.
- `summary`: A brief summary of the post. Recommend a summary based on the content when possible.
- `post_date`: The publication date of the post.

## Content Standards

Blog posts must follow the general markdown content rules defined in `markdown.instructions.md`.

## Validation

- Ensure all required front matter fields are present and properly formatted.
- Verify that each category value appears as a line in `/categories.txt` (for example, use
  `grep -Fx "<category>" categories.txt` for each category or open the file and confirm manually).
- Follow the project's markdown linting rules from `.markdownlint.yaml`.
- Run `pre-commit run markdownlint -a` to verify locally.
