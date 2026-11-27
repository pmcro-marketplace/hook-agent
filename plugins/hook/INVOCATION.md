# Invocation Contract

Human lifecycle surface:
`/agent-startup`, `/input`, `/pre-model-call`, `/post-model-call`, `/pre-tool-call`,
`/post-tool-call`, `/handoff`, `/output`, `/error`, `/agent-shutdown`.

Resolution:
`/<lifecycle-function>` -> `@hook-agent /<lifecycle-function>` -> `/hook:hook:<lifecycle-function>`.

Target capabilities retain:
`@<plugin>-agent /<function>` -> `/<plugin>:<skill>:<function>`.

Autonomous top-layer law:
`RESOLVE -> EMIT HOOK -> INVOKE HOOK WHEN AVAILABLE -> INVOKE TARGET -> VERIFY -> EVIDENCE`.

If a real lifecycle runtime/provider is unavailable, the lifecycle action is `NOT_INVOKED`.
Hook emission never proves hook execution.
