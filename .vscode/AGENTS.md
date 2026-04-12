# VSCode Settings Agent Invariants

- The `chat.tools.terminal.autoApprove` keys must be mirrored in
  `.opencode/opencode.jsonc`, `.github/workflows/opencode.yml`, and
  `.github/workflows/opencode-review.yml`.
- Any allow/deny command change in one surface MUST be mirrored in the other
  three in the same update.
- The list of tool keys in these files MUST be kept in strict alphabetical order.
