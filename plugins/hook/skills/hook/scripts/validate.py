#!/usr/bin/env python3
from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
req=[
    root/"SKILL.md",
    root/"references"/"functions.md",
    root/"references"/"contract.md",
    root/"assets"/"hook-context.example.json",
    root/"assets"/"request.json",
    root/"scripts"/"dispatch.py"
]
missing=[str(p) for p in req if not p.exists()]
if missing:
    print("FAIL: missing "+", ".join(missing)); sys.exit(1)
json.loads((root/"assets"/"hook-context.example.json").read_text(encoding="utf-8"))
print("PASS: hook")
sys.exit(0)
