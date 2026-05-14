---
name: chrome-devtools
description: 'Expert-level browser automation, debugging, and performance analysis using Chrome DevTools MCP. Use for interacting with web pages, capturing screenshots, analyzing network traffic, and profiling performance.'
license: MIT
---

# Chrome DevTools

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

A specialized skill for controlling and inspecting a live Chrome browser. This skill leverages the `chrome-devtools` MCP server to perform a wide range of browser-related tasks, from simple navigation to complex performance profiling.

## Core Process

1. **Context Awareness**: Always run `list_pages` and `select_page` if you are unsure which tab is currently active.
2. **Visual Inspection**: Take a new `take_snapshot` after any major navigation or DOM change to get updated `uid` values.
3. **Execution**: Perform interactions using `uid` or `wait_for` specific text to appear.
4. **Validation**: Use screenshots sparingly for visual verification, but rely on snapshots for logic.

## Core Principles

- **Snapshot-First Identification**: Always prefer `take_snapshot` over `take_screenshot` for finding elements. The snapshot provides `uid` values required by interaction tools.
- **Troubleshoot Objectively**: When a page fails, check both console logs (`list_console_messages`) and network requests (`list_network_requests`).
- **Profile Methodically**: Use `performance_start_trace` and `performance_analyze_insight` to identify LCP issues or layout shifts.

## Commands / Usage Patterns

### Navigation & Page Management
- `new_page`: Open a new tab/page.
- `navigate_page`: Go to a specific URL, reload, or navigate history.
- `select_page`: Switch context between open pages.
- `list_pages`: See all open pages and their IDs.
- `close_page`: Close a specific page.
- `wait_for`: Wait for specific text to appear on the page. Use reasonable timeouts.

### Input & Interaction
- `click`: Click on an element (use `uid` from snapshot).
- `fill` / `fill_form`: Type text into inputs or fill multiple fields at once.
- `hover`: Move the mouse over an element.
- `press_key`: Send keyboard shortcuts or special keys (e.g., "Enter", "Control+C").
- `drag`: Drag and drop elements.
- `handle_dialog`: Accept or dismiss browser alerts/prompts.
- `upload_file`: Upload a file through a file input.

### Debugging & Inspection
- `take_snapshot`: Get a text-based accessibility tree (best for identifying elements).
- `take_screenshot`: Capture a visual representation of the page or a specific element.
- `list_console_messages` / `get_console_message`: Inspect the page's console output.
- `evaluate_script`: Run custom JavaScript in the page context.
- `list_network_requests` / `get_network_request`: Analyze network traffic and request details.

### Emulation & Performance
- `resize_page`: Change the viewport dimensions.
- `emulate`: Throttling CPU/Network or emulating geolocation.
- `performance_start_trace(reload=true, autoStop=true)`: Start recording a performance profile.
- `performance_stop_trace`: Stop recording and save the trace.
- `performance_analyze_insight`: Get detailed analysis from recorded performance data.

## What to Avoid

- Avoid using `take_screenshot` for element identification; always prefer `take_snapshot` for the logical layout and `uid` extraction.
- Do not forget to use `wait_for` after navigation to prevent interacting with elements that have not yet loaded.

## Limitations

- `uid` values from snapshots are transient; any significant DOM mutation may invalidate them, requiring a new snapshot.

## Related Skills

- **critical-thinking**:
  You MUST load this skill when interpreting performance profiles or debugging complex DOM state issues.
