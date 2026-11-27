# Hook Contract

Plugin: `hook`
Skill/subagent: `hook`
Agent: `@hook-agent`

Core invariant:
`RESOLVE -> EMIT HOOK -> INVOKE HOOK WHEN AVAILABLE -> INVOKE TARGET -> VERIFY -> EVIDENCE`

Status vocabulary:
`PASS`, `FAIL`, `BLOCKED`, `NOT_INVOKED`.

Hook Agent must not claim lifecycle execution unless a real provider/runtime returns evidence.
