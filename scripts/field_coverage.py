#!/usr/bin/env python3
"""Diff backend fields vs UI controls. Exit 1 on any FAIL.

backend.json: {"fieldname": {"default": any}, ...}  or ["fieldname", ...]
ui.json:      {"fieldname": {"value": any}, ...}    or ["fieldname", ...]
whitelist.json (optional): {"fieldname": "reason", ...}  backend-only fields allowed to be absent.
"""
import argparse, json, re, sys

PLACEHOLDER = re.compile(r"(^todo$|lorem|example\.com|^test_|^foo$|^changeme$)", re.I)

def load(p):
    with open(p) as f:
        d = json.load(f)
    return {k: {} for k in d} if isinstance(d, list) else d

ap = argparse.ArgumentParser()
ap.add_argument("--backend", required=True)
ap.add_argument("--ui", required=True)
ap.add_argument("--whitelist")
a = ap.parse_args()
b, u = load(a.backend), load(a.ui)
wl = json.load(open(a.whitelist)) if a.whitelist else {}

missing = sorted(k for k in b if k not in u and k not in wl)
orphan = sorted(k for k in u if k not in b)
matched = sorted(k for k in b if k in u)
bad = []
for k in matched:
    if "default" in b[k] and "value" in u[k] and b[k]["default"] != u[k]["value"]:
        bad.append((k, f"default {b[k]['default']!r} != UI {u[k]['value']!r}"))
    v = u[k].get("value")
    if isinstance(v, str) and PLACEHOLDER.search(v):
        bad.append((k, f"placeholder value {v!r}"))

print(f"{'FORGOTTEN IN UI (backend-only)':40}{'ORPHAN (UI-only)':30}MATCHED")
for i in range(max(len(missing), len(orphan), len(matched), 1)):
    c = lambda l: l[i] if i < len(l) else ""
    print(f"{c(missing):40}{c(orphan):30}{c(matched)}")
for k, m in bad:
    print(f"MISMATCH {k}: {m}")
fail = bool(missing or orphan or bad)
print("RESULT:", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
