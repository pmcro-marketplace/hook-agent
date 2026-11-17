#!/usr/bin/env python3
import argparse, json, sys
EVENTS = {
    "agent-startup","input","pre-model-call","post-model-call","pre-tool-call",
    "post-tool-call","handoff","output","error","agent-shutdown"
}
p=argparse.ArgumentParser()
p.add_argument("event", choices=sorted(EVENTS))
p.add_argument("--context")
a=p.parse_args()
ctx=None
if a.context:
    with open(a.context, "r", encoding="utf-8") as f:
        ctx=json.load(f)
print(json.dumps({
    "kind":"HookInvocation",
    "status":"NOT_INVOKED",
    "direct_function":f"/{a.event}",
    "capability":f"/hook:hook:{a.event}",
    "context":ctx,
    "note":"Dispatcher resolves the contract only. A real host/runtime provider must perform lifecycle execution."
}, indent=2))
sys.exit(0)
