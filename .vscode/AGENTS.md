# VSCode Settings Agent Invariants

- The `chat.tools.terminal.autoApprove` keys must be mirrored in
  `.github/workflows/opencode-agent.yml` and
  `.github/workflows/cogni-ai-agent.yml`.
- Any allow/deny command change in one surface MUST be mirrored in the other
  two in the same update.
- The list of tool keys in these files MUST be kept in strict alphabetical order.
