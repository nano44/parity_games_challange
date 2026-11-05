#!/usr/bin/env python3
"""L-RED R199 ALLGATES: every W-feasible gate / start choice of a genk target (build.py want_all; distinct state sequences / gate
bits), each written as a target, so that a refutation can be made exact over ALL gate choices. Usage: allgates.py k nper outdir"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build
k, NP, od = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; os.makedirs(od, exist_ok=True); P = 2 ** k; L = NP * P; m = {}
def put(l, prompt, late): m[2 * l] = set(prompt); m[2 * l + 1] = set(late)
put(0, [P + 1], [2 * P + 1] if NP == 3 else [])
for j in range(1, k + 1):
    per = P // 2 ** (j - 1); put(j, list(range(1, L + 1, per)), list(range(1 + per // 2, L + 1, per)))
A = build.build(L, k + 1, m, want_all=True); seen = set(); n = 0
for T in A:
    key = json.dumps([T["states"], T["gate"]])
    if key in seen: continue
    seen.add(key); json.dump(T, open(os.path.join(od, f"ag_{n}.json"), "w")); n += 1
print("ALLGATES k", k, "nper", NP, "feasible choices", len(A), "distinct", n, "F", sorted({tuple(T["F"]) for T in A}))
