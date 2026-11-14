#!/usr/bin/env python3
"""L-NEW box 161: trace an external-flip run: genome json + level-0 schedule (JSON list of [q0, q1] per state).
Per step: level-0 config, b_0, per level: states, moved (*), Xi-unhappy (u), KP. Also prints the Xi-targets."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from ext import *
G = json.load(open(sys.argv[1])); sched = json.loads(sys.argv[2]); g = Gen(G); d = max(g.lev) + 1
print("xt", [[o[1] for o in G["opts"][x]] for x in range(g.N)], "xorder", G.get("xorder"))
cur = tuple(sched[0] + G["start"][2:])
def kp(s, v):
    key = g.keys(s); return min((0, 1), key=lambda k: g.optkey(key, v, k))
rows = [cur]
for t in range(1, len(sched)): rows.append(step_forced(g, rows[-1], list(sched[t]) + [0] * (g.N - 2)))
for t, s in enumerate(rows):
    cells = []
    for l in range(d):
        c = ""
        for v in (2 * l, 2 * l + 1):
            mv = t > 0 and rows[t][v] != rows[t - 1][v]; un = len(g.avail(s, v)) == 2
            c += f"{s[v]}{'*' if mv else ' '}{'u' if un else '.'}{kp(s, v)} "
        cells.append(c)
    print(f"t{t:2d} b0={b0(g, s)} | " + " | ".join(cells))
