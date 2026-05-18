---
name: chrome-devtools
description: >-
  Expert-level browser automation, debugging, and performance analysis using
  Chrome DevTools MCP. Use for interacting with web pages, capturing
  screenshots, analyzing network traffic, and profiling performance.
license: MIT
---

# Chrome DevTools

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use

- **Browser Automation**: Navigating pages, clicking elements, filling forms, and handling dialogs in a live browser.
- **Visual Inspection**: Taking screenshots or text accessibility snapshots of web pages for visual verification.
- **Debugging**: Inspecting console messages, evaluating JavaScript in the page context, and analyzing network request failures.

## When Not to Use

- Static HTML parsing or content scraping without browser interaction — use HTTP clients (curl, wget) or headless scripts instead.
- API testing or endpoint validation — use dedicated tools like `curl`, Postman, or REST API clients.
- Network-level packet analysis or deep protocol inspection — use Wireshark or `tcpdump` instead.

## Common Pitfalls

- **Stale `uid` Values**: Snapshot `uid` values change after any DOM mutation or page navigation. Always call `take_snapshot` again after clicking, filling forms, or navigating to get current `uid` values.
- **Snapshot Over Screenshot**: Use `take_snapshot` (text-based accessibility tree) for element identification, not `take_screenshot`. Screenshots do not provide the `uid` values required by interaction tools.
- **Page Context Tracking**: Always run `list_pages` and `select_page` to confirm which browser tab is active before interacting. Operations on the wrong tab cause confusing failures and wasted time.
- **Console Message Buffering**: `list_console_messages` may return stale or buffered messages from earlier page activity. Clear page state or open a new page before starting a fresh debugging session.
- **Performance Trace Overhead**: Starting a performance trace (`performance_start_trace`) increases page load time and memory usage. Use targeted, short-duration traces rather than long continuous recordings.

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
- `performance_start_trace`: Start recording a performance profile.
- `performance_stop_trace`: Stop recording and save the trace.
- `performance_analyze_insight`: Get detailed analysis from recorded performance data.

## Tool Categories

### 1. Navigation & Page Management

- `new_page`: Open a new tab/page.
- `navigate_page`: Go to a specific URL, reload, or navigate history.
- `select_page`: Switch context between open pages.
- `list_pages`: See all open pages and their IDs.
- `close_page`: Close a specific page.
- `wait_for`: Wait for specific text to appear on the page.

### 2. Input & Interaction

- `click`: Click on an element (use `uid` from snapshot).
- `fill` / `fill_form`: Type text into inputs or fill multiple fields at once.
- `hover`: Move the mouse over an element.
- `press_key`: Send keyboard shortcuts or special keys (e.g., "Enter", "Control+C").
- `drag`: Drag and drop elements.
- `handle_dialog`: Accept or dismiss browser alerts/prompts.
- `upload_file`: Upload a file through a file input.

### 3. Debugging & Inspection

- `take_snapshot`: Get a text-based accessibility tree (best for identifying elements).
- `take_screenshot`: Capture a visual representation of the page or a specific element.
- `list_console_messages` / `get_console_message`: Inspect the page's console output.
- `evaluate_script`: Run custom JavaScript in the page context.
- `list_network_requests` / `get_network_request`: Analyze network traffic and request details.

### 4. Emulation & Performance

- `resize_page`: Change the viewport dimensions.
- `emulate`: Throttling CPU/Network or emulating geolocation.
- `performance_start_trace`: Start recording a performance profile.
- `performance_stop_trace`: Stop recording and save the trace.
- `performance_analyze_insight`: Get detailed analysis from recorded performance data.

## Workflow Patterns

### Pattern A: Identifying Elements (Snapshot-First)

Always prefer `take_snapshot` over `take_screenshot` for finding elements. The snapshot provides `uid` values which are required by interaction tools.

```markdown
1. `take_snapshot` to get the current page structure.
2. Find the `uid` of the target element.
3. Use `click(uid=...)` or `fill(uid=..., value=...)`.
```

### Pattern B: Troubleshooting Errors

When a page is failing, check both console logs and network requests.

```markdown
1. `list_console_messages` to check for JavaScript errors.
2. `list_network_requests` to identify failed (4xx/5xx) resources.
3. `evaluate_script` to check the value of specific DOM elements or global variables.
```

### Pattern C: Performance Profiling

Identify why a page is slow.

```markdown
1. `performance_start_trace(reload=true, autoStop=true)`
2. Wait for the page to load/trace to finish.
3. `performance_analyze_insight` to find LCP issues or layout shifts.
```

## Best Practices

- **Context Awareness**: Always run `list_pages` and `select_page` if you are unsure which tab is currently active.
- **Snapshots**: Take a new snapshot after any major navigation or DOM change, as `uid` values may change.
- **Timeouts**: Use reasonable timeouts for `wait_for` to avoid hanging on slow-loading elements.
- **Screenshots**: Use `take_screenshot` sparingly for visual verification, but rely on `take_snapshot` for logic.

## References

- <https://github.com/github/awesome-copilot/blob/main/skills/chrome-devtools/SKILL.md>

## Related Skills

- **critical-thinking**:
  You MUST load this skill when interpreting performance profiles or debugging complex DOM state issues.
