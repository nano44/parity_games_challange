#!/usr/bin/env python3
"""L-RED R199 SLACK: «doubling plus slack» targets. Start from a genk target (k nested doubling levels) and delete up to D moves of the
LATE movers of levels 1..k (one deleted move removes one late answer); keep the variants whose W side is satisfiable (r199/build.py),
compute F and the slack c = max over the doubling levels of 2F_(l-1) - F_l. Writes each target and an index. Usage:
slack.py k nper D outdir   (then run r199/xbmc.py on each target with the chosen extra levels)"""
import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build
k, NP, D, od = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(od, exist_ok=True)
P = 2 ** k; L = NP * P; base = {}
def put(m, l, prompt, late): m[2 * l] = set(prompt); m[2 * l + 1] = set(late)
put(base, 0, [P + 1], [2 * P + 1] if NP == 3 else [])
for j in range(1, k + 1):
    per = P // 2 ** (j - 1); put(base, j, list(range(1, L + 1, per)), list(range(1 + per // 2, L + 1, per)))
late = [(2 * j + 1, t) for j in range(1, k + 1) for t in sorted(base[2 * j + 1])]
idx = []; seen = set()
for r in range(1, D + 1):
    for dele in itertools.combinations(late, r):
        m = {v: set(s) for v, s in base.items()}
        for v, t in dele: m[v].discard(t)
        T = build.build(L, k + 1, m)
        if T["bad"]: continue
        F = T["F"]; key = (tuple(F), tuple(sorted(dele)))
        c = max(2 * F[l - 1] - F[l] for l in range(1, k + 1))
        name = "sl_k%d_p%d_" % (k, NP) + "_".join(f"{v}t{t}" for v, t in dele)
        json.dump(T, open(os.path.join(od, name + ".json"), "w")); idx.append(dict(name=name, dele=dele, F=F, c=c, nreq=T["nreq"]))
json.dump(idx, open(os.path.join(od, "index.json"), "w"))
print("SLACK k", k, "nper", NP, "D", D, "W-feasible variants", len(idx))
for e in sorted(idx, key=lambda e: e["c"])[:40]: print(" ", e["name"], "F", e["F"], "c", e["c"])
