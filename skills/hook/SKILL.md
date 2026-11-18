---
name: hook
description: Use as the shared lifecycle subagent above installed agent capability execution. USE FOR applicable agent, input, model, tool, handoff, output, error, and shutdown lifecycle boundaries. DO NOT USE FOR replacing the target business capability or simulating lifecycle execution when no real provider exists.
---
# Hook

## Purpose
Provide one shared lifecycle subagent that can sit above every installed Agent -> Plugin -> Skill -> Function execution.

## When to Use
Use automatically at applicable agent, input, model, tool, handoff, output, error, and shutdown boundaries.

## When Not to Use
Do not replace the target business function, duplicate another domain capability, or claim lifecycle execution without provider evidence.

## Inputs
A HookContext, the resolved target Agent -> Plugin -> Skill -> Function, current lifecycle event, governance posture, and correlation evidence.

## Deliverables
A lifecycle disposition plus preserved target execution and evidence. If no real lifecycle runtime/provider is available, return NOT_INVOKED for the hook action.

## Workflow
1. Resolve the target Agent -> Plugin -> Skill -> Function.
2. Determine which lifecycle functions are actually applicable.
3. Emit each applicable lifecycle functionality before attempting it.
4. Invoke the real lifecycle provider when one exists.
5. Preserve and invoke the original target capability.
6. Run the corresponding post/error/output lifecycle functions when applicable.
7. Verify target and lifecycle evidence independently.
8. Never treat emission, routing, or a declared function name as proof of execution.

## Validation
Direct lifecycle functions resolve as:
- `/agent-startup` -> `/hook:hook:agent-startup`
- `/input` -> `/hook:hook:input`
- `/pre-model-call` -> `/hook:hook:pre-model-call`
- `/post-model-call` -> `/hook:hook:post-model-call`
- `/pre-tool-call` -> `/hook:hook:pre-tool-call`
- `/post-tool-call` -> `/hook:hook:post-tool-call`
- `/handoff` -> `/hook:hook:handoff`
- `/output` -> `/hook:hook:output`
- `/error` -> `/hook:hook:error`
- `/agent-shutdown` -> `/hook:hook:agent-shutdown`

## Pitfalls
Marketplace installation makes the Hook Agent discoverable; it does not by itself prove that a runtime adapter exists. Do not simulate lifecycle execution.

## Resources
See `references/functions.md`, `references/contract.md`, `assets/hook-context.example.json`, `assets/request.json`, `scripts/dispatch.py`, and `scripts/validate.py`.
