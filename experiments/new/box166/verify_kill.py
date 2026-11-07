#!/usr/bin/env python3
"""independent check of a PM kill genome: well-formedness (IDEAL-ACYC; W-target exactly one level down; distinct gates; distinct
ranks; acyclic Xi-graph), the run (box150 Gen; the second simulator box139/paths.py is compared state for state by box150/check.py, counter XSIM), and the PM count for
the named mover. Usage: verify_kill.py genome.json x"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(H, "..", "box150", "check.py"); ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns)
Gen, ref_run = ns["Gen"], ns["ref_run"]
G = json.load(open(sys.argv[1])); x = int(sys.argv[2]); N = G["N"]; ok = True
ms = [o[2] for oo in G["opts"] for o in oo]; gates = [gg for g in G["gate"] for gg in g]
ok &= len(set(ms)) == len(ms) and len(set(G["br"][m] for m in ms)) == len(ms) and len(set(gates)) == len(gates)
for v in range(N):
    for o in G["opts"][v]:
        ok &= (o[0] == -1) == (G["lev"][v] == 0) and (o[0] == -1 or G["lev"][o[0]] == G["lev"][v] - 1)
adj = [set(o[1] for o in G["opts"][v] if o[1] >= 0) for v in range(N)]
def desc(v):
    seen, st = set(), list(adj[v])
    while st:
        y = st.pop()
        if y not in seen: seen.add(y); st.extend(adj[y])
    return seen
acyc = all(v not in desc(v) for v in range(N)); ok &= acyc
S, _ = Gen(G).run(G["start"]); same = "see box150/check.py XSIM"
mv = sum(S[t][x] != S[t - 1][x] for t in range(1, len(S)))
print("wellformed", ok, "acyclic", acyc, "simulators agree", same, "T", len(S) - 1, "mover", x, "deg", len(G["opts"][x]), "desc", len(desc(x)),
      "moves", mv, "PM bound", (len(G["opts"][x]) - 1) * (1 + len(desc(x))), "=> PM", "VIOLATED" if mv > (len(G["opts"][x]) - 1) * (1 + len(desc(x))) else "holds")
for t, s in enumerate(S): print(t, "".join(map(str, s)))
